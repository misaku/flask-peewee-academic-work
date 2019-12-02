from peewee import *
from App.Config.conection import db
from App.Model.Local import *
from App.Model.Pessoa import *

class Tarefa(db.Model):
    id = AutoField()
    nome = CharField()
    descricao = TextField()
    pessoa =  ForeignKeyField(Pessoa, backref='tarefas')
    contato =  ForeignKeyField(Pessoa, backref='tarefas')
    local = ForeignKeyField(Local, backref='tarefas')
    feita = BooleanField()