<!DOCTYPE html>
<?php

session_start();
if (isset($_SESSION['loggedIn'])) {
	header("Location: index.php");
}
else {
  if (isset($_SESSION['loginErrorMessage'])) {
    $loginErrorMessage = $_SESSION['loginErrorMessage'];
    unset($_SESSION['loginErrorMessage']);
  }
}


?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Login Page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="heading">
      Sign in to Labchecker
    </div>
    <div class="form-box">
      <form action="Login.php" method="post" autocomplete="off">  <!--haven't made main page-->
        <div class="textbox">
        Username
        <input type="text" name="Username" Placeholder="your username here" onclick="checkInput()" id="Username" maxlength=128 required><br>
        </div>
        <div class="textbox">
        Password
        <input type="password" name="Password" Placeholder="your password here" onclick="checkInput()" id="Password" maxlength=128 required><br>
        </div>
        <p style="color:red; font-size: 50px;"><?php echo "$loginErrorMessage"; ?> </p>
         <input type="button" class="btn" onclick="showPassword()" value="Show Password" id="showPassBtn">
         <script type="text/javascript">
              function showPassword() {
                var inputText = document.getElementById("Password");
                if (inputText.type == "password") {
                  inputText.type = "text";
                } else {
                  inputText.type = "password";
                }
              }
        </script>

        <script type="text/javascript">
              function checkInput() {
                if (Username.value.length > 0 && Password.value.length > 0)
                 document.getElementById('loginBtn').disabled = false;
                else
                 document.getElementById('loginBtn').disabled = true;
                }
        </script>
        <!--<input type="submit" class="btn" value="Login" id="loginBtn" onclick="index.php">-->
        <input type="submit" class="btn" value="Login" id="loginBtn">
     </form>
    </div>
    <a class="footer"></a>
  </body>
</html>
