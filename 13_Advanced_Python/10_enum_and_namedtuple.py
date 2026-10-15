from enum import Enum, IntEnum, auto, Flag, IntFlag
from collections import namedtuple

# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

# Iterate
for c in Color:
    print(c.name, c.value)

# Access by value
print(Color(1))

# Auto values
class Day(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()

print(Day.MON.value)

# IntEnum (can compare to int)
class Size(IntEnum):
    S = 1
    M = 2
    L = 3

print(Size.S == 1)
print(Size.S < Size.M)

# Flag (bitmask)
class Perm(Flag):
    R = auto()
    W = auto()
    X = auto()

rw = Perm.R | Perm.W
print(rw)
print(Perm.R in rw)

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
print(p[0], p[1])
print(p)
x, y = p
print(x, y)

# With defaults
Point3D = namedtuple("Point3D", ["x", "y", "z"], defaults=[0])
print(Point3D(1, 2))

# Methods via subclass
class Point2(namedtuple("Point", ["x", "y"])):
    __slots__ = ()
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1, p2 = Point2(0, 0), Point2(3, 4)
print(p1.dist(p2))

# Enum as dict keys
colors = {Color.RED: "red", Color.GREEN: "green"}
print(colors[Color.RED])