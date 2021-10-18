
from client import *
from game import game
from world import *
import threadStuff
import threading


# connect with server 
s = connect()
player, world = recieve_world(s) # this will download the world from the other player

gameTick = 0
my_actions = []

threadStuff.create(player, world)
t = threading.Thread(target=threadStuff.clientThread, args=(s,))
t.start()

try: # need this so that the other thread stops if there is an error
	while True:
		if len(other_actions) != 0:
			dealWithActions(other_actions, player, world)
			other_actions = []
		if (other_player != ""):
			breaking, my_actions = game(player, other_player, gameTick, world)
			if breaking:
				break
		globalPlayer = player
		globalWorld = world
		gameTick += 1
except:
	pass

global stop
stop = True
print("here")