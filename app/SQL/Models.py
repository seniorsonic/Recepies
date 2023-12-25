from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Login(db.Model):
    __tablename__ = 'login'

    login_id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(Text, nullable=False)
    secondname = Column(Text, nullable=False)
    password_d = Column(Text, nullable=False)
    email = Column(Text, nullable=False)


class Recipe(db.Model):
    __tablename__ = 'recipe'

    recipe_id = Column(Integer, primary_key=True, nullable=False)
    login_id = Column(Integer, ForeignKey('login.login_id'), nullable=False)
    name_recipe = Column(Text, nullable=False)
    ingredients = Column(Text, nullable=False)
    txt_recipe = Column(Text, nullable=False)
    login = relationship('Login', back_populates='recipes')


Login.recipes = relationship('Recipe', back_populates='login')
