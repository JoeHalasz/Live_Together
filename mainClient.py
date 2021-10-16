
from client import *
from game import game
from world import *
from player import Player

justJumped=False
loadWorld() # create the world
# connect with server 
s = connect()
player = Player("Joe", getRoom("starterRoom"))
player.x = 50
gameTick = 0

while True:
	other_player = recieve_data(s) # the client recieves the first bit of data
	dealWithActions()
	if (other_player != ""):
		if game(player, other_player, gameTick):
			break

	send_data(s, player, my_actions)
	my_actions = [] # reset my actions 
	gameTick += 1
