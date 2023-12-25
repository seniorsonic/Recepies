from app.SQL.Models import Recipe, Login


def choise_recipe(recipe_id):
    recipe = Recipe.query.with_entities(Recipe.login_id, Recipe.name_recipe, Recipe.ingredients,
                              Recipe.txt_recipe).filter(Recipe.recipe_id == recipe_id).first()
    login = Recipe.query.with_entities(Login.firstname).filter(Login.login_id == recipe.login_id).first()
    recipe = [login.firstname, recipe.name_recipe, recipe.ingredients, recipe.txt_recipe]
    return recipe
