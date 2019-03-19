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
$con = mysqli_connect($database_host, $database_user, $database_pass, $group_dbnames[0]);
$is_TA = TRUE;

//$is_TA = $_SESSION['teacher'];

$lab = $_POST['selected_lab'];

echo "<h5>$lab</h5><br>";
$array_index = 0;
$lab_to_query = null;

if ($lab == 'LF31') {
    $array_index = 0;
    $lab_to_query = 'LF31';
}
else if ($lab == 'TOOTILL1') {
    $array_index = 1;
    $lab_to_query = 'Tootill 1';
}
else if ($lab == 'TOOTILL0') {
    $array_index = 2;
    $lab_to_query = 'Tootill 0';
}
else {
    $array_index = 0;
}


//do this part for all - free computers
$query = mysqli_query($con, "SELECT * FROM compStatus");
while ($query_row = mysqli_fetch_assoc($query)){
    $computerID = $query_row['computerID'];
    $labs = $query_row['labs'];
    $labs_array = explode(',', $labs);
/*
    echo "Comp number = $computerID<br>";
    echo "LF31 = $labs_array[0]<br>";
    echo "TOOTILL 1 = $labs_array[1]<br>";
    echo "TOOTILL 0 = $labs_array[2]<br>";
*/
    if ($labs_array[$array_index] == 'empty') {
        echo "Computer no.$computerID is free<br>";
    }
}


$lab_query = mysqli_query($con, "SELECT $lab_to_query FROM desiredGroups");
$desired_lab = mysqli_fetch_assoc($lab_query);
echo "///////////////////////<br>";
echo "$desired_lab<br>";
echo "///////////////////////<br>";

//do this part only if they are an admin - show people that shouldnt be there
$query = mysqli_query($con, "SELECT * FROM compStatus");
while ($query_row = mysqli_fetch_assoc($query)){
    $computerID = $query_row['computerID'];
    $labs = $query_row['labs'];
    $labs_array = explode(',', $labs);
/*
    echo "Comp number = $computerID<br>";
    echo "LF31 = $labs_array[0]<br>";
    echo "TOOTILL 1 = $labs_array[1]<br>";
    echo "TOOTILL 0 = $labs_array[2]<br>";
*/

/*
    if ($labs_array[$array_index] != 'empty' && $labs_array[$array_index] != 'empty') {
        echo "Computer no.$computerID is free<br>";
    }*/
}

//if lab == a database lab
///////////////////$query = mysqli_query($con, );
//else if lab == other database lab

/////////////////////while ($query_row = mysqli_fetch_assoc($query)){
  //echo this computer is free
/////////////////////}


echo "<p>This form has submitted correctly</p>";




?>
