<?php
    $number = readline("enter number");
    for($j= 2; $j<=$number; $j++){
        for($i=2 ; $i<$j; $i++){
            if($j%$i == 0){
                // echo "number is composite";
                break;
            }
            else{
                echo " $j ";
                break;
            }
        }
    }
    