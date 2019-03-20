<?php

session_start();

require ("config.inc.php");
$con = mysqli_connect($database_host, $database_user, $database_pass, $group_dbnames[0]);

$is_TA = $_SESSION['teacherBool'];

$lab = $_POST['selected_lab'];

echo "<h4>$lab</h4><br>";
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
        //echo "Computer no.<b>$computerID</b> is free<br>";
        $num_free_seats++;
    }
}

if ($num_free_seats == 0) {
    echo "There are no free seats<br>";
}
else if ($num_free_seats == 1) {
    echo "There is 1 free seat<br>";
}
else {
    echo "There are $num_free_seats free seats";
}

echo "<br><hr><br>";


$lab_query = mysqli_fetch_assoc(mysqli_query($con, "SELECT * FROM desiredGroups"));
$desired_lab = $lab_query[$lab_to_query];

$noOfStudentsNotInLab = 0;

//do this part only if they are an admin - show people that shouldnt be there
if ($is_TA) {
  if ($desired_lab != '-') {
      echo "<h6><b>Students that shouldn't be in the lab:</b></h6>";
      $query = mysqli_query($con, "SELECT * FROM compStatus");
      while ($query_row = mysqli_fetch_assoc($query)){
          echo "<br>";
          $computerID = $query_row['computerID'];
          $labs = $query_row['labs'];
          $labs_array = explode(',', $labs);

          if ($labs_array[$array_index] != 'empty'
              && $labs_array[$array_index] != $desired_lab
                && $labs_array[$array_index] != ' ') {
              echo "Student at computer no.<b>$computerID</b> is not in this lab";
              $noOfStudentsNotInLab++;
          }
      }
      if ($noOfStudentsNotInLab == 0) {
          echo "None";
      }
  }
  else {
      echo "There are no labs currently scheduled in this room";
  }
}

else {
  if ($desired_lab != '-') {
      echo "There is currently a scheduled lab in this room";
  }
  else {
      echo "There are no labs currently scheduled in this room";
  }
}



echo "<br>";
/*
$commandLF31 = escapeshellcmd('python LF31/drawLF31.py');
$outputLF31 = shell_exec($commandLF31);
echo "$outputLF31";

$commandTootill0 = escapeshellcmd('python Tootill0/drawTootill0.py');
$outputTootill0 = shell_exec($commandTootill0);
echo "$outputTootill0";

$commandTootill1 = escapeshellcmd('python Tootill1/drawTootill1.py');
$outputTootill1 = shell_exec($commandTootill1);
echo "$outputTootill1";


sleep(3);
*/


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

