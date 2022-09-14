<html>
    <head>
        <title>php forms</title>
    </head>


    <body>
        
        <form method = "post">
        <table>
            <tr>
                <td>Enter name: </td>
                <td><input type = "text" name = "name"/><hr/></td>
            </tr>
            <tr>
                <td>Enter class: </td>
                <td><input type = "text" name = "class"/><hr/></td>
            </tr>
            <tr>
                <td>Enter roll_no: </td>
                <td><input type = "text" name = "roll_no"/><hr/></td>
            </tr>
        </table>

        </form>
        <?php

        // if(isset($_POST['add'])){
        //     $x = $_POST['fno'];
        //     $y = $_POST['sno'];
        //     $sum = $x + $y;
        //     echo "Result: <input type = 'text' value = '$sum'\>";
        // }


        ?>
    </body>


</html>