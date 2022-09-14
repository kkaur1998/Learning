<html>
	<head>
		<title>HTML Forms </title>
	</head>
	<body>
		<h1>HTML Form</h1>
		<form method="POST" action="login.php">
			Name: <input type="text" placeholder="enter user name" name="name"><br/>
			Email: <input type="email" placeholder="enter user name" name="name"><br/>
			Password: <input type="password" placeholder="enter password" name="pwd"><br/>
		</form>
	</body>

</html>
<?php
	if(empty($_POST['name']) && empty($_POST['
?>