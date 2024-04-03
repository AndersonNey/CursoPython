#basicamnete map pega uma funçao e executa essa funcao em cada interaçao 
#no exemplo dos dicionarios supondo que ira modifica so uma coluna ele executa a funçao sobre o item informado modificando seu valor e 
#deixando o que nao foi informado do jeito que tava.
#map retorna um interator

from dados import produtos , pessoas , lista                     # fiz assim porque os arquivos estao no mesmo lugar
#lembrando que para fazer mais modificaçoes com lambda fica um pouco limitado

print(lista)

nova_lista = map(lambda x: x*2 , lista)  #map recebe uma funçao como primeiro argumento , e um interavel como segundo
print(nova_lista)                        # map nao retorna uma lista pronta, ela retorna um interador
print(list(nova_lista))                  #para conseguir ver a lista 

nova_lista1 = [x1*2  for x1 in lista]    # fazendo a mesma coisa usando list comprehension
print(nova_lista1)


print('--------------------------TRABALHANDO COM OS DICIONARIOS-----------------------------------------')


for produto in produtos:  # vendo o dicionario organizado
    print(produto)

#acrecentar 5% em todos os produtos usando map

def coletando_preco(w):    #é necessario pedir o w porque ele é o dado inteiro da interaçao que ele esta 
    return w['preco']   # W assumira o como se fosse o nome do dicionario na linha que ele esta 


#precos = map(lambda w : w['preco'],produtos)   tambem daria certo usando funçao lambda

precos = map(coletando_preco , produtos)

for preco in precos:
    print(preco)


print('--------------MODIFICANDO SOMENTE UMA PARTE DO DICIONARIO (SEM ALTERAR O RESTANTE)-----------------')


def modificando_somente_o_valor(t):  # no caso ta 'importando' a linha do dicionario inteira, mas a funçao somente esta alterando [preco] pelo novo valor
    t['preco'] = round(t['preco']*1.05, 2) #arredondando para no maximo 2 casas decimais 
    return t

nova_lista2 = map(modificando_somente_o_valor, produtos)


for q in nova_lista2:
    print(q)


print('--------------------------TRABALHANDO COM A TABELA DE PESSOAS-----------------------------------------')

for pessoa in pessoas:  # vendo a lista de pessoas mais organizado
    print(pessoa)

def extraindo_nome(s):
    return s['nome']


#lista_com_nomes = map(lambda s: s['nome'],pessoas)     Assim tambem da certo

lista_com_nomes = map(extraindo_nome,pessoas)

for e in lista_com_nomes:
    print(e)

print('--------------------------CRIANDO NOVA CHAVE-----------------------------------------')


for pessoa1 in pessoas:  # vendo a lista de pessoas mais organizado
    print(pessoa1)

def nova_chave(s):
    s['idade_modificada']= s['idade']*2
    return s


novas_idades = map(nova_chave,pessoas)

for u in novas_idades:
    print(u)