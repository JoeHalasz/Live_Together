from room import Room
from object import Object 
import pickle
from os.path import exists
import sys
from catBehavior import catMovement
from room import Sendroom
from pynput.keyboard import Key, Controller


highestId = 100
k = Controller()


def getRoom(roomName, world):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room
	print()
	print("ERROR Could not find room " + roomName)
	print("rooms are:")
	for r in world:
		print(r.name)
	raise Exception("could not find room")
	quit()


from player import Player # THIS HAS TO BE BELOW getRoom


def connectRooms(leftRoom, rightRoom, hasDoors=False):
	leftRoom.addRoom(rightRoom, "right", hasDoors)
	rightRoom.addRoom(leftRoom, "left", hasDoors)



def fix_world():
	global highestId
	global world
	cat = Object("cat", 80, 0,1)
	cat2 = Object("small cat", 25, 0, 2)
	bed = Object("bed", 66, 0, 4)
	monitor = Object("monitor", 45, 0, 5)
	highestId = 100

	starterRoom = Room("Starter Room", 600,300,[cat, cat2])
	leftRoom = Room("left Room", 500,160,[])
	gianaRoom = Room("Next Room", 800,400,[bed, monitor])

	connectRooms(leftRoom, starterRoom)
	connectRooms(starterRoom, gianaRoom)

	world = []
	world.append(starterRoom)
	world.append(leftRoom)
	world.append(gianaRoom)
	player = getPlayer(world)
	player.roomName = starterRoom.name
	return player, world


def loadWorld(recieved=None):
	return fix_world()
	global highestId
	if recieved == None:
		world = load("world/world.wld")
		if world == None:
			return fix_world(), world
	else:
		world = recieved

	# remember to update highestId for new objects
	highest = 0
	for room in world:
		print()
		print(room.name)
		for obj in room.roomObjects:
			print(obj.name + " [" + str(obj.x) + " " + str(obj.y) + "]")
			highest = max(highestId, obj.objectId)
	highestId = highest + 1
	player = getPlayer(world)
	return player, world

# this will loop through the other players actions and do them on this clients side
def dealWithActions(other_actions, player, world):
	for action in other_actions:
		if action != None:
			# if the object moved then just remove the old one and readd the new one 
			if action.name == "removed" or action.name == "moved":
				done=False
				for room in world:
					for obj in room.roomObjects:
						if (obj.objectId == action.objId):

							room.roomObjects.remove(obj)
							done=True
							break
					if done:
						break

			if action.name == "added object" or action.name == "moved":
				getRoom(action.roomName, world).roomObjects.append(action.obj)
				action.obj.beingHeld = False

			if "added room" == action.name:
				# action.obj is a room object
				roomData = action.obj
				room = roomData.room
				otherRoom = getRoom(roomData.connectedRoom.name, world)
				world.append(roomData.room)
				if roomData.whichSide == "left":
					connectRooms(room, otherRoom)
				else:
					connectRooms(otherRoom, room)
			# assumes that this is not the last room and there are only left and right rooms
			if "removed room" == action.name:
				room = getRoom(action.obj.name, world)
				remove_room(room, player, world)

				


def remove_room(room, player, world):
	if room.left != None and room.right != None:
		room.left.right = room.right
		room.right.left = room.left
		player.changeRoom(room.left, "right", world)
	elif room.left != None: # there is only a left room
		player.changeRoom(room.left, "right", world)
		room.left.right = None
		room.left.deleteObjectByName("door right")
	else: # there is only a right room
		print("here")
		player.changeRoom(room.right, "left", world)
		room.right.left = None
		room.right.deleteObjectByName("door left")
	world.remove(room)


def refreshTextures(world):
	for room in world:
		for obj in room.roomObjects:
			obj.setDesign(obj.name) # get all the new designs


def refreshWorld(gameTick, fps, player, world):
	inc = .1 # this is times per second a stage will change 
	inc *= fps
	for o in getRoom(player.roomName, world).roomObjects:
		if "cat" in o.name or "cat" == o.name:
			catMovement(o, inc)




def addNewObject(player, world): # this will stop the game and prompt the user for a new object
	global highestId
	print("Please input the type of object you want to add to the world")
	print("If adding a room format it like this: room (left or right), roomName, width, height")
	print("If removing a room just say: remove room")
	

	# now remove all the text the user has typed during playing

	k.press(Key.ctrl)

	for x in range(20):
		k.press(Key.backspace)
		k.release(Key.backspace)

	k.release(Key.ctrl)
	name = ""
	while True: # this will ensure that there are no keyboard interupts
		try:
			name = input() # get the name of the object ( could also be a tag )
			break
		except:
			pass

	if "door" not in name and name != "" and name != " ":
		if name == "/getobjects":
			for o in getRoom(player.roomName, world).roomObjects:
				print(o.name, o.x, o.y)
			print("Press enter to continue")
			input()
		elif name == "remove room":
			#  make sure there is somewhere for the player to go
			room = getRoom(player.roomName, world)
			if (room.left != None or room.right != None) and player.roomName != "Starter Room":
				remove_room(room, player, world)
				return Object(room.name, -1,-1,-1), "removed room" # only the name will be used from this 
		elif "room" in name:
			# its adding a room
			# make sure this roomName doesnt already exist
			playerRoom = getRoom(player.roomName, world)
			roomParts = name.split(",")
			if roomParts[1][0] == ' ': # if the first letter is a space then remove it 
				roomParts[1] = roomParts[1][1:] 
			for room in world:
				if room.name == roomParts[1]: # this means there is a room of that name already
					return None, None
			newRoom = Room(roomParts[1], int(roomParts[2]), int(roomParts[3]), [])
			
			if "left" in name: # add it to the left of this room if available
				if playerRoom.left == None:
					connectRooms(newRoom, playerRoom) # this will make the doors too
					world.append(newRoom)
					
					return Sendroom(newRoom, playerRoom, "left"), "added room"
			else: # add it to the right
				if playerRoom.right == None:
					connectRooms(playerRoom, newRoom) # this will make the doors too
					world.append(newRoom)
					
					return Sendroom(newRoom, playerRoom, "right"), "added room"

		else:
			obj = Object(name, player.x, player.y, highestId) # the new object has same pos as player
			
			highestId += 1 # add 1 to the highest id
			getRoom(player.roomName, world).roomObjects.append(obj) # add to the room we are in 
			return obj, "added object"
	return None, None
	




def getPlayer(world):

	if len(sys.argv) < 2:
		print("Please provide a username")
		quit()

	username = sys.argv[1].lower()
	if exists("save/"+username):
		return load("save/"+username)
	else:
		return Player(username, getRoom("starterRoom", world))


def load(filename):
	if not exists(filename):
		return None
	f = open(filename, mode='rb')
	data = f.read()
	f.close()
	return pickle.loads(data)


def saveAll(player, world):
	save("save/" + player.name, player)
	save("world/world.wld", world)


def save(name, thing):
	f = open(name, 'wb')
	f.write(pickle.dumps(thing))
	f.close()