//$newFileName = '';
/*
if (file_exists('LF31Staff.png')) {
    $newFileName = 'LF31Staff2.png';
    //unlink('LF31Staff.png');
}
if (file_exists('LF31Student.png')) {
    $newFileName = 'LF31Student2.png';
    //unlink('LF31Student.png');
}
if (file_exists('Tootill1Staff.png')) {
    $newFileName = 'Tootill1Staff2.png';
    //unlink('Tootill1Staff.png');
}
if (file_exists('Tootill1Student.png')) {
    $newFileName = 'Tootill1Student2.png';
    //unlink('Tootill1Student.png');
}
if (file_exists('Tootill0Staff.png')) {
    $newFileName = 'Tootill0Staff2.png';
    //unlink('Tootill0Staff.png');
}
if (file_exists('Tootill0Student.png')) {
    $newFileName = 'Tootill0Student2.png';
    //unlink('Tootill0Student.png');
}

if ($_SESSION['newFileName'] == 'image1') {

    file_put_contents('LF31Staff.png', base64_decode($staffStringLF31[0]));
    file_put_contents('LF31Student.png', base64_decode($studentStringLF31[0]));
    file_put_contents('Tootill1Staff.png', base64_decode($staffStringTootill1[0]));
    file_put_contents('Tootill1Student.png', base64_decode($studentStringTootill1[0]));
    file_put_contents('Tootill0Staff.png', base64_decode($staffStringTootill0[0]));
    file_put_contents('Tootill0Student.png', base64_decode($studentStringTootill0[0]));



    if ($lab == 'LF31' && $is_TA) {
        echo "<script>document.getElementById('image').src='LF31Staff.png';</script>";
    }
    else if ($lab == 'LF31' && !$is_TA) {
        echo "<script>document.getElementById('image').src='LF31Student.png';</script>";
    }

    else if ($lab == 'TOOTILL1' && $is_TA) {
        echo "<script>document.getElementById('image').src='Tootill1Staff.png';</script>";
    }
    else if ($lab == 'TOOTILL1' && !$is_TA) {
        echo "<script>document.getElementById('image').src='Tootill1Student.png';</script>";
    }

    else if ($lab == 'TOOTILL0' && $is_TA) {
        echo "<script>document.getElementById('image').src='Tootill0Staff.png';</script>";
    }
    else if ($lab == 'TOOTILL0' && !$is_TA) {
        echo "<script>document.getElementById('image').src='Tootill0Student.png';</script>";
    }



    $_SESSION['newFileName'] = 'image2';
}

else {

    file_put_contents('LF31Staff2.png', base64_decode($staffStringLF31[0]));
    file_put_contents('LF31Student2.png', base64_decode($studentStringLF31[0]));
    file_put_contents('Tootill1Staff2.png', base64_decode($staffStringTootill1[0]));
    file_put_contents('Tootill1Student2.png', base64_decode($studentStringTootill1[0]));
    file_put_contents('Tootill0Staff2.png', base64_decode($staffStringTootill0[0]));
    file_put_contents('Tootill0Student2.png', base64_decode($studentStringTootill0[0]));



    if ($lab == 'LF31' && $is_TA) {
        echo "<script>document.getElementById('image').src='LF31Staff2.png';</script>";
    }
    else if ($lab == 'LF31' && !$is_TA) {
        echo "<script>document.getElementById('image').src='LF31Student2.png';</script>";
    }

    else if ($lab == 'TOOTILL1' && $is_TA) {
        echo "<script>document.getElementById('image').src='Tootill1Staff2.png';</script>";
    }
    else if ($lab == 'TOOTILL1' && !$is_TA) {
        echo "<script>document.getElementById('image').src='Tootill1Student2.png';</script>";
    }

    else if ($lab == 'TOOTILL0' && $is_TA) {
        echo "<script>document.getElementById('image').src='Tootill0Staff2.png';</script>";
    }
    else if ($lab == 'TOOTILL0' && !$is_TA) {
        echo "<script>document.getElementById('image').src='Tootill0Student2.png';</script>";
    }



    $_SESSION['newFileName'] = 'image1';
}
*/

$newFileName = $_SESSION['newFileName'];

file_put_contents("LF31Staff$newFileName.png", base64_decode($staffStringLF31[0]));
file_put_contents("LF31Student$newFileName.png", base64_decode($studentStringLF31[0]));
file_put_contents("Tootill1Staff$newFileName.png", base64_decode($staffStringTootill1[0]));
file_put_contents("Tootill1Student$newFileName.png", base64_decode($studentStringTootill1[0]));
file_put_contents("Tootill0Staff$newFileName.png", base64_decode($staffStringTootill0[0]));
file_put_contents("Tootill0Student$newFileName.png", base64_decode($studentStringTootill0[0]));



if ($lab == 'LF31' && $is_TA) {
    echo "<script>document.getElementById('image').src='LF31Staff' . '$newFileName' . '.png';</script>";
}
else if ($lab == 'LF31' && !$is_TA) {
    echo "<script>document.getElementById('image').src='LF31Student'.$newFileName.'.png';</script>";
}

else if ($lab == 'TOOTILL1' && $is_TA) {
    echo "<script>document.getElementById('image').src='Tootill1Staff' . '$newFileName' . '.png';</script>";
}
else if ($lab == 'TOOTILL1' && !$is_TA) {
    echo "<script>document.getElementById('image').src='Tootill1Student'.$newFileName.'.png';</script>";
}

else if ($lab == 'TOOTILL0' && $is_TA) {
    echo "<script>document.getElementById('image').src='Tootill0Staff' . '$newFileName' . '.png';</script>";
}
else if ($lab == 'TOOTILL0' && !$is_TA) {
    echo "<script>document.getElementById('image').src='Tootill0Student'.$newFileName.'.png';</script>";
}


$_SESSION['newFileName'] = $newFileName + 1;



?>
