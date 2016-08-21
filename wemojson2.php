<?php
$wemoip = 192.168.0.101

if(isset($_GET['command'])){

	if($_GET['command']=="on"){
	        exec('/var/www/html/homecontrol/wemo '.$wemoip.' ON', $output, $retval);
	}
	if($_GET['command']=="off"){
	        exec('/var/www/html/homecontrol/wemo '.$wemoip.' OFF', $output, $retval);
	}
	sleep(2);
}   
        exec('/var/www/html/homecontrol/wemo '.$wemoip.' GETSTATE', $output, $retval);


        $stack['status'] = $output;

echo json_encode($stack);

?>


