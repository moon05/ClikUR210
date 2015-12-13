$(document).ready( function(){

	$("#fadeInFirst").fadeIn(1000);
	$("#fadeInSecond").fadeIn(5500);

	$(".clickable-row").click(function(){
		// var class_id =$.get('/class_js/'+$(this).attr('class_id'), function( data ) {
		// 	alert(JSON.stringify(data));
		// });

		window.document.location = $(this).data("href")
	})
	
	// for quiz
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

	//for question
	$("#btn_add_question").click(function(data){
		
		var quiz_id = $("h3#quiz_id").html();
		var questionText = $("#createQuestion_form>dd>input#questionText").val();
		
		$.post('/createQuestion',{'questionText':questionText,'quiz_id': quiz_id},function(data){
			alert(JSON.stringify(data));
		});
	});

	$(".btn_remove_question").click(function(data){
		
		var quiz_id = $("h3#quiz_id").html();
		var question_id = $(this).attr('question_id');

		$.post('/removeQuestion',{'question_id':question_id,'quiz_id':quiz_id},function(data){
			//alert(JSON.stringify(data));
			if (data.status == 'True'){
				$("tr#question_"+question_id).hide();
			}else{
				alert('Error trying to delete question '+ question_id);
			}
		});

	});

	//for option
	$("#btn_add_option").click(function(data){
		
		var question_id = $("h3#question_id").html();
		var option = $("#createOption_form>dd>input#option").val();
		
		$.post('/createOption',{'option':option,'question_id': question_id},function(data){
			alert(JSON.stringify(data));
		});
	});

	$(".btn_remove_option").click(function(data){
		
		var question_id = $("h3#question_id").html();
		var option_id = $(this).attr('option_id');

		$.post('/removeOption',{'option_id':option_id,'question_id':question_id},function(data){
			//alert(JSON.stringify(data));
			if (data.status == 'True'){
				$("tr#option_"+option_id).hide();
			}else{
				alert('Error trying to delete option '+ option_id);
			}
		});

	});
















	// // $("#drop").append($("#btn_add_option"))

	// //for option
	// $(".add_question").click(function(data){

	// 	var question_id = $(this).attr("question_id");
	// 	var quiz_id = $("h3#quiz_id").html();
	// 	var option = $("#createOption_form>dd>input#option").val();
		

	// 	//oops... is this where u create options or questions?
	// 	// this is where I am supposed to add question....

	// 	$.get('/options_js/'+quiz_id+'/'+question_id,function(data){
	// 		//alert(JSON.stringify(data));
		
	// 	});
	// });

	// // how do I actually add to the option

	// $(".question").click(function(data){
	// 	//toggle the td that has the add thing...
	// 	$('.add_option_td' ).toggle();
	// });


	// $("#add_option").click(function(data){
		
	// 	var question_id = $(this).attr('question_id');
	// 	var option = $("#createOption_form>dd>input#option").val();
		
		
	// 	$.post('/createOption',{'option':option,'question_id': question_id},function(data){
			
			
	// 		$("tbody#"+question_id).append("<tr><td></td><td>SHITSHOW</td></tr>");
	// 		alert(JSON.stringify(data));
	// 	});
	// });

	// $(".btn_remove_option").click(function(data){
		
	// 	var question_id = $("h3#question_id").html();
	// 	var option_id = $(this).attr('option_id');

	// 	$.post('/removeOption',{'option_id':question_id,'question_id':quiz_id},function(data){
	// 		//alert(JSON.stringify(data));
	// 		if (data.status == 'True'){
	// 			$("tr#question_"+question_id).hide();
	// 		}else{
	// 			alert('Error trying to delete quiz '+ question_id);
	// 		}
	// 	});

	// });



});