from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, request, render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/index/<name>')
def login(name):
    return render_template('base.html', title=name)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)