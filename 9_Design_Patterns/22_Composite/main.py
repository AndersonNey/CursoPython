

from __future__ import annotations
from abc import ABC , abstractmethod
from typing import List

class BoxStructure(ABC):
    """Componet"""

    @abstractmethod
    def print_content(self) -> None:pass
    
    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass 

    def remove(self, child: BoxStructure) -> None: pass 



class Box(BoxStructure):
    """Composite"""

    def __init__(self, name) -> None:
       self.name = name
       self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()
    
    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)

class Product(BoxStructure):
    """Leaf"""

    def __init__(self, name: str , price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name , self.price)
    
    def get_price(self) -> float:
        return self.price




if __name__ == "__main__":
    #Leaf
    camiseta1 = Product('Camiseta1' , 49.90)
    camiseta2 = Product('Camiseta2' , 19.90)
    camiseta3 = Product('Camiseta3' , 10.90)

    #Composite
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)


    #Leaf
    smartphone1 = Product('Smartphone1' , 9000)
    smartphone2 = Product('Smartphone2' , 11000)

    #Composite
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    #Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())
