#dicionario-> a chave pode ser numero , caracter,tupla | o valor pode ser numero , caracter

#se tiver chaves com o mesmo nome, prevalece o valor da ultimo valor que apareceu
#exemplo->  dicionario1  = {'chave':2,'chave':3,'chave':4,'chave':5,}
#no caso acima o verdadeiro valor de chave seria 5, pois foi o ultimo valor setado,
# e apareceria somente como {'chave':5} no terminal se fosse print(dicionario1)



# criando dicionario
d00= dict()   #dicionario vazio
print(d00)

d0 =dict(carro='celta',carro2='saveiro',carro3='maverick')  #outra maneira de criar um dicionario
print(d0)
print(d0['carro2'])
d0['carro4']='golf'  #adicionando outra chave
print(d0)


d1 = {}     #dicionario vazio
print(d1)


d2 = {'carro':'fiat',
      'moto':'suzuki'}   #dicionario com dados
print(d2)




#adicionando valor ao dicionario

d10 = {'carro1':'mercedes',
       'carro2':'ferrari'}

d10['carro10']= 'lamborghini' #criando um indice e dando valor a ele
print(d10)

print('---------------------------------------------------------------------------------------------------')


d11 =  {
      'str':'valor1',
       123: 'valor2',
      (1,2,3,4):'valor3'
}
print(d11)
#print(d11[753])  --> se rodasse esse comando iria da erro ,pois chave nao existe
#para resolver isso segue abaixo

if 753 not in d11:  #se esta chave nao esta no dicionario d11 crie e defina um valor
      d11[753]='valor4'
print(d11)


print('-----------------------------------get----------------------------------------------------------------')

d12 = {
      'str':'valor1',
       'carro': 'valor2',
      'moto':'valor3'
}

print(d12.get('caminhao')) # como essa chave nao existe retorna none
print(d12.get('carro')) # como essa chave existe retorna o seu valor

print('----------------------------------update-----------------------------------------------------------------')

d13 = {
      'carro1':'valor1',
      'carro2':'valor2',
      'carro3':'valor3'
}

print(d13)
d13.update({'carro3':'valor0'}) #atualizando o valor de uma das chaves OBSERVE QUE ESTA DENTRO DE UM DICIONARIO
print(d13)

print('----------------------------------update-----------------------------------------------------------------')

d14 = {
      'carro1':'valor1',
      'carro2':'valor2',
      'carro3':'valor3'
}

print(d14)
d14.update({'carro4':'valor0'}) #atualizando o valor de uma das chaves OBSERVE QUE ESTA DENTRO DE UM DICIONARIO
                                #SE A CHAVE NA EXISTIR ELE CRIA
print(d14)


print('-----------------------------------del-------------------------------------------------------------')

d15 = {
      'carro1':'valor1',
      'carro2':'valor2',
      'carro3':'valor3'
}
print(d15)
del d15['carro1']
print(d15)

print('---------------------------------------------------------------------------------------------------')

d16 = {
      'carro1':'fiat',
      'carro2':'subaru',
      'carro3':'jac'
}

print('carro1'in d16)
print('carro1'in d16.keys())   #mesma coisa que o de cima
print('fiat' in d16.values())


print('-----------------------------------len-------------------------------------------------------------')

d17 = {
      'carro1':'fiat',
      'carro2':'subaru',
      'carro3':'jac'
}

print(len(d17)) #quantos pares a no dicionario

print('---------------------------------------------------------------------------------------------------')

d18 = {
      'carro1':'fiat',
      'carro2':'subaru',
      'carro3':'jac'
}

for k in d18:    #inteirando no dicionario
    print(k)

print('+++++++++++++++++++++')

for r in d18.keys():   # inteirando nas chaves   eu acho que é a mesma coisa que o de cima
    print(r)

print('+++++++++++++++++++++')

for u in d18.values(): # inteirando nos valores
    print(u)

print('+++++++++++++++++++++')

for p in d18.items(): # inteirando os itens (mostrando todos os itens do dicionario)
    print(p)

print('+++++++++++++++++++++')

for g in d18.items():
    print(g[0],g[1])
print('---------------------------------------------------------------------------------------------------')

d19 = {
    'chave1':'valor1',
    'chave2':'valor1',
    'chave3':'valor1'
}

for w in d19.items():  # W retorna uma tupla
    print(w)

for a in d19.items():
    print(a[0],a[1]) #consultando a tupla

for b , c in d19.items(): #outra maneira
    print(b,c)

print('---------------------------------------------------------------------------------------------------')

