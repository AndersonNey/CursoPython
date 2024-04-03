"""
append , insert , pop , del , clear , extend
"""



lista = ["maça",10 ,"melancia",7.5]
lista[2] = "melao" #troca o valor do indice 2
print(lista[2]) # mostrar indice 2


print(lista[0:3:2])  #[onde começa , onde termina nesse caso vai ate o indice 2 , passo]


l1 = [1,2,3]
l2 = [4,5,6]
#posso soma de duas maneiras
l3 = l1+l2
#ou
l1.extend(l2) #e agora l1 alem de ter seu valor tambem tera a l2 somado ao seu
#somando apenas mais um item
l1.extend("A")
print(l1)

#Adiciona um item ao fim da lista

list1=[1,2,3,4,5]
list1.append("T")
print(list1)

# insere um determinado elemento em um determinado índice em uma lista , e empura os outros para frente

list2=[1,2,3,4,5,6]
list2.insert(0,"deu certo")
print(list2)

# exclui o ultimo elemento da lista se estiver "()" e exclui o selelecinado ex:(2)exclui no indice 2

list3=[1,2,3,4,5,6]
list3.pop(2)
print(list3)

#exclui os elementos selecionados

list4 = [1,2,3,4,5,6,7,8]
del(list4[2:6])
print(list4)

#pegar valor maximo e valor minimo

list5=[1,2,3,4,5,6,7,8,9]
print(max(list5))
print(min(list5))

#range com lista

lista6 = list(range(1,10))
print(lista6)

#range com lista

list7 = [0,1,2,3,4,5,6,7,8,9]
soma=0
for valor in list7: #somando todos os valores
    soma=soma+valor
print(soma)

#Desempacotando uma lista

lista_teste=['joao','miguel','julio']

n1,n2,n3 = lista_teste  # pode perceber que o numero de variaveis é da exata quantidade de valores que tem na lista
print(n1,n2,n3)

#lista_teste=['joao','miguel','julio']   #o exemplo abaixo daria erro porque a quantidade de varivaveis nao condis com o que tem dentro daa lista
#n1,n2 = lista_teste
#print(n1,n2)
                  #para resolver essse tipo dde problema segue o exemplo abaixo

lista_teste=['joao','miguel','julio','kaio','fernanda',1,2,3,4,5,6]

n1,*restante = lista_teste
print(n1,restante)

lista_teste=['joao','miguel','julio','kaio','fernanda',1,2,3,4,5,6]    #retirando os valores da variavel restante

n1,*restante = lista_teste
print(n1,*restante)

lista_teste=['joao','miguel','julio','kaio','fernanda',1,2,3,4,5,6]    #pegando a ultimo valor da lista

n1,*restante,pegando_ultimo_valor = lista_teste
print(n1,restante,pegando_ultimo_valor)

