<?php

$numbers = array(40,61,2,22,13);
sort($numbers);
// rsort($numbers);
echo "till here\n";
$arrlength = count($numbers);
for ($x = $arrlength-1 ; $x >=0 ; $x--){
    echo $numbers[$x], "\n";
    // echo "<br>";
}

?>