from world import getRoom
from action import Action



class Player:
	name = ""
	x = 2 # xpos 
	y = 0 # ypos
	roomName = ""
	head = "o"
	jumpState = 0
	design = "player" # this is for the current design that should be drawn
	holding = None


	def __init__(self, _name, _room):
		self.name = _name
		self.roomName = _room.name
		self.y = _room.height-2 # put the player on the floor
	

	def moveLeft(self, my_actions, amount=1):
		room = getRoom(self.roomName)
		if (self.x == 1 and room.left!=""):
			self.changeRoom(room.left, room.left.width-7, room.left.height)
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"
		self.move_holding(my_actions)

	def moveRight(self, my_actions, amount=1):
		room = getRoom(self.roomName)
		if (self.x == room.width-7 and room.right!=""):
			self.changeRoom(room.right, 2, room.right.height)
		else:
			self.x = min(room.width-7, self.x+amount)
		self.head = ">"
		self.move_holding(my_actions)

	def moveUp(self, my_actions, amount=1):
		self.y = max(3, self.y-amount)
		self.move_holding(my_actions)

	def moveDown(self, my_actions, amount=1):
		room = getRoom(self.roomName)
		self.y = min(self.y+amount, room.height)
		self.move_holding(my_actions)

	def move_holding(self, my_actions):
		if self.holding != None:
			obj = getRoom(self.roomName).getObject(self.holding)
			obj.x = self.x
			obj.y = self.y
			my_actions.append(Action("moved", self.roomName, obj))

	def jump(self, my_actions, amount=1):
		room = getRoom(self.roomName)
		self.moveUp(my_actions, amount)

	def changeRoom(self, newRoom, newPosX, newPosY):
		room = getRoom(self.roomName)
		if self.holding != None:
			holding = room.getObject(self.holding)
			newRoom.roomObjects.append(holding)
		room.deleteObject(self.holding)
		if self.holding != None:
			holding = newRoom.getObject(self.holding) # now get the new object
			holding.x = newPosX
			holding.y = newPosY
		self.roomName = newRoom.name
		self.x = newPosX
		self.y = newPosY

