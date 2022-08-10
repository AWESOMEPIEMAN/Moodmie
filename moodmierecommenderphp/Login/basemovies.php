<?php
require "conn.php";

$id = $_GET['id'];

$query = "Select * from nodup where Movie_id between ($id+1) and ($id+10) and  Rating > 51";

$results = mysqli_query($con,$query);

while ($row = mysqli_fetch_assoc($results))
{
    $array[] = $row;
}
header('Content-Type:Application/json');
echo json_encode($array);

?>