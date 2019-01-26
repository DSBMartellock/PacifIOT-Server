# PacifIOT-Server
The main data collection/inbetween for the pacifIOT project. Completed for RIT senior design. 

Im a mechanical engineer, its a bit hacky, cut me some slack!

Input data monitoring: 
Connects to our Microcontroller on the baby jumper, and watches for any changes in the data being broadcast to it over BLE.
Compares the data gotten from BLE to a yaml file. 
Posts all of the data to an apache web page which was then parsed by a simple android application. 
This was used to display accelerometer data for the microcontroller, Fitbit for babies! 

Output/Microcontroller state change. 
The webpage also had some urls to set the state of the yaml file, the main script checks if there are any changes to the yaml file that werent caused by the script changing it, and ipso facto, sent out the appropriate command to the microcontroller to write the state to the microcontroller. 
This was used to change the volume, change the song playing, play and pause audio, and set the LED brightness. 
