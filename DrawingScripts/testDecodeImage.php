
<?php

# this PHP script will pull the images as base64 encoded strings and save them 
# in the same directory the script is in. this script can be invoked whenever 
# needed, eg every 5 seconds for the demo of the website. remember to write a 
# config.php file (check the README). the images are saved and can then be displayed
# on the website as necessary


  # import the config file
  include 'config.php';


  # connect to the db using variables from the dbconfig file
  $conn = new mysqli($dbhost,$dbusername,$dbpassword, $dbname);

  if ($conn->connect_error)
  {
    die("oops" . $conn -> connect_error);
  }




  $queryLF31Staff = "SELECT LF31 FROM base64Images WHERE Type = 'Staff'";
  $queryLF31Student = "SELECT LF31 FROM base64Images WHERE Type = 'Student'";
  $queryTootill1Staff = "SELECT `Tootill 1` FROM base64Images WHERE Type = 'Staff'";
  $queryTootill1Student = "SELECT `Tootill 1` FROM base64Images WHERE Type = 'Student'";
  $queryTootill0Staff = "SELECT `Tootill 0` FROM base64Images WHERE Type = 'Staff'";
  $queryTootill0Student = "SELECT `Tootill 0` FROM base64Images WHERE Type = 'Student'";


  $resultLF31Staff = mysqli_query($conn, $queryLF31Staff);
  $resultLF31Student = mysqli_query($conn, $queryLF31Student);
  $resultTootill1Staff = mysqli_query($conn, $queryTootill1Staff);
  $resultTootill1Student = mysqli_query($conn, $queryTootill1Student);
  $resultTootill0Staff = mysqli_query($conn, $queryTootill0Staff);
  $resultTootill0Student = mysqli_query($conn, $queryTootill0Student);


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




?>
