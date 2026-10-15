from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

class ShapeFactory:
    @staticmethod
    def create(kind, **kwargs):
        if kind == "circle":
            return Circle(kwargs["r"])
        if kind == "square":
            return Square(kwargs["s"])
        raise ValueError(f"Unknown: {kind}")

# Usage
s = ShapeFactory.create("circle", r=5)
print(f"{s.area():.2f}")

# Registration-based factory
class Factory:
    _creators = {}

    @classmethod
    def register(cls, name):
        def deco(creator):
            cls._creators[name] = creator
            return creator
        return deco

    @classmethod
    def create(cls, name, *args, **kwargs):
        return cls._creators[name](*args, **kwargs)

@Factory.register("circle")
def make_circle(r):
    return Circle(r)

print(Factory.create("circle", 3).area())