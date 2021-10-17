
from client import *
from game import game
from world import *

# connect with server 
s = connect()
player = recieve_world(s) # this will download the world from the other player

gameTick = 0
my_actions = []


while True:
	other_player, other_actions = recieve_data(s, player) # the client recieves the first bit of data
	dealWithActions(other_actions)
	if (other_player != ""):
		breaking, my_actions = game(player, other_player, gameTick)
		if breaking:
			break

	send_data(s, player, my_actions)
	my_actions = [] # reset my actions 
	gameTick += 1
