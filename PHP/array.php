<?php

//declare multidimentsional array
$a = array();
$a[0][0] = "arun";
$a[0][1] = "kumar";
$a[1][0] = "Kavitha";
$a[1][1] = "Prema";


//display multi-dimentsional array
foreach ($a as $e1){
    foreach($e1 as $e2){
        echo "$e2 \n";
    }
}
?>