#http://127.0.0.1:8080/image_mars
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index11():
    return "Миссия Колонизация Марса"
@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    pr_list = list()
    for i in '''Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!'''.split('\n'):
        pr_list.append(i)
    return '</br>'.join(pr_list)
@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                    <h2>Вот она какая, красная планета<h2>
                </html>"""
@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1><p class="text-danger">Жди нас, Марс!</p></h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary" role="alert">
                    Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                    Человечеству мала одна планета
                    </div>
                    <div class="alert alert-secondary" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                    И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Присоединяйся!
                    </div>
                  </body>
                </html>'''
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)