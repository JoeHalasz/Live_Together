

class Player:
	name = ""
	x = 0 # xpos 
	y = 0 # ypos
	room = ""
	head = "o"
	jumping = 0


	def __init__(self, _name, _room):
		self.name = _name
		self.room = _room
		self.y = _room.height-1 # put the player on the floor
	

	def moveLeft(self, amount):
		self.x = max(1, self.x-amount)
		self.head = "<"


	def moveRight(self, amount):
		self.x = min(self.room.width-8, self.x+amount)
		self.head = ">"

	def moveUp(self, amount):
		self.y = max(3, self.y-1)

	def moveDown(self, amount):
		self.y = max(1, self.room.height-1)

	def jump(self):
		pass

