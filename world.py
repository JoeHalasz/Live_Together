from room import Room
from object import Object 
import pickle
from os.path import exists
import sys


world = []
objects = []


def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room


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




def loadWorld():

	cat = Object("cat", 80, 12,1)
	cat2 = Object("small cat", 25, 12, 2)
	gianaTag = Object("Giana's Room", -6, 1, 3, centered=True) # centered means that x=0 is the center of the room instead of the left wall
	bed = Object("bed", 66, 20, 4)
	monitor = Object("monitor", 45, 20, 5)

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

			if action.name == "added" or action.name == "moved":
				getRoom(action.roomName).roomObjects.append(action.obj)
				action.obj.beingHeld = False
				objects.append(action.obj)


def refreshTextures():
	for room in world:
		for obj in room.roomObjects:
			obj.setDesign(obj.name) # get all the new designs


def refreshWorld(gameTick, fps):
	inc = .1 # this is times per second a stage will change 
	inc *= fps

	for o in objects:
		if "cat" in o.name:
			reset = False
			if not o.beingHeld:
				if o.actionStage == inc*2:
					o.x += 1
				elif o.actionStage == inc*4:
					o.x -= 1
				elif o.actionStage == inc*6:
					o.x += 1
				elif o.actionStage == inc*8:
					o.x -= 1
				elif o.actionStage == inc*10:
					o.x += 1
				elif o.actionStage == inc*12:
					o.x -= 1
				elif o.actionStage == inc*14:
					o.x += 1
				elif o.actionStage == inc*16:
					o.x -= 1
				elif o.actionStage == inc*17:
					o.y -= 1
					o.x += 1
				elif o.actionStage == inc*18:
					o.y += 1
					o.x += 1
					o.actionStage += 1
				elif o.actionStage == inc*19:
					o.y -= 1
					o.x -= 1
				elif o.actionStage == inc*20:
					o.y += 1
					o.x -= 1
					o.actionStage = 0
					o.flip()
			o.actionStage += 1


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
	# save the world


def save(name, thing):
	f = open(name, 'wb')
	f.write(pickle.dumps(thing))
	f.close()