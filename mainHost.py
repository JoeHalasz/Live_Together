from client import *
from host import host
from game import game
from world import *
import threading
import traceback


other_player = ""
other_actions = []
my_actions = []
sendStage = 0
player = ""
world = ""
breaking = False


def hostThread(s): # this is going to send then recieve the sendData
	while True:
		global my_actions
		global other_player
		global other_actions
		send_data(s, player, my_actions) # the host sends the first bit of data
		my_actions = []
		other_player, other_actions = recieve_data(s, player, world)
		if breaking:
			break





def main():
	global my_actions
	global other_player
	global other_actions
	global player
	global world
	global breaking

	player, world = loadWorld() # load the world
	# connect with server 
	s = host()
	gameTick = 0
	send_world(s[0], world)

	t = threading.Thread(target=hostThread, args=(s[0],))
	t.start()

	try: # need this so that the other thread stops if there is an error
		while True:
			
			breaking, my_actions = game(player, other_player, gameTick, world)
			if breaking:
				break
			
			if len(other_actions) != 0:
				dealWithActions(other_actions, player, world)
				other_actions = []
			gameTick += 1
	
	except Exception as e:
		print(traceback.format_exc())


if __name__ == '__main__':
	main()