
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy
          
#nesse codigo vai ta usando padrao prototype (uma parte dele)
#OBSERVADO QUE AO QUERER CUSTOMIZAR OS HOTDOGS IRAR TER UMA EXPLOSAO DE CLASSES DE TANTO TIPO DE CLASSES DIFERENTE
#EX: SimpleHotdog COM BACON , SimpleHotdog SEM PotatoSticks ...


########### INGREDIENTS ###########
@dataclass
class Ingredient:
    price:float

@dataclass
class Bread(Ingredient):
    price:float = 1.5

@dataclass
class Sausage(Ingredient):
    price:float = 4.99

@dataclass
class Bacon(Ingredient):
    price:float = 7.99

@dataclass
class Egg(Ingredient):
    price:float = 1.50

@dataclass
class Cheese(Ingredient):
    price:float = 6.35

@dataclass
class MashedPotatoes(Ingredient):
    price:float = 2.25

@dataclass
class PotatoSticks(Ingredient):
    price:float = 0.99


########### HOTDOGS ###########
class Hotdog:
    _name: str
    _ingredients : List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([ ingredient.price for ingredient in self.ingredients]),2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name} ({self.price}) -> {self.ingredients}'



class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [Bread(),Sausage(),PotatoSticks()]

class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [Bread(),Sausage(),Bacon(),Egg(),Cheese(),MashedPotatoes(),PotatoSticks()]

########### DECORATORS ###########
class HotdogDecorator(Hotdog):
    def __init__(self,hotdog:Hotdog , ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


  


if __name__ == "__main__":
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog,Bacon())
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog,Egg())
    mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(egg_bacon_simple_hotdog , MashedPotatoes())
    mashed_potato_mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(mashed_potato_egg_bacon_simple_hotdog , MashedPotatoes())
    print(bacon_simple_hotdog)
    print(egg_bacon_simple_hotdog)
    print(mashed_potato_egg_bacon_simple_hotdog)
    print(mashed_potato_mashed_potato_egg_bacon_simple_hotdog)




