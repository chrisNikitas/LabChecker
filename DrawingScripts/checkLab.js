$(document).ready(function() {

    var form = $('#list_form');

    $('#list_form').submit(function(event) {

        var formData = {
            'selected_lab'    : $('#hidden_selected_lab').val()
        };

        $.ajax({
            type        : 'POST',
            url         : 'checkLab.php',
            data        : formData,
            success     : function(data){
                $('.return_pc_data').html(data);
              }
        })

        event.preventDefault();

    });
});
