$(document).ready(function() {
	$('#login-button').click(function() {
		var email = $('#email').val()
		var password = $('#password').val()
		$.ajax({
		    type: 'POST',
		    url: '/api/method/login',
		    data: {
		    	usr:email,
		    	pwd:password
		    },
		    dataType: "json",
		    success: function(output, status, xhr) {
		        alert(xhr.getResponseHeader("MyCookie"));
		    },
		    error: function(output, status, xhr) {
		    	if (output.statusText == 'UNAUTHORIZED') {
		    		alert('Invalid email / password')
		    	}
		    }
		});
	})
})