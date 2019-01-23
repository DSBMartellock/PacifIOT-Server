<?php 
//run on page load only? hmmmm
exec("sudo bluetoothctl power on");
exec("sudo hciconfig hci0 up");

//RUN THE YAML WRITER FLASK PYTHON SCRIPT RUNNER:
$output = shell_exec("/usr/bin/php /var/www/html/yamlwriterunner.php | at now &");
echo($output);

//RUN the BLE OVERWATCHER HERE:
$output = shell_exec("/usr/bin/php /var/www/html/blerunner.php | at now &");
echo($output);


include('mainpage.html');

?>
