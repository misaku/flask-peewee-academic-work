from App.Model.Local import Local
from App.Model.Pessoa import Pessoa
from App.Model.Tarefa import Tarefa
from App.Model.UserAuth import UserAuth

def creatTable():
    Local.create_table(fail_silently=True)
    Pessoa.create_table(fail_silently=True)
    Tarefa.create_table(fail_silently=True)
    UserAuth.create_table(fail_silently=True)