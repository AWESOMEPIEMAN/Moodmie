<?php
require "conn.php";
if(isset($_POST["user_email"]) && isset($_POST["password"]))
{
    $email = $_POST["user_email"];
    $password = $_POST["password"];

    $usercheckquery = "SELECT * FROM user_info where user_email='$email' and password='$password'";
    $results = $con->query($usercheckquery);
    if ($results->num_rows > 0)
    {
        echo "Success";
    }
    else{echo "Failed";}
}
?>