from app.SQL.Models import Recipe
from sqlalchemy.sql.expression import func


def one_recipe_name(recipe_id):
    recipe = Recipe.query.with_entities(Recipe.name_recipe).filter(Recipe.recipe_id == recipe_id).first()
    return recipe


def last_recipe():
    end_recipe = Recipe.query.with_entities(func.max(Recipe.recipe_id)).first()
    return str(end_recipe[0])
