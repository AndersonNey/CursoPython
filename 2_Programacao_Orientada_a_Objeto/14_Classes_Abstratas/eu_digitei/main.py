from packages.conta import Conta       #importei esse so para testar

from packages.cc import ContaCorrente
from packages.cp import ContaPoupaca


cp = ContaPoupaca(111,100,400)

cp.depositar(10)

print('+'*80)

cc= ContaCorrente(111,100,52)
cc.depositar(100)
cc.sacar(250)
cc.sacar(1000)





#teste = Conta()     testando se tem como instacia essa classe