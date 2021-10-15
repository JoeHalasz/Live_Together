from room import Room
from player import Player



def getDesign(name):
	if (name == "player"):
		return ["  o  "
				"_/*\\_"
				"  *  "
				"_/ \\_"
				]
	if (name == "playerleft"):
		return ["  <  "
				"_/*\\_"
				"  *  "
				"_/ \\_"
				]
	if (name == "playerright"):
		return ["  >  "
				"_/*\\_"
				"  *  "
				"_/ \\_"
				]
	if (name == "cat"):

		return [
				"\\    /\\",
				" )  ( ')",
				"(  /  )",
				" \\(__)|"
				]




def loadWorld():
	starterRoom = Room("Starter Room", 100,12)
	nextRoom = Room("Next Room", 50,8)

	starterRoom.left = nextRoom
	nextRoom.right = starterRoom

	player = Player("Joe", starterRoom)

	return player