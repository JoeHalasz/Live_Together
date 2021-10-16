


class Package(): # this is what is sent to the other player over the socket
	player = ""
	actions = []

	def __init__(self, player, actions):
		self.player = player
		self.actions = actions

