import pickle
import threading
import socket 

host_ip = '25.13.61.235'

def send_data(s, player):	
	# send message back
	send = pickle.dumps(player)

	length = pickle.dumps(len(send))
	final = length + send
	s.send(final)


def recieve_data(s):
	global otherPlayer
	len_data = s.recv(5) # might need to change this if its a bigger message
	new_len = pickle.loads(len_data[:5])
	data = s.recv(new_len) 
	data = pickle.loads(data)
	return data



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

