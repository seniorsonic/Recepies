function display(recipe) {
    const nameElement = document.getElementById('name-data');
    const ingredientsElement = document.getElementById('ingredients-data');
    const recipeElement = document.getElementById('recipe-data');
    const avtorElement = document.getElementById('avtor-data');

    nameElement.innerHTML = recipe.name_recipe;
    ingredientsElement.innerHTML = recipe.ingredients;
    recipeElement.innerHTML = recipe.txt_recipe;
    avtorElement.innerHTML = recipe.login_id;
}

fetch('/current_recipe.html', {
    method: 'POST'
})
    .then(response => response.json())
    .then(data => {
        display(data);
    })
display()