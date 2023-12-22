function log() {
    const emailValue = document.getElementById('emailInput').value;
    const passwordValue = document.getElementById('passwordInput').value;
    validateField(emailValue, 'emailError');
    validateField(passwordValue, 'passwordError');
    if (emailValue) {
        validateEmail(emailValue, 'emailError');
    }
    if (emailValue && passwordValue) {
        // Создаем объект для данных
        const data = {
          email: emailValue,
          password: passwordValue
        };

        // Отправляем POST-запрос на сервер Flask
        fetch('/login.html', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
//                    alert("Вы зашли");
                    window.location.href = '/';
                } else {
                    alert("Ошибка при входе: " + data.error);
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
