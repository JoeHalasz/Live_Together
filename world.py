from room import Room
from object import Object 
from designs import getDesign


world = []
cats = []


def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room


def connectRooms(leftRoom, rightRoom):
	# create the doors
	doorLeft = Object("door left", getDesign("door left"), 1, rightRoom.height)
	doorRight = Object("door right", getDesign("door left"), leftRoom.width-3, leftRoom.height) 

	# add the doors
	rightRoom.roomObjects.append(doorLeft)
	leftRoom.roomObjects.append(doorRight)

	# connect the rooms
	rightRoom.left = leftRoom
	leftRoom.right = rightRoom






def loadWorld():

	

	cat = Object("cat", getDesign("cat"), 50, 12)
	cat2 = Object("small cat", getDesign("small cat"), 25, 12)

	starterRoom = Room("Starter Room", 100,12,[cat, cat2])
	leftRoom = Room("left Room", 50,8,[])
	rightRoom = Room("Next Room", 80,20,[])

	
	connectRooms(leftRoom, starterRoom)
	connectRooms(starterRoom, rightRoom)

	world.append(starterRoom)
	world.append(leftRoom)
	world.append(rightRoom)
	cats.append(cat)
	cats.append(cat2)


def refreshWorld(gameTick):
	for cat in cats:
		if (gameTick%20 == 0):
			cat.x += 1
		elif (gameTick%20 == 10):
			cat.x -= 1

