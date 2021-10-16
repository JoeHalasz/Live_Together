from designs import getDesign


class Object():

	name = ""
	objectId = 0
	design = [] # this is a 2d list of what the object will look like
	x = 0 # offset from the center
	y = 5 # offset from the cieling 
	centered = False
	size = [0,0]
	beingHeld = False

	def __init__(self,name, x, y, objectId=0, centered=False):
		self.name = name
		self.design = getDesign(name)
		self.x = x
		self.y = y
		self.objectId = objectId
		self.centered = centered
		maxWidth = 0
		for line in self.design:
			if len(line) > maxWidth:
				maxWidth = len(line)

		self.size = [maxWidth, len(self.design)] # this will be used for collisions



	def checkCollidingPlayer(self, player):
		fakeObj = Object("player", player.x, player.y, -1) # make this so that we have a size for the player
		return self.checkCollidingObj(fakeObj)


	def checkCollidingObj(self, otherObj): # THIS DOES NOT WORK FOR CENTERED OBJECTS
		if (otherObj.x+otherObj.size[0] > self.x and otherObj.x < self.x+self.size[0]):
			if (otherObj.y+otherObj.size[1] > self.y and otherObj.y < self.y+self.size[1]): # there is a collision
				return True
		return False