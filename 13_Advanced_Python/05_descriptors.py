# Descriptor protocol: __get__, __set__, __delete__

class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

p = Product(10, 5)
print(p.total())
# p.price = -1  # ValueError

# Type-checking descriptor
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        setattr(obj, self.name, value)

class User:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Alice", 30)
print(u.name, u.age)
# u.age = "old"  # TypeError

# Property is a descriptor!