import psycopg2
from app.show_class import current_login


def new_user(firstname, secondname, password_d, email):
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
    sql = "SELECT email FROM login where email = '" + emails[0] + '@' + emails[1] + "';"
    cur.execute(sql, email)
    email_good = cur.fetchone()
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
    sql = "SELECT email, password_d, firstname, login_id FROM login where email = '" + emails[0] + '@' + emails[1] + "';"
    cur.execute(sql, email)
    coincidence = cur.fetchone()
    if coincidence is None:
        return False
    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    if coincidence[1] == password:
        current_login.email = coincidence[0]
        current_login.id_user = coincidence[3]
        current_login.name_user = coincidence[2]
        return True
    return False


# new_user(1, 1, 1, "1@1")
# new_user('Николай', 'Кравчук', 'molodez', 'pochta@yandex.ru')
# old_user("pochta@yandex.ru", 'molodez')
