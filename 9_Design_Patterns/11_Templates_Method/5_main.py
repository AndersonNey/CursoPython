


from abc import ABC, abstractmethod


class Pizza(ABC):
    """Class abstrata"""    
    def prepare(self) -> None:
        """Template Method"""
        self.hook_before_add_ingredients()
        self.hook_after_add_ingredients()
        self.add_ingrentients() #Abstract
        self.cook()             #Abstract
        self.cut()  #Concreto
        self.serve()  #Concreto
        

    def hook_before_add_ingredients(self) -> None:pass
    def hook_after_add_ingredients(self) -> None:pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando a pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo a pizza.')

    @abstractmethod
    def add_ingrentients(self) -> None:pass

    @abstractmethod
    def cook(self) -> None:pass


class AModa(Pizza):

    def add_ingrentients(self) -> None:
        print(f'AModa - Adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None:
        print(f'AModa - Cozinhando por 45 min no forno a lenha')

class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('VEG - Lavando ingredientes')

    def add_ingrentients(self) -> None:
        print(f'VEG - Adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        print(f'VEG - Cozinhando por 5 min no forno comum')    


if __name__ == "__main__":
    a_moda =AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()













