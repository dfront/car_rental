$(document).ready(function(){
   
    /* Form Login */
    $("#form_login").submit(function(event){
	
	event.preventDefault();	
	var username = $("#id_username").val(); 
	var password = $("#id_password").val();
	login(username,password);

    })
})

/* Login  */
function login(username,password){

    $.ajax({
	url: "/api/auth/",
	method: "POST",
	dataType: "json",
	beforeSend: function(xhr) {
	    xhr.setRequestHeader("Authorization", "Basic " + btoa(username+":"+password));
	}
    }).done(function(data) {
	window.location.href="/";
    }).fail(function(xhr, textStatus, errorThrown){
	alert(xhr.responseJSON.detail);
    });

}


