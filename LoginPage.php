<!DOCTYPE html>
<?php

session_start();
if (isset($_SESSION['loggedIn'])) {
	header("Location: index.php");
}
else {
  if (isset($_SESSION['loginErrorMessage'])) {
    $loginErrorMessage = "<br><br><i>".$_SESSION['loginErrorMessage']."</i><br>";
    unset($_SESSION['loginErrorMessage']);
  }
  else {
    $loginErrorMessage = "";
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
      <form action="Login.php" method="post" autocomplete="off">
        <div class="textbox">
        Username
        <input type="text" name="Username" Placeholder="your username here" onclick="checkInput()" id="Username" maxlength=128 required><br>
        </div>
        <div class="textbox">
        Password
        <input type="password" name="Password" Placeholder="your password here" onclick="checkInput()" id="Password" maxlength=128 required><br>
        </div>
        <p style="color:red; font-size: 18px; text-align: center;"><?php echo "$loginErrorMessage"; ?> </p>
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

        <input type="submit" class="btn" value="Login" id="loginBtn">
     </form>
    </div>
    <a class="footer"></a>
  </body>
</html>
