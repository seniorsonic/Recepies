import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'index.html' in response.data

def test_index_post(client):
    data = {'id_recipe': 1}
    response = client.post('/', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) is None


def test_quit(client):
    response = client.post('/quit.html')
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': True}

def test_RuorEng(client):
    response = client.post('/RuorEng.html')
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': True}

def test_RuorEng_current(client):
    response = client.post('/RuorEng_current.html')
    assert response.status_code == 200
    assert json.loads(response.data) == {'switcher': "en"}


def test_register_post(client):
    data = {'name': 'John', 'surname': 'Doe', 'password': 'password', 'email': 'test@example.com'}
    response = client.post('/register.html', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': False, 'error': 'Такая почта уже зарегистрирована'}


def test_current_recipe_post(client):
    response = client.post('/current_recipe.html')
    assert response.status_code == 200
    assert 'login_id' in json.loads(response.data)


def test_new_recipe_post(client):
    data = {'name': 'Рецепт', 'ingredients': 'Ингридиенты', 'txt_recipe': 'Инструкция'}
    response = client.post('/new_recipe.html', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': False}


def test_login_post(client):
    data = {'email': 'test@example.com', 'password': 'password'}
    response = client.post('/login.html', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': True}
