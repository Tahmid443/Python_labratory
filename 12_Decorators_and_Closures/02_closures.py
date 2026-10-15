def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c(), c(), c())

# Closure captures variable, not value
def make_multipliers():
    funcs = []
    for i in range(3):
        funcs.append(lambda x: x * i)
    return funcs

# BUG: all use final i=2
for f in make_multipliers():
    print(f(10), end=" ")
print()

# Fix with default argument
def make_multipliers_fixed():
    funcs = []
    for i in range(3):
        funcs.append(lambda x, i=i: x * i)
    return funcs

for f in make_multipliers_fixed():
    print(f(10), end=" ")
print()

# Closure inspection
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f.__closure__[0].cell_contents)

# Practical: memoization
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))