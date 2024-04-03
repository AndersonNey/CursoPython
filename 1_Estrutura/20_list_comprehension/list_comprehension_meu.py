# IF ANTES DO FOR É UM OPERADOR TERNARIO E DEPOIS DO FOR É UM FILTRO  + ou -  isso
# FORS NA LIST COMPREHENSION SAO ANINHADOS , NAO SAO UM DENTRO DO OUTRO
lista1 = [1,2,3,4,5,6,7,8,9]

l1x1= [ x for x in lista1  if x > 8  ]
print(l1x1)



def somador(var1):#Dobrando o valor da variavel
    var1=var1+var1
    return var1

lista2 = [1,2,3,4,5,6,7,8,9]

l1x2= [ somador(x) for x in lista2 ]
print(l1x2)

print('--------------------------OUTRO_EXEMPLO-----------------------------')
linhas_e_colunas = [
    (x,y)
    for x in range(1,11)
    for y in range(1,6)
   # if x != 2           tirando os valores de x = 2

]
print(linhas_e_colunas)

print('--------------------------OUTRO_EXEMPLO1-----------------------------')

string = 'Otavio Miranda'
outra_string = [letra for letra in string]      #tipo o extend
nova_string = ''.join([letra for letra in string])  #tipo juntando o extend
print(outra_string)
print(nova_string)