#https://docs.python.org/2/library/datetime.html

from datetime import datetime ,timedelta


print('------------------EXEMPLO 1---------------------------')

data1 = datetime(2019,4,20,10,52,20)
print(data1)  #formato padrao americano
print(data1.strftime('%d/%m/%Y  %H:%M:%S'))         #formatando a data para o formato brasileiro atravez das diretivas

print('------------------EXEMPLO 2---------------------------')
#Criando um objeto data 

data2 =datetime.strptime('20/04/2019','%d/%m/%Y')      # (data recebida)(formato da data que esta sendo recebida)
print(data2)



print('------------------EXEMPLO 3---------------------------')
#timestamp  contagem de segundos desde 1/1/1970 ate a data que eu quero saber

data3 =datetime.strptime('20/04/2019','%d/%m/%Y')    
print(data3.timestamp())


print('------------------EXEMPLO 4---------------------------')
#fazer uma data pelo timestamp
#valor que eu escolhi : 1555729200.0

data4 =datetime.fromtimestamp(1555729200.0)
print(data4)

print('------------------EXEMPLO 5---------------------------')
#somando uma data com um tempo que eu desejar

data5 =datetime.strptime('20/04/1987 20:00:00' , '%d/%m/%Y %H:%M:%S')
data5 = data5 + timedelta(days=90,seconds=57, hours=2)

print(data5.strftime('%d/%m/%Y %H:%M:%S'))


print('------------------EXEMPLO 6---------------------------')
# fazendo a diferença de datas

data6 =datetime.strptime('20/04/1987 20:00:00' , '%d/%m/%Y %H:%M:%S')
data7 =datetime.strptime('25/04/1987 22:33:00' , '%d/%m/%Y %H:%M:%S')

dif = data6 - data7
dif2 = data7 -data6
print(dif)
print(dif2)

print(dif.days)
print(dif2.seconds)  #esse segundos se voce converte vai representar as horas (nao entedi muito bem) # acho que é apenas os segundos da diferenca das datas
print(dif2.total_seconds()) #os segundos totais da diferença

print('------------------EXEMPLO 7---------------------------')
#pegando os valores

data8 =datetime.strptime('20/04/1987 20:00:00' , '%d/%m/%Y %H:%M:%S')
data9 =datetime.strptime('25/04/1987 22:33:00' , '%d/%m/%Y %H:%M:%S')

print(data8.day)
print(data8.time())


print('------------------EXEMPLO 8---------------------------')
#comparando datas

data10 =datetime.strptime('20/04/1987 20:00:00' , '%d/%m/%Y %H:%M:%S')
data11 =datetime.strptime('25/04/1987 22:33:00' , '%d/%m/%Y %H:%M:%S')

print(data10 > data11)













