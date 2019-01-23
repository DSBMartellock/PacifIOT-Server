#!/usr/bin/env python
#Author: David Martellock
#Date: April 1st 2018
#Purpose: Test Blupy python Package

from bluepy import btle
import sys
import binascii
import yaml

if len(sys.argv) <= 2 :
	sys.exit(0)

charchoice = int(sys.argv[1])
if charchoice >= 7:
	sys.exit(0)
charvalue = int(sys.argv[2])

#VARIABLE DECLERATIONS:
chardict = {} #UUID : characteristic object
VolumeUUID =	 "babe1121-0000-0000-0001-000000000001" # 0-16
NextTrackUUID =	 "babe1122-0000-0000-0001-000000000002" # 0/1
PlayPauseUUID =	 "babe1123-0000-0000-0001-000000000003" # 0/1
ModeUUID =	 "babe1124-0000-0000-0001-000000000004" # 0/1
BrightUUID =	 "babe1125-0000-0000-0001-000000000005" # 0 - 16
ZAccelUUID =	 "babe1131-0000-0000-0002-000000000001" # -127 to 127
uuidList = [VolumeUUID,NextTrackUUID,PlayPauseUUID,ModeUUID,BrightUUID,ZAccelUUID]

charlist = ['char1','char2','char3','char4','char5','char6']

indexs = uuidList[charchoice-1]
print "here lies"+ indexs
print VolumeUUID
print hex(charvalue) 

# read yaml doc for comparisons.
vardict = {}
with open('variables.yml','r') as f:
	vardict = yaml.load(f)

print vardict
# READ READ READ READ READ READ READ READ READ:
#print "Inital Data read from yaml " 
#for var in vardict: 
#	print var
#	print vardict[var]
	

	
# Manually change a value in the dictionary representation of the yaml file:
#charvaluedict[VolumeUUID] = str("\x01") # this seems to be == to 1 for the microcontroller.
#charvaluedict[ModeUUID] = str("\x01")



vardict[indexs] = hex(charvalue)


#write all to variables yaml file:
with open('variables.yml','w') as f:
	print yaml.dump(vardict,f)

#readall from yaml file:
with open('variables.yml','r') as f:
	vardict = yaml.load(f)

#print "changed var yaml file:"
print vardict

	


