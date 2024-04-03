
class Carro:

    def __init__(self,empresa,potencia,empuxo):
        self.empresa = empresa
        self.motor = Motor(potencia,empuxo)

    def exibri_valor(self):
        print(self.motor.cavalos)
        print(self.motor.torque)

    def alterar_valor(self,novo_valor1 , novo_valor2):
        self.motor.cavalos = novo_valor1
        self.motor.torque = novo_valor2


class Motor:
    def __init__(self,cavalos,torque):
        self.cavalos = cavalos
        self.torque =torque
        self.ligado = False


    def Ligar(self):
        if self.ligado  == False:
            print('Motor agora está ligado')
            self.ligado = True
            return
        print('Motor já está ligado')

    def Desligar(self):
        if self.ligado  == False:
            print('Motor já está desligado')
            return
        print('Motor agora está desligado')
        self.ligado = False




carrinho = Carro('ferrari',1000,100)

carrinho.exibri_valor()
carrinho.alterar_valor(300,50)
carrinho.exibri_valor()