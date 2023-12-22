from app.SQL.login_sql import new_user, old_user


# тест для проверки создания и прохождения логина новым юзером
# new_user(1, 1, 1, "arbuz@yandex.ru")
print(old_user("arbuz@yandex.ru", '1'))
