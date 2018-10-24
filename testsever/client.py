#!python
'''
Creating Client application for Drone

Attempt one - send random.random() from client
Author --
Prajwal T R
Date LAst MOdified = 18/09/18
'''

import socket
import random

try:
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
	print("Socket Creation Failed")

host = input('Enter the hoSTnaME : ')
port = 9999
client_socket.connect((host,port))
'''
if (client_socket.recv(100).decode()) == 'dir':
	client_socket.send(str('work in progress').encode())
'''
while True:
	print(client_socket.send(str(random.randint(0,9)).encode()))
	#ConnectHost.clientstatus = str('Client RUnning On IP : {} Port = {}'.format(host,port))
	#host = str(input('ENter thE hoSTnaME OF yOUR pC :'))

	#printing HostName ANd POrt ON Client Side
client_socket.close()
