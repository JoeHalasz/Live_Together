from os.path import exists

def getDesign(name, head=" "):
	fileName = "designs/" + name + ".txt"

	if exists(fileName):
		lst = []
		if (name == "player" or name == "player crouch"):
			lst.append("  "+head+"  ")
		# open file and read stuff
		f = open(fileName, 'r')
		lines = f.readlines()
		for line in lines:
			line=line.replace("\n","").replace("Â","")
			if (line != ""):
				lst.append(line)
		f.close()
		
		return lst

	else:
		if "flipped" in name: # if flipped design DNE then return None
			return None
		return [name] # else its just a name so return that 

