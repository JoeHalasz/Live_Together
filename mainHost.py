
from client import *
from host import host
from game import game
from world import *
import threadStuff
import threading


player, world = loadWorld() # load the world
# connect with server 
s = host()
gameTick = 0
send_world(s[0], world)

threadStuff.create(player, world)
t = threading.Thread(target=threadStuff.hostThread, args=(s[0],))
t.start()

try: # need this so that the other thread stops if there is an error
	while True:
		if (other_player != ""):
			breaking, my_actions = game(player, other_player, gameTick, world)
			if breaking:
				break
		
		if len(other_actions) != 0:
			dealWithActions(other_actions, player, world)
			other_actions = []
		globalPlayer = player
		globalWorld = world
		gameTick += 1
except:
	pass

global stop
stop = True
print("here")