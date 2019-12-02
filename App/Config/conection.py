import datetime
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from peewee import *
from flask_peewee.db import Database
from flask_peewee.admin import Admin

DATABASE = {
    'name': 'my_app',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'password': 'postgres',
    'host':'localhost',
    'port':5432
}

DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)
