import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

    def __init__(self, name):
        self.name = name

if os.environ['TEST_MODE'] == 'true':
    db.create_all()
    db.session.add(Person("Clement"))
    db.session.commit()

location = '/api'
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Person, url_prefix=location, methods=['GET', 'POST', 'DELETE'])