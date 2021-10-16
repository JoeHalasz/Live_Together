import pickle
import threading
import socket 
from package import Package

host_ip = '25.13.61.235'

def send_data(s, player, my_actions):
	package = Package(player, my_actions)
	# send message back
	send = pickle.dumps(package)

	length = pickle.dumps(len(send))
	final = length + send
	s.send(final)
	


def recieve_data(s):
	len_data = s.recv(5) # might need to change this if its a bigger message
	thelen = 5
	while True: # get more data until we have a full message
		try:
			new_len = pickle.loads(len_data[:thelen])
			break
		except:
			len_data += s.recv(1)
			thelen+=1
	data = s.recv(new_len) 
	data = pickle.loads(data)
	other_actions = data.actions
	return data.player, other_actions



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

