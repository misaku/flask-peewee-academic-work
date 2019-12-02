from peewee import *
from App.Config.conection import db

class Local(db.Model):
    id = AutoField()
    nome = CharField()
    endereco = TextField()
