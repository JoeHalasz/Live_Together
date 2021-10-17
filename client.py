import pickle
import threading
import socket 
from package import Package
from world import *

host_ip = '25.13.61.235'

def send_data(s, player, my_actions):
	package = Package(player, my_actions)
	# send message back
	send = pickle.dumps(package)

	length = pickle.dumps(len(send))
	final = length + send
	s.send(final)
	
def recieve_data(s, player, world): # need player just incase we need to save
	len_data = s.recv(5) # might need to change this if its a bigger message
	thelen = 5
	while True: # get more data until we have a full message
		try:
			new_len = pickle.loads(len_data[:thelen])
			break
		except:
			len_data += s.recv(1)
			thelen+=1
			if thelen > 20: # this means that the other player disconnected
				print("Other player disconnected")
				saveAll(player, world)
				quit()
	data = s.recv(new_len) 
	data = pickle.loads(data)
	other_actions = data.actions
	return data.player, other_actions



def send_world(s,world):
	send = pickle.dumps(world)
	length = pickle.dumps(len(send))
	final = length + send
	print(send)
	print(len(send))
	s.send(final)

def recieve_world(s):
	thelen = 6
	new_len = 0
	len_data = s.recv(thelen) # might need to change this if its a bigger message

	while True: # get more data until we have a full message
		try:
			new_len = pickle.loads(len_data[:thelen])
			break
		except:
			len_data += s.recv(1)
			thelen+=1
			if thelen > 20: # this means that the other player disconnected
				print("Other player disconnected")
				saveAll(player, world)
				quit()

	print(new_len)
	data = b''
	while new_len != 0:
		if new_len > 512: # recv can only get 1024 max i think
			data += s.recv(512)
			print(data, end="")
			new_len -= 512
		else:
			data += s.recv(new_len)
			new_len = 0
	
	print(data)
	world = pickle.loads(data)
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

