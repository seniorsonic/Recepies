# прописать что юзер логин на данный момент = 0 и тогда попробовать добавить рецепт
import app.show_class
from app.show_class import CurrentLogin
from app.SQL.new_recipe_sql import new_recipe


app.show_class.CurrentLogin.id_user = 0


