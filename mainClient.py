
from client import *
from game import game
from world import *

# connect with server 
s = connect()
player, world = recieve_world(s) # this will download the world from the other player

gameTick = 0
my_actions = []


while True:
	other_player, other_actions = recieve_data(s, player, world) # the client recieves the first bit of data
	dealWithActions(other_actions, player, world)
	if (other_player != ""):
		breaking, my_actions = game(player, other_player, gameTick, world)
		if breaking:
			break

	send_data(s, player, my_actions)
	my_actions = [] # reset my actions 
	gameTick += 1
