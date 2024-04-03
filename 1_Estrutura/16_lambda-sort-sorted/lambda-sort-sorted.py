#-----------------------------EXEMPLO 1------------------------------------------------------------------


#em funcao tradicional+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def funcao_soma(arg,arg2):
    return arg*arg2

var = funcao_soma(2,2)
print(var)

#em funcao lambda++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = lambda x , y : x * y

print(a(2,2))


#-----------------------------EXEMPLO 2------------------------------------------------------------------



#em funcao tradicional+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lista_produtos = [
    ['P1',13],
    ['P2', 6],
    ['P3', 7],
    ['P4',50],
    ['P5', 8]

]


def func(item):# ordenar a lista por categoria
    return item[1]  # ordenara a lista com o criterio do indice 1 eu acho

lista_produtos.sort(key=func)
print(lista_produtos)

#em funcao lambda++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

lista_produtos2 = [
    ['P1',13],
    ['P2', 6],
    ['P3', 7],
    ['P4',50],
    ['P5', 8]

]


lista_produtos2.sort(key = lambda  item : item[1])  # ordenar a lista por categoria
#print(sorted(lista_produtos2, key =lambda i : i[1])) #outra maneira tbm

print(lista_produtos2)