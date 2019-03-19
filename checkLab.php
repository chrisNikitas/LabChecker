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

    if ($labs_array[$array_index] == 'empty') {
        echo "Computer no.$computerID is free<br>";
    }
}


$lab_query = mysqli_fetch_assoc(mysqli_query($con, "SELECT * FROM desiredGroups"));
$desired_lab = $lab_query[$lab_to_query];
$desired_lab = 'MW';
if ($desired_lab != '-') {
    echo "<br><h6>These students should not be in the lab</h6><br>"
}

//do this part only if they are an admin - show people that shouldnt be there
$query = mysqli_query($con, "SELECT * FROM compStatus");
while ($query_row = mysqli_fetch_assoc($query)){
    $computerID = $query_row['computerID'];
    $labs = $query_row['labs'];
    $labs_array = explode(',', $labs);

    if ($labs_array[$array_index] != 'empty'
        && $labs_array[$array_index] != $desired_lab
          && $labs_array[$array_index] != ''
            && $desired_lab != '-') {
        echo "Student at computer no.$computerID is not in this lab<br>";
    }
}

//if lab == a database lab
///////////////////$query = mysqli_query($con, );
//else if lab == other database lab

/////////////////////while ($query_row = mysqli_fetch_assoc($query)){
  //echo this computer is free
/////////////////////}


?>
