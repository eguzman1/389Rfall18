#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
def padded(s):
    i = 0
    while(i < len(s)):
        if(s[i] == 0):
            break
        i += 1 
    while(i < len(s)):
        if(s[i] != 0):
            return False
        i += 1
    return True
            
def is_ascii(S):
	return all(ord(c) < 128 for c in S)

magic,version,timestamp = struct.unpack("<LLL", data[0:12])
author = data[12:20]
sections = struct.unpack("<L",data[20:24])[0]

try:
    author_d = author.decode('ascii','strict')
except UnicodeDecodeError:
    print("Not valid author")

if(padded(author_d)==False):
    bork("NOT NULL PADDED")
 
SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x1
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9
offset = 24


if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
   bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
print("AUTHOR: %s " % author_d)
print("SECTIONS: %s " % sections)
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

#section_count = author[1]
i = 0
print("-------  BODY  -------")
while(offset <len(data)):
    i += 1
    print("\nSection is: %d" % i)
    stype,slen = struct.unpack('<LL', data[offset:offset+8])
    offset += 8
    #SEction 1
    if(stype == SECTION_PNG):
        print(" PNG ")
        fileout = 'photo.png'
        with open(fileout, 'wb') as f:
            f.write(b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a")
            f.write(data[offset:offset+slen])
    #Section 2
    elif (stype == SECTION_DWORDS):
        print (" DWORDS ")
        if(slen % 8 != 0 ):
            bork("DWORDS IS NOT VALID")
    	svalue = struct.unpack("<" + "q" * int(slen/8),data[offset:offset+slen])
    	print(svalue)

    #SEction 3
    elif(stype == SECTION_UTF8):
    	try:
    		svalue = data[offset:offset+slen]
    		print("UTF-8: %s " % svalue.decode("utf-8") )
    	except UnicodeDecodeError:
    		bork("UTF NOT VALID")

    #SEction 4
    elif(stype== SECTION_DOUBLES):
    	print("DOUBLE")
    	if(slen % 8 != 0):
    		bork("DWORDS NOT divisible by 8")
    	svalue = struct.unpack("<" + 'd'*int(slen/8),data[offset:offset+slen])
    	print(svalue)
    #SEction 5
    elif(stype == SECTION_WORDS):
    	print("WORDS")
    	if(slen %4 != 0):
    		bork("WORDS")
    	svalue = struct.unpack("<" + 'L' * int(slen/4),data[offset:offset+slen])
    	print(svalue)
    
    #SEction 6
    elif(stype == SECTION_COORD):
    	print("COORD")
    	if(slen %8 != 0):
    		bork("COORD IS NOT VALID")
    	latitude,longtitude = struct.unpack("<dd",data[offset:offset+slen])
    	#print("latitude: %f"% latitude)
    	#print("longtitude:%f"%longtitude)
    	p = (latitude,longtitude)
    	print(p)
    #SEction 7
    elif(stype == SECTION_REFERENCE):
    	if(slen != 4):
    		bork("REFERENCE HAS NO LEN OF 4 ")
    	svalue = struct.unpack("<L", data[offset:offset+slen])[0]
    	if(svalue <0 or svalue > sections -1):
    		bork("REFERENCE COUNT OUT OF BOUNDS")
    	print("SCALUE for REF COUNT: %d" % svalue)

    #SEction 9
    elif(stype == SECTION_ASCII):
    	print(" ASCII")
    	svalue = data[offset:offset+slen]
    	if not is_ascii(svalue):
    		bork("ASCII NOT ENCODED")
    	print("SVALUE : %s" % svalue.decode("ascii"))
    offset += slen



    
