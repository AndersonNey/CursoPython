"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)

            Se não encontrar duplicados na lista, retorne -1
"""
#           0  1  2  3  4  5  6  7  8  9
my_lista = [9, 1, 8, 9, 9, 7, 2, 1, 6, 8]
conjunto_lista = set(my_lista)
dicionario_de_registro = {}
cont = 0
acompanha_indice = -1  # comecei com -1 porque a lista comeca do 0
for x in conjunto_lista:   #interirando o conjunto sobre a lista
    for y in my_lista:# inteirando os valores  para conferir com os do conjunto
        acompanha_indice += 1
        if y == x:        # se o valor da lista for o mesmo do conjunto
            cont+=1
            if cont==2:
                print(f'o valor {y} se repetiu pela segunda vez no indice {acompanha_indice}')
            dicionario_de_registro.update({y:cont})    #{numero: quantas vezes que ele aparece}
    cont=0  # resetando para o valor original
    acompanha_indice = -1  # resetando para o valor original


print(dicionario_de_registro)
