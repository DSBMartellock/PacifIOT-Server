#!/usr/bin/env python
#Author: David Martellock
#Date: April 1st 2018
#Purpose: Work Magic with Bluepy on a seperate daemon.

import time
from bluepy import btle
import sys
import os
import binascii
import yaml
import subprocess
import writeYAML as wryml
from multiprocessing import Pool
pool = Pool(processes=1)


def blockPrint():
	sys.stdout = open(os.devnull, 'w')

def enablePrint():
	sys.stdout = sys.__stdout__



# NOTIFICATION BLE DELEGATE --------------------------------------------------------
# Code from ianharvey.github.io/bluepy-doc/notifications.html
class MyDelegate(btle.DefaultDelegate):
	def __init__(self, params):
		btle.DefaultDelegate.__init__(self)
		#... Initialize here
	
	def handleNotification(self, cHandle, data):
		print cHandle
		try:
			print "notifying from >" + handlerdict[cHandle] # if handle exists in uuidlist:
			index =  uuidList.index(handlerdict[cHandle])
		except:
			print "Exception Handler :" + cHandle + " Not in handlerdict?"
			sys.exit(0)
					
		print index	

		# ...Run the subroutine to write the characteristic. 
		print "  called with " + str(binascii.hexlify(data))
		print "(this is after str call)"

		try:
			#commandstring = "python /var/www/html/writeYAML.py " + index + " " + data
			#print commandstring
			commandstring = str(index)+str(data)
			result = pool.apply_async(wryml.writeYaml,[str(index)+changeformat(data)],callback=finish)

			#subprocess.call(commandstring, shell=True)
						
		except:
			print "some problem with subprocess call to writeYAML.py"
		

		# ... process "data"
def changeformat(data):
#	print "this is the changeformat"
	#print type(binascii.hexlify(data))
	return int(binascii.hexlify(data),16)

# VARIABLE DECLERATIONS ------------------------------------------------------------
MAC_ADDR = "54:6C:0E:9B:53:A8"
#MAC_ADDR = "54:6C:0E:83:2B:80"
#characteristic handle : uuid string
handlerdict = {}
#characteristic handle notification string : notify char
notifyhandlerdict = {}


chardict = {} #UUID : characteristic object
VolumeUUID =	 "babe1121-0000-0000-0001-000000000001" # 0-16
NextTrackUUID =	 "babe1122-0000-0000-0001-000000000002" # 0/1
PlayPauseUUID =	 "babe1123-0000-0000-0001-000000000003" # 0/1
ModeUUID =	 "babe1124-0000-0000-0001-000000000004" # 0/1
BrightUUID =	 "babe1125-0000-0000-0001-000000000005" # 0 - 16 
ZAccelUUID =	 "babe1131-0000-0000-0002-000000000001" # -127 to 127
uuidList = [VolumeUUID,NextTrackUUID,PlayPauseUUID,ModeUUID,BrightUUID,ZAccelUUID]


charlist = ['char1','char2','char3','char4','char5','char6']


# CONNECT TO DEVICE ---------------------------------------------------------------
print "Connecting..."
try:
	dev = btle.Peripheral(MAC_ADDR)
except:
	# Will throw a "BTLE Exception" if connection fails!
	print "Connection Failed, try power cycle!"
	sys.exit(1)
print "Connected!"


#Set up char connection so can be accessed like chardict[str(uuid)].read/write/ect
for char in dev.getCharacteristics(): # add all characteristics to map
	if str(char.uuid) in uuidList: 
		chardict[str(char.uuid)] = char
		print char.getHandle()

		handlerdict[char.getHandle()] = str(char.uuid)
		print "Attempting to turn on notifications"
		if str(char.uuid) == BrightUUID:
			try:
				print "Heres where notifications would turn on anyways" 
# NOT TURNING ON NOTIFICATIONS, SOME HOLE IN BLUETOOTH STACK?
#				dev.writeCharacteristic((char.getHandle()+1), b"\x01\x00", withResponse=True)
			except: 
				print "Failed to turn on notifications at handle..."
				print  char.getHandle()
		
	else:
		print "Else called with: " 
		print  char.getHandle()		
	
