from room import Room

world = []

def getRoom(roomName):
	for room in world:
		if room.name.replace(" ", "").lower() == roomName.replace(" ", "").lower():
			return room


def loadWorld():

	starterRoom = Room("Starter Room", 100,12,[])
	nextRoom = Room("Next Room", 50,8,[])

	
	starterRoom.left = nextRoom
	nextRoom.right = starterRoom

	
	world.append(starterRoom)
	world.append(nextRoom)
