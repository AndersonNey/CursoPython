#primeiro exemplo   

class Pessoa:

    def __init__(self, nome ,idade,classe):
        self.nome = nome
        self.idade = idade
        self.acao = classe


class Interruptor:

    def __init__(self, estado = 'Desligado'):
        self.estado = estado

    def Ligar_luz(self):
        if not self.estado == 'Ligado':
            self.estado = 'Ligado'
            print(f'A luz agora está {self.estado}')
            return
        print('A luz já esta ligada')
    
    def Desligar_luz(self):
        if not self.estado == 'Desligado':
            self.estado = 'Desligado'
            print(f'A luz agora está {self.estado}')
            return
        print('A luz já esta desligada')




t = Interruptor()

p = Pessoa('Carlos',17, t)

p.acao.Desligar_luz()
p.acao.Ligar_luz()
p.acao.Ligar_luz()
p.acao.Desligar_luz()







#segundo exemplo   

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
        

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')
        
    
escritor = Escritor('João')
caneta = Caneta('Bic')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()




