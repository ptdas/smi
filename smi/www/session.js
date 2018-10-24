$(document).ready(function() {
	$.ajax({
		    type: 'GET',
		    url: '/api/method/smi.api.me',
		    dataType: "json",
		    success: function(output, status, xhr) {
		    	$('#name').html("Hi, you're login as " + output.message)
		    },
		    error: function(output, status, xhr) {
		    	
		    }
		});
})