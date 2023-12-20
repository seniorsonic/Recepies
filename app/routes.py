# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify, Response
from app import app
from app.SQL.login_sql import new_user
from app.SQL.main_recipes_sql import one_recipe, last_recipe


@app.route('/')
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register.html', methods=['GET'])
def register_get():
    return render_template('register.html')


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
    return render_template('contact.html')


@app.route('/new_recipe.html', methods=['GET'])
def recipe():
    return render_template('new_recipe.html')


# @app.route('/new_recipe.html', methods=['POST'])
# def recipe():
#     # Получаем данные из тела запроса
#     data = request.json
#
#     # Теперь переменные доступны на сервере
#     login_id = current_login.user
#     img = data.get('img')
#     txt_recipe = data.get('txt_recipe')
#
#     if new_recipe(login_id, img, txt_recipe):
#         return jsonify({'success': True})


@app.route('/get_last_recipe_data')
def get_last_recipe_text():
    index_data = last_recipe()
    return Response(index_data)


@app.route('/get_recipe_data/<recipe_id>')
def get_recipe_text(recipe_id):
    text_data = one_recipe(recipe_id)
    return Response(text_data)