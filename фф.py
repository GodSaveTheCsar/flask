import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.departaments import Department
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init(input())
db_sess = db_session.create_session()
a = db_sess.query(Department).filter(Department.id == 1).all()
for user in db_sess.query(User).all():
    if user.name in a.members:
        b = db_sess.query(Jobs).filter(Jobs.id == user.id, Jobs.work_size > 25).all()
        print(b)

