from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/index/<name>')
def login(name):
    return render_template('base.html', title=name)
@app.route('/galery', methods=['POST', 'GET'])
def galery():
    images = ["/static/img/mars1.jpg", "/static/img/mars2.jpg", "/static/img/mars3.jpeg", "/static/img/mars4.jpg", "/static/img/mars5.jpg"]
    if request.method == 'GET':
        return render_template('carousel.html', title='Красная планета', images=images)
    elif request.method == "POST":
        f = request.files['file']
        file_path = "/static/img/" + str(f).split()[1][1:-1]
        images.append(file_path)
        return render_template('carousel.html', title='Красная планета', images=images)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)