from room import Room
from player import Player


def loadWorld():
	starterRoom = Room("Starter Room", 100,12)
	nextRoom = Room("Next Room", 50,8)

	starterRoom.left = nextRoom
	nextRoom.right = starterRoom

	player = Player("Joe", starterRoom)

	return player