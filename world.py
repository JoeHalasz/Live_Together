from room import Room
from object import Object 


world = []
cats = []


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

	cat = Object("cat", 80, 12,1)
	cat2 = Object("small cat", 25, 12, 2)
	gianaTag = Object("Giana's Room", -6, 1, 3, centered=True) # centered means that x=0 is the center of the room instead of the left wall
	bed = Object("bed", 66, 20, 4)
	monitor = Object("monitor", 45, 20, 5)

	cats.append(cat)
	cats.append(cat2)

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
							room.roomObjects.remove(obj)
							done=True
							break
					if done:
						break

			if action.name == "added" or action.name == "moved":
				getRoom(action.roomName).roomObjects.append(action.obj)
				action.obj.beingHeld = False
				if "cat" in action.obj.name:
					cats.append(action.obj)


def refreshTextures():
	for room in world:
		for obj in room.roomObjects:
			obj.setDesign(obj.name) # get all the new designs


def refreshWorld(gameTick, fps):
	inc = .1 # this is times per second a stage will change 
	inc *= fps

	for cat in cats:
		reset = False
		if not cat.beingHeld:
			if cat.actionStage == inc*2:
				cat.x += 1
			elif cat.actionStage == inc*4:
				cat.x -= 1
			elif cat.actionStage == inc*6:
				cat.x += 1
			elif cat.actionStage == inc*8:
				cat.x -= 1
			elif cat.actionStage == inc*10:
				cat.x += 1
			elif cat.actionStage == inc*12:
				cat.x -= 1
			elif cat.actionStage == inc*14:
				cat.x += 1
			elif cat.actionStage == inc*16:
				cat.x -= 1
			elif cat.actionStage == inc*17:
				cat.y -= 1
				cat.x += 1
			elif cat.actionStage == inc*18:
				cat.y += 1
				cat.x += 1
				cat.actionStage += 1
			elif cat.actionStage == inc*19:
				cat.y -= 1
				cat.x -= 1
			elif cat.actionStage == inc*20:
				cat.y += 1
				cat.x -= 1
				cat.actionStage = 0
				cat.flip()
		cat.actionStage += 1

		


