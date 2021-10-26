import pygame
import pygame_assets as assets
from world import getRoom



def frameStuff(screen, player, world):
	w, h = pygame.display.get_surface().get_size()
	room = getRoom(player.roomName, world)
	roomWidth = room.width
	roomHeight = room.height
	boarderWidth = 5

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	
	screen.fill("black")
	spaceFromGround = (h - roomHeight)
	spaceFromLeft = (w - roomWidth) / 2
	
	pygame.draw.rect(screen, "white",  # this is the room
		pygame.Rect(spaceFromLeft, spaceFromGround, roomWidth, roomHeight - (boarderWidth*2)), 
		width=boarderWidth)

	

	player_img = assets.load.image('player.png')

	groundLevel = h - (boarderWidth*2)

	screen.blit(player_img, (player.x, (player.y + h/2 - boarderWidth)))

	

	

	# Flip the display
	pygame.display.flip()
	

def setup():
	pygame.init()
	screen = pygame.display.set_mode([1536, 801], pygame.RESIZABLE)
	return screen