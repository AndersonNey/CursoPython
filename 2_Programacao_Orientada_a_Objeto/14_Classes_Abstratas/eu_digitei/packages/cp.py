from packages.conta import Conta

class ContaPoupaca(Conta):
    def sacar(self,valor):
        if self.saldo<valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()