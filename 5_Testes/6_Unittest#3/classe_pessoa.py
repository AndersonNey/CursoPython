import requests


"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obitidos bool

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)

"""

class Pessoa:
    def __init__(self,nome,sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos= False

    def obter_todos_os_dados(self):
        resposta = requests.get('122333')  #Essa tentativa nem vai ocorre nos testes porque eu estou simulando ela la

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERROR 404'