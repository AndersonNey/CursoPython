class Carro:

    def __init__(self,empresa,potencia,empuxo):
        self.empresa = empresa
        self._motor = Motor(potencia,empuxo)

    @property
    def motor(self):
        return f'{self._motor.cavalos} e {self._motor.torque}'



class Motor:
    def __init__(self,cavalos,torque):
        self.cavalos = cavalos
        self.torque =torque



carrinho = Carro('ferrari',1000,100)

print(carrinho.motor)
