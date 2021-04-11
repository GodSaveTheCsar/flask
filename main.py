from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

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
    user1 = User()
    user1.name = "Ridley"
    user1.surname = "Well"
    user1.email = "scott_engineer@mars.org"
    user1.age = 19
    user1.position = 'yed'
    user1.speciality = 'yull'
    user1.address = 'module_2'
    user2 = User()
    user2.name = "Ridley"
    user2.surname = "Aught"
    user2.email = "scott_bruh@mars.org"
    user2.age = 20
    user2.position = 'rad'
    user2.speciality = 'yell'
    user2.address = 'module_3'
    user3 = User()
    user3.name = "Yalley"
    user3.surname = "Aught"
    user3.email = "scott_yalley@mars.org"
    user3.age = 14
    user3.position = 'ra1d'
    user3.speciality = 'yel1'
    user3.address = 'module_4'
    job = Jobs()
    job.team_leader = 1
    job.job = ' deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = 'now'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(job)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()