class A:
    def __init__(self):
        print("A")
        super().__init__()

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

d = D()
print(D.__mro__)
# D -> B -> C -> A -> object

# super() follows MRO
class Base:
    def greet(self):
        return "Base"

class Mixin:
    def greet(self):
        return "Mixin -> " + super().greet()

class Child(Mixin, Base):
    pass

print(Child().greet())    # Mixin -> Base
print(Child.__mro__)

# Diamond problem
class A2:
    def hi(self): return "A"
class B2(A2):
    def hi(self): return "B->" + super().hi()
class C2(A2):
    def hi(self): return "C->" + super().hi()
class D2(B2, C2):
    def hi(self): return "D->" + super().hi()

print(D2().hi())
print(D2.__mro__)

# cooperative multiple inheritance
class Logger:
    def __init__(self, **kwargs):
        self.log = []
        super().__init__(**kwargs)

class Storage:
    def __init__(self, **kwargs):
        self.data = {}
        super().__init__(**kwargs)

class Service(Logger, Storage):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

s = Service("svc")
print(s.name, s.log, s.data)