import psycopg2


def one_recipe(recipe_id):
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
    sql = "SELECT txt_recipe FROM recipe where login_id = %s;"
    cur.execute(sql, str(recipe_id))
    recipe = cur.fetchone()[0]
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    return recipe

