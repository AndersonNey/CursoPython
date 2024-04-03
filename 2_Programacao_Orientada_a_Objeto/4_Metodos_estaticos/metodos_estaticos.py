from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self,nome,idade):   #metodo de instacia tem coisas relacionadas com a instacia da classe 
        self.nome=nome
        self.idade=idade

    def get_ano_nascimento(self):
        resultado = (self.ano_atual - self.idade)
        return resultado

    @classmethod
    def por_ano_nascimento(cls,nome,ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento                           # 'idade' variavel local     cls.ano_atual   aqui estou falando que vou pegar a variavel da classe
        return cls(nome,idade)

    @staticmethod
    def gerar_id():
        rand = randint(100 ,200)
        return rand







p1 = Pessoa('luiz',32)        #cadastrando usando nome e idade
print(p1.idade)
print(p1.get_ano_nascimento())

p2 = Pessoa.por_ano_nascimento('joao',1960)      #cadastrando usando nome e ano de nascimento
print(p2.idade)


print(Pessoa.gerar_id())  #LEMBRANDO QUE DESSE JEITO NAO ESTA SALVANDO O VALOR EM LUGAR ALGUM , ESTA APENAS EXECUTANDO A FUNÇAO E ACABOU
print(p2.gerar_id())      #LEMBRANDO QUE DESSE JEITO NAO ESTA SALVANDO O VALOR EM LUGAR ALGUM , ESTA APENAS EXECUTANDO A FUNÇAO E ACABOU