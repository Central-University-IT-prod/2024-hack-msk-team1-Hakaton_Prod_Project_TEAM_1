from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Добавьте секретный ключ для работы с сессиями

accounts = []


@app.route('/')
def index():
    if session.get('auth') == True:
        return render_template("index.html")
    else:
        return render_template("info.html")


@app.route('/login')
def log():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']

    for acc in accounts:
        if login == acc["login"] and password == str(acc["password"]):
            session['auth'] = True
            return redirect('/')

    return redirect('/login')


@app.route('/reg')
def register():
    return render_template("register.html")


@app.route('/reg', methods=['POST'])
def reg():
    login = request.form['login']  # Изменено для получения логина
    password = request.form['password']
    double_password = request.form['double_password']

    if double_password == password:
        for acc in accounts:
            if acc["login"] == login:
                return "Такой Логин уже существует."

        accounts.append({"login": login, "password": password})  # Здесь используем логин
        return redirect('/')
    else:
        return "Пароли не сходятся, попробуйте снова."


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
