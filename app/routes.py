# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify
from app import app
from app.login_sql import new_user
from app.main_recipes_sql import recipe


@app.route('/')
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login.html', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route('/login.html', methods=['POST'])
def login_post():
    # Получаем данные из тела запроса
    data = request.json

    # Теперь переменные доступны на сервере
    name = data.get('name')
    surname = data.get('surname')
    password = data.get('password')
    email = data.get('email')

    if new_user(name, surname, password, email):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Такая почта уже зарегистрирована'})


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/recipe.html')
def recipe():
    return render_template('recipe.html')
