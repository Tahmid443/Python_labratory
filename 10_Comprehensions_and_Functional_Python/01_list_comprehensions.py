# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
flat = [x for row in matrix for x in row]

# Multiple conditions
result = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]

# Transform
words = ["hello", "world"]
upper = [w.upper() for w in words]
lengths = [len(w) for w in words]

# Function calls
import math
roots = [math.sqrt(x) for x in range(1, 6)]

# Strings
s = "hello"
chars = [c for c in s if c not in "aeiou"]

# Filtering with function
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primes = [x for x in range(50) if is_prime(x)]

# vs map/filter
result1 = [x * 2 for x in range(5) if x > 1]
result2 = list(map(lambda x: x * 2, filter(lambda x: x > 1, range(5))))
print(result1, result2)

# Readability - avoid deep nesting
# Bad
# [[y*2 for y in [x+1]] for x in range(3)]