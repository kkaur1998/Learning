<html>
    <head>
        <title>php forms</title>
    </head>


    <body>
        <form method = "post">
            Enter First no.: <input type = "text" name = "fno"/><hr/>
            Enter Second no.: <input type = "text" name = "sno"/><hr/>

            <input type="submit" name= "add" value = "ADD"/>
        </form>
        <?php

        if(isset($_POST['add'])){
            $x = $_POST['fno'];
            $y = $_POST['sno'];
            $sum = $x + $y;
            echo "Result: <input type = 'text' value = '$sum'\>";
        }


        ?>
    </body>


</html>