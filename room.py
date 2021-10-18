import os
import sys
from designs import getDesign
from object import Object


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
				#if int(ypos)-y < len(room):
				room[int(ypos)-y] = room[int(ypos)-y][:x+int(xpos)] + objectSplit[y][x] + room[int(ypos)-y][x+int(xpos)+1:]
	return room




class Room:
	name = ""
	width = 0
	height = 0
	left = None # this is the actual room object
	right = None # this is the actual room object
	roomObjects = [] # a lst of the different objects in the room


	def __init__(self , _name, _width=15, _height=5, _roomObjects=[]):
		self.name = _name
		self.width = min(max(_width,15), 100)
		self.height = min(max(_height,5), 26)
		hasTag = False
		for o in _roomObjects:
			if o.name == _name:
				hasTag = True
				break
		if not hasTag:
			tag = Object(_name, -1*int(len(_name)/2), 1,centered=True)
			_roomObjects.append(tag)
		self.roomObjects = _roomObjects
		if len(self.roomObjects) == len(_roomObjects) or len(self.roomObjects)-1 == len(_roomObjects):
			pass
		else:
			raise Exception("dont use python")


	def deleteObject(self, objectId):
		for o in self.roomObjects:
			if o.objectId == objectId:
				self.roomObjects.remove(o)
				break

	def deleteObjectByName(self, name): # ONLY USE THIS FOR DOORS PLEASE 
		for o in self.roomObjects:
			if o.name == name:
				self.roomObjects.remove(o)
				break

	def getObject(self, objectId):
		for o in self.roomObjects:
			if o.objectId == objectId:
				return o

	def addRoom(self, otherRoom, leftOrRight, hasDoors=False):
		if leftOrRight == "left":
			self.left = otherRoom
			if not hasDoors:
				self.roomObjects.append(Object("door left", 1, self.height) )
		else:
			self.right = otherRoom
			if not hasDoors:
				self.roomObjects.append(Object("door right", self.width-3, self.height) )


	def drawRoom(self, player, world, other_player=None):
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
		
		#sys.stdout.write("%s" % screen)
		#sys.stdout.flush()



class Sendroom():
	whichSide = None
	connectedRoom = None
	room = None

	def __init__(self, room, connectedRoom, whichSide):
		self.room = room
		self.connectedRoom = connectedRoom
		self.whichSide = whichSide