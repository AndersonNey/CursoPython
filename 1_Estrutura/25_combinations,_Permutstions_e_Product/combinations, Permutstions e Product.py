""" 
Combinations, Permutations e Product - Itertools

Combinaçao - ordem nao importa 
Permutaçao - ordem importa
Ambos nao repetem valores unicos 

Produto - ordem importa e repete valores unicos 
"""

from itertools import combinations, permutations, product


pessoas = ['Luiz','Andre','Eduardo','Leticia','Fabrício','Rose']

for grupo in combinations(pessoas,2):    # valor interavel e a quantidade por grupo
    print(grupo)

print('-'*50)
for grupo1 in permutations(pessoas,2):
    print(grupo1)

print('-'*50)
for grupo2 in product(pessoas, repeat=2):   # esse precisa de repeat para falar a quantidade por grupo
    print(grupo2)