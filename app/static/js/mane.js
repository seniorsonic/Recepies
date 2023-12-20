var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 1220,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>";
        },
    },
});
async function addNewRecipes(first, second) {
    const slider = document.querySelector(".swiper-wrapper");
    const countRecipes = second;

    for (let index = 0; index < countRecipes; index = index + 7) {
        const newT = document.createElement("div");
        newT.classList.add("swiper-slide");
        slider.appendChild(newT);
    }

    const slidersCount = document.querySelectorAll(".swiper-slide");
    for (let recipeId = first; recipeId <= second; recipeId++) {
        try {
            const response = await fetch('/get_recipe_data/' + recipeId);
            const data = await response.text();
            displayRecipe(data, recipeId, slidersCount);
        } catch (error) {
            console.error('Error:', error);
        }
    }
    swiper.update();
    swiper.pagination.update();
    swiper.pagination.render();
    swiper.slideTo(0);
}
function displayRecipe(recipeText, currentRecipe, slider) {
    let currentSlider = slider[Math.ceil(currentRecipe/7)-1];
    const newD = document.createElement("div");
    newD.classList.add("swiper-slide-text");
    newD.textContent = recipeText;
    currentSlider.appendChild(newD);
}

async function fetchLastRecipeData() {
    try {
        const response = await fetch('/get_last_recipe_data');
        const data = await response.text();
        addNewRecipes(1, data);
    } catch (error) {
        console.error('Error:', error);
    }
}

fetchLastRecipeData();
