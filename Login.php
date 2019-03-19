 <?php
        //function login() {
         //$database_host = "dbhost.cs.man.ac.uk";
         //$database_user = "[insert username]";
         //$database_pass = "[insert password]";
         //$group_dbNames = array("2018_comp10120_w4",);
         require ("config.inc.php");
         $dbConn = new mysqli($database_host, $database_user, $database_pass, $group_dbnames[0]);
         if ($dbConn->connect_error) {
          die("Connection failed: " . $dbConn->connect_error);
         }
         else {
          $inputUsername = $_POST['Username'];
          $inputPassword = $_POST['Password'];
          $sqlQuery = "SELECT Teacher, Lab Group FROM Account WHERE Username = '$inputUsername' AND Password = '$inputPassword'";
          $result = $dbConn->query(sqlQuery);
          if ($result->num_rows > 0) {
           session_start();
           $_SESSION['usernameLog'] = $result["Username"];
           $_SESSION['passwordLog'] = $result["Password"];
           $_SESSION['teacherBool'] = $result["Teacher"];
           $_SESSION['labGroup'] = $result["Lab Group"];
           header("Location: index.php");
           }
          else {
           $noResults = "Username or password is wrong";
           echo '<script type="text/javascript">alert("Username or password is wrong");</script>';
           $dbConn->close();
           //header("Location: Login.html");
          }
        }
?>
