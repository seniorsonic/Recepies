function Add {
    const nameValue = document.getElementById('name-recipe').value;
    const ingredientsValue = document.getElementById('ingredients').value;
    const recipeValue = document.getElementById('recipe').value;
    validateField(nameValue, 'nameError');
    validateField(ingredientsValue, 'ingredientsError');
    validateField(recipeValue, 'recipeError');
    if (nameValue && ingredientsValue && recipeValue) {
        // Создаем объект для данных
        const data = {
          name: nameValue,
          ingredients: ingredientsValue,
          txt_recipe: recipeValue
        };

        // Отправляем POST-запрос на сервер Flask
        fetch('/new_recipe.html', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Вы успешно добавили рецепт");
                    window.location.href = '/';
                } else {
                    alert("Ошибка при вводе рецепта: " + data.error);
                }
            })
                .catch((error) => {
                alert("Произошла ошибка при отправке запроса");
                });
    }
}

function validateField(value, errorId) {
    const errorElement = document.getElementById(errorId);
    if (!value) {
        errorElement.textContent = "Это поле обязательно для заполнения";
    } else {
        errorElement.textContent = "";
    }
}

const btn = document.querySelector(".btn-1");
btn.addEventListener("click", Add);
