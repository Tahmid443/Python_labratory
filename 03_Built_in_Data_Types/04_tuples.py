# Creating
t = (1, 2, 3)
single = (1,)      # comma needed!
empty = ()
from_tuple = tuple([1, 2, 3])

# Access
print(t[0], t[-1])
print(t[1:])

# Unpacking
a, b, c = t
print(a, b, c)

# Nested
nested = (1, (2, 3), 4)
print(nested[1][0])

# Immutable
# t[0] = 100  # TypeError

# Methods
print(t.count(1))
print(t.index(2))

# Concatenation
print((1, 2) + (3, 4))
print((1, 2) * 2)

# Membership
print(2 in t)

# Swap using tuples
x, y = 1, 2
x, y = y, x
print(x, y)

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)