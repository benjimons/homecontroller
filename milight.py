#!/usr/bin/python
#
# Milight Control Script
#
# Author Ben McDowall
# 21 August 2016
#
# Usage: ./milight.py action

import socket
import sys

# addressing information of target
IPADDR = '192.168.0.101'
PORTNUM = 8899

#Get action and print it back
action = str(sys.argv[1])
print(action)

#Create packet data based on selection action
if action == "on":
	PACKETDATA = '420055'.decode('hex')
if action == "off":
	PACKETDATA = '410055'.decode('hex')
if action == "blue":
	PACKETDATA = 'C00090'.decode('hex')
if action == "white":
	PACKETDATA = 'C50000'.decode('hex')
if action == "discoon":
	PACKETDATA = '4D0055'.decode('hex')
if action == "discofaster":
	PACKETDATA = '440055'.decode('hex') 
if action == "discoslower":
	PACKETDATA = '440055'.decode('hex') 
if action == "discomode":
	PACKETDATA = '4D0055'.decode('hex') 
if action == "allwhite":
	PACKETDATA = 'C20055'.decode('hex') 
if action == "col_lilac":
	PACKETDATA = '400055'.decode('hex')
if action == "col_royal_blue":
	PACKETDATA = '401055'.decode('hex')
if action == "col_baby_blue":
	PACKETDATA = '402055'.decode('hex')
if action == "col_aqua":
	PACKETDATA = '403055'.decode('hex')
if action == "col_mint":
	PACKETDATA = '404055'.decode('hex')
if action == "col_mint2":
	PACKETDATA = '404555'.decode('hex')
if action == "col_seafoam_green":
	PACKETDATA = '405055'.decode('hex')
if action == "col_green":
	PACKETDATA = '406055'.decode('hex')
if action == "col_lime_green":
	PACKETDATA = '407055'.decode('hex')
if action == "col_yellow":
	PACKETDATA = '408055'.decode('hex')
if action == "col_yelloworange":
	PACKETDATA = '409055'.decode('hex')
if action == "col_orange":
	PACKETDATA = '40A055'.decode('hex')
if action == "col_red":
	PACKETDATA = '40B055'.decode('hex')
if action == "col_pink":
	PACKETDATA = '40C055'.decode('hex')
if action == "col_fusia":
	PACKETDATA = '40D055'.decode('hex')
if action == "col_lilac":
	PACKETDATA = '40E055'.decode('hex')
if action == "col_lavendar":
	PACKETDATA = '40F055'.decode('hex')

# initialize a socket, think of it as a cable
# SOCK_DGRAM specifies that this is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
 
# connect the socket, think of it as connecting the cable to the address location
s.connect((IPADDR, PORTNUM))
 
# send the command
s.send(PACKETDATA)
 
# close the socket
s.close()

