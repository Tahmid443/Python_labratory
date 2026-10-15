class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"{self.name} is {self.age} years old"

# Create objects
d1 = Dog("Rex", 3)
d2 = Dog("Buddy", 5)

print(d1.bark())
print(d2.info())
print(d1.species)

# Attributes are mutable
d1.age = 4
print(d1.info())

# Objects are unique
print(d1 is d2)  # False

# Attribute access
print(d1.__dict__)
print(type(d1))