<!DOCTYPE html>
<?php
$user_display = "Error identifying user";

session_start();
if (isset($_SESSION['loggedIn'])) {
	if ($_SESSION['teacherBool']) {
		$user_display = "Teacher";
	}
	else {
		$user_display = "Student";
	}
}
else {
	header("Location: logout.php");
}

?>


<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Labchecker</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="labStyle.css">
	</head>

<body onload="getData()">

	<nav class="navbar navbar-light bg-dark-transparent">
		<a class="navbar-brand" id="titleLab" href="#">Lab<span id="titleChecker">Checker<sup><?php echo "$user_display"; ?></sup></a>
		<span>
			<a class="btn btn-light btn-lg " role="button" href="logout.php"><i class="fas fa-sign-out-alt">SignOut</i></a>
		</span>
	</nav>
	<div class="container-fluid bg-green-transparent">
		<div class="row">
			<div class="col-md-4 col-lg-3 border-right py-2" id="list">
				<form id="list_form" method="POST">
					<input type="hidden" id="hidden_selected_lab" name="hidden_selected_lab" value="LF31">
				</form>
				<h3>PC Listings</h3>
				<hr>
				<div id="return_pc_data_outer">
					<div class="return_pc_data" id="return_pc_data">
          <!-- Holds data returned from checkLab.php -->
					Loading data from lab...
				  </div>
			  </div>
			</div>
			<div class = "col-md-8 col-lg-9">
				<div class="row">
					<div class="col-md-12 bg-dark-transparent p-0">
						<nav class="nav navbar rounded-bottom">
							<div class="btn-group d-flex w-100 ">
								<button type="button" id="button_LF31" class="btn btn-light w-100 active" onclick="SHOW_LF31()">LF31</button>
								<button type="button" id="button_TOOTILL0" class="btn btn-light w-100" onclick="SHOW_TOOTILL0()">TOOTILL0</button>
								<button type="button" id="button_TOOTILL1" class="btn btn-light w-100" onclick="SHOW_TOOTILL1()">TOOTILL1</button>
							</div>
						</nav>
					</div>
				</div>
			<div class="row">
				<div class="col-md-12 d-flex justify-content-center align-items-start" id="lab"  >
					<img id="image" src="GreyLF31.png" alt="lab">
				</div>
			</div>
			</div>
		</div>
	</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="checkLab.js?2"></script>
<script>

	function SHOW_LF31() {
		document.getElementById("button_LF31").className = "btn btn-light w-100 active";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100";
		document.getElementById('hidden_selected_lab').value = "LF31";
		document.getElementById('image').src="GreyLF31.png";
		document.getElementById('return_pc_data').innerHTML = "Loading data from lab...";
	}
	function SHOW_TOOTILL0() {
		document.getElementById("button_LF31").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100 active";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100";
		document.getElementById('hidden_selected_lab').value = "TOOTILL0";
		document.getElementById('image').src="GreyTootill0.png";
		document.getElementById('return_pc_data').innerHTML = "Loading data from lab...";
	}
	function SHOW_TOOTILL1() {
		document.getElementById("button_LF31").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100 active";
		document.getElementById('hidden_selected_lab').value = "TOOTILL1";
		document.getElementById('image').src="GreyTootill1.png";
		document.getElementById('return_pc_data').innerHTML = "Loading data from lab...";
	}


  function getData() {
		$('#list_form').trigger("submit");
	}

  var oldLab = 'LF31';
	var keepGettingData = setInterval(getData, 5000);
</script>
</body>
</html>
