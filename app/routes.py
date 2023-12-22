# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify, Response
from app import app
from app.SQL.login_sql import new_user, old_user
from app.SQL.main_recipes_sql import one_recipe_name, last_recipe
from app.SQL.new_recipe_sql import new_recipe
from app.curr_login import current_login
from app.SQL.current_recipe_SQL import choise_recipe


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index_get():
    return render_template('index.html', name_user=current_login.name_user)


@app.route('/', methods=['POST'])
@app.route('/index.html', methods=['POST'])
def index_post():
    data = request.json
    recipe = choise_recipe(data.get('id_recipe'))
    current_recipe(recipe)
    return jsonify({'success': True})


@app.route('/quit.html', methods=['POST'])
def quit():
    current_login.id_user = 0
    current_login.name_user = ''
    current_login.email = ''
    return jsonify({'success': True})


@app.route('/login.html', methods=['GET'])
def login_get():
    return render_template('login.html', name_user=current_login.name_user)


@app.route('/login.html', methods=['POST'])
def login_post():
    data = request.json

    # Теперь переменные доступны на сервере
    email = data.get('email')
    password = data.get('password')

    if old_user(email, password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Не верный ввод'})


@app.route('/register.html', methods=['GET'])
def register_get():
    return render_template('register.html', name_user=current_login.name_user)


@app.route('/register.html', methods=['POST'])
def register_post():
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
    return render_template('contact.html', name_user=current_login.name_user)


@app.route('/new_recipe.html', methods=['GET'])
def new_recipe_get():
    if current_login.name_user != '':
        return render_template('new_recipe.html', name_user=current_login.name_user)
    else:
        return render_template("error.html")


@app.route('/new_recipe.html', methods=['POST'])
def new_recipe_post():
    # Получаем данные из тела запроса
    data = request.json

    # Теперь переменные доступны на сервере
    login_id = current_login.id_user
    name_recipe = data.get('name')
    ingredients = data.get('ingredients')
    txt_recipe = data.get('txt_recipe')

    if new_recipe(login_id, name_recipe, ingredients, txt_recipe):
        return jsonify({'success': True})


@app.route('/current_recipe.html')
def current_recipe(recipe):
    return render_template("current_recipe.html", login_id=recipe[0], name_recipe=recipe[1], ingredients=recipe[2],
                           txt_recipe=recipe[3])


@app.route('/get_last_recipe_data')
def get_last_recipe_text():
    index_data = last_recipe()
    return Response(index_data)


@app.route('/get_recipe_data/<recipe_id>')
def get_recipe_text(recipe_id):
    text_data = one_recipe_name(recipe_id)
    return Response(text_data)
