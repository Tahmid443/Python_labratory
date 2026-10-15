from dataclasses import dataclass, field, asdict, astuple

@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1)
print(p1 == Point(0, 0))
print(p1.distance(p2))

# With defaults
@dataclass
class User:
    name: str
    age: int = 0
    tags: list = field(default_factory=list)

u = User("Alice", 30)
u.tags.append("admin")
print(u)

# Frozen (immutable)
@dataclass(frozen=True)
class Config:
    host: str
    port: int

c = Config("localhost", 8080)
print(c)
# c.port = 9090  # FrozenInstanceError
print(hash(c))   # hashable

# Order
@dataclass(order=True)
class Score:
    points: int
    name: str = ""

print(sorted([Score(3), Score(1), Score(2)]))

# Convert
print(asdict(u))
print(astuple(u))

# Nested dataclass
@dataclass
class Address:
    city: str
    zip: str

@dataclass
class Employee:
    name: str
    address: Address

e = Employee("Bob", Address("NYC", "10001"))
print(e.address.city)