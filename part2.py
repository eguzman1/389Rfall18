#!/usr/bin/env python
#-*- coding:utf-8 -*-


# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re
import time
host = "142.93.117.193"   # IP address or URL
port =  7331    # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
# use these to connect to the service
while(True):
# receive some data	
	
	print("We are here under data")
	stri = str(data).split('\n')
	str1 = stri[len(stri)-2]
	z = re.match("Find me the (sha\d{1,3}|md\d) hash of (\w*)",str1)
	ha = z.group(1).strip()
	st = z.group(2).strip()
	h = hashlib.new(str(ha).strip())
	h.update(st.strip())
	answer = h.hexdigest() + "\n"
	s.send(answer)
	data = s.recv(1024)
	print(data)
	
# close the connection
s.close()
