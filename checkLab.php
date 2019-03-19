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
        echo "Computer no.<b>$computerID</b> is free<br>";
    }
}


$lab_query = mysqli_fetch_assoc(mysqli_query($con, "SELECT * FROM desiredGroups"));
$desired_lab = $lab_query[$lab_to_query];

if ($desired_lab != '-') {
    echo "<br><h6><b>These students should not be in the lab:</b></h6>";
}

//do this part only if they are an admin - show people that shouldnt be there
if ($is_TA) {
  if ($desired_lab != '-') {
      echo "<br><h6><b>These students should not be in the lab:</b></h6>";
      $query = mysqli_query($con, "SELECT * FROM compStatus");
      while ($query_row = mysqli_fetch_assoc($query)){
          $computerID = $query_row['computerID'];
          $labs = $query_row['labs'];
          $labs_array = explode(',', $labs);

          if ($labs_array[$array_index] != 'empty'
              && $labs_array[$array_index] != $desired_lab
                && $labs_array[$array_index] != ' ') {
              echo "Student at computer no.<b>$computerID</b> is not in this lab<br>";
          }
      }
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

if (file_exists('LF31Staff.png')) {
    unlink('LF31Staff.png');
}
if (file_exists('LF31Student.png')) {
    unlink('LF31Student.png');
}
if (file_exists('Tootill1Staff.png')) {
    unlink('Tootill1Staff.png');
}
if (file_exists('Tootill1Student.png')) {
    unlink('Tootill1Student.png');
}
if (file_exists('Tootill0Staff.png')) {
    unlink('Tootill0Staff.png');
}
if (file_exists('Tootill0Student.png')) {
    unlink('Tootill0Student.png');
}


file_put_contents('LF31Staff.png', base64_decode($staffStringLF31[0]));
file_put_contents('LF31Student.png', base64_decode($studentStringLF31[0]));
file_put_contents('Tootill1Staff.png', base64_decode($staffStringTootill1[0]));
file_put_contents('Tootill1Student.png', base64_decode($studentStringTootill1[0]));
file_put_contents('Tootill0Staff.png', base64_decode($staffStringTootill0[0]));
file_put_contents('Tootill0Student.png', base64_decode($studentStringTootill0[0]));



if ($lab == 'LF31' && $is_TA) {
    echo '<script>document.getElementById("image").src="LF31Staff.png"</script>';
}
else if ($lab == 'LF31' && !$is_TA) {
    echo '<script>document.getElementById("image").src="LF31Student.png"</script>';
}

else if ($lab == 'TOOTILL1' && $is_TA) {
    echo '<script>document.getElementById("image").src="Tootill1Staff.png"</script>';
}
else if ($lab == 'TOOTILL1' && !$is_TA) {
    echo '<script>document.getElementById("image").src="Tootill1Student.png"</script>';
}

else if ($lab == 'TOOTILL0' && $is_TA) {
    echo '<script>document.getElementById("image").src="Tootill0Staff.png"</script>';
}
else if ($lab == 'TOOTILL0' && !$is_TA) {
    echo '<script>document.getElementById("image").src="Tootill0Student.png"</script>';
}



?>
