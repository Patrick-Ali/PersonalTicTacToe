#!/usr/bin/python3, https://docs.python.org/3/library/select.html
# https://mail.python.org/pipermail/tutor/2013-May/095756.html

import socket, select, random         
from collections import Counter

class Chat:
	def __init__(self, port=12346):
		self.connections = []

		self.server = socket.socket()         
		self.server.bind(('', port))          
		self.server.listen(2)                 

	def shutdown(self):
		for c in self.connections:
			c.close()

		self.server.shutdown(1)
		self.server.close()

	def poll(self):

		while True:
		
			try:
				read, write, error = select.select( self.connections+[self.server], self.connections, self.connections, 0 )

				n = random.randint(0,1)

				First = "Player 1, "
				Seond = "Player 2"
				
				Mark = "Choose Marker, X or O"

				try:
					for conn in read:
						 if conn is self.server:
							 print('Connected!')
							 people = []
							 c, addr = conn.accept()
							 if self.connections == []:
								 people.append(1)
							 self.connections.append(c)                              
							 if self.connections[0] != ' ':
								 people.append(1)
								 people.append(1)
							
							 counts = Counter(people)
							
							 if counts[1] == 2: 
								 if n == 1:
									 self.connections[1].send(First.encode('utf-8')+ Mark.encode('utf-8'))
									 self.connections[0].send(Seond.encode('utf-8'))
									
								 else:
									 self.connections[0].send(First.encode('utf-8')+ Mark.encode('utf-8'))
									 self.connections[1].send(Seond.encode('utf-8'))
										

						 else:
							
							 msg = conn.recv(1024)              
							 msg = msg.decode('utf-8').rstrip('\r\n')        
							 msg = msg.upper()

							 X = "You are X, "
							 O = "You are O, "
							 Wait = "please wait for player 1"
							 Move = "Make first move"
							
							 for other in self.connections:
									 if other != conn and msg == "O":
										 other.send( X.encode('utf-8') + Wait.encode('utf-8') )
									 elif other != conn and msg == "X":
										 other.send( O.encode('utf-8') + Wait.encode('utf-8'))
							

							 if msg == 'X' or msg == 'O':
								 continue 

							 if msg == "EXIT":
								 Chat.shutdown(self)

							 try:
								 rtrnmsg = msg[::-1]                                             
								 print( '%s -> %s' % (msg,rtrnmsg) )

								 rtrnmsg = rtrnmsg 
								
									
								 for other in self.connections:
									 if other != conn:
										 other.send( rtrnmsg.encode('utf-8') )
							 except socket.error:
								 socket.close()
								 
								

				except OSError as e:
					if e.winerror == 10057:
						Chat.poll(self)
				
			except ValueError:
				self.connections = []
				continue
			
		
			

		       
if __name__ == '__main__':
	try:
		c = Chat()
		while True:
			c.poll()
	except OSError as e:
		if e.winerror == 10057:
			c.poll()
	except KeyboardInterrupt:
		c.shutdown()
							
