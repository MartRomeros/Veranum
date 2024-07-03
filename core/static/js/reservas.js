console.log("funcionando");
var campos = document.querySelectorAll(".campo");
var form = document.querySelector("main > section > form");

form.addEventListener("submit",(evento)=>{
    for (let i=0;i<campos.length; i++){
        //validar campos vacios:
        if(campos[i].value == ""){
            campos[i].style.border = "red solid 1px";
            evento.preventDefault();
        }else{
            campos[i].style.border = "lightgrey solid 1px";
        }
        //validar numero de telefono:
        let fono = document.querySelector("#fono");
        if (fono.value.length < 9){
            fono.style.border = "solid 1px yellow"; 
            evento.preventDefault();
        }
        //validar fechas:
        let fechaActual = Date.now();
        let fechaIni = document.querySelector("#fec-ini");
        let fechaTer = document.querySelector("#fec-ter");
        alert(typeof fechaIni.value);
        evento.preventDefault();
        //validar fecha inicio:
        
    }
});

