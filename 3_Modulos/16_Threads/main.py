

#o python executa tudo um seguido do outro
# print('hello')
# for x in range(10):
#     print(x)
#     sleep(.5)
# print('WORLD')

from time import sleep
from threading import Thread
from threading import Lock

#PRIMEIRA MANEIRA DE CRIAR =======================================================================

class MeuThread(Thread):
    def __init__(self,texto,tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()
    
    #sobrescrevendo o metodo da super classe chamado run
    def run(self):
        sleep(self.tempo)
        print(self.texto)

#cada MeuThread abaixo é um thread  diferente

t1 = MeuThread("carro1",5)
t1.start()

t2 = MeuThread("carro2",4)
t2.start()

t3 = MeuThread("carro3",2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)


#SEGUNDA MANEIRA DE CRIAR =======================================================================

def vai_demorar(texto , tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar , args = ('ola mundo1' , 5))
t1.start()

t2 = Thread(target=vai_demorar , args = ('ola mundo2' , 1))
t2.start()

t3 = Thread(target=vai_demorar , args = ('ola mundo3' , 2))
t3.start()

for i in range(10):
    print(i)
    sleep(1)



#OBSERVANDO O COMPORTAMENTO DAS THREADS ========================================================

def vai_demorar(texto , tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar , args = ('ola mundo1' , 10))
t1.start()
#t1.join()  # colocando o thread devolta na thread principal

while t1.is_alive():   #enquanto essa Thread estiver viva fosse fica executando
    print('Esperando a thread')
    sleep(2)

print('thread acabou')


#PROBLEMAO QUE PODE TER========================================================================

class Ingressos:
    def __init__(self,estoque) -> None:
        self.estoque = estoque

    def comprar(self, quantidade):
        if self.estoque < quantidade: # acabou que as threads chegaram tudo ao 'mesmo tempo' e foram liberadas para passar para resolver isso usa Lock
            print('Nao temos ingressos suficientes.')
            return

        sleep(1)

        self.estoque -= quantidade        
        print(f'Voce comprou {quantidade} ingresso(s). Ainda temeos {self.estoque}')



if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    
    print(ingressos.estoque)



#RESOLVENDO O PROBLEMA==========================================================================

class Ingressos:
    def __init__(self,estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()   #libera a passagem de um 

        if self.estoque < quantidade: 
            print('Nao temos ingressos suficientes.')
            self.lock.release() #saber quando o cara saiu para poder liberar o outro la emcima
            return

        sleep(1)

        self.estoque -= quantidade        
        print(f'Voce comprou {quantidade} ingresso(s). Ainda temeos {self.estoque}')

        self.lock.release() #saber quando o cara saiu para poder liberar o outro la emcima



if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    
    print(ingressos.estoque)


#====================================================================================================


#verificando todas as threads , para ver se elas terminaram para poder exibir a quantidade do estoque no final

class Ingressos:
    def __init__(self,estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()   #libera a passagem de um 

        if self.estoque < quantidade: 
            print('Nao temos ingressos suficientes.')
            self.lock.release() #saber quando o cara saiu para poder liberar o outro la emcima
            return

        sleep(1)

        self.estoque -= quantidade        
        print(f'Voce comprou {quantidade} ingresso(s). Ainda temeos {self.estoque}')

        self.lock.release() #saber quando o cara saiu para poder liberar o outro la emcima



if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads =[]

    for i in range(1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:     #iniciando todas juntas
        t.start()

    executando  = True
    while executando:
        executando = False  #mesmo executando recebendo false aqui ele executa o que tem dentro, LEMBRA
    
        for t in threads:
            if t.is_alive():
                executando = True
                break            #eu testei e nao precisou do break


    print(ingressos.estoque)