# GET STRING VALUES OF VARIABLES ON MICROCONTROLLER: 
charvaluedict = {} # MC data for comparison
for uuid in chardict:
	charvaluedict[ uuid ] =  changeformat(chardict[uuid].read()) #returns binary version of hex value



#print "Charvaluedict: "
#print charvaluedict

with open('variables.yml','w') as f:
	yaml.dump(charvaluedict,f)

# READ YAML DOC --------------------------------------------------------------------
vardict = {} # yaml data for comparison
with open('variables.yml','r') as f:
	vardict = yaml.load(f)
#print vardict
print "dictionary compare test: "
print vardict == charvaluedict 

# Manually change a value in the yaml file: 
#charvaluedict[VolumeUUID] = str("\x01") # this seems to be 
#== to 1 for the microcontroller. charvaluedict[ModeUUID] = 
#hex(2)
# COMPARE YAML VARIABLES TO MICROCONTROLLER VARIABLES -------------------------------
# ... updates MC if not equal
#for var in vardict:
#	print "Value from yaml to be written to mc"
#	print vardict[var]	
#	print type(vardict[var])
#
#	if chardict[var].read() != vardict[var]:
#		chardict[var].write(chr(vardict[var]))
#		charvaluedict[var] = vardict[var]
#		print "init Writing " + var

#THIS MUST BE AFTER NOTIFICATIONS HAVE BEEN SET UP OR ELSE NOTIFICATIONS WILL TRIGGER 
dev.withDelegate(MyDelegate(btle.DefaultDelegate))


# MAIN LOOP =========================================================================
notification_timer = time.clock()
while True:
	# NOTE: MAY BE PROBLEMS WITH A TIMEOUT
	if dev.waitForNotifications(0.25): # checks for notifications for a second every loop
		#handleNotification() was called
		
#		print "Time since notification Handler called: " + str(time.clock()-notification_timer) 
		notification_timer = time.clock()

	
	print "Waiting..."	
	start_time = time.clock()
	# print ord(chardict[VolumeUUID].read())
	# here we want to watch the yaml file for any changes:
	with open('variables.yml', 'r') as f:
		vardict = yaml.load(f)
	#Read the accelerometer variable:
	#Add it to the yaml doc for writing. 	
	


	# this is only looking at the yaml:
	for var in vardict:
		#print vardict[var]
		if var == ZAccelUUID: 
#			print "Results read from mc & yaml for accel initial: "
			#print str(changeformat(chardict[var].read()))
#			print vardict[var]
			try:
				#print "read mc " + str(changeformat(chardict[var].read()))

				# This is where the yaml doc is updated with the value from the mc.
				#result = pool.apply_async(wryml.writeYaml,[str(5)+str(changeformat(chardict[var].read()))],callback=finish)
				wryml.writeYaml(str(5)+str(changeformat(chardict[var].read())))
			except:
				print "Failure to read from MC OR to write to yaml doc."
			
		else:
			if charvaluedict[var] != vardict[var]:
				print "\n vardict[var] value :" + str(vardict[var])
				try:
					if var == NextTrackUUID:
						print " Next Track Attempted Write!"

						# then we need to check if its a zero attempted write, and then just skip this.
						if vardict[var] == 1:
							chardict[var].write(chr(vardict[var]))
							print " Successful Write! Next Track"
							wryml.writeYaml(str(10))
						else:
							#chardict[var].write(chr(vardict[var]))

							print "attempted to write a zero to already zero!"

					else:
						chardict[var].write(chr(vardict[var]))
				
				except:
					print "BTLE EXCEPTION THROWN"
				
				charvaluedict[var] = vardict[var]
				#print "\nWriting Successful! " + str(vardict[var])
	
	#print "Time Elapsed: " + str(time.clock() - start_time)

	
try:
	dev.disconnect()
except Keboardinterrupt:
	print("cntrl+c Detected!")
	
sys.exit(0)
