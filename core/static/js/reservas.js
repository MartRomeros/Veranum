console.log("funcionando");

var main = document.querySelector("main");

window.addEventListener("load",()=>{
    if(main.clientHeight < 518){
        main.style.marginBottom = "20vh";
    }
});