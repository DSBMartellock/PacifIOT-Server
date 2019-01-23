<?php 
//RUN the BLE OVERWATCHER HERE:
 //THIS IS HOW:
$commandstring = 'python bleOverwatcher.py';
$command = escapeshellcmd($commandstring);
$output = shell_exec($command);
echo($output);
//*/
?>
