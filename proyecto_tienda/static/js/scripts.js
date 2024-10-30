document.addEventListener("DOMContentLoaded", function(){
    var navlink = document.querySelectorAll('nav a');

    navlink.forEach(function(link){
        link.addEventListener("mouseover", function(){
            link.style.backgroundColor = "#ffe4c4";
        });
        link.addEventListener("mouseout", function(){
            link.style.backgroundColor = "";
        });
    });
});