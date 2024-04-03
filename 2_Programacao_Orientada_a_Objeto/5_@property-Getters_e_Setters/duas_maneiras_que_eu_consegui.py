#as duas maneiras que eu consegui aplicar o property 
class Pessoa:  #OS DOIS EXEMPLOS FUNCIONAM MAS ESSE 1° EXEMPLO É O QUE PARECE MAIS CERTO

    def __init__(self,NOME,IDADE,PESO,ALTURA):
        self.nome= NOME
        self.idade = IDADE
        self.peso = PESO
        self.altura = ALTURA
    
    @property
    def idade(self):
        return f'{self.variavel_temporaria} oi'

    @idade.setter
    def idade(self,valor):                                #se eu deixasse apenas self o valor que eu desejaria guardar nao conseguiria 
        self.variavel_temporaria = valor                  #vir junto x1._idade = 25  sao dois argumnetos o proprio objeto e o valor

x1 = Pessoa('lucas','18','80','1.90')


print(x1.idade)



class Pessoa:

    def __init__(self,NOME,IDADE,PESO,ALTURA):
        self.nome= NOME
        self._idade = IDADE
        self.peso = PESO
        self.altura = ALTURA
    
    @property
    def idade(self):
        return f'{self._idade} oi'

    @idade.setter
    def idade(self,valor):                   #se eu deixasse apenas self o valor que eu desejaria guardar nao conseguiria 
        self._idade = valor                  #vir junto x1._idade = 25  sao dois argumnetos o proprio objeto e o valor

x1 = Pessoa('lucas','18','80','1.90')



print(x1.idade)

