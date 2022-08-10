<?php
$servername = "localhost";
$username = "root";
$password = "";
$databasename = "moodmie";
$con = new mysqli($servername,$username,$password,$databasename);
if($con->connect_error)
{
    die("Failed to connect to database");
}

?>