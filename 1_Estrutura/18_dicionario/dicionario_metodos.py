#pelo o que eu entendi   ITEM é  chave e seu valor


# dicionario ={
#     'cliente1':{
#         'nome':'joao',
#         'sobrenome': 'filipe',
#         'idade': 17,
#         'habilidades':{
#             'dança':'nenhuma',
#             'esporte':'futebol'}},
#     'cliente2':{
#         'nome':'maria',
#         'sobrenome': 'luiza',
#         'idade': 19,
#         'habilidades':{
#             'dança':'hiphop',
#             'esporte':'basquete'}},
#     'cliente3':{
#         'nome':'carlos',
#         'sobrenome': 'fernando',
#         'idade': 21,
#         'habilidades':{
#             'dança':'valsa',
#             'esporte':'handbol'}},
#     'cliente4':{
#         'nome':'paulo',
#         'sobrenome': 'henrique',
#         'idade': 34,
#         'habilidades':{
#             'dança':'samba',
#             'esporte':'volei'}},
# }

print('---------------------------------------CLEAR-------------------------------------------------------------------------')



dicionario1 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}
print(dicionario1)
dicionario1.clear()
print(dicionario1)

print('-------------------------------------COPY------------------------------------------------------------------------------')

# o metodo copy criar uma referencia do mesmo lugar na memoria da outra variavel , tipo um atalho , tudo que fazer em um vai alterar os dois
#TER CUIDADO com o uso do COPY

dicionario2 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

print(dicionario2)
x = dicionario2.copy()
print(x)


print('-------------------------------------FROMKEYS---------------------------------------------------------------------------')

#cria um dicionario usando outro dicionario mudando seu valores para o que voce definir

dicionario3 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}
d3x1=5   #variavel dicionario 3 variavel 1  ---- fiz desse jeito para nao me perder

dicionario3_1= dict.fromkeys(dicionario3,d3x1)  #setando os valores padroes
print(dicionario3_1)


print('-------------------------------------GET----------------------------------------------------------------------')

#no GET  é necessario informa a chave , mas nao é obrigatorio o inserir o valor da chave
dicionario4 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}
d4x1= (dicionario4.get('cliente1'))  # mostra tudo do cliente 1
print(d4x1)

d4x2= (dicionario4.get('cliente0'))  #ao tentar retornar uma chave que nao existe ele retorna none
print(d4x2)

d4x3= (dicionario4.get('cliente1','nome'))  #pelo o que eu entendi nao da certo tentar olhar so os dados do 'nome' ,porque o valor da chave cliente 1
print(d4x3)                                 # é um dicionario ou seja um valor unico


print('-------------------------------------ITEMS----------------------------------------------------------------------')

dicionario5 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

d5x1 =dicionario5.items()  #retorna todos seu itens
print(d5x1)

print('-------------------------------------KEYS----------------------------------------------------------------------')

dicionario6 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

d6x1 =dicionario6.keys()  #retorna todas as chaves
print(d6x1)

print('-------------------------------------POP----------------------------------------------------------------------')

dicionario7 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

d7x1 = dicionario7.pop('cliente1')   #removendo tudo do cliente 1
print(d7x1)  #perceba que antes de excluir ele retorna o valor
print(dicionario7)

d7x2 = dicionario7['cliente2']['habilidades'].pop('dança') # observa que dança foi retirado de habilidades do cliente 2
print(dicionario7)


print('-------------------------------------POPITEM------------------------------------------------------------------')

dicionario8 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}
print(dicionario8)
d8x1 =dicionario8.popitem()   #exclui o ultimo item adicionado
print(d8x1)   #perceba que antes de excluir ele retorna o valor
print(dicionario8)

print('-------------------------------------SETDEFAULT------------------------------------------------------------------')

dicionario9 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}
d9x1= dicionario9.setdefault('cliente0')  # como a chave nao existia ele criou a chave e como padrao setou o valor None
print(d9x1)
print(dicionario9)

d9x2 = dicionario9.setdefault('cliente1','palavra_de_backup')
print(d9x2) #retornou o valor da chave, como a chave existia ele nao precisou setar esse valor na chave - 'palavra_de_backup' (foi tipo ignorado)
print(dicionario9)

d9x3 = dicionario9.setdefault('cliente5','palavra_de_backup')
print(d9x3) #retornou o valor da chave, como a chave nao existia ele criou a chave e ja setou seu valor que no caso foi 'palavra_de_backup'
print(dicionario9)

print('-------------------------------------UPDATE------------------------------------------------------------------')
#para usar o update precisar ser interavel
dicionario10 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

d10x1= dicionario10.update({'cliente10':'Fernando'})
print(d10x1)     # fiz so pra ter certeza que update nao retorna nada
print(dicionario10)  # o valor foi setado

dicionario_exemplo = {
    'cliente_alpha':'XXXXX',
    'cliente_beta': 'YYYYY'
}

dicionario10.update(dicionario_exemplo) # concatenando dicionarios
print(dicionario10)


print('-------------------------------------VALUES------------------------------------------------------------------')

dicionario11 ={
    'cliente1':{'nome':'joao','sobrenome': 'filipe','idade': 17,'habilidades':{'dança':'nenhuma','esporte':'futebol'}},
    'cliente2':{'nome':'maria','sobrenome': 'luiza','idade': 19,'habilidades':{'dança':'hiphop','esporte':'basquete'}},
    'cliente3':{'nome':'carlos','sobrenome': 'fernando','idade': 21,'habilidades':{'dança':'valsa','esporte':'handbol'}},
    'cliente4':{'nome':'paulo','sobrenome': 'henrique','idade': 34,'habilidades':{'dança':'samba','esporte':'volei'}},
}

d11x1= dicionario11.values()  # retornarar somente os valores das chaves     |   nao recebe parametro na funçao
print(d11x1)

# so uma observaçao no exemplo abaixo que é
#Quando um valor é alterado no dicionário, o objeto de visualização também é atualizado:

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values()
# car["year"] = 2018
# print(x)
#
#CMD >>>  dict_values(['Ford', 'Mustang', 2018])


