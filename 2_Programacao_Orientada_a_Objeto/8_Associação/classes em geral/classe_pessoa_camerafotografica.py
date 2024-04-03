

class Pessoa:

    def __init__(self,NOME,IDADE):
        self.nome = NOME
        self.__idade = IDADE

    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_valor):
        self.__nome = novo_valor
    
    @property
    def idade(self):
        return 'Você não possui autorização para essa informação'

    @idade.setter
    def idade(self,impossivel_configurar):
        return None
        
    def exibir_idade(self):
        return self.__idade

    @classmethod
    def anonimo(cls):
        return cls('sem nome','sem idade')


class CameraFotografica:
    
    def __init__(self,MARCA='Bic',COR='Preta'):
        self.marca = MARCA
        self.cor = COR
    
    def escrever(self,outro_objeto):
        print(f'{outro_objeto.nome} esta escrevendo com a caneta {self.marca} {self.cor}')

    

p1 = Pessoa('Joao','16')
c1 = CameraFotografica()

p1.açoes = c1
p1.açoes.escrever(p1)