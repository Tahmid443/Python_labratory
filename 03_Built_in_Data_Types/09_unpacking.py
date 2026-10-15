# Basic
a, b = 1, 2
print(a, b)

# With star
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

# Star at start
*start, last = [1, 2, 3, 4]
print(start, last)

# Swap
a, b = b, a

# Nested
(a, b), c = (1, 2), 3
print(a, b, c)

# In function calls
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))

# Dict unpacking
def greet(name, age):
    return f"{name} is {age}"

info = {"name": "Alice", "age": 30}
print(greet(**info))

# Merge dicts
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)

# Merge lists
l1 = [1, 2]
l2 = [3, 4]
print([*l1, *l2])

# Ignore values
_, b, _ = (1, 2, 3)
print(b)