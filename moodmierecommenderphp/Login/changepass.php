<?php
require "conn.php";
if(isset($_POST["user_email"]) && isset($_POST["password"]))
{
    $email = $_POST["user_email"];
    $password = $_POST["password"];
    $passwordquery = "UPDATE user_info SET password='$password' WHERE user_email='$email'";
    $checkquery = "SELECT * FROM user_info where user_email='$email'";
    $result = $con->query($checkquery);
    if ($result->num_rows > 0)
    {
        $con->query($passwordquery);
        echo "Success";
    }
    else{
        echo "Failed";
    }


}
?>