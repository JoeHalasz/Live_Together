from room import Room
from object import Object 
import pickle
from os.path import exists
import sys
from catBehavior import catMovement
from room import Sendroom

world = []
objects = []
highestId = 100


def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room
	print()
	print("ERROR Could not find room " + roomName)
	print("rooms are:")
	for r in world:
		print(r.name)
	quit()


from player import Player # THIS HAS TO BE BELOW getRoom


def connectRooms(leftRoom, rightRoom):
	# create the doors
	doorLeft = Object("door left", 1, rightRoom.height)
	doorRight = Object("door right", leftRoom.width-3, leftRoom.height) 

	# add the doors
	rightRoom.roomObjects.append(doorLeft)
	leftRoom.roomObjects.append(doorRight)

	# connect the rooms
	rightRoom.left = leftRoom
	leftRoom.right = rightRoom


def fix_world():
	global highestId 
	cat = Object("cat", 80, 12,1)
	cat2 = Object("small cat", 25, 12, 2)
	gianaTag = Object("Giana's Room", -6, 1, 3, centered=True) # centered means that x=0 is the center of the room instead of the left wall
	bed = Object("bed", 66, 20, 4)
	monitor = Object("monitor", 45, 20, 5)
	highestId = 100

	objects.append(cat)
	objects.append(cat2)
	objects.append(gianaTag)
	objects.append(bed)
	objects.append(monitor)

	starterRoom = Room("Starter Room", 100,12,[cat, cat2])
	leftRoom = Room("left Room", 50,8,[gianaTag])
	gianaRoom = Room("Next Room", 80,20,[gianaTag, bed, monitor])

	connectRooms(leftRoom, starterRoom)
	connectRooms(starterRoom, gianaRoom)

	world.append(starterRoom)
	world.append(leftRoom)
	world.append(gianaRoom)
	return getPlayer(), world


def loadWorld(recieved=None):
	# return fix_world()
	global highestId 
	global world
	if recieved == None:
		world = load("world/world.wld")
	else:
		world = recieved

	# remember to update highestId for new objects
	highest = 0
	for room in world:
		print()
		print(room.name)
		for obj in room.roomObjects:
			print(obj.name + " [" + str(obj.x) + " " + str(obj.y) + "]")
			if "door" not in obj.name:
				objects.append(obj)
			highest = max(highestId, obj.objectId)
	highestId = highest + 1
	player = getPlayer()
	return player, world

# this will loop through the other players actions and do them on this clients side
def dealWithActions(other_actions):
	for action in other_actions:
		if action != None:
			# if the object moved then just remove the old one and readd the new one 
			if action.name == "removed" or action.name == "moved":
				done=False
				for room in world:
					for obj in room.roomObjects:
						if (obj.objectId == action.objId):
							for o in objects: # delete object from objects
								if o.name == obj.name:
									objects.remove(o)

							room.roomObjects.remove(obj)
							done=True
							break
					if done:
						break

			if action.name == "added object" or action.name == "moved":
				getRoom(action.roomName).roomObjects.append(action.obj)
				action.obj.beingHeld = False
				objects.append(action.obj)

			if "added room" in action.name:
				# action.obj is a room object
				roomData = action.obj
				world.append(roomData.room)
				if roomData.whichSide == "left":
					connectRooms(roomData.room, roomData.connectedRoom)
				else:
					connectRooms(roomData.connectedRoom, roomData.room)


def refreshTextures():
	for room in world:
		for obj in room.roomObjects:
			obj.setDesign(obj.name) # get all the new designs


def refreshWorld(gameTick, fps):
	inc = .1 # this is times per second a stage will change 
	inc *= fps

	for o in objects:
		if "cat" in o.name or "cat" == o.name:
			catMovement(o, inc)




def addNewObject(player): # this will stop the game and prompt the user for a new object
	global highestId
	print("Please input the type of object you want to add to the world")
	print("If adding a room format it like this: room (left or right), roomName, width, height")
	name = ""
	while True: # this will ensure that there are no keyboard interupts
		try:
			name = input() # get the name of the object ( could also be a tag )
			break
		except:
			pass

	if "door" not in name:
		if "room" in name:
			playerRoom = getRoom(player.roomName)
			roomParts = name.split(",")
			newRoom = Room(roomParts[1], int(roomParts[2]), int(roomParts[3]))
			if "left" in name: # add it to the left of this room if available
				if playerRoom.left == None:
					connectRooms(newRoom, playerRoom) # this will make the doors too
					world.append(newRoom)
					return Sendroom(newRoom, playerRoom, "left")
			else: # add it to the right
				if playerRoom.right == None:
					connectRooms(playerRoom, newRoom) # this will make the doors too
					world.append(newRoom)
					return Sendroom(newRoom, playerRoom, "right")

		else:
			obj = Object(name, player.x, player.y, highestId) # the new object has same pos as player
			
			highestId += 1 # add 1 to the highest id
			objects.append(obj) # add to objects
			getRoom(player.roomName).roomObjects.append(obj) # add to the room we are in 
		return obj
	




def getPlayer():

	if len(sys.argv) < 2:
		print("Please provide a username")
		quit()

	username = sys.argv[1].lower()
	if exists("save/"+username):
		return load("save/"+username)
	else:
		return Player(username, getRoom("starterRoom"))


def load(filename):
	f = open(filename, mode='rb')
	data = f.read()
	f.close()
	return pickle.loads(data)


def saveAll(player):
	save("save/" + player.name, player)
	save("world/world.wld", world)


def save(name, thing):
	f = open(name, 'wb')
	f.write(pickle.dumps(thing))
	f.close()