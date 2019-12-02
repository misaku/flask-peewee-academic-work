from peewee import *
from App.Config.conection import db

class Pessoa(db.Model):
    id = AutoField()
    nome = CharField()