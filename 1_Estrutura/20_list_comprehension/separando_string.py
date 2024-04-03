
string  = '012345678901234567890123456789012345678901234567890123456789'
n = 10    #tamanho que eu quero separar
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i,i+n) for i in range(0, len(string),n)]
lista = [string[i:i+n] for i in range (0,len(string),n)]   # a soluçao em si ta somente aqui o resto é explicaçao
raw = [f'string[{i}:{i+n}]' for i in range(0, len(string),n)]
retorno = '.'.join(lista)
print(contadores)
print(tuplas)
print('-'*100)
print(lista)
print('-'*100)
print(raw)
print(retorno)

palavra  = '012345678901234567890123456789012345678901234567890123456789'
nova_lista=[]
m =10

for i in range(0,len(palavra),m):  # vai executar 6 vezes porque começa no 0 vai pulando de 10 em 10 ate chegar no maximo que no caso é do tamanho da string 60 caracteres
    nova_lista.append((i,i+m))    #quem vai incrementar o i sera o proprio for
    print(nova_lista)             #na primeira execuçao i vale 0     e i+10=10        (0,10)
                                  #na segunda execuçao i vale 10     e i+10=20        (10,20)
                                  #na terceira execuçao i vale 20    e i+10=30        (20,30)
                                  #...
