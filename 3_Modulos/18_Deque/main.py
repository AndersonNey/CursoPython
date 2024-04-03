
"""
Pilhas e filas

Pilha (stack) - LIFO - last in , first out.
    Exemplo: Pilha de livros que sao adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo> Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item 
alterado, todos os indices serao modificados.

"""


#LIFO

livros = list()
livros.append('Livro 1')  #1
livros.append('Livro 2')  #2
livros.append('Livro 3')  #3
livros.append('Livro 4')  #4
livros.append('Livro 5')  #5
livro_removido = livros.pop() #5
livro_removido = livros.pop() #4
livro_removido = livros.pop() #3
livro_removido = livros.pop() #2
livro_removido = livros.pop() #1

#FIFO
#quando voce exclui o primeiro valor todos os outros teram que troca o valor de seu indice mais ou menos isso.
#uma alternativa para nao ter perca de desempenho é usar o deque é tipo uma lista normal

from collections  import deque
from time import sleep


fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Luiz Otavio')
fila.append('Marcos')
fila.append('Jose')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')


#quando eu adiciono mais um elemento do que é alem do permitido , esse elemento entra e o primeiro sai
fila1 = deque(maxlen=5)  #o maximo de elementos dentro da lista

fila1.extend([1,2,3,4])
fila1.append(5)
fila1.append(6)
print(fila1)

for i in range(30):
    fila1.append(i)
    sleep(0.01)
    print(fila1)


#COMANDOS DO DEQUE

# Append adiciona um item so a direita
# Append adiciona um item so a esquerda
# Pop left vai remover o primeiro elemneto da lista
# Pop remove o ultimo elemento
# insert vai inserir em um determindo indice

fila_exemplo1=deque()
fila_exemplo1.extend([1,2,3,4,5,6])
fila_exemplo1.insert(2, 'Nome qualquer')
print(fila_exemplo1)

# extendleft inserindo apartir da esquerda da fila
# extend inserindo apartir da direita da fila
# remove o elemento da fila
# index retorna o indice em que o elemento esta podemos colocar um ponto de partida e um ponto final
# count conta quantas vezes um elemento apareceu na lista
# clear remove tudo da lista
# maxlen ------> parametro para falar o tamanho maximo que a fila pode ter
# reverse inverte a fila
# rotate  recebe a quantidade que eu passar e com essa quantidade pega a quantidade de item na parte de tras da lista e coloca na frente                           

