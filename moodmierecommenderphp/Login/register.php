<?php

require "conn.php";

if (isset($_POST["user_email"]) && isset($_POST["username"]) && isset($_POST["password"])) {
    $email = $_POST["user_email"];
    $username = $_POST["username"];
    $password = $_POST["password"];

    $querysave = "INSERT INTO user_info(username,password,user_email) VALUES ('$username','$password','$email')";
    if($con->query($querysave))
    {
        echo "Success";
    }
    else{echo "Error";}
}