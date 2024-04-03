print('--------------------------------EXEMPLO 1--------------------------------------------------------------------------')

def funcao():
    print('ola, bom dia')

funcao()

print('--------------------------------EXEMPLO 2 COM ARGUMENTO------------------------------------------------------------')

def funcao(msg):
    print(msg)

funcao("mensagem")

print('--------------------------------EXEMPLO 3 COM VARIOS ARGUMENTOS----------------------------------------------------')

def funcao(msg,nome):
    print(msg,nome)

funcao("mensagem","Joao")

print('--------------------------------EXEMPLO 4 COM VALORES PADROES------------------------------------------------------')

def funcao(msg='ola',nome='lucy'):
    print(msg,nome)

funcao()             #com valores padroes
funcao('oi','joao')  #com valores alterados
funcao('oiiiii')     #com 1 parametro modificado e o segundo padrao
funcao(nome='maria') #com 2 parametro modificado e o primeiro padrao
funcao(msg='olha',nome='so')  # - - -mesma coisa <-=
funcao(nome='so',msg='olha')  # - - -mesma coisa <-=

print('--------------------------------EXEMPLO 5 RETORNANDO NADA-----------------------------------------------------------')

def funcao(nome='teresa',numero=2):     #nao retornara nada
    pass                            #mesmo tendo valores em  variaveis nao retorna nada

variavel =  funcao()
print(variavel)

print('--------------------------------EXEMPLO 6 RETORNANDO --------------------------------------------------------------')

def funcao(nome='teresa',numero=2):     #nao retornara nada
    return                         #mesmo tendo valores em  variaveis nao retorna nada

variavel =  funcao()
print(variavel)

print('--------------------------------EXEMPLO 7 RETORNANDO COM VALORES---------------------------------------------------')

def funcao(nome='teresa',numero=2):
    return nome,numero

variavel =  funcao()
print(variavel)

print('--------------------------------EXEMPLO 8 RETORNANDO COM VALORES---------------------------------------------------')

def funcao(nome='teresa',numero=2):
    return f'{nome},{numero}'              #retornando sem parenteses e aspas

variavel =  funcao()
print(variavel)

print("--------------------------------EXEMPLO 9 ASSIM QUE O 'RETURN' FOR ENCONTRADO NADA ABAIXO SERA EXECUTADO-----------")

def funcao(nome='teresa',numero=2):
    print("testando esse ponto")
    return nome,numero
    print("testando esse ponto")

variavel =  funcao()
print(variavel)

print("--------------------------------EXEMPLO 10 DIVISAO DE NUMEROS -----------------------------------------------------")

def divisao(n1,n2):
    return n1/n2

divide =divisao(8,2)
print(divide)

print("--------------------------------EXEMPLO 11 DIVISAO DE NUMEROS (CASO O USUARIO INSIRA UM NUMERO O) -----------------")

def divisao(n1,n2):
    if n2>0:     #se n2 maior que 0 executa o que ta dentro do if
        return n1/n2

divide =divisao(8,0)
if divide:
    print(divide)
else:
    print("conta invalida")

print("--------------------------------EXEMPLO 12 DIVISAO DE NUMEROS (CASO O USUARIO INSIRA UM NUMERO 0)(OUTRA MANEIRA DE CHECAR)")

def divisao(n1,n2):
    if n2==0:    #se n2 igual a 0  nao executa o que ta dentro do if  e pula para o proximo comando que no caso return n1/n2
        return
    return n1/n2

divide =divisao(8,0)
if divide:
    print(divide)
else:
    print("conta invalida")

print("--------------------------------EXEMPLO 13 UMA FUNCAO PASSANDO UM VALOR DE OUTRA FUNCAO PARA VARIVEL")

def carro(valor1):  #o que ocorreu foi que transferi() so serviu para 'copiar' a funcao carro e passar para valor1
    print(valor1)   #ou seja tem duas funcoes que fazem  mesma coisa so que com nomes diferente  mais ou menos isso

def transferi():
    return carro

valor1=transferi()

valor1('agora valor1 e capaz de fazer a mesma coisa que carro')
print(valor1)

print(id(valor1),id(carro))

print("--------------------------------EXEMPLO 13.1 MANEIRA MAIS SIMPLIFICADA-----------------------------")

def moto(seu_valor):
    print(seu_valor)

def transfere_fucao():
    return moto

variavel_nova = transfere_fucao()     #variavel_nova == moto

variavel_nova('variavel_nova e capaz de fazer a mesma coisa que moto') #ou seja exibir o que e escrito
print(variavel_nova)

print(id(variavel_nova),id(moto))

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("--------------------------------EXEMPLO 14 NOMEANDO ARGUMENTOS------------------------------------")
def func (a1,a2,a3,a4,a5,nome=None):    #APARTIR DO MOMENTO QUE EU DOU VALOR A ALGUM ARGUMENTO ,COMO NESSE CASO 'nome' os argumentos seguintes
    print(a1,a2,a3,a4,a5,nome)          #VAO OBRIGATORIAMENTE PRECISAR RECEBER ALGUM VALOR

func(1,2,3,4,5,nome='luiz')

#def func (a1,a2,a3,a4,a5,nome=None,a6):    NESSE CASO O PYCHARM DARIA ERRO PORQUE O ARGUMENTO 'a6' NAO RECEBEU UM VALOR
#    print(a1,a2,a3,a4,a5,nome,a6)

#func(1,2,3,4,5,nome='luiz',6)


def func (a1,a2,a3,a4,a5,nome=None):    #observe que a funçao return retorna mais de dois valores dentro de uma tupla
    print(a1,a2,a3,a4,a5,nome)
    return a2,a4
