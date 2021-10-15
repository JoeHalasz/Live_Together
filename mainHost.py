
from client import *
from host import host
from main import main
from world import loadWorld

justJumped=False

loadWorld()
# connect with server 
s = host()
other_player = ""
player = loadWorld()

while True:
	send_data(s[0], player) # the host sends the first bit of data
	
	if (other_player != ""):
		if main(player, other_player):
			break
	
	other_player = recieve_data(s[0])
	