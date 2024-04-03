import sys    #utilizando essa biblioteca so para ver o quanto de memoria esta sendo ultilizado no exemplo la embaixo
import time   # usar em um exemplo abaixo

#geradores podem ser convertidos em lista

#Para saber se o objeto é interavel, pergunta se ela tem o metodo __iter__, se TRUE é um objeto interavel se FALSE nao é um objeto interavel
print('a lista é um interavel')

lista = [0,1,2,3,4,5]
print(hasattr(lista,'__iter__'))

print('outro exemplo: numeros nao sao interaveis')

numeros = 12345
print(hasattr(numeros,'__iter__'))

print('outro exemplo: string sao interaveis')

string = 'carro'
print(hasattr(string,'__iter__'))


for x in string:  # o for transforma a lista em um interador e fica pedindo cada item seguinte (e trata para chegar ate o ultimo item sem ocorre erro)
    print(x)





print('Para saber se o objeto é interador pergunta se ela tem o metodo __next__, se TRUE é um objeto interador se FALSE nao é um objeto interador')


lista1 = [0,1,2,3,4,5]
print(hasattr(lista,'__next__'))  #false

#print(next(lista1))    esse trecho de codigo daria erro porque a lista nao é interador para nao ocorrer isso segue abaixo

lista1 = iter(lista)
print(next(lista1))   #0
print(next(lista1))   #1
print(next(lista1))   #2
print(next(lista1))   #3
print(next(lista1))   #4
print(next(lista1))   #5
#print(next(lista1))   nesse ultimo o python retorna StopInteration (Isso porque nao tem mais item para repassar)

# um interavel é um objeto que voce pode interar sobre ele , mas ele nao é necessariamente um interador ,
#ele nao necessariamente vai te dar um valor de cada vez

#um interador vai te dar um valor de cada vez quando vc precisar desse valor

print('Geradores')

# o gerador geralmente sao usados quando a gente precisa de usar valores que vao usar muita memoria
#(antes de salvar na memoria definitiva passa pela memoria ram, por isso tem risco de cracha) --> eu acho

lista2= list(range(10))  # 0 - 9      # como ela recebe os valores e guarda tudo isso ocupa muito espaço
print(sys.getsizeof(lista2))       # quantidade de memoria que essa lista esta consumindo em BYTES

#os geradores vao entregar o proximo valor conforme vc requisita

#esse aqui nao é um gerador ainda
def gera():
    r=[]
    for n in range(100):
        r.append(n)
        time.sleep(0.001)  #esse time ta aqui para simular uma operacao pesada no computador
    return r

g = gera()  # recebendo o return

for v in g:   #interando sobre a lista
    print(v)

#esse aqui é um gerador

def gerador():
    for t in range(100):
        yield t
        time.sleep(0.001)  #esse time ta aqui para simular uma operacao pesada no computador

ger = gerador()  # recebendo o return

for u in ger:   #interando sobre a lista
    print(u)


ger1 =gerador()  # recebendo o return

print(next(ger1))
print(next(ger1))
print(next(ger1))
print(next(ger1))

print(hasattr(ger,'__iter__')) #conferindo se ele é um interavel e deu TRUE
print(hasattr(ger,'__next__')) #conferindo se ele é um interador e deu TRUE

# basicamente a diferença é que no primeiro tem que fazer a lista toda e depois interar sobre ela e quanto no
# gerador ele ja te entregar o valor assim que é pedido

print('---------------------------------------------------------------------------------------------------------------')
print('outro exemplo:')

def gerar():
    variavel = 'valor1'
    yield variavel
    variavel = 'valor2'
    yield variavel
    variavel = 'valor3'
    yield variavel

receb= gerar()

print(next(receb))
print(next(receb))
print(next(receb))

print('---------------------------------------------------------------------------------------------------------------')
def gerar1():
    variavel = 'valor1'
    yield variavel
    variavel = 'valor2'
    yield variavel
    variavel = 'valor3'
    yield variavel

receb1= gerar1()

for k in receb1:
    print(k)


print('-----------------------------------OUTRA MANEIRA DE CRIAR UM GERADOR-------------------------------------------')

l1=[x for x in range(1000)]   # A FUNCAO RANGE É UM INTERAVEL MAS NAO É UM INTERADOR
print(type(l1))
l2=(x for x in range(1000))  #ISSO AQUI NA VERDADE É UM GERADOR  deixei l2 so para seguir a aula
print(type(l2))


l3=[x for x in range(1000)]
l4=(x for x in range(1000))  #ISSO AQUI NA VERDADE É UM GERADOR  deixei l4 so para seguir a aula


print(sys.getsizeof(l3))   #resulta em tamanhos diferentes
print(sys.getsizeof(l4))   #resulta em tamanhos diferentes

variavel = ((x,y) for x,y in zip('alo','alo'))     #tipo geredor comprehension
print(next(variavel))

#as listas vão  reter todos os valores que você mandar nela e salvar na memória .
#Os geradores vão reter todos os valores normal porém eles não vai salvar todos os valores na memória
#ele só vai te entregar um valor qualquer quando você pedir por esse valor e a gente pede esse valor
#utilizando a função next.