""" 
count - itertools
"""

from itertools import count    #count vai gerar um ITERADOR

contador = count(start = 5,step=0.2)     #count nao tem fim    start ->inicio      step=pulo(aceita inteiro e ponto flutuante (e numeros negativos))       

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))


print('--------------------------matricula-------------------------------')


matricula = count()
lista=['luiz','joao','maria']
lista= zip(matricula,lista)
print(list(lista))
