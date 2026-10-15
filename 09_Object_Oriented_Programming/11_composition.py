# "has-a" relationship
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        return "Engine started"

class Wheels:
    def __init__(self, count):
        self.count = count
    def rotate(self):
        return f"{self.count} wheels rotating"

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)     # composition
        self.wheels = Wheels(4)

    def start(self):
        return f"{self.brand}: {self.engine.start()}, {self.wheels.rotate()}"

c = Car("Toyota", 150)
print(c.start())

# Composition vs inheritance
# Inheritance: "is-a"
class Animal:
    def eat(self): return "eating"

class Dog(Animal):   # Dog IS-A Animal
    pass

# Composition: "has-a"
class Logger:
    def log(self, msg): print(msg)

class UserService:
    def __init__(self, logger):
        self.logger = logger    # HAS-A logger
    def create(self, name):
        self.logger.log(f"Creating {name}")
        return {"name": name}

svc = UserService(Logger())
svc.create("Alice")

# Prefer composition for flexibility