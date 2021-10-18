
from client import *
from game import *
from world import *
import threading
import traceback
import time

other_player = ""
other_actions = []
my_actions = []
sendStage = 0
player = ""
world = ""
breaking = False


def clientThread(s): # this is going to recieve then send the sendData
	while True:
		global my_actions
		global other_player
		global other_actions

		other_player, new_other_actions = recieve_data(s, player, world)
		for o in new_other_actions:
			if o != None:
				other_actions.append(o)
		send_data(s, player, my_actions) # the host sends the first bit of data
		my_actions = []
		if breaking:
			break
	


def main():
	global my_actions
	global other_player
	global other_actions
	global player
	global world
	global breaking

	# connect with server 
	s = connect()
	player, world = recieve_world(s) # this will download the world from the other player

	gameTick = 0
	my_actions = []

	t = threading.Thread(target=clientThread, args=(s,))
	t.start()
	
	oldTime = time.perf_counter()
	
	try: # need this so that the other thread stops if there is an error
		while True:
			if time.perf_counter() - oldTime > (1/fps):
				if len(other_actions) != 0:
					dealWithActions(other_actions, player, world)
					other_actions = []
				
				breaking, my_actions = game(player, other_player, gameTick, world)
				if breaking:
					break
				gameTick += 1
				oldTime = time.perf_counter()	
	except Exception as e:
		print(traceback.format_exc())


if __name__ == '__main__':
	main()