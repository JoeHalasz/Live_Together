
from client import *
from game import game
from world import *
from player import Player

justJumped=False
loadWorld() # create the world
# connect with server 
player = Player("Joe", getRoom("starterRoom"))
player.x = 50
gameTick = 0


while True:
	
	if game(player, None, gameTick):
		break

	gameTick += 1
