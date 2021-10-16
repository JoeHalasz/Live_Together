from room import Room
from player import Player
from time import sleep
import keyboard
from client import *
from world import getRoom
from world import refreshWorld
from action import Action


fps = 60

def movement(player):
	global justJumped
	my_actions = []
	speed = 1
	done = False
	
	if keyboard.is_pressed('shift'):
		speed*=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(speed)
	if keyboard.is_pressed('d'):
		player.moveRight(speed)
	if keyboard.is_pressed('s'):
		player.design = "player crouch"
	else:
		player.design = "player"

	if keyboard.is_pressed('e'):
		obj = getRoom(player.roomName).getObject("small cat")
		if obj != None:
			my_actions.append(Action("removed", player.roomName, obj))
			getRoom(player.roomName).deleteObject("small cat")

	if keyboard.is_pressed(" ") and player.y == getRoom(player.roomName).height: # player is on ground and pressed space
		player.jumpState = 6
	
	if keyboard.is_pressed('q'):
		player.moveRight(speed)
		done = True

	if player.jumpState > 0:
		player.jump(.5)
		player.jumpState -= 1

	if (player.jumpState == 0): # this has to happen after jump so that the player hits the ground before next jump
		player.moveDown(.5) # gravity

	return done, my_actions




def game(player, other_player, gameTick):

	refreshWorld(gameTick, fps)

	done, my_actions = movement(player)

	getRoom(player.roomName).drawRoom(player, other_player)

	sleep(1/fps)

	return done, my_actions