respost=func(1,2,3,4,5,nome='luiz')
print(respost)

print("---------------------------EXEMPLO 15 QUANTIDADE DE ARGUMENTOS INDEFINIDA------------------------")

                   # nao precisa ser necessariamente a palavra 'args',mas a comunidade python uso como convensao
def func (*args):
    print(args)      #vendo todos os argumentos acima
    print(args[0])   #vendo o primeiro valor
    print(args[-1])  #vendo o ultimo valor
    print(len(args)) #vendo a quantidade de argumentos na funçao
func(1,2,3,4,5)

print("---------------------------EXEMPLO 16 listas e tuplas -------------------------------------------")

def func1 (*args):
    print(args)

lista = [1,2,3,4,5]

func1(lista,6,7,8,9)

print("---------------------------EXEMPLO 16.1 listas e tuplas -----------------------------------------")

def func1 (*args):       #a diferença nesse exemplo e que agora a lista esta desempacotada dentro da tupla
    print(args)

lista = [1,2,3,4,5]

func1(*lista,6,7,8,9)

print("---------------------------EXEMPLO 17 -----------------------------------------------------------")

def func1 (*args,**kwargs):  #basicamente args é para colocar uma quantidade de valores indefinidos dentro dos argumentos, que NAO POSSUEM VALORES PADROES
    print(args)              #basicamente kwargs é para colocar uma quantidade de valores indefinidos dentro dos argumentos, que JA POSSUEM VALORES PADROES
    print(kwargs)            #e KWARGS sao colocados dentro de dicionarios

lista = [1,2,3,4,5]

func1(*lista,6,7,8,9,nome='joazinho',nome1='luzinha')

#def func1 (*args):         Codigo abaixo apreseta erro porque nao consegue colocar valores tipo Kwargs dentro de args
#    print(args)

#lista = [1,2,3,4,5]

#func1(*lista,6,7,8,9,nome='joazinho',nome1='luzinha')


print("---------------------------EXEMPLO 18 CHECANDO VALOR DENTRO DO  KWARGS -------------------------")

def func1 (*args,**kwargs):
    print(kwargs)
    idade = kwargs.get('idade')
    print(idade)
    nome = kwargs.get('nome')
    print(nome)

    if idade is not None:    #outra maneira de checar sem  que de erro por  que  valor nao existe
        print(idade)
    else:
        print('valor nao existe')
    if nome is not None:
        print(nome)
    else:
        print('valor nao existe')


#    idade = kwargs['idade']  se eu por acaso fissese assim e idade nao existir vai dar um erro
#    print(idade)

lista = [1,2,3,4,5]
func1(*lista,6,7,8,9,nome='joaozinho',nome1='luzinha')



print("---------------------------EXEMPLO 19 VARIAVEIS GLOBAIS E LOCAIS ------------------------")

variavel123 = "valor"

def fun():                    #perceba que sendo  uma varivael global a funçao teve acesso
    print(variavel123)

fun()

print("---------------------------EXEMPLO 20 VARIAVEIS GLOBAIS E LOCAIS ------------------------")

variavel456 = "valor"

def fun():
    print(variavel456)

def fun2():              #apesar de ter os mesmos nomes a de cima é uma variavel global e a de baixo local
    variavel456 ="agora tem outro valor"  #essa variavel foi criada dentro do escopo local ,ou seja, dentro da funcao
    print(variavel456)

fun()
fun2()

print("---------------------------EXEMPLO 21 VARIAVEIS GLOBAIS E LOCAIS ------------------------")

variavel789 = "valor"

def fun():
    print(variavel789)

def fun2():
    variavel789 ="agora tem outro valor"
    print(variavel789)

fun()
fun2()
print(variavel789)   #perceba que pegou o valor da variavel global

print("---------------------------EXEMPLO 22 VARIAVEIS GLOBAIS E LOCAIS ------------------------")

variavel789 = "valor"

def fun():
    print(variavel789)

def fun2():
    variavel789 ="agora tem outro valor"
    print(variavel789)

fun()
fun2()
print(variavel789)   #perceba que pegou o valor da variavel global


print("---------------------------EXEMPLO 23 VARIAVEIS GLOBAIS E LOCAIS ------------------------")
                #nesse caso nao é uma boa pratica de programacao usa o comando 'global'
variavel111 = "valor"

def fun():
    print(variavel111)

def fun2():
    global variavel111
    variavel111 = "agora tem outro valor"
    print(variavel111)

fun()
fun2()
print(variavel111)   #perceba que pegou o valor da variavel que estava dentro da funcao

print("---------------------------EXEMPLO 23 VARIAVEIS GLOBAIS E LOCAIS ------------------------")
                #fazendo da maneira correta para nao fazer igual la  em cima
variavel222 = "valor"

def fun():
    print(variavel222)

def fun2(arg=None):
    arg = arg.replace('v','c')
    return arg
fun()
outra_variavel=fun2(arg=variavel222)
print(outra_variavel)

print("---------------------------EXEMPLO 24 VARIAVEIS GLOBAIS E LOCAIS ------------------------")

#n1 = "valor"          nesse caso da erro porque se vc tentar mostra o valor da variavel global depois tentar altera o valor
#                      e e querer mostra agora o novo valor da variavel ira gerar erro por que a variavel foi referenciada
#def funcao():         antes de ser criada                                                                         ^
#    print(n1) ----------------------------------------------------------------------------------------------------|
#    n1  = "novo valor"       ou seja como se tivesse considerando somente a variavel criada nessa linha
#    print(n1)                ou seja nao adianta tentar mesclar os valores das variaveis

#funcao()

print("+++++++++++++++++++++++++++++++++++ZONA DE TESTE++++++++++++++++++++++++++++++++++++++++")





