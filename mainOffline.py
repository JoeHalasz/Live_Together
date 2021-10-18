
from client import *
from game import *
from world import *
from player import Player
import time

player, world= loadWorld() # load the world
gameTick = 0
printing = False
oldTime = time.perf_counter()
while True:
	if time.perf_counter() - oldTime >= (1/fps):
		sys.stdout.write("%s" % str(round(1/(time.perf_counter() - oldTime), 2)))
		if game(player, None, gameTick, world)[0]:
			break

		gameTick += 1
		oldTime = time.perf_counter()
