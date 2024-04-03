

#metodo final é um metodo que nao pode ser subescrito (mas python nao tem isso (essa regra))

from abc import ABC, abstractmethod

class Abstract(ABC):
    def template_method(self):
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):pass


    @abstractmethod
    def operation2(self):pass


class ConcreteClass1(Abstract):
    def operation1(self):
        print('Operacao 1 concluida')

    def operation2(self):
        print('Operacao 2 concluida')



if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()