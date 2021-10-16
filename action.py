

class Action():
	name = ""
	roomName = "" # the name of the room that this action was done in
	obj = "" # the object that this action was done on with the action done to it if applicable

	def __init__(self, name, roomName, obj):
		self.name = name # removed, moved, added
		self.roomName = roomName
		self.obj = obj
