import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

# App configuration
app = Flask(__name__, instance_relative_config=True)
dburl = "{DBMS}://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}".format(**os.environ)
app.config['SQLALCHEMY_DATABASE_URI'] = dburl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

    def __init__(self, name):
        self.name = name

# Test data
if os.environ['TEST_MODE'] == 'true':
    db.create_all()
    db.session.add(Person("Clement"))
    db.session.commit()

# REST service
location = '/api'
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Person, url_prefix=location, methods=['GET', 'POST', 'DELETE'])