

#metodo final é um metodo que nao pode ser subescrito (mas python nao tem isso (essa regra))

from abc import ABC, abstractmethod

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()



    def hook(self):
        pass

    def base_class_method(self):
        print('ola eu sou da classe abstrata e serei executado tambem')

    @abstractmethod
    def operation1(self):pass


    @abstractmethod
    def operation2(self):pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Utilizando o GANCHO')

    def operation1(self):
        print('Operacao 1 concluida')

    def operation2(self):
        print('Operacao 2 concluida')

class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operacao 1 concluida (de maneira diferente)')

    def operation2(self):
        print('Operacao 2 concluida (de maneira diferente)')






if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method() 