import os
import sys
from designs import getDesign



def addObject(room, add, xpos, ypos, isCenteredOBJ=False, realRoom=None):
	objectSplit = []
	
	for x in add:
		lst = (list(x)) # turn the string into a list 
		objectSplit.insert(0, lst)

	if (isCenteredOBJ):
		xpos = xpos+int(realRoom.width/2) # move x=0 to the center of the room

	for y in range(len(objectSplit)):
		for x in range(len(objectSplit[y])):
			if (objectSplit[y][x] != " "):
				room[int(ypos)-y] = room[int(ypos)-y][:x+int(xpos)] + objectSplit[y][x] + room[int(ypos)-y][x+int(xpos)+1:]
	return room




class Room:
	name = ""
	width = 0
	height = 0
	left = ""
	right = ""
	roomObjects = [] # a lst of the different objects in the room

	def __init__(self , _name, _width=15, _height=5, _roomObjects=[]):
		self.name = _name
		self.width = max(_width,15)
		self.height = max(_height,5)
		self.roomObjects = _roomObjects


	def deleteObject(self, name):
		for o in self.roomObjects:
			if o.name == name:
				self.roomObjects.remove(o)
				break

	def getObject(self, name):
		for o in self.roomObjects:
			if o.name == name:
				return o

	def drawRoom(self, player, other_player=None):
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
		for o in self.roomObjects:
			screenList = addObject(screenList, o.getDesign(), o.x, o.y+nBuffer, o.centered, self)

		# now add the player
		screenList = addObject(screenList, getDesign(player.design, head=player.head), player.x, player.y+nBuffer)

		# now add the other player if they are in the same room
		if (other_player!=None and self.name == other_player.roomName):
			screenList = addObject(screenList, getDesign(other_player.design, head=other_player.head), other_player.x, other_player.y+nBuffer)


		screen=""
		for x in screenList:
			screen += x + "\n"
		#screen += str(player.x) + " " + str(player.y) + "\n"
		
		
		sys.stdout.write("%s" % screen)
		sys.stdout.flush()

