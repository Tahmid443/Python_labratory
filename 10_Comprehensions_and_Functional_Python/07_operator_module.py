from operator import (
    add, sub, mul, truediv,
    itemgetter, attrgetter, methodcaller,
    lt, le, eq, ne, gt, ge,
    and_, or_, not_,
    concat, contains,
)

# Arithmetic as functions
print(add(2, 3))
print(sub(5, 2))
print(mul(4, 3))

# With reduce
from functools import reduce
print(reduce(add, [1, 2, 3, 4]))
print(reduce(mul, [1, 2, 3, 4]))

# itemgetter - fast key functions
data = [("Alice", 30), ("Bob", 25)]
data.sort(key=itemgetter(1))
print(data)

# Get multiple fields
records = [("a", 1, "x"), ("b", 2, "y")]
getter = itemgetter(0, 2)
print([getter(r) for r in records])

# attrgetter
class P:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"P({self.x}, {self.y})"

pts = [P(1, 2), P(3, 1)]
print(sorted(pts, key=attrgetter("y")))

# methodcaller
words = ["hello", "WORLD"]
upper = methodcaller("upper")
print([upper(w) for w in words])

# Comparison operators
print(lt(1, 2), gt(1, 2), eq(1, 1))

# Logical
print(and_(True, False))
print(or_(True, False))

# Avoid lambdas for these
print(list(map(add, [1, 2, 3], [4, 5, 6])))