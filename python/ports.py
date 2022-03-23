#!/usr/bin/env python3

import socket
import time
import datetime
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])


def timing(function):
	#time a function
	start = time.time()
	function()
	end = time.time()
	return(end - start)
	

def connect():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'Hello, world')
		data = s.recv(1024)
		print('Received', repr(data))

#print(timing(connect))
connect()
			
