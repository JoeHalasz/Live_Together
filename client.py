import pickle
import threading
import socket 
from package import Package
from world import save, loadWorld, saveAll

host_ip = '25.13.61.235'

def send_data(s, player, my_actions):
	package = Package(player, my_actions)
	# send message back
	send = pickle.dumps(package)

	length = pickle.dumps(len(send))
	final = length + send
	s.send(final)
	
def recieve_data(s, player): # need player just incase we need to save
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
				saveAll(player)
				quit()
	data = s.recv(new_len) 
	data = pickle.loads(data)
	other_actions = data.actions
	return data.player, other_actions



def send_world(s, world):
	send = pickle.dumps(world)
	length = pickle.dumps(len(send))
	final = length + send
	print(data)
	print(len(send))
	s.send(final)

def recieve_world(s):
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
				save("save/" + player.name, player) # dont save the empty world. just the player
				quit()
	data = s.recv(new_len)
	print(data)
	print(new_len)
	world = pickle.loads(data)
	return loadWorld(world)[0]





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

