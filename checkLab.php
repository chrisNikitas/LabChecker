<?php

/*
Connect to Database

Get the lab that we want


if not TA then:

For every computer in that lab that is free
print the computer number

if TA then:

For every computer in that lab that is free
print the computer number

For every computer that is occupied wrongly
print the computer number

return stuff to the div

*/

require ("connectivity.php");

//$is_TA = $_SESSION['TA'];

$lab = $_POST['lab_name'];


//if lab == a database lab
$query = mysqli_query($con, );
//else if lab == other database lab

while ($query_row = mysqli_fetch_assoc($query)){
  //echo this computer is free
}




?>
