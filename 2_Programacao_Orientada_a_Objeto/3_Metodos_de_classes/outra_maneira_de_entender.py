
#o metodo de classe utiliza a base original mas pode acrescentar por cima outra maneira de fazer um objeto com outros parametros


class Pessoa:
    ano_atual = 2022

    def __init__(self,nome,idade):   #metodo de instacia tem coisas relacionadas com a instacia da classe 
        self.nome=nome
        self.idade=idade

    def get_ano_nascimento(self):
        resultado = (self.ano_atual - self.idade)
        return resultado

    def __repr__(self) -> str:
        return f'NOME = {self.nome}\nIDADE = {self.idade}'

    @classmethod
    def por_ano_nascimento(cls,nome,ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento        # 'idade' variavel local     cls.ano_atual   aqui estou falando que vou pegar a variavel da classe
        return cls(nome,idade)



class Humano:

    def __init__(self,nome,idade):  
        self.nome=nome
        self.idade=idade

    def get_ano_nascimento(self):
        resultado = (self.ano_atual - self.idade)
        return resultado

    def __repr__(self) -> str:
        return f'NOME = {self.nome}\nIDADE = {self.idade}'

    @classmethod
    def por_ano_nascimento(cls):
        nome = 'Anonimo'
        idade = 'Sem idade'   
        return cls(nome,idade)


x = Humano('Joao',17)
print(x)

y = Humano.por_ano_nascimento()
print(y)