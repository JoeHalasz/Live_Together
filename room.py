import os
import sys


class Room:
	name = ""
	width = 0
	height = 0
	left = ""
	right = ""

	def __init__(self , _name, _width=15, _height=5):
		self.name = _name
		self.width = max(_width,15)
		self.height = max(_height,5)


	def drawRoom(self, player=""):
		screen = ""
		for x in range(30-self.height):
			screen += '\n'
		for x in range(self.width):
			screen += '-'

		for y in range(self.height):
			screen += '\n'
			screen += '|'
			for x in range(self.width-2):
				if (player!=""):
					if (x == player.x and y == player.y): # left foot
						screen += "_"
					elif (x == player.x+1 and y == player.y): # left leg
						screen += "/"
					elif (x == player.x+3 and y == player.y): # right leg
						screen += "\\"
					elif (x == player.x+4 and y == player.y): # right foot
						screen += "_"

					elif (x == player.x+2 and y == player.y-1): # middle bottom
						screen += "*"
					elif (x == player.x+2 and y == player.y-2): # middle
						screen += "*"

					elif (x == player.x+1 and y == player.y-2): # left arm
						screen += "/"
					elif (x == player.x and y == player.y-2): # left hand
						screen += "_"
					elif (x == player.x+3 and y == player.y-2): # right arm
						screen += "\\"
					elif (x == player.x+4 and y == player.y-2): # right hand
						screen += "_"

					elif (x == player.x+2 and y == player.y-3): # middle top
						screen += player.head

					else:
						screen += ' '
				else:
					screen += ' '
			screen += "|"

		screen += '\n'
		for x in range(self.width):
			screen += '-'
		screen += '\n'

		sys.stdout.write("%s" % screen)
		sys.stdout.flush()

