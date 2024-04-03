class Eletronico:
    def __init__(self,nome):
        self._nome=nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} ja esta ligado')
            return
        self._ligado = True
        print(f'{self._nome} agora esta ligado')

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} ja esta desligado')
            return
        self._ligado = False
        print(f'{self._nome} agora esta desligado')