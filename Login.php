 <?php
         session_start();
         require ("config.inc.php");
         $dbConn = mysqli_connect($database_host, $database_user, $database_pass, $group_dbnames[0]);
         if ($dbConn->connect_error) {
           die("Connection failed: " . $dbConn->connect_error);
         }
         else {
           $inputUsername = $_POST['Username'];
           $inputPassword = $_POST['Password'];

           $query = mysqli_query($dbConn, "SELECT * FROM Users WHERE Username = '$inputUsername' AND Password = '$inputPassword'");
           if (mysqli_num_rows($query) != 0) {
             $query_row = mysqli_fetch_assoc($query);
             $_SESSION['teacherBool'] = $query_row["Teacher"];
             $_SESSION['labGroup'] = $query_row["LabGroup"];
             $_SESSION['loggedIn'] = TRUE;

             header("Location: index.php");
           }
           else {
             $noResults = "Username or password is incorrect";

             $_SESSION['loginErrorMessage'] = $noResults;
             header("Location: LoginPage.php");
           }
         }
?>
