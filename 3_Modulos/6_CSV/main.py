
"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""

import os
caminho = os.path.dirname(os.path.realpath(__file__))


import csv

print('-----------RETORNANDO OS DADOS COMO LISTA---------------------')

with open(caminho + '\clientes.csv','r',encoding='utf-8') as arquivo:
    dados = csv.reader(arquivo)  #retornar um interador
    next(dados)     #fazendo passar a primeira linha, para somente exibir os dados seguintes, sem exibir nome das colunas.
    for dado in dados:
        print(dado)

print('-----------RETORNANDO OS DADOS COMO DICIONARIO---------------------')

with open(caminho + '\clientes.csv','r',encoding='utf-8') as arquivo:
    dados = csv.DictReader(arquivo)  #retornar um interador
    #a coluna da tabela vem com chave e o valor do campo como valor
    for dado in dados:
        print(dado)

    # outra maneira de pegar os resultados
    # for dado in dados:
    #     print(dado['Nome'],  dado['Sobrenome'],  dado['E-mail'],  dado['Telefone'])

print('----------POSSIVEL PROBLEMA LIGADO AO INTERATOR-------------------')
"""
# se eu fisesse isso  daria erro porque o for esta fora do with e o arquivo esta fechado, e nao tem como buscar o proximo valor ja que dados nao é uma lista mas um interator
with open(caminho + '\clientes.csv','r',encoding='utf-8') as arquivo:
    dados = csv.DictReader(arquivo)  
    
for dado in dados: #daria erro porque o arquivo ja estaria fechado e o interador é incapaz de buscar o proximo valor
    print(dado)
# A solucao para resolver isso seria fazer uma lista resgatando todos os valores e os guardado segue soluca abaixo
"""

with open(caminho + '\clientes.csv','r',encoding='utf-8') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]  #pegando todos os dados possiveis que o interator poderia passar e os guardado em uma lista
    print(dado)
#Agora sim eu posso fazer o for mesmo com o arquivo fechado
for dado in dados:
    print(dado)

print('----------TRANSFERINDO DADOS PARA OUTRO LOCAL--------------')


with open(caminho + '\clientes.csv','r',encoding='utf-8') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]   #lembrando que estou trabalhando com dicionario

with open(caminho + '\destino.csv', 'w',encoding='utf-8') as arquivo:
    #delimiter --> especifica o caractere usado para separar cada campo. O padrão é a vírgula ( ',').
    #quotechar--> especifica o caractere usado para cercar campos que contêm o caractere delimitador. O padrão é aspas duplas
    #escapechar --> especifica o caractere usado para escapar do caractere delimitador, caso as aspas não sejam usadas. O padrão é nenhum caractere de escape.
    escreve = csv.writer(arquivo,delimiter=',', quotechar='"' ,quoting=csv.QUOTE_ALL)  # cuidado que  ''''    """"    '"'      sao diferentes
    
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow([chaves[0],chaves[1],chaves[2],chaves[3]])

    for dado in dados:
        escreve.writerow(
            [dado['Nome'],dado['Sobrenome'],dado['E-mail'],dado['Telefone']]
        )





