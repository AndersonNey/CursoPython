print('--------------------------------------EXEMPLO1--------------------------------------')
lista1 = [1,2,3,4,5,6,7,8,9]

exp1 = [v for v in lista1]   # passando todos os itens de uma lista para outra
print(exp1)

print('--------------------------------------EXEMPLO2--------------------------------------')
exp2 = [v2 *2 for v2 in lista1]  # passando todos os itens de uma lista para outra e multiplicando por 2
print(exp2)

print('--------------------------------------EXEMPLO3--------------------------------------')
exp3 = [(v3,v4) for v3 in lista1 for v4 in range(3)]  #cria uma lista com o numero da lista junto com o numero do range
print(exp3)

print('--------------------------------------EXEMPLO4--------------------------------------')
l2 = ['luiz' , 'mauro' , 'maria']
ex4 = [v5.replace('a','@').upper() for v5 in l2]  #substitui todos os 'a' por '@'
print(ex4)


tupla = (
    ('chave1','valor1'),
    ('chave2','valor2'),
    ('chave3','valor3'),
    ('chave4','valor4'),
)
print('--------------------------------------EXEMPLO5--------------------------------------')
ex5 = [(x,y) for x,y in tupla]  # recriando a tupla
print(ex5)

print('--------------------------------------EXEMPLO6--------------------------------------')
ex6 = [(y,x) for x,y in tupla]  # recriando a tupla invertendo a posicao da chave com o valor
ex6 = dict(ex6) #Transformando o valor em dicionario
print(ex6)
print('--------------------------------------EXEMPLO7--------------------------------------')

l3 = list(range(100))  #criando uma lista com 100 numeros   0-99
ex7 =[v for v in l3 if v % 2 == 0]  # pegando os valores pares
print(ex7)

print('--------------------------------------EXEMPLO8--------------------------------------')
ex8 = [v1 for v1 in l3 if v1 % 3 == 0 if v1 % 8 == 0]
print(ex8)

print('--------------------------------------EXEMPLO10--------------------------------------')
ex9 = [v2 if v2 % 3 == 0 else '0' for v2 in l3]
print(ex9)

print('--------------------------------------EXEMPLO11--------------------------------------')
ex10 = [v3 if v3 % 3 == 0 and v3 % 8 == 0 else 'nao e' for v3 in l3]
print(ex10)

print('--------------------------------------EXEMPLO12--------------------------------------')

numeros = [[numero,numero**2] for numero in range(10)]

outra_lista = [y for x in numeros for y in x ]
print(outra_lista)