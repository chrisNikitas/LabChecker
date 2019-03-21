<?php

session_start();

require ("config.inc.php");
$con = mysqli_connect($database_host, $database_user, $database_pass, $group_dbnames[0]);

$data_to_echo = array();


$is_TA = $_SESSION['teacherBool'];

$lab = $_POST['selected_lab'];
//$_SESSION['navCurrentLab'] = $lab;

echo "<h4>$lab</h4><br>";
//array_push($data_to_echo, "<h4>$lab</h4><br>");

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

$num_free_seats = 0;
//do this part for all - free computers
$query = mysqli_query($con, "SELECT * FROM compStatus");
while ($query_row = mysqli_fetch_assoc($query)){
    $computerID = $query_row['computerID'];
    $labs = $query_row['labs'];
    $labs_array = explode(',', $labs);

    if ($labs_array[$array_index] == 'empty') {
        echo "Computer no.<b>$computerID</b> is free<br>";
        //array_push($data_to_echo, "Computer no.<b>$computerID</b> is free<br>");
        $num_free_seats++;
    }
}

if ($num_free_seats == 0) {
    echo "There are no free seats<br>";
    //array_push($data_to_echo, "There are no free seats<br>");
}
else if ($num_free_seats == 1) {
    echo "There is 1 free seat<br>";
    //array_push($data_to_echo, "There is 1 free seat<br>");
}
else {
    echo "There are $num_free_seats free seats";
    //array_push($data_to_echo, "There are $num_free_seats free seats");
}

echo "<br><hr><br>";
//array_push($data_to_echo, "<br><hr><br>");

echo "<h4><u>Key</u></h4><br>";

//echo "<div style='width:20px; height:20px; margin:5px; margin-top:0px; margin-left:15px; border:1px solid black; background: green'></div> - Available seats";

echo "<div style='display:inline-block;'><div style='width:20px; height:20px; margin:5px; border:1px solid black; background: red'></div> - Unavailable seats</div>";




echo "<br><hr><br>";


$lab_query = mysqli_fetch_assoc(mysqli_query($con, "SELECT * FROM desiredGroups"));
$desired_lab = $lab_query[$lab_to_query];

$noOfStudentsNotInLab = 0;

//do this part only if they are an admin - show people that shouldnt be there
if ($is_TA) {
  if ($desired_lab != '-') {
      echo "<h6><b>Students that shouldn't be in the lab:</b></h6>";
      //array_push($data_to_echo, "<h6><b>Students that shouldn't be in the lab:</b></h6>");
      $query = mysqli_query($con, "SELECT * FROM compStatus");
      while ($query_row = mysqli_fetch_assoc($query)){
          $computerID = $query_row['computerID'];
          $labs = $query_row['labs'];
          $labs_array = explode(',', $labs);

          if ($labs_array[$array_index] != 'empty'
              && $labs_array[$array_index] != $desired_lab
                && $labs_array[$array_index] != ' ') {
              echo "<br>Student at computer no.<b>$computerID</b> is not in this lab";
              //array_push($data_to_echo, "<br>Student at computer no.<b>$computerID</b> is not in this lab");
              $noOfStudentsNotInLab++;
          }
      }
      if ($noOfStudentsNotInLab == 0) {
          echo "None";
          //array_push($data_to_echo, "None");
      }
  }
  else {
      echo "There are no labs currently scheduled in this room";
      //array_push($data_to_echo, "There are no labs currently scheduled in this room");
  }
}

else {
  if ($desired_lab != '-') {
      echo "There is currently a scheduled lab in this room";
      //array_push($data_to_echo, "There is currently a scheduled lab in this room");
  }
  else {
      echo "There are no labs currently scheduled in this room";
      //array_push($data_to_echo, "There are no labs currently scheduled in this room");
  }
}



echo "<br>";
//array_push($data_to_echo, "<br>");






sleep(4);
//usleep(4150000);

