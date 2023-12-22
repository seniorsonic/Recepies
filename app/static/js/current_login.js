let name_user = document.getElementById("user-data").getAttribute("data-name");
let user = document.getElementById("user-data");
let quit = document.querySelector(".quit");
user.textContent = name_user;

let btns = document.querySelectorAll(".navigation__login");

if (user.textContent != "") {
    if (btns.length == 3) {
        btns[0].classList.add("disable");
        btns[1].classList.add("disable");
        btns[2].classList.remove("disableRecipe");
        quit.classList.remove("disable")
        user.classList.remove("disable")
    }
    else if (btns.length == 0) {
        quit.classList.remove("disable")
        user.classList.remove("disable")
    }
}

quit.addEventListener("click",()=>
{
    if (btns.length == 3) {
        btns[0].classList.remove("disable");
        btns[1].classList.remove("disable");
        btns[2].classList.add("disableRecipe");
        quit.classList.add("disableRecipe");
        user.classList.add("disable")
    }
    else if (btns.length == 0) {
        quit.classList.add("disableRecipe");
        user.classList.add("disable")
    }
    fetch('/quit.html', {
                method: 'POST'
                })
})