<?php
//sort array in ascending order according to value asort()

$age = array("ayush"=>23,"shankar"=>47,"Kailash"=>41);
sort($age);

foreach($age as $x => $x_value){
    echo "Key=" .$x. ", Value =" . $x_value . "\n";
    // echo "<br>";
}
?>