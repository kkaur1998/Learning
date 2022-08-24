<?php
    $number = readline("enter number");
    // for($j= 2; $j<=$number; $j++){
    //     for($i=2 ; $i<$j; $i++){
    //         if($j%$i == 0){
    //             // echo "number is composite";
    //             break;
    //         }
    //         else{
    //             echo " $j ";
    //             break;
    //         }
    //     }
    // }

    $num = $number;
    // $num = 2;
    // while($num<=$number){
        $i = 2;
        while($i<$num){
            $i = $i+1;
            if($num%$i == 0){
                $flag = 0;
                break;
            }
            else{
                $flag = 1;
                continue;
            }
            

        }
        if($flag == 1){
            echo "$num is prime";
        }
        else{
            echo "$num is composite";
        }
    //     $num = $num +1;
    // }

    