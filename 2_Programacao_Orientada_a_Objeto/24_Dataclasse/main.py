# criar classes mais rapido


from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict , astuple

#congela a classe se torna imutavel
# frozen = True

@dataclass(eq=True,order=True)
class Pessoa: 
    nome:str   #isso é typehit, nao é forçando tipo
    sobrenome: str = field(repr= False)  #ocutando esse campo

    def __post_init__(self):  # é executado de pois de __init__
        if not isinstance(self.nome,str):
            raise TypeError(f'tipo invalido {type(self.nome)} != str em {self}')

        

    # def __repr__(self):
    #     return self.nome

    # @property
    # def nome_comppleto(self):
    #     return f'{self.nome} {self.sobrenome}'




p1 = Pessoa('A','3')
p2 = Pessoa('B','4')
p3 = Pessoa('C','7')
p4 = Pessoa('D','5')

print(p1==p2)

pessoas = [p1,p2,p3,p4]

print(sorted(pessoas, key= lambda pessoa: pessoa.sobrenome))


print(p1) # ja deixa configurado  #aqui normalmente viria o endereço de memoria 


print(asdict(p1))  #convertendo para dicionario

print(astuple(p1))  #convertendo para tupla


