


class Package(): # this is what is sent to the other player over the socket
	player = ""
	world = []

	def __init__(self, player, world):
		self.player = player
		self.world = world

