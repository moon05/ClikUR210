$(document).ready( function(){

	$("#fadeInFirst").fadeIn(1000);
	$("#fadeInSecond").fadeIn(5500);

	$(".clickable-row").click(function(){
		// var class_id =$.get('/class_js/'+$(this).attr('class_id'), function( data ) {
		// 	alert(JSON.stringify(data));
		// });

		window.document.location = $(this).data("href")
	})
	
	$("#btn_add_quiz").click(function(data){
		
		var class_id = $("h3#class_id").html();
		var quizName = $("#createQuiz_form>dd>input#quizName").val();
		
		$.post('/createQuiz',{'quizName':quizName,'class_id': class_id},function(data){
			alert(JSON.stringify(data));
		});
	});

	$(".btn_remove_quiz").click(function(data){
		
		var class_id = $("h3#class_id").html();
		var quiz_id = $(this).attr('quiz_id');

		$.post('/removeQuiz',{'quiz_id':quiz_id,'class_id':class_id},function(data){
			//alert(JSON.stringify(data));
			if (data.status == 'True'){
				$("tr#quiz_"+quiz_id).hide();
			}else{
				alert('Error trying to delete quiz '+ quiz_id);
			}
		});

	});

});