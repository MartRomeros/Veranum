console.log("funcionando");

var btnDetalles = document.querySelectorAll("#detalles");
var modalBody = document.querySelector(".modal-body");

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
        <h5>Hoteles en donde se encuentra: ${hotel}</h5>
        `;



        modalBody.innerHTML = cuerpo;
    });
});

