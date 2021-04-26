from flask import Flask, render_template, url_for, request, session, redirect, flash, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dsdfxcgssxdrcfvghbjn'

menu = [{"name": "Установка", "url": "install"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Вторая программа", "url": "second-app"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "Авторизация", "url": "login"}]


instal = [{"name": "Главная", "url": "/"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Вторая программа", "url": "second-app"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "Авторизация", "url": "login"}]


firrst_app = [{"name": "Главная", "url": "/"},
        {"name": "Установка", "url": "install"},
        {"name": "Вторая программа", "url": "second-app"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "Авторизация", "url": "login"}]


seccond_app = [{"name": "Главная", "url": "/"},
        {"name": "Установка", "url": "install"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "Авторизация", "url": "login"}]


obrat = [{"name": "Главная", "url": "/"},
         {"name": "Установка", "url": "install"},
         {"name": "Обратная связь", "url": "contact"},
         {"name": "Авторизация", "url": "login"}]



@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    profile1 = [{"name": username}]

    return render_template('profile.html', title="Профиль", menu=profile1)

@app.route('/install')
def about():
    return render_template("install.html", title="Установка компонентов", menu=instal)


@app.route('/')
@app.route('/index')
def indedx():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2 and "@" in request.form['email']:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template("contact.html", title="Обратная связь", menu=obrat)

@app.route('/first-app')
def first_app():
    return render_template("first_app.html", title="Первая программа", menu=firrst_app)


@app.route('/second-app')
def second_app():
    return render_template("second_app.html", title="Вторая программа", menu=seccond_app)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST' and request.form['username'] == "admin" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    elif 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)

@app.errorhandler(404)
def pageNoteFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

@app.errorhandler(500)
def pageNoteFount(error):
    return render_template('page500.html', title="Страница не найдена", menu=menu)

@app.errorhandler(401)
def pageNotFount(error):
    return render_template('page401.html', title="Неверный пользователь", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(port=5000, host='127.0.0.1')