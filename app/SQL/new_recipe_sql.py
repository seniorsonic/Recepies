from sqlalchemy.sql.expression import func
from app.SQL.Models import Recipe
from app import db


def new_recipe(login_id, name_recipe, ingredients, txt_recipe):
    if login_id == 0:
        return False
    max_recipe = Recipe.query.with_entities(func.max(Recipe.recipe_id)).first()
    if None in max_recipe:
        max_recipe = [0]
    newAd = Recipe(recipe_id=max_recipe[0]+1, login_id=login_id, name_recipe=name_recipe,
                   ingredients=ingredients, txt_recipe=txt_recipe)
    db.session.add(newAd)
    db.session.commit()
    return True
