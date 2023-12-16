import psycopg2


def recipe(recipe_id):
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
    sql = "SELECT * FROM recipe where login_id = %s;"
    cur.execute(sql, recipe_id)
    recipe = cur.fetchone()
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    return recipe[3]

