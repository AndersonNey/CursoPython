print('-------------------------------------ADD------------------------------------------------------------------')
# nao aceita adicionar lista

conjunto1 = {1,2,3,4,5,6}

conjunto1.add('carro')
conjunto1.add('melancia')
print(conjunto1)


print('-------------------------------------CLEAR------------------------------------------------------------------')

conjunto2 = {1,2,3,4,5,6}

conjunto2.clear()
print(conjunto2)


print('-------------------------------------COPY------------------------------------------------------------------')
#acho que tem aquele mesmo problema de criar um tipo de atalho
conjunto3 = {1,2,3,4,5,6}
c3x1= conjunto3.copy()
print(c3x1)


print('-------------------------------------DIFFERENCE------------------------------------------------------------------')
#O difference método remove os itens que existem em ambos os conjuntos.
#ordem importa
conjunto4 = {1,2,3,4,5,6}
conjunto5 = {4,5,6,7,8}

c4x1= conjunto4.difference(conjunto5) #retira os numeros que tambem tem em 5
c4x2= conjunto5.difference(conjunto4) #retira os numeros que tambem tem em 4
print(c4x1)
print(c4x2)

c4x3= conjunto4 - conjunto5  #outra maneira de fazer
c4x4= conjunto5 - conjunto4  #outra maneira de fazer
print(c4x3)
print(c4x4)

print('-------------------------------------DIFFERENCE UPDATE---------------------------------------------------------------')
#ordem importa
# Faz a mesma coisa que o de cima, a diferença é que o metodo DIFFERENCE retorna o valor em um novo conjunto, enquanto o DIFFERENCE_UPDATE
#retorna none porque ele ja aplica o novo conjunto no conjunto original, veja abaixo

#"O difference_update()método é diferente do difference()método, pois o difference() método retorna um novo conjunto , sem os itens
# indesejados, e o difference_update()método remove os itens indesejados do conjunto original."

conjunto6 = {1,2,3,4,5,6}
conjunto7 = {4,5,6,7,8}

c6x1 = conjunto6.difference_update(conjunto7)
print(c6x1)
print(conjunto6)
print(conjunto7)

print('-------------------------------------DISCARD---------------------------------------------------------------')
#O discard()método remove o item especificado do conjunto.

#Esse método é diferente do método remove() , porque o  método remove() gerará um erro se o item especificado não existir e o método discard() não .

conjunto8 = {1,2,3,4,5,6}

conjunto8.discard(2)  #remove o item especificicado
print(conjunto8)
conjunto8.discard(7) #tentando remover um item que nao existi ,  simplesmente nao acontece nd
print(conjunto8)

print('-----------------------------------INTERSECTION-------------------------------------------------------------')    #aceita varios parametros
#ordem nao importa
#Retorna um set que contém os itens que existem no conjunto9 e conjunto 10
#O intersection()método retorna um conjunto que contém a semelhança entre dois ou mais conjuntos.

#Significado: O conjunto retornado contém apenas itens que existem em ambos os conjuntos, ou em todos os conjuntos se a comparação for feita com mais de dois conjuntos.
#aceita outros paramentros na funcao ,ou seja, outros conjuntos

conjunto9 = {1,2,3,4,5,6}
conjunto10 = {4,5,6,7,8}
conjunto11 = {4,5}

c9x1 = conjunto9.intersection(conjunto10)
c9x2 = conjunto10.intersection(conjunto9)
print(c9x1)
print(c9x2)

c9x3 = conjunto9 & conjunto10  # outra maneira de se fazer
c9x4 = conjunto10 & conjunto9  # outra maneira de se fazer
print(c9x3)
print(c9x4)

c9x5 = conjunto9.intersection(conjunto10,conjunto11)
print(c9x5)

print('-----------------------------------INTERSECTION_UPDATE---------------------------------------------------')  #aceita varios parametros

# faz a mesma coisa que o de cima com a diferença de aplicar o novo conjunto no conjunto original , ao inves de numa variavel como ocorre no caso acima
#tambem aceita varios parametros na funcao
#a ordem importa no sentido que fica a escolha de qual conjunto original quer modificar para receber o novo

conjunto12 = {1,2,3,4,5,6}
conjunto13 = {4,5,6,7,8}
conjunto14 = {4,5}

conjunto12.intersection_update(conjunto13,conjunto14)
print(conjunto12) #aplicou o resultado no conjunto original

print('-----------------------------------ISDISJOINT---------------------------------------------------')

#O método isdisjoint() retorna True se nenhum dos itens estiver presente em ambos os conjuntos, caso contrário, retorna False.

#Retorna True se nenhum item em conjunto15 estiver presente no conjunto 16:
conjunto15 = {"apple", "banana", "cherry"}
conjunto16= {"google", "microsoft", "facebook"}

c15x1 = conjunto15.isdisjoint(conjunto16)
print(c15x1)

conjunto17 = {"apple", "banana", "cherry"}
conjunto18= {"apple", "google", "microsoft" }

c15x2 = conjunto17.isdisjoint(conjunto18)
print(c15x2)


print('-----------------------------------ISSUBSET---------------------------------------------------')   #muito parecido com a proxima funçao
#Suponha que você tenha dois conjuntos A e B. O conjunto A é um subconjunto do conjunto B se todos os elementos de A também
#são elementos de B. Então, o conjunto B é um superconjunto do conjunto A.

#O método issubset() retornará True se todos os itens do conjunto existirem no conjunto especificado, caso contrário, retornará False.

