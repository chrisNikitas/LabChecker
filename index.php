<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Labchecker</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="labStyle.css">
	</head>

<body>
	<nav class="navbar navbar-light bg-dark-transparent">
		<a class="navbar-brand" id="titleLab" href="#">Lab<span id="titleChecker">Checker<sup>Teacher</sup></a>
		<span>
			<a class="btn btn-light btn-lg " role="button" href="logout.php"><i class="fas fa-sign-out-alt">SignOut</i></a>
		</span>
	</nav>
	<div class="container-fluid bg-green-transparent">
		<div class="row">
			<div class="col-md-4 col-lg-3 border-right pt-2" id="list">
				<form id="list_form" method="POST">
					<input type="hidden" id="hidden_selected_lab" name="hidden_selected_lab" value="LF31">
					<input type="submit" name="test_submit_button" value="test_submit_button" id="test_submit_button">
				</form>
				<h3>PC Listings</h3>
				<hr>
				<ul>
					<li>PC 3 is free</li>
					<li>PC 5 is free</li>
					<li>PC 13 is free</li>
					<li>PC 25 is free</li>
					<li>PC 4 is occupied</li>
					<li>PC 6 is occupied</li>
				</ul>
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
					<img id="image" src="DrawingScripts_staffImage.png" alt="lab">
				</div>
			</div>
			</div>
		</div>
	</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="checkLab.js"></script>
<script>

	function SHOW_LF31() {
		document.getElementById('image').src="DrawingScripts_LF31_staffImage.png";
		document.getElementById("button_LF31").className = "btn btn-light w-100 active";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100";
		document.getElementById('hidden_selected_lab').value = "LF31";
	}
	function SHOW_TOOTILL0() {
		document.getElementById('image').src="otherPicture.jpg";
		document.getElementById("button_LF31").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100 active";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100";
		document.getElementById('hidden_selected_lab').value = "TOOTILL0";
	}
	function SHOW_TOOTILL1() {
		document.getElementById('image').src="DrawingScripts_Tootill1_staffImage.png";
		document.getElementById("button_LF31").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL0").className = "btn btn-light w-100";
		document.getElementById("button_TOOTILL1").className = "btn btn-light w-100 active";
		document.getElementById('hidden_selected_lab').value = "TOOTILL1";
	}


  function getData() {


		//document.forms["list_form"].submit();
		//$(document).ready(function() {
/*
		    var form = $('#list_form');

		    $('list_form').submit(function(event) {

		        var formData = {
		            'selected_lab'    : $('#hidden_selected_lab').val()
		        };

		        $.ajax({
		            type        : 'POST',
		            url         : 'checkLab.php',
		            data        : formData,
		            success     : //function(data){
		                //$('#list').html(data);
										function() {
											alert('Hello');
										}
		        })

		        event.preventDefault();

		    });
	//});

		$('list_form').trigger('submit');
*/


		//call javascript ajax for left column
		//^^need to make a made up form
		//run karam's python scripts -- if possible
    //wait
		//collect Karam's image
		//^^run karams testDecodeImage.php
	}

	var keepGettingData = setInterval(getData, 5000);
</script>
</body>
</html>
