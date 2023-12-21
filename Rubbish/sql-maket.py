def old_user(email, password):
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
    emails = email.split('@')
    sql = "SELECT email, password FROM login where email = '" + emails[0] + '@' + emails[1] + "';"
    cur.execute(sql, email)
    email_good = cur.fetchone(0)
    if email_good is not None:
        return False
    # SQL-запрос для выполнения операции INSERT
    sql = "SELECT MAX(login_id) FROM login;"
    cur.execute(sql)
    max_login = cur.fetchone()[0]
    sql = "INSERT INTO Login (Login_id, firstname, secondname, password_d, email) " \
          "VALUES (%s, %s, %s, %s, %s);"
    if max_login:
        cur.execute(sql, (max_login + 1, firstname, secondname, password_d, email))
    else:
        cur.execute(sql, (1, firstname, secondname, password_d, email))
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    current_login.user = emails[0] + '@' + emails[1]
    return True