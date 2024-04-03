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
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     #0   <-indice
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],      #1   <-indice
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],      #2   <-indice
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],      #3   <-indice
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],     #4   <-indice
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],      #5   <-indice
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],   #6   <-indice
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],      #7   <-indice
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],     #8   <-indice
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],      #9   <-indice
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],      #10  <-indice
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],     #11  <-indice
]
def checagem(lista):
    print(f'Lista de indice {chave}')
    conjunto_lista = set(lista)
    dicionario_de_registro = {}
    cont = 0
    acompanha_indice = -1  # comecei com -1 porque a lista comeca do 0
    for x in conjunto_lista:   #interirando o conjunto sobre a lista
        for y in lista:# inteirando os valores  para conferir com os do conjunto
            acompanha_indice += 1
            if y == x:        # se o valor da lista for o mesmo do conjunto
                cont+=1
                if cont==2:
                    print(f'o valor {y} se repetiu pela segunda vez no indice {acompanha_indice}')
            dicionario_de_registro.update({y:cont})    #{numero: quantas vezes que ele aparece}
        cont=0  # resetando para o valor original
        acompanha_indice = -1  # resetando para o valor original


chave = 0
while chave<12:

    checagem(lista_de_listas_de_inteiros[chave])

    chave +=1