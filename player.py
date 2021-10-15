from world import getRoom

class Player:
	name = ""
	x = 2 # xpos 
	y = 0 # ypos
	roomName = ""
	head = "o"
	jumpState = 0
	design = "player" # this is for the current design that should be drawn


	def __init__(self, _name, _room):
		self.name = _name
		self.roomName = _room.name
		self.y = _room.height-2 # put the player on the floor
	

	def moveLeft(self, amount=1):
		room = getRoom(self.roomName)
		if (self.x == 1 and room.left!=""):
			self.changeRoom(room.left, room.left.width-7, room.left.height)
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"

	def moveRight(self, amount=1):
		room = getRoom(self.roomName)
		if (self.x == room.width-7 and room.right!=""):
			self.changeRoom(room.right, 2, room.right.height)
		else:
			self.x = min(room.width-7, self.x+amount)
		self.head = ">"

	def moveUp(self, amount=1):
		self.y = max(3, self.y-amount)

	def moveDown(self, amount=1):
		room = getRoom(self.roomName)
		self.y = min(self.y+amount, room.height)

	def jump(self, amount=1):
		room = getRoom(self.roomName)
		self.moveUp(amount)

	def changeRoom(self, newRoom, newPosX, newPosY):
		room = getRoom(self.roomName)
		self.roomName = newRoom.name
		self.x = newPosX
		self.y = newPosY

