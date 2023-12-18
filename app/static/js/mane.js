var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 5250,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>";
        },
    },
});
const slider = document.querySelector(".swiper-wrapper");
const countRecipes = document.querySelectorAll(".swiper-slide-text");
const countSliders = document.querySelectorAll(".swiper-slide");
if (countRecipes.length > 7 * countSliders.length) {
    const newT = document.createElement("div");
    newT.classList.add("swiper-slide");
    slider.appendChild(newT);
}

const currentSlider = countSliders[countSliders.length - 1]; // Доступ к последнему слайдеру


// был бы я не дауном который в три часа ночи пишет знал бы куда засунуть, это типо один рецепт должно выводить пройто айди от 1 пиши
const recipeId = /* ваш способ получения идентификатора рецепта */;

fetch(`/get_recipe_data/${recipeId}`)
    .then(response => response.text())
    .catch(error => console.error('Error:', error));