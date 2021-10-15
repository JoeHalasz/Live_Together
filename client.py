import pickle
import threading
import socket 
from package import Package

host_ip = '25.13.61.235'

def send_data(s, player, world):	
	package = Package(player, world)
	# send message back
	send = pickle.dumps(package)

	length = pickle.dumps(len(send))
	final = length + send
	print(len(send))
	s.send(final)


def recieve_data(s):

	len_data = s.recv(6) # might need to change this if its a bigger message
	new_len = pickle.loads(len_data[:6])
	print(new_len)
	data = s.recv(new_len) 
	data = pickle.loads(data)
	print(data)
	print(data.player.name)
	print(data.world[0].name)
	quit()
	return data.player, data.world



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

