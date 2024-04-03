print('-----------------------------EXEMPLO1------------------------------------')
lista0= [
    ('chave1','valor1'),
    ('chave2','valor2'),
]


for x,y in lista0:
    print(f'{x}------{y}')

print('-----------------------------EXEMPLO2------------------------------------')

lista1= [
    ('chave1','valor1'),
    ('chave2','valor2'),
]

d1= {x:y for x,y in lista1}
print(d1)

print('-----------------------------EXEMPLO2------------------------------------')
#o exemplo acima é a mesmo coisa que esse aqui
lista2= [
    ('chave1','valor1'),
    ('chave2','valor2'),
]

dic1=dict(lista2)
print(dic1)

print('-----------------------------EXEMPLO3------------------------------------')
#fazendo alguns testes
lista3= [
    ('chave1','valor1'),
    ('chave2','valor2'),
]

d1= {x:y*2 for x,y in lista3}
print(d1)
print('-----------------------------EXEMPLO4------------------------------------')

dic2= {f'chave_{x}':x**2 for x in range(5)}
print(dic2)

print('-----------------------------EXEMPLO5---------CONJUNTO COMPREHENSION----')
#parece muito com dicionario
conjunto1 = {x for x in range(5)}
print(conjunto1)