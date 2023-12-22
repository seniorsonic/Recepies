const langRu=document.querySelector(".langRu");
const langEng=document.querySelector(".langEng");

const lang1=document.getElementById("lang1")
const lang2=document.getElementById("lang2")
const lang3=document.getElementById("lang3")
const lang4=document.getElementById("lang4")
const lang5=document.getElementById("lang5")

const lang6=document.getElementById("lang6")
const lang7=document.getElementById("lang7")
const lang8=document.getElementById("lang8")

const lang9=document.getElementById("lang9")
const lang10=document.getElementById("lang10")
const lang11=document.getElementById("lang11")
const lang12=document.getElementById("lang12")
const lang13=document.getElementById("lang13")

const lang14=document.getElementById("lang14")
const lang15=document.getElementById("lang15")
const lang16=document.getElementById("lang16")
const lang17=document.getElementById("lang17")

const lang18=document.getElementById("lang18")
const lang19=document.getElementById("lang19")
const lang20=document.getElementById("lang20")
const lang21=document.getElementById("lang21")

const lang22=document.getElementById("lang22")
fetch('/RuorEng_current.html', {
    method: 'POST'
})
    .then(response => response.json())
    .then(data => {
        if (data.switcher == 1) {
            langRu.classList.remove("activeLang")
            langEng.classList.add("activeLang")
            if (lang1 != null) lang1.textContent="Recipes"
            if (lang2 != null) lang2.textContent="Authorization"
            if (lang3 != null) lang3.textContent="Register"
            if (lang4 != null) lang4.textContent="Add a recipe"
            if (lang5 != null) lang5.textContent="Go out"
            if (lang6 != null) lang6.textContent="Enter your email:"
            if (lang7 != null) lang7.textContent="Enter password:"
            if (lang8 != null) lang8.textContent="Send"
            if (lang9 != null) lang9.textContent="Enter your name:"
            if (lang10 != null) lang10.textContent="Enter your family:"
            if (lang11 != null) lang11.textContent="Enter password:"
            if (lang12 != null) lang12.textContent="Enter your email:"
            if (lang13 != null) lang13.textContent="Send"
            if (lang14 != null) lang14.textContent="Recipe name:"
            if (lang15 != null) lang15.textContent="Ingredients:"
            if (lang16 != null) lang16.textContent="Recipe:"
            if (lang17 != null) lang17.textContent="Author:"
            if (lang18 != null) lang18.textContent="Enter recipe name:"
            if (lang19 != null) lang19.textContent="Enter ingredients:"
            if (lang20 != null) lang20.textContent="Enter recipe:"
            if (lang21 != null) lang21.textContent="Send"
            if (lang22 != null) lang22.textContent="Error 404."
        }
    });



langRu.addEventListener("click", ()=>{
    langRu.classList.add("activeLang")
    langEng.classList.remove("activeLang")
    fetch('/RuorEng.html', {
        method: 'POST'
    })
    if (lang1 != null) lang1.textContent="Рецепты"
    if (lang2 != null) lang2.textContent="Авторизация"
    if (lang3 != null) lang3.textContent="Зарегистрироваться"
    if (lang4 != null) lang4.textContent="Добавить рецепт"
    if (lang5 != null) lang5.textContent="Выйти"
    if (lang6 != null) lang6.textContent="Введите вашу почту:"
    if (lang7 != null) lang7.textContent="Введите пароль:"
    if (lang8 != null) lang8.textContent="Отправить"
    if (lang9 != null) lang9.textContent="Введите ваше имя:"
    if (lang10 != null) lang10.textContent="Введите вашу фамилию:"
    if (lang11 != null) lang11.textContent="Введите пароль:"
    if (lang12 != null) lang12.textContent="Введите вашу почту:"
    if (lang13 != null) lang13.textContent="Отправить"
    if (lang14 != null) lang14.textContent="Название рецепта:"
    if (lang15 != null) lang15.textContent="Ингредиенты:"
    if (lang16 != null) lang16.textContent="Рецепт:"
    if (lang17 != null) lang17.textContent="Автор:"
    if (lang18 != null) lang18.textContent="Введите название рецепта:"
    if (lang19 != null) lang19.textContent="Введите ингредиенты:"
    if (lang20 != null) lang20.textContent="Введите рецепт:"
    if (lang21 != null) lang21.textContent="Отправить"
    if (lang22 != null) lang22.textContent="Ошибка 404."
})

langEng.addEventListener("click", ()=>{
    langRu.classList.remove("activeLang")
    langEng.classList.add("activeLang")
    fetch('/RuorEng.html', {
        method: 'POST'
    })
    if (lang1 != null) lang1.textContent="Recipes"
    if (lang2 != null) lang2.textContent="Authorization"
    if (lang3 != null) lang3.textContent="Register"
    if (lang4 != null) lang4.textContent="Add a recipe"
    if (lang5 != null) lang5.textContent="Go out"
    if (lang6 != null) lang6.textContent="Enter your email:"
    if (lang7 != null) lang7.textContent="Enter password:"
    if (lang8 != null) lang8.textContent="Send"
    if (lang9 != null) lang9.textContent="Enter your name:"
    if (lang10 != null) lang10.textContent="Enter your family:"
    if (lang11 != null) lang11.textContent="Enter password:"
    if (lang12 != null) lang12.textContent="Enter your email:"
    if (lang13 != null) lang13.textContent="Send"
    if (lang14 != null) lang14.textContent="Recipe name:"
    if (lang15 != null) lang15.textContent="Ingredients:"
    if (lang16 != null) lang16.textContent="Recipe:"
    if (lang17 != null) lang17.textContent="Author:"
    if (lang18 != null) lang18.textContent="Enter recipe name:"
    if (lang19 != null) lang19.textContent="Enter ingredients:"
    if (lang20 != null) lang20.textContent="Enter recipe:"
    if (lang21 != null) lang21.textContent="Send"
    if (lang22 != null) lang22.textContent="Error 404."
})
