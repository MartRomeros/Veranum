console.log("funcionando");
var campos = document.querySelectorAll(".campo");
var form = document.querySelector("main > section > form");

form.addEventListener("submit",(evento)=>{
    for (let i=0;i<campos.length; i++){
        //validar campos vacios:
        if(campos[i].value == ""){

            campos[i].style.border = "red solid 1px";
            alert(`Un campo debe de estar vacio (${campos[i].id})`);
            evento.preventDefault();
            return;

        }else{
            campos[i].style.border = "lightgrey solid 1px";
        }

        //validar numero de telefono:
        let fono = document.querySelector("#fono");

        if (fono.value.length < 9 || fono.value.length > 9){
            alert("El telefono esta incorrecto! (verifica que deben de ser 9 digitos)!");
            fono.style.border = "solid 1px yellow";
            evento.preventDefault();
            return;
        }

        //validar fechas:
        let fechaActual = new Date();
        let fechaIni = document.querySelector("#fec-ini").value;
        let fechaTer = document.querySelector("#fec-ter").value;

        fechaIni = new Date(fechaIni);
        fechaTer = new Date(fechaTer);

        if (fechaIni < fechaActual){
            alert("fecha de inicio menor a la actual!");
            evento.preventDefault();
            return;
        }

        if (fechaTer < fechaIni){
            alert("La fecha de termino de la reserva debe ser mayor a la fecha de inicio!");
            evento.preventDefault();
            return;
        }
    }
    alert("Reserva Confirmada!");
});

