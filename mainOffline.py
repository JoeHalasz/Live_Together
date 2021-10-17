
from client import *
from game import game
from world import *
from player import Player

player, world = loadWorld() # load the world
gameTick = 0


while True:
	
	if game(player, None, gameTick)[0]:
		break

	gameTick += 1
