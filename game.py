from room import Room
from player import Player
from time import sleep
import keyboard
from client import *
from world import *
from action import Action
from room import Sendroom


fps = 60


def handleHolding(player, moved, world):
	room = getRoom(player.roomName, world)
	
	if keyboard.is_pressed('e'): # this has to happen after all player movement
		if player.holding == None:
			for o in room.roomObjects:
				if "door" not in o.name: # dont wanna move doors
					if o.checkCollidingPlayer(player):
						player.holding = o.objectId
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



def handleJumps(player, world):
	my_actions = []
	moved = "none"
	room = getRoom(player.roomName, world)

	if keyboard.is_pressed(" ") and player.y == room.height: # player is on ground and pressed space
		player.jumpState = 6	

	if player.jumpState > 0:
		player.jump(world, .5)
		player.jumpState -= 1
		moved = "up"

	if (player.jumpState == 0): # this has to happen after jump so that the player hits the ground before next jump
		player.moveDown(world, .5) # gravity
		moved = "down"

	return moved



def movement(player, world):
	speed = 1
	done = False
	try:
		room = getRoom(player.roomName, world)
	except:
		room = world[0]
		player.roomName = room.name
	my_actions = []
	moved = handleJumps(player, world)

	if keyboard.is_pressed('p'):
		refreshTextures(world)
	if keyboard.is_pressed('tab'):
		obj, actionName = addNewObject(player, world)
		if obj != None:
			my_actions.append(Action(actionName, player.roomName, obj))

	if keyboard.is_pressed('shift'):
		speed*=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(world, speed)
		moved = "left"
	if keyboard.is_pressed('d'):
		player.moveRight(world, speed)
		moved = "right"
	room = getRoom(player.roomName, world) # the player might have changed rooms
	if keyboard.is_pressed('s'):
		player.design = "player crouch"
	else:
		player.design = "player"
	
	if keyboard.is_pressed('j'):
		saveAll(player, world)

	if keyboard.is_pressed('r'):
		obj = None
		for o in room.roomObjects:
			if "door" not in o.name: # dont wanna move doors
				if o.checkCollidingPlayer(player):
					obj = o
					break
		if obj != None:
			room.deleteObject(obj.objectId)
			my_actions.append(Action("removed", player.roomName, obj))


	my_actions.append(handleHolding(player, moved, world))

	if keyboard.is_pressed('q'):
		saveAll(player, world)
		done = True

	return done, my_actions




def game(player, other_player, gameTick, world):

	refreshWorld(gameTick, fps, player, world)

	done, my_actions = movement(player, world)

	getRoom(player.roomName, world).drawRoom(player, world, other_player)

	sleep(1/fps)

	return done, my_actions

