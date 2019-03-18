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

require ("config.inc.php");
//$con = mysqli_connect($dbhost,$dbusername,$dbpassword,$dbname);
$con = new mysqli($database_host, $database_user, $database_pass, $group_dbnames[0]);
$is_TA = TRUE;
//$is_TA = $_SESSION['teacher'];

//////$lab = $_POST['selected_lab'];


//if lab == a database lab
///////////////////$query = mysqli_query($con, );
//else if lab == other database lab

/////////////////////while ($query_row = mysqli_fetch_assoc($query)){
  //echo this computer is free
/////////////////////}


echo "<p>This form has submitted correctly</p>";




?>
