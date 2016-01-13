$(document).ready(function(){

    $('#datetimepicker_initialDate').datetimepicker({format: 'YYYY-MM-DDThh:mm',});
    $('#datetimepicker_endDate').datetimepicker({format: 'YYYY-MM-DDThh:mm',});
    $('#my_rents').DataTable();

    myRents();   
    $("#logout").click(function(){logout()});


    /* Load Vehicles */
    $.ajax({
      url: "/vehicles/",
      context: document.body
    }).done(function(data) {
	var vehicle_input;
	for(var i in data){
	    vehicle_input =$('<input type="radio" name="vehicle" id="vehicle_id_'+data[i].pk+'" value="'+data[i].pk+'"/> <label for="vehicle_id_'+data[i].pk+'">' + data[i].model  + '</label> <br/>');
	    $("#vehicles").append(vehicle_input)
	}
    });


    /* Make Rent */
    $( "#rent_form" ).submit(function( event ){
	event.preventDefault();

	var data = {}
	data['client'] = $("#client").val(); //eca
	data['initialDate'] = $("#id_initialDate").val();
	data['endDate'] = $("#id_endDate").val();
	data['vehicle'] = $('input[name=vehicle]:checked', '#rent_form').val()

	if(data){
	    $.ajax({
		url: "makeRent/",
		method: "POST",
		data: JSON.stringify(data),
		contentType: "application/json;", 
		dataType: "json",
		context: document.body,
		beforeSend: function(xhr) {
		    xhr.setRequestHeader("Authorization", "Token " + $("#token").val());
		}
	    }).done(function(data) {
		 myRents();
	    }).fail(function(xhr, textStatus, errorThrown){
		alert(xhr.responseJSON.vehicle)
	    });
	}
    }) 
});


/* List my Rents */
function myRents(){  
    $("#my_rents tbody").html("");
    $.ajax({
	url: "/rents/",
	context: document.body
    }).done(function(data) {
	$("#my_rents tbody").html("");
	var my_rents;	
	var row;
	for(var i in data){
	    row = ""
	    row = $('<tr><td>'+data[i].vehicle_str+'</td><td>'+data[i].initialDate+'</td><td>'+data[i].endDate+'</td><td>'+data[i].kmRound+'</td></tr>')
	    $("#my_rents tbody").append(row)
	}
    })
}



/* Logout */
function logout(){    
    $.ajax({
	url: "/api/auth/",
	type: "DELETE",
	dataType:"json",
	beforeSend: function(xhr) {
	    xhr.setRequestHeader("X-CSRFToken", Cookies('csrftoken'));
	},
	xhrFields: {
	    withCredentials: true
	}
    }).done(function(data) {
	window.location.href="";
    }).fail(function(xhr, textStatus, errorThrown){
	alert(xhr.responseJSON.detail);
    });
}

