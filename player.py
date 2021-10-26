from world import getRoom

class Player:
	name = ""
	x = 2 # xpos 
	y = 0 # ypos
	roomName = ""
	head = "o"
	jumpState = 0
	design = "player" # this is for the current design that should be drawn
	holding = None # this is the actual object 


	def __init__(self, _name, _room):
		self.name = _name
		self.roomName = _room.name
		self.y = 0 # put the player on the floor
	

	def moveLeft(self, world, amount=1):
		room = getRoom(self.roomName, world)
		if (self.x == 1 and room.left!=None):
			self.changeRoom(room.left, "right", world)
		else:
			self.x = max(1, self.x-amount)
		self.head = "<"

	def moveRight(self, world, amount=1):
		room = getRoom(self.roomName, world)
		if (self.x == room.width-7 and room.right!=None):
			self.changeRoom(room.right, "left", world)
		else:
			self.x = min(room.width-7, self.x+amount)
		self.head = ">"

	def moveUp(self, world, amount=1):
		self.y = max(5, self.y-amount)

	def moveDown(self, world, amount=1):
		room = getRoom(self.roomName, world)
		self.y = min(self.y+amount, room.height)

	def jump(self, world, amount=1):
		room = getRoom(self.roomName, world)
		self.moveUp(world, amount)

	def changeRoom(self, newRoom, rightOrLeft, world):
		room = getRoom(self.roomName, world)
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

