from room import Room
from object import Object 
from designs import getDesign


world = []
cats = []


def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room


def loadWorld():

	cat = Object("cat", getDesign("cat"), 50, 12)
	cat2 = Object("small cat", getDesign("small cat"), 25, 12)

	starterRoom = Room("Starter Room", 100,12,[cat, cat2])
	nextRoom = Room("Next Room", 50,8,[])

	
	starterRoom.left = nextRoom
	nextRoom.right = starterRoom

	
	world.append(starterRoom)
	world.append(nextRoom)
	cats.append(cat)
	cats.append(cat2)


def refreshWorld(gameTick):
	for cat in cats:
		if (gameTick%20 == 0):
			cat.x += 1
		elif (gameTick%20 == 10):
			cat.x -= 1

