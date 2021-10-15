from room import Room
from player import Player
from time import sleep
import keyboard

starterRoom = Room("Starter Room", 40,8)
player = Player("Joe", starterRoom)
movedUp=False

def movement(player):
	speed = 1
	done = False
	if movedUp:
		movedUp=False
	else:
		player.moveDown(1) # gravity

	if keyboard.is_pressed('shift'):
		speed=2
	if keyboard.is_pressed('a'):  
		player.moveLeft(speed)
		needUpdate=True
	if keyboard.is_pressed('d'):
		player.moveRight(speed)
		needUpdate=True
	if keyboard.is_pressed(" "):
		player.moveUp(speed)
		movedUp=True
	if keyboard.is_pressed('q'):
		player.moveRight(speed)
		done = True



	return done



def main():
	while True:
		if movement(player):
			break
		player.room.drawRoom(player)

		sleep(1/20)

	

if __name__ == '__main__':
	main()


