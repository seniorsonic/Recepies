from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/Recepies'
db = SQLAlchemy(app)
# from app.SQL import Models
with app.app_context():
    db.create_all()

from app import routes