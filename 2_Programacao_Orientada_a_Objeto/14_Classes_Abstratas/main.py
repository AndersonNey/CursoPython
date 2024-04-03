#classes abstratas - ela pode ter métodos concretos e métodos abstratos

#métodos concretos são métodos normais que você escreve código e ele funciona perfeitamente na herança 

#Um método abstrato é um método que não tem corpo geralmente,  você cria o método, não escreve o código dele, voce fala que é abstrato para qua as outras classes filhas 
#herdem esse metodo e sejam obrigadas a criar esse metodo

from abc import ABC , abstractmethod


class A(ABC):            #nao tem como criar um objeto apartir dessa classe, apartir do momento que eu crio um metodo abstrato dentro dela

    @abstractmethod
    def falar(self):
        pass 

class B(A):
    def falar(self):
        print('Falando')


a = B()
a.falar()