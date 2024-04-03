"""
zip - unindo interaveis 
zip_longest - intertools
"""
# zip pode ser convertido para lista e dicionario
#zip_longest vai prencher ate a maior lista com o valor definido (padrao None)


from itertools import zip_longest , count   # tem que usar para poder usar o zip_longest  a funçao count é um INTERADOR infinito começando do 0 , e é usado no exemplo 5


print('-----------------------EXEMPLO1----------------------------')

cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

#zip vai unir ate a menor lista

var = zip(cidades, estados)   #irar gerar um INTERADOR  <zip object at 0x00000285EAC47580>
print(var)    # lembrando que nao da para ver o INTERADOR direto , para isso converta em lista



for x in var:
    print(x[0],x[1])

lista1 = list(var)  # os valores nao puderam entrar para lista por que ja tinha se esgotado do INTERADOR 
print(lista1)


print('-----------------------EXEMPLO2----------------------------')

cidades2 = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados2 = ['SP', 'MG', 'BA']

var2=zip(cidades2,estados2,cidades2) # ou seja aceita outro parametros
print(list(var2))


print('-----------------------EXEMPLO3----------------------------')

cidades3 = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados3 = ['SP', 'MG', 'BA']

var3=zip_longest(cidades3,estados3)    #perceba que o ultimo valor ficou  com o valor None
print(list(var3))                      # [('Sao Paulo', 'SP'), ('Belo Horizonte', 'MG'), ('Salvador', 'BA'), ('Monte Belo', None)]


print('---------EXEMPLO4--------TROCANDO O VALOR PADRAO--------------------')

cidades4 = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo','outra cidade']
estados4 = ['SP', 'MG', 'BA']

var4=zip_longest(cidades4,estados4 , fillvalue='CIDADE') #trocando o valor padrao de None para Cidade 
print(list(var4))                      

#lembrando que o zip_longest tem que importa do modulo itertools :
#tem duas maneiras de fazer

#importando dessa maneira 
#                          from itertools import zip_longest
# e usando                           zip_longest()
#ou
#                           from itertools
#e usando                            itertools.zip_longest()


print('-----------------------EXEMPLO5--------------------------------')

cidades5 = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo','outra cidade']
estados5 = ['SP', 'MG', 'BA']
indice =count()

var5=zip(indice ,cidades5,estados5) # se eu usa o zip_longest nao tem fim porque o cont sempre ficaria mandando numero e o zip_longest ficaria colocando None

for valor in var5:   
    print(valor)

#for x , y , z in var5:     teria como desempacotar esses resultados tbm 
#    print( x , y , z )


print('---------------EXEMPLO6------OBSERVACAO DA FUNCAO ZIP----------------')

cidades6 = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados6 = ['SP', 'MG', 'BA']

#zip vai unir ate a menor lista

var6 = zip(cidades6, estados6, strict=True)   #irar gerar um INTERADOR  <zip object at 0x00000285EAC47580>   A opçao strict gerar um erro se os valores se esgotou , ou seja, basicamente
                                              #                                                            informa que uma lista tem tamanho diferente da outra
print(var6)    # lembrando que nao da para ver o INTERADOR direto , para isso converta em lista



#for x in var6:          lembrando que nao tem como fazer for usando strict
#    print(x[0],x[1])