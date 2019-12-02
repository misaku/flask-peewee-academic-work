from App.Model.Local import Local
from App.Model.Pessoa import Pessoa
from App.Model.Tarefa import Tarefa
from App.Model.UserAuth import UserAuth

def routes(api):
    api.register(Local)
    api.register(Pessoa)
    api.register(Tarefa)
    api.register(UserAuth)
