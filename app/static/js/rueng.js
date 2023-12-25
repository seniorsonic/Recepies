function switchLanguage(language) {
    const langTexts = texts[language];
    for (const key in langTexts) {
        if (langTexts.hasOwnProperty(key)) {
            const element = document.getElementById(key);
            if (element) {
                element.textContent = langTexts[key];
            }
        }
    }
}

function main(lang) {
    const langRu = document.querySelector(".langRu");
    const langEng = document.querySelector(".langEng");

    langRu.addEventListener("click", () => {
        langRu.classList.add("activeLang");
        langEng.classList.remove("activeLang");
        switchLanguage("ru");
        fetch('/RuorEng.html', { method: 'POST' });
    });

    langEng.addEventListener("click", () => {
        langRu.classList.remove("activeLang");
        langEng.classList.add("activeLang");
        switchLanguage("en");
        fetch('/RuorEng.html', { method: 'POST' });
    });
    if (lang == "en") {
        langRu.classList.remove("activeLang");
        langEng.classList.add("activeLang");
        switchLanguage(lang);
    }
}

fetch('/RuorEng_current.html', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        main(data.switcher);
    });

const texts = {
    ru: {
        lang1: "Рецепты",
        lang2: "Авторизация",
        lang3: "Зарегистрироваться",
        lang4: "Добавить рецепт",
        lang5: "Выйти",
        lang6: "Введите вашу почту:",
        lang7: "Введите пароль:",
        lang8: "Отправить",
        lang9: "Введите ваше имя:",
        lang10: "Введите вашу фамилию:",
        lang11: "Введите пароль:",
        lang12: "Введите вашу почту:",
        lang13: "Отправить",
        lang14: "Название рецепта:",
        lang15: "Ингредиенты:",
        lang16: "Рецепт:",
        lang17: "Автор:",
        lang18: "Введите название рецепта:",
        lang19: "Введите ингредиенты:",
        lang20: "Введите рецепт:",
        lang21: "Отправить",
        lang22: "Ошибка 404."
    },
    en: {
        lang1: "Recipes",
        lang2: "Authorization",
        lang3: "Register",
        lang4: "Add a recipe",
        lang5: "Go out",
        lang6: "Enter your email:",
        lang7: "Enter password:",
        lang8: "Send",
        lang9: "Enter your name:",
        lang10: "Enter your family:",
        lang11: "Enter password:",
        lang12: "Enter your email:",
        lang13: "Send",
        lang14: "Recipe name:",
        lang15: "Ingredients:",
        lang16: "Recipe:",
        lang17: "Author:",
        lang18: "Enter recipe name:",
        lang19: "Enter ingredients:",
        lang20: "Enter recipe:",
        lang21: "Send",
        lang22: "Error 404."
    }
};