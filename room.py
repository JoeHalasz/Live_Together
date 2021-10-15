import os
import sys
from designs import getDesign



def addObject(room, add, xpos, ypos):
	objectSplit = []
	
	for x in add:
		lst = (list(x)) # turn the string into a list 
		objectSplit.insert(0, lst)


	for y in range(len(objectSplit)):
		for x in range(len(objectSplit[y])):
			room[ypos-y] = room[ypos-y][:x+xpos] + objectSplit[y][x] + room[ypos-y][x+xpos+1:]
			#room[len(room)-(y+1)][x] = objectSplit[y][x]
	return room




class Room:
	name = ""
	width = 0
	height = 0
	left = ""
	right = ""
	roomObjects = [] # a lst of the different objects in the room

	def __init__(self , _name, _width=15, _height=5, objects=[]):
		self.name = _name
		self.width = max(_width,15)
		self.height = max(_height,5)
		self.roomObjects = objects


	def drawRoom(self, player, other_player):
		screenList = []
		nBuffer = 30-self.height
		for x in range(nBuffer): # white space above roof
			screenList.append('\n')
		
		screenList.append(('-'*self.width)) # roof

		line = ''
		line += '|'
		for x in range(self.width-2):
			line += ' '
		line += "|"

		for y in range(self.height):
			screenList.append(line) # the walls and inner space except the floor

		screenList.append(('-'*self.width)) # floor

		# now add all the room objects


		# now add the player
		screenList = addObject(screenList, getDesign("player"), player.x, player.y+nBuffer)
		screenList = addObject(screenList, getDesign("player"), other_player.x, other_player.y+nBuffer)

		# now add the other player


		screen=""
		for x in screenList:
			screen += x + "\n"
		screen += str(player.x) + " " + str(player.y) + "\n"
		
		sys.stdout.write("%s" % screen)
		sys.stdout.flush()

