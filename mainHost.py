
from client import *
from host import host
from game import game
from world import *
import time

player, world = loadWorld() # load the world
# connect with server 
s = host()
other_player = ""
gameTick = 0
my_actions = []
send_world(s[0], world)

while True:
	timebefore = time.perf_counter()
	send_data(s[0], player, my_actions) # the host sends the first bit of data
	timeAfterSend = time.perf_counter()
	my_actions = [] # reset my actions 
	if (other_player != ""):
		breaking, my_actions = game(player, other_player, gameTick, world)
		if breaking:
			break
	timeAfterLoop = time.perf_counter()
	other_player, other_actions = recieve_data(s[0], player, world)
	timeAfterRecieve = time.perf_counter()
	dealWithActions(other_actions, player, world)
	gameTick += 1
	timeAfterActions = time.perf_counter()

	timeForSend = timeAfterSend - timebefore
	timeForLoop = timeAfterLoop - timeAfterSend
	timeForRecieve = timeAfterRecieve - timeAfterLoop
	timeForActions = timeAfterActions - timeAfterRecieve
	print()
	print("Time for send: " + str(timeForSend))
	print("Time for Loop: " + str(timeForLoop))
	print("Time for recv: " + str(timeForRecieve))
	print("Time for acts: " + str(timeForActions))


	