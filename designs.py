

def getDesign(name, head=""):
	if (name == "player"):
		return ["  "+head+"  ",
				"_/*\\_",
				"  *  ",
				"  *  ",
				"_/ \\_"
				]

	if (name == "player crouch"):
		return ["  "+head+"  ",
				"_/*\\_",
				"  *  ",
				"_/ \\_"
				]
	

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


	return [name]

