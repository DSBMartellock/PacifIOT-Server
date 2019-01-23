
<?php echo(nl2br("hello \nfrom \nindex!\n")) ?> 


<?php
/*
//INITIALIZE VARIABLES:
$setup = (int) 1;

//BLE SET UP FIRST TIME ONLY:
if($setup == 1){
	exec("sudo bluetoothctl power on");
	echo(exec("sudo hciconfig hci0 up"));
	@setup = (int) 0;
}
//set up javascript:
//has own variables that are settable

// monitors a change in those variables:
//USES SOME KIND OF PYTHON PROGRAM THAT will check the variables and the difference in the variables. 
//Response from python program  will be the current variable values
//Python program will take any differences in the variables passed to it for designated writable chars and send write requests (asynch?)
//portion of python program that uses the notfiy char things and runs continuously?

//*/


?>



<?php //HERE BE URLS:

//First Time Set Up:
if(isset($_GET['setup'])){
	exec("sudo bluetoothctl power on");
	echo(exec("sudo hciconfig hci0 up"));
}

//Write Methods:
if(isset($_GET['volume'])) {
	if(empty($_GET['volume'])){
	 	$commandstring = '/home/pi/Documents/python_projects/readChar.py 1';
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo("Value: ");
		echo("<br>");
		echo($output);
	}
	else{	
		$shiftedvar = (int)$_GET['volume'];
		$stringShifted =  $shiftedvar-1;
		$commandstring = '/home/pi/Documents/python_projects/writeChar.py 1 '.$stringShifted;
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo($output);
	}	
}
if(isset($_GET['nexttrack'])) {
	if(empty($_GET['nexttrack'])){
	 	$commandstring = '/home/pi/Documents/python_projects/readChar.py 2';
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo("Value: ");
		echo("<br>");
		echo($output);

	}
	else{	
		$shiftedvar = (int)$_GET['nexttrack'];
		$stringShifted =  $shiftedvar-1;

		$commandstring = '/home/pi/Documents/python_projects/writeChar.py 2 '.$stringShifted;
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo($output);
	}
}
if(isset($_GET['play'])) {
	if(empty($_GET['play'])){
	 	$commandstring = '/home/pi/Documents/python_projects/readChar.py 3';
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo("Value: ");
		echo("<br>");
		echo($output);

	}
	else{	

		$shiftedvar = (int)$_GET['play'];
		$stringShifted =  $shiftedvar-1;

		$commandstring = '/home/pi/Documents/python_projects/writeChar.py 3 '.$stringShifted;
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo($output);
	}
}
if(isset($_GET['mode'])) {
	if(empty($_GET['mode'])){
	 	$commandstring = '/home/pi/Documents/python_projects/readChar.py 4';
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo("Value: ");
		echo("<br>");
		echo($output);

	}
	else{	
		$shiftedvar = (int)$_GET['mode'];
		$stringShifted =  $shiftedvar-1;

		$commandstring = '/home/pi/Documents/python_projects/writeChar.py 4 '.$stringShifted;
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo($output);
	}
}
if(isset($_GET['brightness'])) {
	if(empty($_GET['volume'])){
	 	$commandstring = '/home/pi/Documents/python_projects/readChar.py 5';
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo("Value: ");
		echo("<br>");
		echo($output);

	}
	else{	
		$shiftedvar = (int)$_GET['brightness'];
		$stringShifted =  $shiftedvar-1;

		$commandstring = '/home/pi/Documents/python_projects/writeChar.py 5 '.$stringShifted;
		$command = escapeshellcmd($commandstring);
		$output = shell_exec($command);
		echo($output);
	}
}

if(isset($_GET['setup'])){
	echo(exec("sudo hciconfig hci0 up"));

}



?>
