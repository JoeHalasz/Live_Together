
from client import *
from game import game
from world import loadWorld


justJumped=False

# connect with server 
s = connect()
player = loadWorld()
player.x = 50

while True:
	other_player = recieve_data(s) # the client recieves the first bit of data
	
	if (other_player != ""):
		if game(player, other_player):
			break

	send_data(s, player)
