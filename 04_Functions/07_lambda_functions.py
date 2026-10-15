# Basic lambda
square = lambda x: x ** 2
print(square(5))

# Multiple args
add = lambda a, b: a + b
print(add(2, 3))

# With condition
max_of = lambda a, b: a if a > b else b
print(max_of(3, 5))

# Common usage: sorted with key
words = ["banana", "apple", "cherry"]
print(sorted(words, key=lambda w: len(w)))

# With map
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))

# With filter
print(list(filter(lambda x: x % 2 == 0, nums)))

# With reduce
from functools import reduce
print(reduce(lambda a, b: a + b, nums))

# Multiple keys
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
data.sort(key=lambda p: p[1])
print(data)

# When NOT to use: complex logic
# Bad: lambda x: (x ** 2 + 1 if x > 0 else -x) * 3
# Better: def complex_fn(x): ...