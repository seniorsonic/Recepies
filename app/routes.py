# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
    # оригинальный контент:
    # user = {'username': 'Эльдар Рязанов'}
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     },
    #     {
    #         'author': {'username': 'Ипполит'},
    #         'body': 'Какая гадость эта ваша заливная рыба!!'
    #     }
    # ]
    # return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login.html')
def login():
    return render_template('login.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/recipe.html')
def recipe():
    return render_template('recipe.html')
