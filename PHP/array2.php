<?php
$name_one = array("arun","kk","SS","Sandeep","Kamal");

// echo $name_one[2], "\n", $name_one[0], "\n", $name_one[4],"\n" ;


//way to create an array
$name_two[0] = "arun";
$name_two[1] = "sanjay";
$name_two[2] = "kumar";
$name_two[3] = "prema";
$name_two[4] = "priya";

//accessing

// echo $name_two[2], "\n";
// echo $name_two[0], "\n";
// echo $name_two[4], "\n";

//using for loop
// foreach ($name_two as $name) {
//     # code...
//     echo $name ,"\n";
// }

for($i=0; $i<count($name_two); $i++){
    if($name_two[$i]=='kumar'){
            $start = $i;
        }
        else if($name_two[$i] == 'prema'){
            $end = $i;
        }
}
for ($i = $start; $i<=$end; $i++){
    echo $name_two[$i], "\n";
}

?>