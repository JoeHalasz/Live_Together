from room import Room
from player import Player


starterRoom = Room("Starter Room", 100,12,[])
nextRoom = Room("Next Room", 50,8,[])



def getRoom(roomName):
	for room in rooms:
		if (room.name == roomName):
			return room


def loadWorld():
	
	starterRoom.left = nextRoom
	nextRoom.right = starterRoom

	player = Player("Joe", starterRoom)


	return player