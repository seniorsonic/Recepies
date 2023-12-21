import psycopg2


def one_recipe_name(recipe_id):
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
    sql = "SELECT name_recipe FROM recipe where recipe_id = %s;"
    cur.execute(sql, (recipe_id,))
    recipe = cur.fetchone()[0]
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    return recipe


def last_recipe():
    conn = psycopg2.connect(
        database="Recepies",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    sql = "SELECT MAX(recipe_id) FROM recipe;"
    cur.execute(sql)
    recipe = str(cur.fetchone()[0])
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    return recipe
