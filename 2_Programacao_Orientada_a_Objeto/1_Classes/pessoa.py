from datetime import datetime   #pegar o ano atual
#variaveis da instacia sao variaveis das funçoes 
#acho que metodo sao as funçoes da classe
#acho que instanciar é usar o metodo da classe



class Pessoa:                                                                #Por covençao usa letra Maiuscula

    ano_atual= int(datetime.strftime(datetime.now(),'%Y'))

    def __init__(self,NOME,IDADE,COMENDO=False , FALANDO = False):      #nao precisa enviar o parametro self, o python ja faz isso automaticamente      #ele é executado assim que a classe é instanciada
        self.nome=NOME
        self.idade= IDADE
        self.comendo=COMENDO
        self.falando= FALANDO          #variaveis do tipo self sao validas em toda a classe

        variavel = 'seu valor'       #essa variavel é valida, porem somente no metodo init (ela é local) 
        print(variavel)

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
            return
        
        print(f'{self.nome} nao esta falando')

    def comer(self,alimento):
        if self.comendo :                      # se self.comendo igual True ele vai retornar
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo=True                       # observe que modifiquei o estado desta variavel
    
    def parar_de_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo=False
            return
        print(f'{self.nome} ja nao estava comendo')

    def ano_nascimento(self):
        return self.ano_atual - self.idade      #perceba que para usar a variavel da classe dentro da funçao precisei usar self.
        
        

        
            

        