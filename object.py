from designs import getDesign


class Object():

	name = ""
	design = [] # this is a 2d list of what the object will look like
	x = 0 # offset from the center
	y = 5 # offset from the cieling 
	centered = False

	def __init__(self,name, x, y, centered=False):
		self.name = name
		self.design = getDesign(name)
		self.x = x
		self.y = y
		self.centered = centered

