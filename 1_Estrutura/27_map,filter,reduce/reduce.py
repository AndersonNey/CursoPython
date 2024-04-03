
from dados import produtos , pessoas , lista 
from functools import reduce                  # é necessario importa essa funçao


print('--------------------------JEITO ANTIGO----------------------------------------------------')
acumula = 0

for item in lista:
    acumula += item

print(acumula)


print('--------------------------JEITO NOVO----------------------------------------------------')

#COM LISTA

def acumulador_outra_maneira(ac , i):
    return ac + i

soma_lista0  = reduce(acumulador_outra_maneira, lista , 0)
print(soma_lista0)


soma_lista = reduce(lambda ac, i : i+ac , lista , 0)                #recebe uma funçao como primeiro parametro , o segundo o interavel , o terceiro apartir da onde ira começar
print(soma_lista)

#COM DICIONARIO
#lembrando que para fazer mais modificaçoes com lambda fica um pouco limitado

soma_dicionario0 = reduce(lambda ac , i : i['preco']+ac , produtos , 0)  #lembrando que i assumi o valor da linha que ele esta interando
print(soma_dicionario0/len(produtos))

#COM DICIONARIO OUTRO EXEMPLO

soma_dicionario = reduce(lambda ac , i : i['idade']+ac , pessoas , 0)
print(soma_dicionario)
