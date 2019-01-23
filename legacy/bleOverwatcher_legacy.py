#!/usr/bin/env python
#Author: David Martellock
#Date: April 1st 2018
#Purpose: Work Magic with Bluepy on a seperate daemon.

from bluepy import btle
import sys
import binascii
import yaml

# NOTIFICATION BLE DELEGATE --------------------------------------------------------
# Code from ianharvey.github.io/bluepy-doc/notifications.html
class MyDelegate(btle.DefaultDelegate):
	def __init__(self, params):
		btle.DefaultDelegate.__init__(self)
		#... Initialize here
	
	def handleNotifications(self, cHandle, data):
		print cHandle
		# ... perhaps check cHandle?
		# ... process "data"



#VARIABLE DECLERATIONS
MAC_ADDR = "54:6C:0E:83:2B:80"

chardict = {} #UUID : characteristic object
VolumeUUID =	 "babe1121-0000-0000-0001-000000000001" # 0-16
NextTrackUUID =	 "babe1122-0000-0000-0001-000000000002" # 0/1
PlayPauseUUID =	 "babe1123-0000-0000-0001-000000000003" # 0/1
ModeUUID =	 "babe1124-0000-0000-0001-000000000004" # 0/1
BrightUUID =	 "babe1125-0000-0000-0001-000000000005" # 0 - 16
ZAccelUUID =	 "babe1131-0000-0000-0002-000000000001" # -127 to 127
uuidList = [VolumeUUID,NextTrackUUID,PlayPauseUUID,ModeUUID,BrightUUID,ZAccelUUID]

charlist = ['char1','char2','char3','char4','char5','char6']


#print "Connecting..."
# NOTES: btle.peripheral makes a connection to the device if one is given
# Will throw a "BTLE Exception" if connection fails!
try:
	dev = btle.Peripheral(MAC_ADDR)
	dev.setDelegate(MyDelegate(btle.DefaultDelegate)) # ... What are these "params"
except:
	print "Connection Failed, try power cycle!"
	sys.exit(1)
print "Connected!"

# read yaml doc for initial comparisons.
vardict = {}
with open('variables.yml','r') as f:
	vardict = yaml.load(f)

#actual set up of char connection for later access!
for char in dev.getCharacteristics(): # add all characteristics to map
	if str(char.uuid) in uuidList: 
		chardict[str(char.uuid)] = char
		#print str(char.uuid)

# EDITABLE DICTIONARY WITH STRING UUIDS + CHARAC VALUES:
#current string values of uuid and of charac values:
charvaluedict = {}
for uuid in chardict:
	charvaluedict[ uuid ] =  str(chardict[uuid].read()) #returns binary version of hex value

	
# Manually change a value in the yaml file: 
#charvaluedict[VolumeUUID] = str("\x01") # this seems to be 
#== to 1 for the microcontroller. charvaluedict[ModeUUID] = 
#hex(2)


# update the microcontroller:
for var in vardict:
	if chardict[var].read() != vardict[var]:
		chardict[var].write(vardict[var])
		charvaluedict[var] = vardict[var]
		print "Writing" + var



#write all to variables yaml file:
with open('variables.yml','w') as f:
	yaml.dump(charvaluedict,f)


# updating vars loop: readall from yaml file:
#with open('variables.yml','r') as f:
#	vardict = yaml.load(f)

	

#print "Data read from Microcontroller: " 
#for var in vardict:
#	print binascii.hexlify(chardict[var].read())
				



#get the uuid from the arguments target = 
#uuidList[int(sys.argv[1])]

#print binascii.hexlify(chardict[target].read()) # String of 
#the value desi print 
#binascii.hexlify(chardict[target].read())[-1] # String of 
#the value desired

dev.disconnect	#Cleanup the device resources in system memory

