import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init(input())
db_sess = db_session.create_session()
for user in db_sess.query(User).filter(User.address == 'module_1', User.age < 21).all():
    user.address = 'module_3'
db_sess.commit()
