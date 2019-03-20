 <?php
        //function login() {
         //$database_host = "dbhost.cs.man.ac.uk";
         //$database_user = "[insert username]";
         //$database_pass = "[insert password]";
         //$group_dbNames = array("2018_comp10120_w4",);
         require ("config.inc.php");
         //$dbConn = new mysqli($database_host, $database_user, $database_pass, $group_dbnames[0]);
         $dbConn = mysqli_connect($database_host, $database_user, $database_pass, $group_dbnames[0]);
         if ($dbConn->connect_error) {
           die("Connection failed: " . $dbConn->connect_error);
         }
         else {
           $inputUsername = $_POST['Username'];
           $inputPassword = $_POST['Password'];
           //$sqlQuery = "SELECT * FROM Account WHERE Username = '$inputUsername' AND Password = '$inputPassword'";
           //$result = $dbConn->query($sqlQuery);
           $query = mysqli_query($dbConn, "SELECT * FROM Users WHERE Username = '$inputUsername' AND Password = '$inputPassword'");
           //if ($result->num_rows > 0) {
           if (mysqli_num_rows($query) != 0) {
             $query_row = mysqli_fetch_assoc($query);
             session_start();
             $_SESSION['usernameLog'] = $query["Username"];
             $_SESSION['passwordLog'] = $query_row["Password"];
             $_SESSION['teacherBool'] = $result["Teacher"];
             $_SESSION['labGroup'] = $result["LabGroup"];
             //header("Location: index.php");
             echo "<script>alert('Hello');</script>";
             echo "$_SESSION['usernameLog']";
             echo "<script>alert($_SESSION['passwordLog']);</script>";
           }
           else {
             $noResults = "Username or password is wrong";
             echo "<script type='text/javascript'>alert('Username or password is wrong');</script>";
             $dbConn->close();
             //header("Location: Login.html");
           }
         }
?>
