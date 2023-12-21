import psycopg2


def new_recipe(login_id, name_recipe, ingredients, txt_recipe):
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
    sql = "SELECT MAX(recipe_id) FROM recipe;"
    cur.execute(sql)
    max_recipe = cur.fetchone()
    if None in max_recipe:
        max_recipe = [0]
    sql = "INSERT INTO recipe (recipe_id, login_id, name_recipe, ingredients, txt_recipe) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(sql, (max_recipe[0] + 1, login_id, name_recipe, ingredients, txt_recipe))
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()


# for i in range(40):
#     new_recipe(1, 'ARBUZ', 'arbuz, voda, kostochki', 'Приятного аппетита')
