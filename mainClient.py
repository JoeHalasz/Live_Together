
from client import *
from game import game
from world import *
import time

# connect with server 
s = connect()
player, world = recieve_world(s) # this will download the world from the other player

gameTick = 0
my_actions = []


while True:
	timebefore = time.perf_counter()
	other_player, other_actions = recieve_data(s, player, world) # the client recieves the first bit of data
	timeAfterRecieve = time.perf_counter()
	dealWithActions(other_actions, player, world)
	timeAfterActions = time.perf_counter()
	if (other_player != ""):
		breaking, my_actions = game(player, other_player, gameTick, world)
		if breaking:
			break
	timeAfterLoop = time.perf_counter()
	send_data(s, player, my_actions)
	timeAfterSend = time.perf_counter()
	my_actions = [] # reset my actions 
	gameTick += 1
	timeForRecieve = timebefore - timeAfterRecieve
	timeForActions = timeAfterRecieve - timeAfterActions
	timeForLoop = timeAfterRecieve - timeAfterLoop
	timeForSend = timeAfterRecieve - timeAfterSend

	print()
	print("Time for send: " + str(timeForSend))
	print("Time for Loop: " + str(timeForLoop))
	print("Time for recv: " + str(timeForRecieve))
	print("Time for acts: " + str(timeForActions))