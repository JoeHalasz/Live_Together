
from client import *
from game import game
from world import *
from player import Player

justJumped=False
loadWorld() # create the world
# connect with server 
s = connect()
player = Player("Joe", getRoom("starterRoom"))
player.x = 50

while True:
	other_player = recieve_data(s) # the client recieves the first bit of data
	
	if (other_player != ""):
		if game(player, other_player, world):
			break

	send_data(s, player)
