# Same interface, different behaviors
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h):
        self.b, self.h = b, h
    def area(self):
        return 0.5 * self.b * self.h

shapes = [Circle(1), Rectangle(2, 3), Triangle(4, 5)]
for s in shapes:
    print(f"{type(s).__name__}: {s.area():.2f}")

# Duck typing
class Duck:
    def quack(self): return "Quack!"
class Person:
    def quack(self): return "I'm imitating a duck"

def make_it_quack(x):
    print(x.quack())

make_it_quack(Duck())
make_it_quack(Person())

# Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))