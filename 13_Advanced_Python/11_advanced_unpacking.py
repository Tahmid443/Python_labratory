# Deep unpacking
(a, b), c = (1, 2), 3
print(a, b, c)

# Star unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first, rest)

*init, last = [1, 2, 3, 4, 5]
print(init, last)

a, *mid, z = [1, 2, 3, 4, 5]
print(a, mid, z)

# Multiple stars (only one allowed per level)
# a, *b, *c = [1, 2, 3]  # SyntaxError

# Nested with stars
(a, *b), *c = [1, 2, 3], 4, 5
print(a, b, c)

# In function calls
def f(a, b, c, d):
    print(a, b, c, d)

args = [1, 2]
more = [3, 4]
f(*args, *more)

# Dict merge
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)

# Dict with overrides
defaults = {"host": "localhost", "port": 8080}
overrides = {"port": 9090}
config = {**defaults, **overrides}
print(config)

# Unpacking in loops
pairs = [(1, "a"), (2, "b")]
for (num, letter) in pairs:
    print(num, letter)

for i, (num, letter) in enumerate(pairs):
    print(i, num, letter)

# Ignore with _
a, _, c = (1, 2, 3)
print(a, c)

# Swap nested
p1 = [1, 2]
p2 = [3, 4]
p1[0], p2[0] = p2[0], p1[0]
print(p1, p2)

# Function returning multiple
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([1, 2, 3, 4, 5])
print(lo, hi, avg)

# Or as tuple
result = stats([1, 2, 3])
print(result)

# Extended unpacking with strings
a, *b, c = "hello"
print(a, b, c)