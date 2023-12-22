function log() {
    const nameValue = document.getElementById('nameInput').value;
    const surnameValue = document.getElementById('surnameInput').value;
    const passwordValue = document.getElementById('passwordInput').value;
    const emailValue = document.getElementById('emailInput').value;
    validateField(nameValue, 'nameError');
    validateField(surnameValue, 'surnameError');
    validateField(passwordValue, 'passwordError');
    validateField(emailValue, 'emailError');
    if (emailValue) {
        validateEmail(emailValue, 'emailError');
    }
    if (nameValue && surnameValue && passwordValue && emailValue) {
        // Создаем объект для данных
        const data = {
          name: nameValue,
          surname: surnameValue,
          password: passwordValue,
          email: emailValue
        };

        // Отправляем POST-запрос на сервер Flask
        fetch('/register.html', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
//                    alert("Вы успешно зарегистрировались");
                    window.location.href = '/';
                } else {
                    alert("Ошибка при регистрации: " + data.error);
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
function validateEmail(value, errorId) {
    const errorElement = document.getElementById(errorId);
    if (value.includes('@')) {
        errorElement.textContent = "";
    } else {
        errorElement.textContent = "Введите настоящую почту";
    }
}

const btn = document.querySelector(".btn");
btn.addEventListener("click", log);
