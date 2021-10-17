
from client import *
from host import host
from game import game
from world import *


player, world = loadWorld() # load the world
# connect with server 
s = host()
other_player = ""

gameTick = 0
my_actions = []
send_world(s[0], world)

while True:
	send_data(s[0], player, my_actions) # the host sends the first bit of data
	my_actions = [] # reset my actions 
	if (other_player != ""):
		breaking, my_actions = game(player, other_player, gameTick)
		if breaking:
			break
	
	other_player, other_actions = recieve_data(s[0], player)
	dealWithActions(other_actions)
	gameTick += 1
	