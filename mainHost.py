
from client import *
from host import host
from game import game
from world import *
from player import Player


justJumped=False
loadWorld() # create the world
# connect with server 
s = host()
other_player = ""
player = Player("Joe", getRoom("starterRoom"))
gameTick = 0


while True:
	send_data(s[0], player) # the host sends the first bit of data
	
	if (other_player != ""):
		if game(player, other_player, gameTick):
			break
	
	other_player = recieve_data(s[0])
	gameTick += 1
	