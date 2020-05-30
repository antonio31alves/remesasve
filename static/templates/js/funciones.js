

function  emitir_mensaje_datosuser(icono, titulo, mensaje){
	Swal.fire({icon: icono, title: titulo, text: mensaje}).then(function(){
		if(window.location.pathname != '/dashboard/profile/'){ 
    		window.location = "profile/";
		}
	});	
}

function  emitir_mensaje(icono, titulo, mensaje){
	Swal.fire({icon: icono, title: titulo, text: mensaje})
}


function active_option_menu(value){
	/*ACTIVAR OPCION NOSOTROS*/
	if (value == 1){
		$("#inicio").removeClass("active");
	    $("#nosotros").addClass("active");
	    $("#preguntas_frecuentes").removeClass("active");
	    $("#tipo_cambio").removeClass("active");
	}
	/*ACTIVAR OPCION PREGUNTAS FRECUENTES*/
	if (value == 2){
		$("#inicio").removeClass("active");
	    $("#nosotros").removeClass("active");
	    $("#preguntas_frecuentes").addClass("active");
	    $("#tipo_cambio").removeClass("active");
	}
	/*ACTIVAR OPCION TIPO DE CAMBIO*/
	if (value == 3){
		$("#inicio").removeClass("active");
	    $("#nosotros").removeClass("active");
	    $("#preguntas_frecuentes").removeClass("active");
	    $("#tipo_cambio").addClass("active");
	}
}