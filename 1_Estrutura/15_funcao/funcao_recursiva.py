numeros = (1,2,(3,4,5,(6,(7,8),9),10))



def descop(lista):
    lista_final = []
    for i in lista:
        if isinstance(i,tuple):
            x = descop(i)
            lista_final.append(x)
        else:
            lista_final.append(i)

    return lista_final

print(descop(numeros))







