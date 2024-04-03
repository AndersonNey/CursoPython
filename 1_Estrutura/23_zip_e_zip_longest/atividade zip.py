
from itertools import zip_longest

#professor (estilo para funcionar em qualquer linguagem)
lista01 = [1 ,2 , 3, 4 ,5, 6 , 6]
lista02 = [1 ,2 , 3, 4 ]
lista_resul = []
for i in range(len(lista02)):
    lista_resul.append(lista01[i]+lista02[i])
print(lista_resul)

#minha 
lista1 = [1 ,2 , 3, 4 ,5, 6 , 6]
lista2 = [1 ,2 , 3, 4 ]
lista_resultados = []
juncao = zip(lista1,lista2)
for x ,y in juncao:
    lista_resultados.append(x+y)

print(lista_resultados)

#professor
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)  # Saída: [22, 4, 6, 10, 55]


#professor outra maneira

lista_a1 = [10, 2, 3, 4, 5]
lista_b1 = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a1, lista_b1, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]