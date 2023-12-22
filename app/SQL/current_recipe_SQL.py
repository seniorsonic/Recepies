import psycopg2


def choise_recipe(recipe_id):
    # Подключение к базе данных
    conn = psycopg2.connect(
        database="Recepies",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    # Создание объекта курсора
    cur = conn.cursor()
    sql = "SELECT login_id, name_recipe, ingredients, txt_recipe FROM recipe where recipe_id = %s;"
    cur.execute(sql, (recipe_id,))
    recipe = cur.fetchone()
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    return recipe
