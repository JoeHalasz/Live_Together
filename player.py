from world import getRoom

class Player:
	name = ""
	x = 2 # xpos 
	y = 0 # ypos
	roomName = ""
	head = "o"
	jumping = 0


	def __init__(self, _name, _room):
		self.name = _name
		self.room = _room.name
		self.y = _room.height-1 # put the player on the floor
	

	def moveLeft(self, amount):
		room = getRoom(self.roomName)
		if (self.x == 1 and room.left!=""):
			self.changeRoom(room.left, room.left.width-7)
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"

	def moveRight(self, amount):
		room = getRoom(self.roomName)
		if (self.x == room.width-7 and room.right!=""):
			self.changeRoom(self.room.right, 2)
		else:
			self.x = min(self.room.width-7, self.x+amount)
		self.head = ">"

	def moveUp(self, amount):
		self.y = max(3, self.y-1)

	def moveDown(self, amount):
		room = getRoom(self.roomName)
		self.y = max(1, room.height-1)

	def jump(self):
		room = getRoom(self.roomName)
		if self.y == room.height-1: # if we are on the ground
			self.moveUp(1)

	def changeRoom(self, newRoom, newPos):
		room = getRoom(self.roomName)
		room = newRoom.name
		self.x = newPos
