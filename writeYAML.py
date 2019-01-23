#!/usr/bin/env python
#Author: David Martellock
#Date: April 1st 2018
#Purpose: Test Blupy python Package

from flask import Flask
from bluepy import btle
import sys
import binascii
import yaml

app = Flask(__name__)


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


@app.route("/writeYaml/<string:inputargs>")
def writeYaml(inputargs):
	outputstring = "Output: "
	#Break down input args string:
	charchoice = int(inputargs[0])
#	print charchoice
	if charchoice >= 6:
		sys.exit(0)
	charvalue = int(inputargs[1:])
#	print charvalue
	
	indexs = uuidList[charchoice]
#	outputstring = outputstring + " here lies " + indexs
#	print "hexval: " + str( hex(charvalue) )
	
	# read yaml doc for comparisons.
	vardict = {}
	with open('variables.yml','r') as f:
		vardict = yaml.load(f)
	
#	print "Read from yaml" + str(vardict[indexs])
	# READ READ READ READ READ READ READ READ READ:
	#print "Inital Data read from yaml " 
	#for var in vardict: 
	#	print var
	#	print vardict[var]
	
	
	
	# Manually change a value in the dictionary representation of the yaml file:
	#charvaluedict[VolumeUUID] = str("\x01") # this seems to be == to 1 for the microcontroller.
	#charvaluedict[ModeUUID] = str("\x01")
	
	
	
	vardict[indexs] = charvalue
	
	#write all to variables yaml file:
	with open('variables.yml','w') as f:
		yaml.dump(vardict,f)

	#readall from yaml file:
	with open('variables.yml','r') as f:
		vardict = yaml.load(f)
	outputstring = outputstring + "changed var yaml file!"

	for var in vardict:
		outputstring = outputstring +"\n"+ var + " " + str(vardict[ var])
#	print outputstring
	return outputstring

if __name__=="__main__":
	#app.run()	
	app.run('0.0.0.0')

