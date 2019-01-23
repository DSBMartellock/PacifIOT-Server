<?php 


$commandstring = 'python writeYAML.py';
$command = escapeshellcmd($commandstring);
$output = shell_exec($command);
echo($output);

?>
