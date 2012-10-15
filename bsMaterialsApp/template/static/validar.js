
function validarEntero(valor){ 
     valor = parseInt(valor)  
     	if (isNaN(valor)) { 
           	 return false
     	}else{ 
           	 if (valor>0){
           	    return true
           	 }
            return false
     	} 
}


function vacio(q) {  
    if (q.length != 0){
        for ( i = 0; i < q.length; i++ ) {  
                if ( q.charAt(i) == " "  ) {  
                        return true  
                }  
        }  
        return false  }
    else
        return true
}

function valida(F) {
        if (vacio(F.nombre.value) == true) {  
                    alert("El campo nombre de producto no puede contener espacios vacios, ni ser vacio")
                    return false  
        }
        
        if (validarEntero(F.stock.value) == false) { 
                    alert("El campo stock deber ser un NUMERO mayor a 0")
                    return false  
        }    
        return true     
}    