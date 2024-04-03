#criar uma tupla

t0 = ()
print(t0)

tupla_de_unico_valor = (1,)  #se nao tivesse essa virgula no final seria um inteiro
print(tupla_de_unico_valor)

t1 = (1,2,4,'aviao')
print(t1)

t2  = 22,445,'carro' # para criar uma tupla sem os parenteses
print(t2)

t3  = 2,  #para criar uma tupla sem os parenteses com um  unico item
print(3)

t4 = t1 +t2 # concatenando tuplas
print(t4)

#desempacotando tuplas

n1 ,n2 ,n3 ,n4 = t1
print(n2)

m1,*m2=t1  #o resto vira uma lista
print(m2)

#convertendo tupla

t1 =list(t1)# passando para lista
print(t1)
t1 = tuple(t1)# passando para tupla devolta
print(t1)