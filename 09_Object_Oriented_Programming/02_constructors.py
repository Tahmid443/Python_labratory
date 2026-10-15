class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age})"

p = Person("Alice", 30)
print(repr(p))
print(str(p))
print(p)

# Default constructor values
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print(Point())
print(Point(1, 2))

# Copy constructor pattern
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)

    def area(self):
        return self.width * self.height

r1 = Rectangle(4, 5)
r2 = Rectangle.from_square(5)
print(r1.area(), r2.area())