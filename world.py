from room import Room
from object import Object 
from designs import getDesign


world = []
cats = []
catJumpTimer = 0

def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room


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

	cat = Object("cat", 80, 12)
	cat2 = Object("small cat", 25, 12)
	gianaTag = Object("Giana's Room", -6, 1, centered=True) # centered means that x=0 is the center of the room instead of the left wall

	cats.append(cat)
	cats.append(cat2)

	starterRoom = Room("Starter Room", 100,12,[cat, cat2])
	leftRoom = Room("left Room", 50,8,[gianaTag])
	rightRoom = Room("Next Room", 80,20,[gianaTag])

	connectRooms(leftRoom, starterRoom)
	connectRooms(starterRoom, rightRoom)

	world.append(starterRoom)
	world.append(leftRoom)
	world.append(rightRoom)

	


def refreshWorld(gameTick, fps):
	global catJumpTimer
	
	catJumpTimer+=1

	if (catJumpTimer >= fps*4.8):
		for cat in cats:
			if (catJumpTimer == fps*4.8):
				cat.y -= 1
			elif (catJumpTimer == fps*4.9):
				cat.x += 2
			elif (catJumpTimer == fps*5):
				cat.y += 1
			elif (catJumpTimer == fps*5.1):
				cat.y -= 1
			elif (catJumpTimer == fps*5.2):
				cat.x -= 2
			elif (catJumpTimer == fps*5.3):
				cat.y += 1
			elif (catJumpTimer == fps*5.4):
				catJumpTimer = 0 # reset the cat jump timer
	else:
		for cat in cats:
			if (gameTick%fps == 0):
				cat.x += 1
			elif (gameTick%fps == fps/2):
				cat.x -= 1

		


