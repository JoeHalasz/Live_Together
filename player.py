

class Player:
	name = ""
	x = 2 # xpos 
	y = 0 # ypos
	room = ""
	head = "o"
	jumping = 0


	def __init__(self, _name, _room):
		self.name = _name
		self.room = _room
		self.y = _room.height-1 # put the player on the floor
	

	def moveLeft(self, amount):
		if (self.x == 1 and self.room.left!=""):
			self.changeRoom(self.room.left, self.room.left.width-7)
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"

	def moveRight(self, amount):
		if (self.x == self.room.width-7 and self.room.right!=""):
			self.changeRoom(self.room.right, 2)
		else:
			self.x = min(self.room.width-7, self.x+amount)
		self.head = ">"

	def moveUp(self, amount):
		self.y = max(3, self.y-1)

	def moveDown(self, amount):
		self.y = max(1, self.room.height-1)

	def jump(self):
		if self.y == self.room.height-1: # if we are on the ground
			self.moveUp(1)

	def changeRoom(self, newRoom, newPos):
		self.room = newRoom
		self.x = newPos
