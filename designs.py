

def getDesign(name):
	if (name == "player"):
		return ["  o  ",
				"_/*\\_",
				"  *  ",
				"  *  ",
				"_/ \\_"
				]
	if (name == "playerleft"):
		player = getDesign("player")
		player[0] = "  <  "
		return player
		
	if (name == "playerright"):
		player = getDesign("player")
		player[0] = "  >  "
		return player

	if (name == "cat"):

		return [
				"\\    /\\",
				" )  ( ')",
				"(  /  )",
				" \\(__)|"
				]
	if (name == "small cat"):

		return [
				"\\    /\\",
				" )  ( ')",
				" \\ (__)|"
				]

	if (name == "door left"):

		return [
				"| ",
				"| ",
				"| ",
				"|*",
				"| ",
				"| ",
				]

	if (name == "door right"):

		return [
				" |",
				" |",
				" |",
				"*|",
				" |",
				" |",
				]


	print("Cannot find design " + name)
	return []

