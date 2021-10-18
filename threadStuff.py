from client import *


my_actions = []
other_actions = []
other_player = ""
sendStage = 0
globalPlayer = ""
currentWorld = ""
stop = False


def hostThread(s): # this is going to send then recieve the sendData
	while True:
		global other_player
		global other_actions
		global my_actions
		send_data(s, globalPlayer, my_actions) # the host sends the first bit of data
		my_actions = []
		other_player, other_actions = recieve_data(s, globalPlayer, currentWorld)
		if stop:
			break


def clientThread(s): # this is going to recieve then send the sendData
	while True:
		global other_player
		global other_actions
		global my_actions
		other_player, other_actions = recieve_data(s, globalPlayer, currentWorld)
		send_data(s, globalPlayer, my_actions) # the host sends the first bit of data
		my_actions = []
		if stop:
			break
	


def create(player, world):
	global globalPlayer
	global globalWorld
	globalPlayer = player
	globalWorld = world
