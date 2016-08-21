<?php
//This script will give you the EPOCH format of the date in which the next rubbish and recycling will be collected by Auckland Council.
//Get you valuation from the Council website and enter it in the variable named "valuation_num"
//

$valuation_num = "00000-00000"
$i=0;

function curl($url) {
    $ch = curl_init();  // Initialising cURL
    curl_setopt($ch, CURLOPT_URL, $url);    // Setting cURL's URL option with the $url variable passed into the function
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE); // Setting cURL's option to return the webpage data
     $data = curl_exec($ch); // Executing the cURL request and assigning the returned data to the $data variable
     curl_close($ch);    // Closing cURL
     return $data;   // Returning the data from the function
}
//Retrieve the page
$aklrubbishscrape = curl("https://akl.eps.blinkm.co/_api/interaction/run/mobi/CollectionResult_xhr?valuation_num="+valuation_num);  

$dom = new DOMDocument;
$dom->loadHTML($aklrubbishscrape);
//Get all the spans on the page
$links = $dom->getElementsByTagName('span');
$stack = array();
//Loop through the spans, first is rubbish and second span is recycling.
foreach ($links as $link){
	
	if($i==0){
		$stack['trash'] = strtotime($link->textContent)."001";
	}else{
		$stack['recycle'] = strtotime($link->textContent)."001";
	}
	$i++;
}
echo json_encode($stack);

?>
