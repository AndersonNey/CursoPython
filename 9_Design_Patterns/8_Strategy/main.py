
# Principio do aberto/fechado


from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self,total: float,discount: DiscountStrategy):
        self.__total = total
        self.__discount =discount


    @property
    def total(self):
        return self.__total

    @property
    def total_with_discount(self):
        return self.__discount.calculate(self.total)
        


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)

class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value

class CustomDiscount(DiscountStrategy):
    def __init__(self,discount):
        self.discount = discount / 100 


    def calculate(self, value: float) -> float:
        return value - (value * self.discount)



if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)


    order = Order(1000 , twenty_percent)
    print(order.total , order.total_with_discount)

    order = Order(1000 , fifty_percent)
    print(order.total , order.total_with_discount)

    order = Order(1000 , no_discount)
    print(order.total , order.total_with_discount)

    order = Order(1000 , CustomDiscount(13))
    print(order.total , order.total_with_discount)

























