from room import Room
from player import Player
from time import sleep
import keyboard
from client import *
from world import *
from action import Action


fps = 60


def handleHolding(player, moved):
	room = getRoom(player.roomName)
	
	if keyboard.is_pressed('e'): # this has to happen after all player movement
		if player.holding == None:
			for o in room.roomObjects:
				if "door" not in o.name: # dont wanna move doors
					if o.checkCollidingPlayer(player):
						player.holding = o.name
						o.beingHeld = True # this will stop it from doing any animations
						break
		if (player.holding != None):
			obj = room.getObject(player.holding)
			if obj != None: # make sure that the other player did not move the object to another room
				if moved == "left" and obj.x > 2:
					obj.x = player.x
				if moved == "right" and obj.x+obj.size[0] < room.width-2:
					obj.x = player.x
				if moved != "none":
					if obj.y > 1:
						obj.y = player.y
					return Action("moved", player.roomName, obj)

	else:
		if (player.holding != None):
			room.getObject(player.holding).beingHeld = False
			player.holding = None



def handleJumps(player):
	my_actions = []
	moved = "none"
	room = getRoom(player.roomName)

	if keyboard.is_pressed(" ") and player.y == room.height: # player is on ground and pressed space
		player.jumpState = 6	

	if player.jumpState > 0:
		player.jump(.5)
		player.jumpState -= 1
		moved = "up"

	if (player.jumpState == 0): # this has to happen after jump so that the player hits the ground before next jump
		player.moveDown(.5) # gravity
		moved = "down"

	return moved



def movement(player):
	speed = 1
	done = False
	room = getRoom(player.roomName)
	my_actions = []
	moved = handleJumps(player)

	if keyboard.is_pressed('p'):  
		refreshTextures()
	if keyboard.is_pressed('shift'):
		speed*=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(speed)
		moved = "left"
	if keyboard.is_pressed('d'):
		player.moveRight(speed)
		moved = "right"
	room = getRoom(player.roomName) # the player might have changed rooms
	if keyboard.is_pressed('s'):
		player.design = "player crouch"
	else:
		player.design = "player"

	if keyboard.is_pressed('r'):
		obj = room.getObject("small cat")
		try:
			objects.remove(obj)
		except:
			pass
		if obj != None:
			my_actions.append(Action("removed", player.roomName, obj))
			room.deleteObject("small cat")


	my_actions.append(handleHolding(player, moved))

	if keyboard.is_pressed('q'):
		save(player)
		done = True

	return done, my_actions




def game(player, other_player, gameTick):

	refreshWorld(gameTick, fps)

	done, my_actions = movement(player)

	getRoom(player.roomName).drawRoom(player, other_player)

	sleep(1/fps)

	return done, my_actions

