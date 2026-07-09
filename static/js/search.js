const searchBox = document.getElementById("searchBox");

searchBox.addEventListener("keyup", function () {

    let value = searchBox.value.toLowerCase();

    let cards = document.querySelectorAll(".card");

    cards.forEach(function(card){

        let food = card.querySelector("h3").innerText.toLowerCase();

        if(food.includes(value)){

            card.style.display="block";

        }

        else{

            card.style.display="none";

        }

    });

});