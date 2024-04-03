from time import time   #irar ser usado no UTILIDADE 
from time import sleep  #irar ser usado no UTILIDADE 

#as funçoes decoradoras envolvem a funçao para dar outras funçoes a ela


print('--------------------------BASICO 0--------------------------------------')
def fala_oi0():
    print('oi')

variavel0 = fala_oi0

print(type(variavel0))
print(type(fala_oi0))

print('--------------------------BASICO 1--------------------------------------')

def master1():
    def escrava():
        print('oi')

master1()      #nao faz simplismente nada 

print('--------------------------BASICO 2--------------------------------------')

def master2():
    def escrava():
        print('oi')
    escrava()

master2()      #agora ela faz algo

print('--------------------------BASICO 3--------------------------------------')

def master3():       
    def escrava():   
        print('oi')
    return escrava

variavel3 = master3()       # a funçao master esta retornano uma funçao, é parecido com o exemplo de basico 0
variavel3()

print(type(variavel3))


print('--------------------------INTERMEDIARIO 1--------------------------------------')


def master4(funçao):         # master esta recebendo uma funçao como parametro    
    def escrava():   
        funçao()
    return escrava

def fala_oi1():
    print('oi')

variavel4 = master4(fala_oi1)       # a funçao master esta retornano uma funçao, é parecido com o exemplo de basico 0
variavel4()


print('--------------------------INTERMEDIARIO 2--------------------------------------')


def master5(funçao):         # master esta recebendo uma funçao como parametro    
    def escrava():   
        funçao()
    return escrava

def fala_oi2():
    print('oi')

fala_oi2 = master5(fala_oi2)       
fala_oi2()                       #e como se eu tivesse executado fala_oi2 diretamente   # a funçao fala_oi2 foi decorada com a funçao master


print('--------------------------INTERMEDIARIO 3--------------------------------------')


def master6(funçao):         # master esta recebendo uma funçao como parametro    
    def escrava():   
        funçao()
    return escrava

def fala_oi3():
    print('oi')

#fala_oi3 = master6(fala_oi3)

fala_oi3()                        # a funçao fala_oi3 nao esta decorada com a funçao master

print('--------------------------INTERMEDIARIO 4--------------------------------------')


def master7(funçao):         
    def escrava():
        print('Agora estou decorada')   
        funçao()
    return escrava

def fala_oi4():
    print('oi')

fala_oi4 = master7(fala_oi4)        # a funçao fala_oi4 foi decorada com a funçao master e agora tem novos recursos
fala_oi4()  


print('--------------------------AVANÇADO 1--------------------------------------')

def master8(funçao):         
    def escrava():
        print('Agora estou decorada hehehe')   
        funçao()
    return escrava

@master8
def fala_oi5():          # a funçao fala_oi5 foi decorada com a funçao master e agora tem novos recursos
    print('oi')          # e usando @master8  excluir a nessecidade de usar --> fala_oi5 = master8(fala_oi5)   
                         # para repassar seu novo valor para a funçao  

fala_oi5()  

print('--------------------------AVANÇADO 2--------------------------------------')

# def master9(funçao):         
#     def escrava():
#         print('Agora estou decorada hehehe')   
#         funçao()
#     return escrava

# @master9
# def outra_funcao(msg):   #ocorre erro porque foi enviado um parametro dentro dessa funçao , SOLUÇAO NO CODIGO ABAIXO
#     print(msg)


# outra_funcao('ola,pessoal')

print('--------------------------AVANÇADO 3--------------------------------------')

def master10(funçao):         
    def escrava(*args,**kwargs):
        print('Agora estou decorada oioioi')   
        funçao(*args,**kwargs)
    return escrava

@master10
def outra_funcao1(msg):   #Solucionando o problema que o corre la em cima 
    print(msg)

outra_funcao1('ola,pessoal')


print('--------------------------UTILIDADE 1--------------------------------------')


def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo_que_levou = (end_time - start_time) *1000   #foi multiplicado vezes mil para ter o tempo em milisegundos
        print(f'A funçao {funcao.__name__} levou {tempo_que_levou:.2f}ms para executar.')
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()

print('--------------------------UTILIDADE 2--------------------------------------')

def velocidade1(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo_que_levou = (end_time - start_time) *1000   #foi multiplicado vezes mil para ter o tempo em milisegundos
        print(f'\nA funçao {funcao.__name__} levou {tempo_que_levou:.2f}ms para executar.')
    return interna

@velocidade1
def demora1():
    for i in range(100):
        print(i,end='')

demora1()

print('-------------UTILIDADE 3 (funcionando com entrada de dados)------------------')
# def master(funcao):
#     def escrava(receber):
#         print('Deu certo')
#         funcao(receber)
#     return escrava

# @master
# def comunicacao(msg):
#     print(msg)


# msg = input('Escreva algo:')

# comunicacao(msg)
        