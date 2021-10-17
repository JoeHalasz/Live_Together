from world import getRoom

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
	

	def moveLeft(self, amount=1):
		room = getRoom(self.roomName)
		if (self.x == 1 and room.left!=None):
			self.changeRoom(room.left, "right")
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"

	def moveRight(self, amount=1):
		room = getRoom(self.roomName)
		if (self.x == room.width-7 and room.right!=None):
			self.changeRoom(room.right, "left")
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

	def changeRoom(self, newRoom, rightOrLeft):
		room = getRoom(self.roomName)
		if self.holding != None:
			holding = room.getObject(self.holding)
			newRoom.roomObjects.append(holding)
			holding = newRoom.getObject(self.holding) # now get the new object
		room.deleteObject(self.holding)
		if self.holding != None:
			if rightOrLeft == "right":
				holding.x = newRoom.width - 1 - holding.size[0]
			else: 
				holding.x = 1
			holding.y = newRoom.height
	
		self.roomName = newRoom.name
		if rightOrLeft == "right": # came in from the right side
			self.x = newRoom.width - 2 - 5 # player width
		else: # came in from the left side
			self.x = 1
		self.y = newRoom.height

