# 09. Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects**, which combine data (attributes) and behavior (methods).

OOP helps us write reusable, organized, maintainable, and scalable programs.

## 📚 Table of Contents

1. [Classes and Objects](#1-classes-and-objects)
2. [Constructors](#2-constructors)
3. [Instance and Class Variables](#3-instance-and-class-variables)
4. [Instance, Class, and Static Methods](#4-instance-class-and-static-methods)
5. [Encapsulation](#5-encapsulation)
6. [Inheritance](#6-inheritance)
7. [Polymorphism](#7-polymorphism)
8. [Abstraction](#8-abstraction)
9. [Properties](#9-properties)
10. [Magic Methods](#10-magic-methods)
11. [Composition](#11-composition)
12. [Dataclasses](#12-dataclasses)
13. [OOP Principles Summary](#13-oop-principles-summary)
14. [Common Mistakes](#14-common-mistakes)
15. [OOP for Competitive Programming](#15-oop-for-competitive-programming)
16. [Practice Checklist](#16-practice-checklist)

---

## 1. Classes and Objects

### What is a class?

A **class** is a blueprint that defines the attributes and methods its objects can have.

An **object** is an instance of a class.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name           # Instance attributes
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"{self.name} is {self.age} years old"


# Creating objects
d1 = Dog("Rex", 3)
d2 = Dog("Buddy", 5)

print(d1.bark())
print(d2.info())
print(d1.species)

# Modify an instance attribute
d1.age = 4
print(d1.info())

# Different objects have different identities
print(d1 is d2)  # False

# Inspect the object's instance attributes
print(d1.__dict__)
print(type(d1))
```

### Important concepts

- `class`: Defines a class.
- `self`: Refers to the current instance.
- `__init__()`: Initializes a newly created object.
- Attributes: Variables associated with an object or class.
- Methods: Functions defined inside a class.
- `type(obj)`: Returns the object's type.
- `obj.__dict__`: Usually contains the instance's stored attributes.
- `is`: Checks whether two references point to the same object.

### Class vs object

| Class | Object |
|---|---|
| Blueprint | Instance of a class |
| Defines attributes and methods | Has actual attribute values |
| Example: `Dog` | Example: `Dog("Rex", 3)` |

---

## 2. Constructors

In Python, `__init__()` is the initializer method. It sets up an object's initial state.

Python creates the object before calling `__init__()` to initialize it.

```python
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
```

### Default argument values

You can provide default values for constructor parameters.

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


print(Point())
print(Point(1, 2))
```

Output:

```text
Point(0, 0)
Point(1, 2)
```

### Alternative constructors with `@classmethod`

Python does not have a special built-in copy-constructor syntax like some other languages. However, a class method can provide an alternative way to create objects.

```python
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

print(r1.area())  # 20
print(r2.area())  # 25
```

**Remember:**

- `__init__()` initializes the object.
- `__repr__()` provides a developer-oriented representation.
- `__str__()` provides a readable string representation.
- `@classmethod` can provide alternative constructors.

---

## 3. Instance and Class Variables

Python classes commonly use two types of variables.

### Instance variables

Instance variables belong to individual objects. Each object can have its own value.

### Class variables

Class variables are defined on the class and can be shared by its instances.

```python
class Counter:
    total = 0  # Class variable

    def __init__(self, name):
        self.name = name
        self.count = 0  # Instance variable
        Counter.total += 1

    def increment(self):
        self.count += 1


c1 = Counter("a")
c2 = Counter("b")

c1.increment()
c1.increment()
c2.increment()

print(c1.count)      # 2
print(c2.count)      # 1
print(Counter.total) # 2
```

### The mutable class variable problem

Be careful when using mutable objects such as lists and dictionaries as class variables.

```python
class Team:
    members = []

    def add(self, name):
        self.members.append(name)


t1 = Team()
t2 = Team()

t1.add("Alice")

print(t2.members)  # ['Alice']
```

Both objects access the same list because `members` is a class variable.

### Correct approach

```python
class Team:
    def __init__(self):
        self.members = []

    def add(self, name):
        self.members.append(name)


t1 = Team()
t2 = Team()

t1.add("Alice")

print(t1.members)  # ['Alice']
print(t2.members)  # []
```

### Comparison

| Feature | Instance variable | Class variable |
|---|---|---|
| Belongs to | Individual instance | Class |
| Typical access | `obj.name` | `ClassName.total` |
| Shared between instances | No, not by default | Yes, when accessed as a shared class attribute |
| Typical use | Name, age, score | Constants, shared counters |

**Important:** Assigning `obj.attribute = value` can create or update an instance attribute that shadows a class attribute. It does not necessarily change the class variable itself.

---

## 4. Instance, Class, and Static Methods

Python supports three common method styles.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        # Instance method: uses self
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        # Class method: uses cls
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def is_freezing(celsius):
        # Static method: needs neither self nor cls
        return celsius <= 0


t = Temperature(25)
print(t.to_fahrenheit())  # 77.0

t2 = Temperature.from_fahrenheit(77)
print(t2.celsius)         # 25.0

print(Temperature.is_freezing(0))   # True
print(Temperature.is_freezing(10))  # False
```

### Comparison table

| Method type | First parameter | Decorator | Typical purpose |
|---|---|---|---|
| Instance method | `self` | None | Works with object state |
| Class method | `cls` | `@classmethod` | Works with class-level behavior or creates instances |
| Static method | None automatically | `@staticmethod` | Utility function logically related to the class |

### Quick rule

- Need instance data? Use an instance method.
- Need the class itself? Use a class method.
- Need neither instance nor class state? Consider a static method.

---

## 5. Encapsulation

**Encapsulation** means keeping data and related behavior together and providing a controlled interface for working with an object's state.

Python uses naming conventions rather than strict private access modifiers.

### Public, protected-convention, and name-mangled attributes

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.__pin = "0000"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Invalid PIN")

        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

    @property
    def balance(self):
        return self._balance


account = BankAccount("Alice", 100)

account.deposit(50)
print(account.balance)  # 150

account.withdraw(30, "0000")
print(account.balance)  # 120
```

### Naming conventions

| Syntax | Meaning |
|---|---|
| `name` | Public attribute |
| `_name` | Non-public by convention |
| `__name` | Name-mangled attribute |

A single underscore is a convention that tells developers an attribute is intended for internal use.

A double underscore triggers name mangling. For example, `__pin` inside `BankAccount` is normally stored under a name similar to `_BankAccount__pin`.

Name mangling is not a security mechanism. Python does not guarantee absolute privacy, and developers can still access such attributes.

### Validation through encapsulation

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")

        self._age = value


p = Person(30)
p.age = 35

print(p.age)  # 35

# p.age = -1  # Raises ValueError
```

Encapsulation helps maintain valid object state by placing validation in the class interface.

---

## 6. Inheritance

**Inheritance** allows a class to reuse and extend behavior from another class.

- Parent class: Base class.
- Child class: Derived class.
- `super()`: Accesses the next implementation in the method resolution order (MRO).

### Basic inheritance and method overriding

```python
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


animals = [
    Dog("Rex"),
    Cat("Whiskers"),
    Puppy("Buddy")
]

for animal in animals:
    print(animal.describe())
```

### Using `super()`

```python
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


car = Car("Toyota", "Corolla")
print(car.info())
```

Output:

```text
Vehicle: Toyota, Model: Corolla
```

### Multiple inheritance and MRO

A class can inherit from multiple parent classes.

```python
class A:
    def hi(self):
        return "A"


class B:
    def hi(self):
        return "B"


class C(A, B):
    pass


print(C().hi())  # A
print(C.__mro__)
```

Because `A` appears before `B` in the inheritance list, `A.hi()` is found first in this example.

MRO determines the order Python uses to search for methods and attributes.

### Useful functions

```python
isinstance(obj, ClassName)
issubclass(ChildClass, ParentClass)
```

These help determine whether an object is an instance of a class or its subclass.

---

## 7. Polymorphism

**Polymorphism** means that a common interface can produce different behavior depending on the object.

### Method overriding

```python
class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(1), Rectangle(2, 3)]

for shape in shapes:
    print(shape.area())
```

Both objects provide `area()`, but each calculates it differently.

### Duck typing

Python often cares about what an object can do rather than its exact type.

```python
class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm imitating a duck"


def make_it_quack(obj):
    print(obj.quack())


make_it_quack(Duck())
make_it_quack(Person())
```

Both objects work because both provide a `quack()` method.

### Operator overloading

You can define how operators work with your own objects by implementing special methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(4, 6)
```

---

## 8. Abstraction

**Abstraction** means exposing essential operations while hiding implementation details.

Python supports abstract base classes through the `abc` module.

```python
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    def execute(self, sql):
        self.connect()
        return self.query(sql)


class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"

    def query(self, sql):
        return f"MySQL result: {sql}"


class Postgres(Database):
    def connect(self):
        return "Connected to Postgres"

    def query(self, sql):
        return f"Postgres result: {sql}"


for db in [MySQL(), Postgres()]:
    print(db.execute("SELECT * FROM users"))
```

### Important points

- `ABC` is a base class for abstract classes.
- `@abstractmethod` marks a method that concrete subclasses must implement.
- An abstract class with unresolved abstract methods cannot be instantiated.
- An abstract class can also contain fully implemented methods.

### Abstract properties

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2


print(Square(5).area)  # 25
```

### Abstraction vs encapsulation

| Abstraction | Encapsulation |
|---|---|
| Focuses on what an object provides | Focuses on organizing state and behavior |
| Defines an interface | Controls access through conventions and methods |
| Example: abstract `Database` | Example: validated `BankAccount` |

---

## 9. Properties

Properties let you use method-based logic through attribute-style access.

The `@property` decorator is useful for computed values and validation.

### Getter and setter

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")

        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


t = Temperature(25)

print(t.celsius)
print(t.fahrenheit)

t.fahrenheit = 100
print(t.celsius)
```

The setter for `fahrenheit` delegates to the `celsius` setter, so the validation is applied consistently.

### Computed properties

```python
import math


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)

print(c.area)
print(c.circumference)
```

Notice that you use `c.area`, not `c.area()`.

### Cached properties

`functools.cached_property` computes a value on first access and caches it on the instance.

```python
from functools import cached_property


class Data:
    def __init__(self, nums):
        self.nums = nums

    @cached_property
    def total(self):
        print("Computing...")
        return sum(self.nums)


d = Data([1, 2, 3])

print(d.total)  # Computes the value
print(d.total)  # Reuses the cached value
```

**Important:** If the underlying data changes, a cached property may become stale. Delete the cached attribute or use a regular property if recalculation is needed.

---

## 10. Magic Methods

Magic methods, also called **dunder methods**, are special methods whose names begin and end with double underscores.

They let custom objects integrate with Python's built-in operations.

### Common magic methods

| Method | Purpose |
|---|---|
| `__init__` | Initialize an object |
| `__repr__` | Developer-oriented representation |
| `__str__` | Readable string representation |
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[index]` |
| `__contains__` | `item in obj` |
| `__iter__` | `iter(obj)` |
| `__next__` | `next(obj)` |
| `__abs__` | `abs(obj)` |
| `__bool__` | `bool(obj)` |
| `__call__` | `obj(...)` |
| `__enter__`, `__exit__` | Context manager behavior |

### Example: custom Vector

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 == Vector(1, 2))
print(len(v1))
print(v1[0], v1[1])
print(abs(v1))
print(bool(Vector(0, 0)))
print(v1(2))
```

### A note about `__eq__` and `__hash__`

If you define equality based on an object's values, be careful with hashing. Objects that compare equal must have equal hashes.

Mutable objects whose equality depends on changing attributes are generally poor hash keys. Do not implement `__hash__` casually for mutable objects.

---

## 11. Composition

**Composition** means building a class using objects of other classes. It represents a **has-a** relationship.

### Example: Car has an Engine and Wheels

```python
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
        self.engine = Engine(horsepower)
        self.wheels = Wheels(4)

    def start(self):
        return (
            f"{self.brand}: {self.engine.start()}, "
            f"{self.wheels.rotate()}"
        )


car = Car("Toyota", 150)
print(car.start())
```

### Composition vs inheritance

| Composition | Inheritance |
|---|---|
| Has-a relationship | Is-a relationship |
| Combines objects | Extends a parent class |
| Often improves flexibility | Encourages shared interfaces and behavior |
| Example: `Car` has an `Engine` | Example: `Dog` is an `Animal` |

### Dependency injection

Composition also allows dependencies to be passed into a class.

```python
class Logger:
    def log(self, message):
        print(message)


class UserService:
    def __init__(self, logger):
        self.logger = logger

    def create(self, name):
        self.logger.log(f"Creating {name}")
        return {"name": name}


service = UserService(Logger())
print(service.create("Alice"))
```

This makes it easier to replace dependencies, customize behavior, and test classes independently.

---

## 12. Dataclasses

The `dataclasses` module provides a convenient way to define classes primarily used to store data.

The `@dataclass` decorator can generate methods such as `__init__`, `__repr__`, and `__eq__`.

### Basic dataclass

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        return (
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        ) ** 0.5


p1 = Point(0, 0)
p2 = Point(3, 4)

print(p1)
print(p1 == Point(0, 0))
print(p1.distance(p2))  # 5.0
```

### Default values and `default_factory`

```python
from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age: int = 0
    tags: list[str] = field(default_factory=list)


u1 = User("Alice", 30)
u2 = User("Bob")

u1.tags.append("admin")

print(u1.tags)  # ['admin']
print(u2.tags)  # []
```

Use `default_factory` for mutable defaults such as lists and dictionaries so that each instance receives its own object.

### Frozen dataclasses

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    host: str
    port: int


config = Config("localhost", 8080)

print(config)

# config.port = 9090  # FrozenInstanceError
```

A frozen dataclass prevents ordinary attribute assignment after initialization. With the default equality and hashing settings, a frozen dataclass can be hashable when its fields are hashable.

### Ordering

```python
from dataclasses import dataclass


@dataclass(order=True)
class Score:
    points: int
    name: str = ""


scores = [Score(3), Score(1), Score(2)]

print(sorted(scores))
```

With `order=True`, comparisons are based on the declared field order. Here, `points` is compared first, then `name`.

### Converting dataclasses

```python
from dataclasses import dataclass, asdict, astuple


@dataclass
class Point:
    x: int
    y: int


p = Point(3, 4)

print(asdict(p))   # {'x': 3, 'y': 4}
print(astuple(p))  # (3, 4)
```

### Nested dataclasses

```python
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    zip: str


@dataclass
class Employee:
    name: str
    address: Address


employee = Employee(
    "Bob",
    Address("NYC", "10001")
)

print(employee.address.city)
```

### When should you use dataclasses?

Use dataclasses when a class mainly stores structured data and you want to avoid writing repetitive initialization and representation methods.

---

## 13. OOP Principles Summary

The four commonly taught pillars of OOP are:

| Principle | Meaning | Python example |
|---|---|---|
| Encapsulation | Organize state and expose a controlled interface | Properties and validation |
| Inheritance | Reuse or extend another class | `class Dog(Animal)` |
| Polymorphism | Same interface, different behavior | Different `area()` implementations |
| Abstraction | Define essential operations while hiding implementation details | `ABC` and `@abstractmethod` |

Other important OOP concepts include composition, object identity, method overriding, operator overloading, and dataclasses.

---

## 14. Common Mistakes

### Mistake 1: Forgetting `self`

Incorrect:

```python
class Student:
    def show():
        print("Hello")
```

Correct:

```python
class Student:
    def show(self):
        print("Hello")
```

### Mistake 2: Using a mutable class variable unintentionally

Incorrect:

```python
class Group:
    members = []
```

If each object needs its own list, initialize it inside `__init__()`.

### Mistake 3: Forgetting `super().__init__()`

When a child class overrides `__init__()` but also needs initialization from the parent, call the parent's initializer appropriately.

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

### Mistake 4: Confusing a property with a method

```python
@property
def area(self):
    return 25
```

Access it using `obj.area`, not `obj.area()`.

### Mistake 5: Assuming double underscores provide security

`__attribute` triggers name mangling, but it does not make the attribute truly inaccessible.

### Mistake 6: Using inheritance for every kind of reuse

If an object contains another object, composition may be a better design than inheritance.

### Mistake 7: Using mutable objects as hash keys

Hash keys must maintain consistent hashing and equality behavior. Avoid hashing objects whose equality-relevant state can change.

---

## 15. OOP for Competitive Programming

For competitive programming, you should understand OOP, but **you do not need to use classes in every solution**.

Python's built-in data structures and simple functions are often enough for many problems.

### When classes are useful

- Implementing linked lists, trees, and graph nodes.
- Creating custom data structures.
- Representing states in search or simulation problems.
- Implementing heaps, tries, or other structures with custom behavior.
- Organizing larger solutions into reusable components.

### Example: Binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(root.val)
print(root.left.val)
print(root.right.val)
```

### Example: Graph adjacency list using a class

```python
class Graph:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


g = Graph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

print(g.adj)
```

This example represents an undirected graph.

### Competitive programming priorities

Focus on understanding:

1. Classes and objects.
2. Constructors and instance attributes.
3. Instance methods.
4. Inheritance and polymorphism at a basic level.
5. `__repr__` and other useful magic methods.
6. Dataclasses and `default_factory`.
7. How classes can represent data structures.

For most contest problems, algorithm selection, time complexity, space complexity, and Python's built-in data structures are more important than advanced OOP design patterns.

---

## 16. Practice Checklist

Use this checklist to track your progress.

### Beginner

- [ ] Create a `Student` class with name, ID, and marks.
- [ ] Create multiple objects of the same class.
- [ ] Implement methods to display and update object information.
- [ ] Practice constructors with default arguments.
- [ ] Explain the difference between instance and class variables.
- [ ] Implement instance, class, and static methods.

### Intermediate

- [ ] Build a `BankAccount` class with deposit and withdrawal validation.
- [ ] Implement inheritance using `Animal`, `Dog`, and `Cat`.
- [ ] Demonstrate method overriding and polymorphism.
- [ ] Create an abstract `Shape` class.
- [ ] Use properties to validate attributes.
- [ ] Overload `+` for a custom `Vector` class.
- [ ] Build a `Car` class using composition.
- [ ] Create a data class with a mutable field using `default_factory`.

### Advanced practice

- [ ] Implement a linked list using node objects.
- [ ] Implement a binary tree with traversal methods.
- [ ] Create a graph class with BFS and DFS.
- [ ] Build a priority queue wrapper using Python's `heapq`.
- [ ] Design a small system using composition and clear class interfaces.

---

## Final Notes

- A class is a blueprint; an object is an instance.
- Use `self` to access instance state.
- Use class variables for genuinely shared attributes.
- Use properties when attribute access needs validation or computation.
- Use inheritance for meaningful **is-a** relationships.
- Use composition for **has-a** relationships.
- Use polymorphism to work with different objects through a common interface.
- Use abstract base classes when you need to define a required interface.
- Use magic methods when custom objects should work naturally with Python operations.
- Use dataclasses to reduce boilerplate for data-focused classes.

**Recommended learning order:** Classes and objects → Constructors → Variables → Methods → Encapsulation → Inheritance → Polymorphism → Abstraction → Properties → Magic methods → Composition → Dataclasses.
