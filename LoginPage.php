<!DOCTYPE html>
<?php
/*
session_start();
if (isset($_SESSION['loggedIn'])) {
  $is_it_set = "logged in";
}
else {
  if (isset($_SESSION['loginErrorMessage'])) {
    $is_it_set = "Thats wrong!!";
  }
  else {
    $is_it_set = "";
  }
}

*/
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
        <!--<p><?/*php echo "$is_it_set"; */?> </p>-->
        <div class="textbox">
        Username
        <input type="text" name="Username" Placeholder="your username here" onclick="checkInput()" id="Username" maxlength=128 required><br>
        </div>
        <div class="textbox">
        Password
        <input type="password" name="Password" Placeholder="your password here" onclick="checkInput()" id="Password" maxlength=128 required><br>
        </div>

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
