from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.name = "Ridley"
    user.surname = "Scott"
    user.email = "scott_chief@mars.org"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'

    user.name = "Ridley"
    user.surname = "Well"
    user.email = "scott_engineer@mars.org"
    user.age = 19
    user.position = 'yed'
    user.speciality = 'yull'
    user.address = 'module_2'

    user.name = "Ridley"
    user.surname = "Aught"
    user.email = "scott_bruh@mars.org"
    user.age = 20
    user.position = 'rad'
    user.speciality = 'yell'
    user.address = 'module_3'

    user.name = "Yalley"
    user.surname = "Aught"
    user.email = "scott_yalley@mars.org"
    user.age = 14
    user.position = 'ra1d'
    user.speciality = 'yel1'
    user.address = 'module_4'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()