#quando voce usa o property voce esta falando para o python que voce quer que a funcao se comporte como um atributo e nao como uma funçao

#pensar como se eu estivesse interceptando o acesso e o envio de informaçoes de/e para uma variavel

class Produto:
    def __init__(self,NOME,PRECO) -> None:
        self.nome = NOME
        self.preco = PRECO

    def desconto(self,percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def preco(self):                #o nome das funçoes precisam ser o mesmo que do self.preco 
        return self.bla             # o valor que ira guarda o valor por algum tempo, mas por conversao utiliza-se self._preco    

    @preco.setter                    #como bla nao existe ele procura no setter , o set configura o bla (o que ocorre é o seguinte )
    def preco(self,valor):           # QUANDO ESCREVER p1.preco ELE RETORNA O VALOR DE bla E QUANDO VAI SETAR UM NOVO VALOR p1.preco = 'novovalor'
        if isinstance(valor, str):   #ele seta esse valor em bla 
            valor =  float(valor.replace('R$', ''))         #ou seja esta modificando o valores de GET e SETTER de 'preco' para que começe a 
                                                            #configurar da maneira que eu quero, ela exibe os valores de bla
                                                            # (que em ideia bla esta oculta no metodo de __init__) -> eu acho 
        self.bla = valor



p1 = Produto('Camiseta',50)
p1.desconto(10)
print(p1.preco)


p2 = Produto('Caneca', 'R$15') #'R$15'
p2.desconto(10)
print(p2.preco)


#definiçao definitiva:

#quando eu crio somente o get eu posso modificar a maneira que esse valor é visto

#quando eu crio o setter eu falo para o compilador que apartir desse momento qualquer atribuiçao para esse atributo 
#quem ficara responsavel de fazer sera o setter






class Teste:
    def __init__(self, nome):
         self.nome = nome   #daria diferença seu usa-se self._nome = nome 

    @property
    def nome(self):                                   #modificando o set e get para ficar exibindo os  valores de self._nome
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return f'Meu nome é {self._nome}'

    @nome.setter
    def nome(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self._nome = value.upper()



testinho = Teste('Julio')

print(testinho.nome)
testinho.nome = 'Joao'
print(testinho.nome)












class Teste:
    def __init__(self, nome):
         self.nome = nome   

    @property
    def nome(self):                                   #modificando o set e get para ficar exibindo os  valores de self._nome
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return f'Meu nome é {self._nome}'

    @nome.setter
    def nome(self, value):                                   #seria como nome = self._nome = value.upper()
         # este código é executado sempre que alguém fizer 
         # self.nome = value
        if len(value) > 7:
            self._nome = 'maior que 8'
        else:
            self._nome = 'menor que 8'



testinho = Teste('testetesteteste')

print(testinho.nome)
testinho.nome = 'Joao'
print(testinho.nome)




