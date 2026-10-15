class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Puppy(Dog):
    def speak(self):
        return "Yip!"

# Usage
animals = [Dog("Rex"), Cat("Whiskers"), Puppy("Bud")]
for a in animals:
    print(a.describe())

# isinstance / issubclass
print(isinstance(animals[0], Animal))
print(issubclass(Dog, Animal))

# super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        return f"Vehicle: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def info(self):
        return f"{super().info()}, Model: {self.model}"

c = Car("Toyota", "Corolla")
print(c.info())

# Multiple inheritance
class A:
    def hi(self): return "A"
class B:
    def hi(self): return "B"
class C(A, B):
    pass

print(C().hi())    # A (MRO)
print(C.__mro__)