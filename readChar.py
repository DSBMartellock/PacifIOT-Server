#!/usr/bin/env python
#Author: David Martellock
#Date: April 1st 2018
#Purpose: Test Blupy python Package

from bluepy import btle
import sys
import binascii

if len(sys.argv) is 0:
	print "Error, 1 arguments required!"
	sys.exit(1)

#VARIABLE DECLERATIONS:
chardict = {} #UUID : characteristic object
VolumeUUID =	 "babe1121-0000-0000-0001-000000000001" # 0-16
NextTrackUUID =	 "babe1122-0000-0000-0001-000000000002" # 0/1
PlayPauseUUID =	 "babe1123-0000-0000-0001-000000000003" # 0/1
ModeUUID =	 "babe1124-0000-0000-0001-000000000004" # 0/1
BrightUUID =	 "babe1125-0000-0000-0001-000000000005" # 0 - 16
ZAccelUUID =	 "babe1131-0000-0000-0002-000000000001" # -127 to 127
TipUUID =	 "babe1132-0000-0000-0002-000000000002" # 0/1
AudioUUID =	 "babe1133-0000-0000-0002-000000000003" # UNUSED Current Impl
uuidList = [VolumeUUID,NextTrackUUID,PlayPauseUUID,ModeUUID,BrightUUID,ZAccelUUID,TipUUID,AudioUUID]

#print "Connecting..."
# NOTES: btle.peripheral makes a connection to the device if one is given
# Will throw a "BTLE Exception" if connection fails!
try:
	dev = btle.Peripheral("54:6C:0E:83:2B:80")
except:
	print "Connection Failed, try power cycle!"
	sys.exit(1)
print "Connected!" 

for char in dev.getCharacteristics(): # add all characteristics to map
	if str(char.uuid) in uuidList: 
		chardict[str(char.uuid)] = char

#get the uuid from the arguments
target = uuidList[int(sys.argv[1])]

print binascii.hexlify(chardict[target].read())[-1] # String of the value desired

dev.disconnect	#Cleanup the device resources in system memory

