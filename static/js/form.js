$(document).ready(function() {

	$('form').on('submit', function(event) {
	    //Loading animation code
		$.ajax({
			data : {
				question1 : $('#searchBox1').val(),
				question2 : $('#searchBox2').val()
			},
			type : 'POST',
			url : '/process',
			beforeSend:function(){
				$("#loading").show();
				$('#freepik_stories-web-search').hide();
				$('#status_reply').hide();
				$("#processing").show();
				$("#mytext").hide();


			},
			complete:function() {
				$("#loading").hide();
				$('#status_reply').show();
				$("#processing").hide();



			}
		})
		.done(function(data) {

			if (data.percentage) {
			if(data.percentage < 50){
							$('#mytext').css({'color':'#DB2721'});
			}
			else{
			    $('#mytext').css({'color':'#4ceaac'})
			}
				$('#mytext').text((data.percentage).toString()+'%').show();
				$('#freepik_stories-web-search').hide();
				$('#status_reply').html(data.reply);
			}
			else {
				$('#mytext').text(data.error).hide();
				$('#freepik_stories-web-search').show();
			}

		});


		event.preventDefault();

	});

	$('form').on('reset',function(event){

	    $('#mytext').text('').hide();
	    $('#freepik_stories-web-search').show();
	    $('#status_reply').html('Check the statements<br>in your mind are <strong>same or not</strong>');

//    event.preventDefault();
	});

});