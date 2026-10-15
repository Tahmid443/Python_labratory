# Creating
s = {1, 2, 3}
empty = set()  # not {} (that's a dict)
from_list = set([1, 2, 2, 3, 3])

# No duplicates
print(from_list)   # {1, 2, 3}

# Add / remove
s.add(4)
s.discard(1)       # no error if missing
s.remove(2)        # raises KeyError if missing
print(s)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union
print(a & b)    # intersection
print(a - b)    # difference
print(a ^ b)    # symmetric difference

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Subset / superset
print({1, 2}.issubset(a))
print(a.issuperset({1, 2}))

# Frozen set (immutable)
fs = frozenset([1, 2, 3])
print(fs)

# Common use: deduplication
nums = [1, 2, 2, 3, 3, 3]
print(list(set(nums)))