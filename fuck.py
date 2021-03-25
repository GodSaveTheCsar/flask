from flask import Flask, request, url_for
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
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/style.css">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета Претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text"placeholder="Фамилия" name="text">
                                    <input type="text" class="form-control" id="text"placeholder="Имя" name="text">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее полное</option>
                                          <option>Среднее проффесианальное</option>
                                          <option>Высшее, бакалавр</option>
                                          <option>Высшее, бакалавр, магистратура</option>
                                        </select>
                                     </div>
                                       <label for="form-check">Укажите проффесию</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>инженер-исследователь</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>пилот</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>строитель</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>экзобиолог</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>врач</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>инженер по терраформированию</option>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>климатолог</option>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>специалист по радиационной защите</option>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>астрогеолог</option>
                                        </div><div class="form-check">
                                          <input class="form-check-input" type="radio" name="proffesion">
                                          <option>гляциолог</option>
                                        </div>
                                    </label>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                                                        <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
    <html lang="en">
       <head>
                                   <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/style.css">
       </head>
                         <body>
                    <h1>        Моё предложение: {planet_name}</h1>
                    <h2>
                    <div class="alert alert-secondary" role="alert">
                    Эта планета достаточно близка к земле)
                    </div>
                    <div class="alert alert-success" role="alert">
                    На ней есть ресурсы...
                    </div>
                    <div class="alert alert-secondary" role="alert">
                    Она милая)
                    </div>
                    <div class="alert alert-warning" role="alert">
                    На ней есть небольшое магнитное поле)
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Наконец, она просто красива!
                    </div>
                    </h2>
                  </body>
       
    '''
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def aaa(nickname, level, rating):
    return f"""<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="static/css/style.css">
       </head>
                                 <body>
                    <h1>Результаты отбора</h1>
                    <h2>
                    Претенента на участие в миссии {nickname}:
                    <div class="alert alert-success" role="alert">
                    Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    Составляет {rating}!
                    <div class="alert alert-warning" role="alert">
                    Желаем удачи!
                    </div>
                    </h2>
                  </body>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