#Retorna True se todos os itens no conjunto19 estiverem presentes no conjunto20:

conjunto19 = {"a", "b", "c"}
conjunto20 = {"f", "e", "d", "c", "b", "a"}

c19x1 = conjunto19.issubset(conjunto20)
print(c19x1)

conjunto21 = {"a", "b", "c"}
conjunto22 = {"f", "e", "d", "c", "b"}

c19x2 = conjunto21.issubset(conjunto22)  # TODOS os items precisam estar presentes como 'a' nao esta ele retornou FALSE

print(c19x2)

print('-----------------------------------ISSUPERSET---------------------------------------------------')  #muito parecido com a funçao anterior

#Suponha que você tenha dois conjuntos: A e B. O conjunto A é um superconjunto do conjunto B se todos os elementos do conjunto B são elementos do conjunto A.

#Se o conjunto A é um superconjunto do conjunto B, então o conjunto B é um subconjunto do conjunto A. Para verificar se um conjunto é um
#subconjunto de outro, você usa o issubset()método. Em Python, você usa o issuperset()método set para verificar se um conjunto é um superconjunto de outro conjunto:


conjunto23 = {"f", "e", "d", "c", "b", "a"}
conjunto24 = {"a", "b", "c"}

c23x1 = conjunto23.issuperset(conjunto24)  # vai dar TRUE porque conjunto 23 é superconjunto de conjunto 24, ou seja , conjuto 24 é subconjunto de conjunto de 23

print(c23x1)

conjunto25 = {"f", "e", "d", "c", "b"}
conjunto26 = {"a", "b", "c"}

c23x2 = conjunto25.issuperset(conjunto26) # vai dar FALSE porque conjunto 25 nao é superconjunto de conjunto 26, ou seja , conjuto 26 nao é subconjunto de conjunto de 25
                                         # para conjunto 25 ser superconjunto ele precisaria ter o conjunto 26 dentro dele (mesmos valores de conjunto26)
print(c23x2)


print('-----------------------------------POP---------------------------------------------------')
#Remova um item aleatório do conjunto:
#nao aceita parametro
#retorna o item removido

conjunto27 = {"apple", "banana", "cherry"}

c27x1 = conjunto27.pop()

print(c27x1)
print(conjunto27)

print('-----------------------------------REMOVE---------------------------------------------------')
#O método remove() remove o elemento especificado do conjunto.
#Esse método é diferente do método discard(), porque o método remove()  gerará um erro se o item especificado não existir e o método discard() não .

conjunto28 = {"apple", "banana", "cherry"}
c28x1=conjunto28.remove("banana")  #tentei colocar o resultado dentro de uma variavel mais ele retorna NONE
conjunto28.remove("apple")
#conjunto28.remove("carro")     se eu tentasse rodar esse trecho ocorreria um erro porque esse valor nao existe para remover
print(c28x1)
print(conjunto28)

print('-----------------------------------SYMMETRIC_DIFFERENCE---------------------------------------------------')
#ordem nao importa
#exclui o items que existem em ambos e retorna o valor do novo conjunto

#O método symmetric_difference() retorna um conjunto que contém todos os itens de ambos os conjuntos, mas não os itens presentes em ambos os conjuntos.
#Significado: O conjunto retornado contém uma mistura de itens que não estão presentes em ambos os conjuntos.

conjunto29 = {"apple", "banana", "cherry"}
conjunto30 = {"google", "microsoft", "apple"}

c29x1 = conjunto29.symmetric_difference(conjunto30)

print(c29x1)

c30x1 =conjunto29 ^conjunto30  # outro metodo de fazer essa operaçao
print(c30x1)

print('------------------------------SYMMETRIC_DIFFERENCE_UPDATE---------------------------------------------------')
# faz a mesma coisa que o de cima com a diferença de aplicar o novo conjunto no conjunto original , ao inves de numa variavel como ocorre no caso acima
#a ordem importa no sentido que fica a escolha de qual conjunto original quer modificar para receber o novo

conjunto31 = {"apple", "banana", "cherry"}
conjunto32 = {"google", "microsoft", "apple"}

conjunto31.symmetric_difference_update(conjunto32)
print(conjunto31)

print('------------UNION-------------NAO PRECISA SER CONJUNTO (PRECISA SER QUALQUER OBJETO INTERAVEL)--------') #aceita varios parametros
#ordem nao importa
# unifica varios conjutos (LEMBRANDO QUE CONJUNTO NAO ACEITA VALORES REPITIDOS)
conjunto33 = {"apple", "banana", "cherry"}
conjunto34 = {"google", "microsoft", "apple"}

c33x1 = conjunto33.union(conjunto34)

c33x2 = conjunto33 | conjunto34  #outra maneira de fazer a mesma coisa
print(c33x1)
print(c33x2)

conjunto35 = {"a", "b", "c"}
conjunto36 = {"f", "d", "a"}
conjunto37 = {"c", "d", "e"}

c33x3 = conjunto35.union(conjunto36 ,conjunto37)

print(c33x3)


print('-----------------------------------------UPDATE-----------------------------------------------------------')
#a ordem importa no sentido que fica a escolha de qual conjunto original quer modificar para receber o novo  (ESSA FUNCAO É UM TIPO DE UNION_UPDATE
# PORQUE PRECISAR APLICAR O RESULTADO DENTRO DE UM DOS CONJUNTOS ORIGINAIS )
conjunto38 = {"apple", "banana", "cherry"}
conjunto39 = {"google", "microsoft", "apple"}

conjunto38.update(conjunto39)
print(conjunto38)