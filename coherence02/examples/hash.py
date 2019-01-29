#!/usr/bin/env python

import socket
import json
import os,binascii

def sending(message):
	ip = '127.0.0.1'
	port = 6613
	BUFFER_SIZE = 65536
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message)
	print "Sending Json: \n" + message
	data = s.recv(BUFFER_SIZE)
	print  "Receiving Json: \n" + data+"\n\n"
	s.close()
	return data

algorithms=["SHA3_512", "SHA3_384", "SHA3_256", "SHA3_224",
"SHA_512", "SHA_384", "SHA_256", "SHA_224" , "SHA_1" ,
"WHIRLPOOL" , "BLAKE2B"]
data_js='{"version":1,"algorithm":"SHA3_512","type":"string","plaintext":"Hello world!", "hex":0}'

hash_js=json.loads(data_js)
for i in algorithms:
    hash_js["algorithm"]=i
    sending(json.dumps(hash_js))

hash_js["hex"]=1
hash_js["plaintext"]=hash_js["plaintext"].encode("hex")
for i in algorithms:
    hash_js["algorithm"]=i
    sending(json.dumps(hash_js))

data_js_f='{"version":1,"algorithm":"SHA3_512","type":"file","file":"./bin/../file_test/Mayhem.txt"}'
hash_js=json.loads(data_js_f)
for i in algorithms:
    hash_js["algorithm"]=i
    sending(json.dumps(hash_js))