clientes ={
    'dono1': {'nome':'joazinho','idade': 17},
    'dono2' :{'nome':'maria','idade': 18},
    'dono3' :{'nome':'miguel','idade': 19},
    'dono4' :{'nome':'gabriel','idade': 20},
}


for i1 ,k1 in clientes.items():  # k1 ficara com o valor da chave do dicionario       tem que usar items() porque senao intera somente sobre as chaves 
    print(i1)  #donos
    for u1 in k1.items():  # aqui vai interar o item que ficou guardado no k1 exemplo: 'nome':'joazinho','idade': 17
        print(f'\t {u1}')   #aqui exibira o item em uma tupla


for a1 ,b1 in clientes.items():  # b1 ficara com o valor da chave do dicionario
    print(a1)
    for c1 ,d1 in b1.items():  # aqui vai interar o item que ficou guardado no b1 e retirar o valor da tupla
        print(f'\t {c1} -> {d1}')


print('---------------------------------------------------------------------------------------------------')


#ficar esperto porque o dicionario tem os mesmos problemas que as listas que tentar copiar aponta para o mesmo lugar na memoria

print('---------------------------------------------------------------------------------------------------')


# .copy() funcionar parcialmente bem  |  so como referencia

diciona1 ={1:'a',  2:'b',  3:'c',  4:['luiz','otavio']}

lista1= diciona1.copy()

print(diciona1)
print(lista1)

lista1[1]='luiz'  #perceba que ele irar altera sem mexer na outra

print(diciona1)
print(lista1)

lista1[4][0] = 'joao'   #perceba que ele irar alterar mexendo nas duas

print(diciona1)
print(lista1)

print('---------------------------------------------------------------------------------------------------')

#para resolver isso e fazer uma copia realmente sem ter esse tipo  de problema faça da seguinte maneira
# importy copy
#
#diciona1 ={1:'a',  2:'b',  3:'c',  4:['luiz','otavio']}
#lista1 = copy.deepcopy(d1)
#

print('---------------------------------------------------------------------------------------------------')
#tem como converte lista em dicionario , mas desde que possua a sua estrutura equivalente
lista2 = [
    ['cliente1',17],
    ['cliente2',18],
    ['cliente3',19],
    ['cliente4',14]
]
print(lista2)

dicio1= dict(lista2)
print(dicio1)

print('---------------------------------------------------------------------------------------------------')
#tambem da certo misturado
lista3 = (
    ['cliente1',17],
    ('cliente2',18),
    ['cliente3',19],
    ('cliente4',14)
)
print(lista3)

dicio2= dict(lista3)
print(dicio2)

print('---------------------------------------------------------------------------------------------------')

dicionario1  = {
    'nome1':'CARLOS',
    'nome2':'FERNANDO',
    'nome3':'JOAO',
    'nome4':'LUCAS'
}

print(dicionario1)
dicionario1.pop('nome3')  # pode informar o item para remover
print(dicionario1)
dicionario1.popitem()  #removendo o ultimo item sem precisar de inserir argumento
print(dicionario1)

print('---------------------------------------------------------------------------------------------------')
# operador + nao funciona para concatenar dicionarios

dicionario2 = {
    1:10,
    2:11,
    3:12,
    4:13
}

dicionario3 = {
    'a':'D',
    'b':'E',
    'c':'F'
}

print(dicionario2)
print(dicionario3)

dicionario2.update(dicionario3)  #concatenando o dicionario 3  no dicionario 2

print(dicionario2)
print(dicionario3)


print('---------------------------CONSULTANDO UM VALOR---------------------------------------------------------')

dicionario ={
    'cliente1':{
        'nome':'joao',
        'sobrenome': 'filipe',
        'idade': 17,
        'habilidades':{
            'dança':'nenhuma',
            'esporte':'futebol'}},
    'cliente2':{
        'nome':'maria',
        'sobrenome': 'luiza',
        'idade': 19,
        'habilidades':{
            'dança':'hiphop',
            'esporte':'basquete'}},
    'cliente3':{
        'nome':'carlos',
        'sobrenome': 'fernando',
        'idade': 21,
        'habilidades':{
            'dança':'valsa',
            'esporte':'handbol'}},
    'cliente4':{
        'nome':'paulo',
        'sobrenome': 'henrique',
        'idade': 34,
        'habilidades':{
            'dança':'samba',
            'esporte':'volei'}},
}
var1 =dicionario['cliente1']['habilidades']['esporte']
print(var1)

print('------------------------------------------------------------------------------------')

dicio = {1:"carro",2:"caminhao",3:"moto",4:"trem"}

variavel = dicio.items()  #isso é um gerador nao um interador

#print(next(variavel))