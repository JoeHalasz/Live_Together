import pickle
import threading
import socket 
from package import Package
from world import *

host_ip = '25.13.61.235'
chunkSize = 1024
HEADERSIZE = 20


def send_data_helper(s, data):
	send = pickle.dumps(data)

	length = pickle.dumps(len(send))
	length += b' ' * (HEADERSIZE - len(length))
	s.send(length)
	x = 0
	timesTook = 0
	while True: # send it in chunks
		chunk = send[x:x+chunkSize]
		if not chunk:
			break
		s.send(chunk)
		x+=chunkSize
		timesTook+=1
	print(timesTook)


def send_data(s, player, my_actions):
	package = Package(player, my_actions)
	# send message back
	send_data_helper(s,package)
	

def recieve_data_helper(s):
	len_data = s.recv(HEADERSIZE) # might need to change this if its a bigger message
	new_len = int(pickle.loads(len_data))
	data = b''
	lengthShouldBe = 0
	while new_len != 0:
		if new_len < chunkSize:
			new_data = s.recv(new_len)
			new_len -= len(new_data)
			data += new_data
			lengthShouldBe += len(new_data)
		else:
			new_data = s.recv(chunkSize)
			new_len -= len(new_data)
			data += new_data
			lengthShouldBe += len(new_data)
		
	
	data = pickle.loads(data)
	return data


def recieve_data(s, player, world): # need player just incase we need to save
	
	data = recieve_data_helper(s)

	other_actions = data.actions
	return data.player, other_actions


def send_world(s,world):
	send_data_helper(s,world)


def recieve_world(s):
	world = recieve_data_helper(s)
	
	print(len(world))
	print(world)
	
	player, world = loadWorld(world)
	try:
		getRoom(player.roomName, world)
	except:
		player.roomName = world[0].name
	
	return player, world


	




def connect():
	global s
	threads = []
	
	s = ""
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host_ip, 10003))
	except:
		print("Did not connect")
		pass

	return s

	# we have a connection to the host

