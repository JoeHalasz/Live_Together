from room import Room
from player import Player
from time import sleep
import keyboard
from client import *
from world import getRoom
from world import refreshWorld


def movement(player):
	global justJumped
	speed = 1
	done = False
	player.moveDown(1) # gravity

	if keyboard.is_pressed('shift'):
		speed=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(speed)
	if keyboard.is_pressed('d'):
		player.moveRight(speed)
	if keyboard.is_pressed('s'):
		player.design = "player crouch"
	else:
		player.design = "player"

	if keyboard.is_pressed(" "): # this has to be last other than quit
		if not justJumped:
			player.jump()
		justJumped=True
		return done
	if keyboard.is_pressed('q'):
		player.moveRight(speed)
		done = True

	justJumped = False
	return done




def game(player, other_player, gameTick):

	refreshWorld(gameTick)

	done = movement(player)

	getRoom(player.roomName).drawRoom(player, other_player)

	sleep(1/20)

	return done

