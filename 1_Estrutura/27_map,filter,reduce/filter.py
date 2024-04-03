
#filter basicamente funciona com TRUE OU FALSE (ele nao retorna isso , mas é como o modo de trabalho dele )
#filter retorna um interator
#lembrando que para fazer mais modificaçoes com lambda fica um pouco limitado

from dados import produtos , pessoas , lista 


nova_lista = filter(lambda x: x>5, lista)   #usando filter

#nova_lista = [x for x in lista if x >5]     tambem daria certo usando list comprehension


print(list(nova_lista))      #converti para lista para ver o que ocorreu

print('--------------------------DIFICULTANDO UM POUCO MAIS-----------------------------------------')

nova_lista1 = filter(lambda y: y['preco']>50 , produtos)


for produto in nova_lista1:
    print(produto)



print('---------------------------------------------------------------------------------------------')

def filtra(g):
    if g['preco'] > 60:
        return True
    else:
        return False

nova_lista2 = filter(filtra,produtos)

for c in nova_lista2:
    print(c)

print('----------------------------USANDO FILTER COMO MAP---------------------------------------------------')


def filtra1(g1):
    if g1['preco'] > 60:
        g1['nova_chave']= g1['preco']
    return True


nova_lista3 = filter(filtra1,produtos)

for c1 in nova_lista3:
    print(c1)


print('---------------------------CHECANDO QUEM É MENOR DE IDADE------------------------------------------------------------')

def filtra2(g2):
    if g2['idade']<18:
        return True


nova_lista4 = filter(filtra2,pessoas)

for pessoa in nova_lista4:
    print(pessoa)