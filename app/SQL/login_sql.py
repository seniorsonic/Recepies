from app.SQL.Models import Login
from app.show_class import CurrentLogin
from sqlalchemy.sql.expression import func
from app import db


def new_user(firstname, secondname, password_d, email):
    emails = email.split('@')
    emailg = Login.query.with_entities(Login.email).filter(Login.email == email).first()
    if emailg is not None:
        return False
    max_login = Login.query.with_entities(func.max(Login.login_id)).first()
    if max_login:
        newAd = Login(login_id=max_login[0] + 1, firstname=firstname, secondname=secondname,
                      password_d=password_d, email=email)
    else:
        newAd = Login(login_id=1, firstname=firstname, secondname=secondname,
                      password_d=password_d, email=email)
    db.session.add(newAd)
    db.session.commit()
    CurrentLogin.user = emails[0] + '@' + emails[1]
    return True


def old_user(email, password):
    coincidence = Login.query.with_entities(Login.email, Login.password_d,
                              Login.firstname, Login.login_id).filter(Login.email == email).first()
    print(coincidence)
    if coincidence is None:
        return False
    if coincidence[1] == password:
        CurrentLogin.email = coincidence[0]
        CurrentLogin.id_user = coincidence[3]
        CurrentLogin.name_user = coincidence[2]
        return True
    return False


print(new_user("3", "3", "3", "123@12323"))