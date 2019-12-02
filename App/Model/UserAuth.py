from peewee import *
from App.Config.conection import db


class UserAuth(db.Model):
    id = AutoField()
    nome = CharField()
    email = CharField()
    senha = TextField()