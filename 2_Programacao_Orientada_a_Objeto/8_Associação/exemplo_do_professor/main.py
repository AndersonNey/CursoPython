from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)        #mesmo matando o escritor a caneta e a maquina continua existindo
maquina.escrever()


# basicamente uma classe utiliza outra classe , mas ambas podem viver sem a outra
