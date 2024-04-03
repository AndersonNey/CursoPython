
class Carro:

    def __init__(self,empresa,potencia,empuxo):
        self.empresa = empresa
        self.__motor = Motor(potencia,empuxo)
    
    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self,novo_valor):
        self.__empresa = novo_valor.upper()

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,*args):
        self.__motor = Motor(args[0][0],args[0][1])


class Motor:
    def __init__(self,cavalos,torque):
        self.cavalos = cavalos
        self.torque =torque
        self.ligado = False

    @property
    def cavalos(self):
        return self.__cavalos

    @cavalos.setter
    def cavalos(self,novo_valor):
        self.__cavalos = novo_valor

    @property
    def torque(self):
        return self.__torque

    @torque.setter
    def torque(self,novo_valor):
        self.__torque = novo_valor


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






carro1 = Carro('volkswagen',300,50)

print(carro1.motor.cavalos)
print(carro1.motor.torque)

carro1.motor.cavalos = 500
carro1.motor.torque = 70

print(carro1.motor.cavalos)
print(carro1.motor.torque)


carro1.motor = (800,100)

print(carro1.motor.cavalos)
print(carro1.motor.torque)
