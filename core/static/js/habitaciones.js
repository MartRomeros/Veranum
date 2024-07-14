var btnDetalles = document.querySelectorAll("#detalles");
var modalBody = document.querySelector(".modal-body");
var btnNoReservar = document.querySelectorAll("#no-cupos");
var btnReservar = document.querySelectorAll("#reservar");
var form = document.querySelector(".form-reservar");
var campos = document.querySelectorAll(".form-campo");

btnDetalles.forEach(function (btn, index) {
    btn.addEventListener("click", (evento) => {
        let tipoHabitacion = btn.getAttribute("data-tipo");
        let banios = btn.getAttribute("data-banios");
        let cupo = btn.getAttribute("data-capacidad");
        let unidades = btn.getAttribute("data-cupos");
        let hotel = btn.getAttribute("data-hotel");

        let cuerpo = `<h5>Tipo de habitacion: Habitacion: ${tipoHabitacion}</h5>
        <h5>Cantidad de Baños: ${banios}</h5>
        <h5>Capacidad de Personas: ${cupo} Personas</h5>
        <h5>Habitaciones Disponibles: ${unidades} Habitaciones</h5>
        <h5>Hotel en donde se encuentra: ${hotel}</h5>
        `;
        modalBody.innerHTML = cuerpo;
    });
});

btnNoReservar.forEach(function(btn,index){
    btn.addEventListener("click",(evento)=>{
        alert("No quedan habitaciones disponibles")
    });
});


btnReservar.forEach(function(btn,index){

    btn.addEventListener("click",(evento)=>{

        let nameRoom = btn.getAttribute("data-name");
        document.querySelector("#room-name").innerText = nameRoom;
        document.querySelector("#valor-name").value = nameRoom;

    });
});


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


window.addEventListener("load",()=>{
    let tieneReserva = document.querySelector("tiene-reservas").innerText;
    if(tieneReserva == "vigente"){
        alert("Tienes una reserva en vigencia!")
    }
});




