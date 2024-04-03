#se cria semelhante aos dicionarios e so aceita valores imutaveis , numero , string , tuplas
# sets = conjuntos
# sets nao tem par de chaves e valores->como nos dicionarios
# nao existe indice, mas tem como interar
# se tentar criar um set vazio tipo s1 = {}  ,nao irar criar set , mas sim um dicionario
# lembrando que ele nao exibi organizado

#update é similar a add , porem a diferença é que update itera sobre o valor exemplo s1.update('python')
#>>>{'p','y','t','h','o','n'}
# enquanto add s1.add('python')
#>>>{'python'}

#sets nao aceitam elementos duplicados  , tem exemplo abaixo

s1 ={1,2,3,4,5}

for v in s1:
    print(v)

print('--------------------------------------------------------------------------------------------------------')

#para criar um set vazio

s2 = set()

#para adicionar valor dentro ou excluir

s2.add(2)
s2.add(4)
s2.add((1,2.4))
s2.add('carro')
print(s2)

s2.discard(4)
print(s2)

print('--------------------------------------------------------------------------------------------------------')


s3 = set()
s3.update([1,2,3,4,5],{5,6,7,8})  # nao aceita elementos duplicados ou seja so exibe o 5 apenas uma vez
print(s3)

print('--------------------------------------------------------------------------------------------------------')
#outra funçao legal para sets sobre uma lista

l1 = [1,1,1,1,2,3,3,3,5,5,5,5,5,5,5,5,5,5,5,7,'luiz','luiz','luiz','luiz',2.4,2.4,2.4]
print(l1)
l1 = set(l1) #filtrando repetiçoes ,transformando lista em conjunto
print(l1)

print('------------------------------------OPERACOES------------------------------------------------------------------')

s4={1,2,3,4,5,7}
s5={1,2,3,4,5,6}

s6 = s4 | s5   #uniao   |
print(s6) # concatenado ,mas sem repetir

s7 = s4 & s5  # intersection    &
print(s7) # concatenado ,mas sem repetir e tirando o valor que nao existe nos dois ao mesmo tempo

s8 = s4 - s5  # elemento que nao esteja nos dois sets mas que esteja apenas no elemento da esquerda
print(s8)     # ordem da operaçao importa

s9 = s5 -s4   # elemento que nao esteja nos dois sets mas que esteja apenas no elemento da esquerda
print(s9)      # ordem da operaçao importa

s10 = s4 ^ s5 # elementos que estao nos dois sets , mas nao em ambos
print(s10)    # nao importa a ordem da operaçao nesse

s11 = s5 ^ s4  #mesma coisa que o de cima a ordem nao importa
print(s11)

print('--------------------------------------------------------------------------------------------------------')
#outra utilidade

lista_1 = ['luiz','joao','maria']
lista_2 = ['joao','maria','maria','luiz','luiz','luiz','luiz','luiz','luiz','luiz','luiz','luiz']
print(lista_1)
print(lista_2)


print(lista_1 == lista_2)

lista_1 = set(lista_1)
lista_2 = set(lista_2)
print(lista_1)
print(lista_2)


print(lista_1 == lista_2)  # apesar de ta com nome de lista e em ordem baguçada sao iguais , AS LISTAS VIRARAM SETS (ESTAMOS FALANDO DE SETS)
                           # para listas serem iguais a ordem nao importa tbm
lista_4 = [1,2,4]
lista_5 = [1,4,2]
print(lista_4)
print(lista_5)

print(lista_1 == lista_2)