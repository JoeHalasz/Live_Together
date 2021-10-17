


def catMovement(o, inc):
	if not o.beingHeld:
		if o.actionStage == inc*2:
			o.x += 1
		elif o.actionStage == inc*4:
			o.x -= 1
		elif o.actionStage == inc*6:
			o.x += 1
		elif o.actionStage == inc*8:
			o.x -= 1
		elif o.actionStage == inc*10:
			o.x += 1
		elif o.actionStage == inc*12:
			o.x -= 1
		elif o.actionStage == inc*14:
			o.x += 1
		elif o.actionStage == inc*16:
			o.x -= 1
		elif o.actionStage == inc*17:
			o.y -= 1
			o.x += 1
		elif o.actionStage == inc*18:
			o.y += 1
			o.x += 1
			o.actionStage += 1
		elif o.actionStage == inc*19:
			o.y -= 1
			o.x -= 1
		elif o.actionStage == inc*20:
			o.y += 1
			o.x -= 1
			o.flip()
	o.actionStage += 1
	if o.actionStage > inc*20:
		o.actionStage = 0