$queryLF31Staff = "SELECT LF31 FROM base64Images WHERE Type = 'Staff'";
$queryLF31Student = "SELECT LF31 FROM base64Images WHERE Type = 'Student'";
$queryTootill1Staff = "SELECT `Tootill 1` FROM base64Images WHERE Type = 'Staff'";
$queryTootill1Student = "SELECT `Tootill 1` FROM base64Images WHERE Type = 'Student'";
$queryTootill0Staff = "SELECT `Tootill 0` FROM base64Images WHERE Type = 'Staff'";
$queryTootill0Student = "SELECT `Tootill 0` FROM base64Images WHERE Type = 'Student'";


$resultLF31Staff = mysqli_query($con, $queryLF31Staff);
$resultLF31Student = mysqli_query($con, $queryLF31Student);
$resultTootill1Staff = mysqli_query($con, $queryTootill1Staff);
$resultTootill1Student = mysqli_query($con, $queryTootill1Student);
$resultTootill0Staff = mysqli_query($con, $queryTootill0Staff);
$resultTootill0Student = mysqli_query($con, $queryTootill0Student);


$staffStringLF31 = array_values(mysqli_fetch_assoc($resultLF31Staff)); # numerically indexed array
$studentStringLF31 = array_values(mysqli_fetch_assoc($resultLF31Student)); # numerically indexed array
$staffStringTootill1 = array_values(mysqli_fetch_assoc($resultTootill1Staff)); # numerically indexed array
$studentStringTootill1 = array_values(mysqli_fetch_assoc($resultTootill1Student)); # numerically indexed array
$staffStringTootill0 = array_values(mysqli_fetch_assoc($resultTootill0Staff)); # numerically indexed array
$studentStringTootill0 = array_values(mysqli_fetch_assoc($resultTootill0Student)); # numerically indexed array



file_put_contents('LF31Staff.png', base64_decode($staffStringLF31[0]));
file_put_contents('LF31Student.png', base64_decode($studentStringLF31[0]));
file_put_contents('Tootill1Staff.png', base64_decode($staffStringTootill1[0]));
file_put_contents('Tootill1Student.png', base64_decode($studentStringTootill1[0]));
file_put_contents('Tootill0Staff.png', base64_decode($staffStringTootill0[0]));
file_put_contents('Tootill0Student.png', base64_decode($studentStringTootill0[0]));


echo "<script>var d = new Date();</script>";
//array_push($data_to_echo, "");

if ($lab == 'LF31' && $is_TA) {
    echo "<script>document.getElementById('image').src='LF31Staff.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='LF31Staff.png?'+d.getTime();</script>");
}
else if ($lab == 'LF31' && !$is_TA) {
    echo "<script>document.getElementById('image').src='LF31Student.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='LF31Student.png?'+d.getTime();</script>");
}

else if ($lab == 'TOOTILL1' && $is_TA) {
    echo "<script>document.getElementById('image').src='Tootill1Staff.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='Tootill1Staff.png?'+d.getTime();</script>");
}
else if ($lab == 'TOOTILL1' && !$is_TA) {
    echo "<script>document.getElementById('image').src='Tootill1Student.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='Tootill1Student.png?'+d.getTime();</script>");
}

else if ($lab == 'TOOTILL0' && $is_TA) {
    echo "<script>document.getElementById('image').src='Tootill0Staff.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='Tootill0Staff.png?'+d.getTime();</script>");
}
else if ($lab == 'TOOTILL0' && !$is_TA) {
    echo "<script>document.getElementById('image').src='Tootill0Student.png?'+d.getTime();</script>";
    //array_push($data_to_echo, "<script>document.getElementById('image').src='Tootill0Student.png?'+d.getTime();</script>");
}
/*
$new_lab = $_SESSION['navCurrentLab'];
if ($new_lab == $lab) {
    foreach($data_to_echo as $item_to_echo) {
        echo $item_to_echo;
    }
}
else {
  echo "$new_lab";
  echo "<br>";
  echo "$lab";
}
*/
/*
foreach($data_to_echo as $item_to_echo) {
    echo "$item_to_echo";
}
*/
?>
