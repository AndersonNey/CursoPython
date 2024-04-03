#https://docs.python.org/3/library/json.html
"""
JSON (Javascript Object Notation) é um formato de troca de dados entre sistemas e 
programas muito leve e de fácil utilizaçao. Muito utilizado por APIs
"""
#fiz isso so pra direcionar para essa pasta de maneira mais facil
import os
caminho = os.path.dirname(os.path.realpath(__file__))



import json

clientes_dicionario = {
    1: {
        'nome': 'Luiz Otávio',
        'sobrenome': 'Miranda',
        'idade': 25,
        'altura': 1.80,
        'peso': 80.53,
    }
}

clientes_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    }
}
"""

lista = [1,2,3,4,5,6]


print('CONVERTENDO DE PYTHON PARA JSON----------------------------------------------------------------------------')

dados_json = json.dumps(clientes_dicionario ,indent=4)   #Quando voce quer converter um tipo de dado para uma STRING que contem dados   # indent-> melhora a visualizacao com identacao
print(dados_json)
print(type(dados_json))

print('CONVERTENDO DE JSON PARA PYTHON----------------------------------------------------------------------------')

dicionario = json.loads(clientes_json)
print(dicionario)
print(type(dicionario))

print('ESCREVENDO EM UM ARQUIVO JSON------------------------------------------------------------------------------')

with open(caminho +'\clientes.json','w+') as arquivo:
    json.dump(clientes_dicionario , arquivo,indent = 4)

print('LENDO UM ARQUIVO JSON--------------------------------------------------------------------------------------')

with open(caminho +'\clientes.json','r') as arquivo:
    dados_dicionario = json.load(arquivo)
print(dados_dicionario)










