
import pickle
import socket


client_ip = 'localhost'
def get_connection(s):
	# Establish connection with client. 
	s.settimeout(.0001)
	try:
		new_c, new_addr = s.accept()
		print(new_addr, "connected.")
		return [new_c, new_addr]
	except:
		return None
		pass # this means we did not get a connection


def connect():
	player1 = "No connection to other player"
	player2 = "No connection to other player"
	connections = []
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((client_ip, 10003))
	s.listen(5)
	while True:
		# If no connections wait for a connection. 
		if len(connections) == 0:
			new_c = get_connection(s)
			if new_c != None:
				connections.append(new_c)


		# If only 1 connection send that ip None over and over and check for another connection	and recieve the garbage data	
		if len(connections) == 1:	
			print("1 connection")		
			# send none so that connection doesnt wait for too long
			c = connections[0][0]
			send = pickle.dumps("CONNECTED YAY")
			length = pickle.dumps(len(send))
			final = length + send
			try:
				c.send(final)
			except:
				print(connections[0][1], "disconnected")
				connections = []
				continue
			
			# Recieve the garbage data that this ip is trying to send to the other player
			try:
				print("here")
				len_data = c.recv(5) 
				new_len = pickle.loads(len_data[:5])
				print(new_len)
				data = c.recv(new_len) # this is garbage because there is no other player yet 
				print(data)
			except:
				print(connections[0][1], "disconnected")
				connections = []
				continue

			# check for new connection
			# new_c = get_connection(s)
			# if new_c != None:
			# 	connections.append(new_c)

		# If 2 connections create 2 threads and join them:
		# one for recieving from ip 1 and sending to ip 2
		# one for recieving from up 2 and sending to ip 1
		# if one of those connections drop have the thread return 
		elif len(connections) == 2:
			print("2 connections")
			c1 = connections[0][0]
			c2 = connections[1][0]
			# get from c1 send to c2
			final = ''
			try:
				len_data = c1.recv(5)
				new_len = pickle.loads(len_data[:5])
				data = c1.recv(new_len) 
				final = len_data + data
				print("recieved from c1")
			except:
				print(connections[0][1], "disconnected")
				connections.remove(connections[0])
				continue
			
			try:
				c2.send(final)
				print("sent to c2")
			except:
				print(connections[1][1], "disconnected")
				connections.remove(connections[1])
				continue

			# get from c2 send to c1
			try:
				len_data = c2.recv(5) 
				new_len = pickle.loads(len_data[:5])
				data = c2.recv(new_len) 
				final = len_data + data
				print("recieved from c2")
			except:
				print(connections[1][1], "disconnected")
				connections.remove(connections[1])
				continue
			
			try:
				c1.send(final)
				print("sent to c1")
			except:
				print(connections[0][1], "disconnected")
				connections.remove(connections[0])
				continue



def host():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((client_ip, 10003))
	s.listen(5)
	while True:
		new_c = get_connection(s)
		if new_c != None:
			return new_c

