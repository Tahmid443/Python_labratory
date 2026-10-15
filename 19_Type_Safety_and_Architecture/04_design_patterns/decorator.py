from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float: ...
    @abstractmethod
    def description(self) -> str: ...

class Espresso(Coffee):
    def cost(self): return 2.0
    def description(self): return "Espresso"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

class Milk(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.5
    def description(self): return self._coffee.description() + ", Milk"

class Sugar(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.3
    def description(self): return self._coffee.description() + ", Sugar"

c = Espresso()
print(c.description(), c.cost())

c = Milk(c)
print(c.description(), c.cost())

c = Sugar(Milk(Espresso()))
print(c.description(), c.cost())