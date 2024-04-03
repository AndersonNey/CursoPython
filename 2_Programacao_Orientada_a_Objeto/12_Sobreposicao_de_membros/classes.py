from shelve import Shelf


class Pessoa:
    def __init__ (self,nome,idade):
        self.nome =nome
        self.idade= idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando ...')

    def falar(self):
        print('metodo esta em cliente')

class ClienteVIP(Cliente):                                    
                                                #
    def __init__(self, nome, idade,sobrenome):
        super().__init__(nome, idade)           #Pessoa.__init__(self,nome,idade) ->dessa maneira tambem daria certo  |  os dados de nome e idade estao sendo criados em Pessoa
        self.sobrenome = sobrenome              #mas este esta sendo setado somente em cliente vip

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)



"""
                                                                        #o python procura primeiro na propria classe depois ele vai procurar em outro lugar   
    def falar(self):                                                    #sobreescrevendo o metodo falar, agora esse aqui ira se chamado quando o clienteVIP chamar
        super().falar()                                                  #chamando o metodo da super classe (o primeiro metodo que ele achar na herarquia)
        Pessoa.falar(self)              #chamando funcao de outra classe, quando se utiliza dessa maneira ele precisa saber qual objeto ta falando, por isso se utiliza o self. 
        Cliente.falar(Shelf)
        print('outra coisa qualquer')



"""