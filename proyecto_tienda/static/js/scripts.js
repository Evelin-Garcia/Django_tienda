document.addEventListener("DOMContentLoaded", function(){
    var navlink = document.querySelectorAll('nav a');

    //cambiar color de fondo de los links
    navlink.forEach(function(link){
        link.addEventListener("mouseover", function(){
            link.style.backgroundColor = "#ffe4c4";
        });
        link.addEventListener("mouseout", function(){
            link.style.backgroundColor = "";
        });
    });
    //para hacer efecto en boton de html
    const showAlertButton = document.getElementById('show-alert');
    if (showAlertButton){
    showAlertButton.addEventListener("click", function(){
        alert('Felicitaciones! Desbloqueaste un cupon de descuento!');
        });
    }
});

