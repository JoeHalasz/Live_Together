from room import Room
from player import Player
from time import sleep
import keyboard


starterRoom = Room("Starter Room", 40,8)
nextRoom = Room("Next Room", 100,12)

starterRoom.left = nextRoom
nextRoom.right = starterRoom

player = Player("Joe", starterRoom)
justJumped=False


def movement(player):
	global justJumped
	speed = 1
	done = False
	player.moveDown(1) # gravity

	if keyboard.is_pressed('shift'):
		speed=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(speed)
		needUpdate=True
	if keyboard.is_pressed('d'):
		player.moveRight(speed)
		needUpdate=True

	if keyboard.is_pressed(" "): # this has to be last other than quit
		if not justJumped:
			player.jump()
		justJumped=True
		return done
	if keyboard.is_pressed('q'):
		player.moveRight(speed)
		done = True

	justJumped = False
	return done



def main():
	while True:
		if movement(player):
			break
		player.room.drawRoom(player)

		sleep(1/20)

	

if __name__ == '__main__':
	main()


