def simple_gen():
    yield 1
    yield 2
    yield 3

for x in simple_gen():
    print(x, end=" ")
print()

# Lazy computation
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

# Infinite generator
def naturals():
    n = 1
    while True:
        yield n
        n += 1

# Take first 5 (manual)
gen = naturals()
print([next(gen) for _ in range(5)])

# With islice
from itertools import islice
print(list(islice(naturals(), 5)))

# Read large files efficiently
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip()

# Pipeline
def read_nums():
    for x in ["1", "2", "3"]:
        yield int(x)

def squared(nums):
    for n in nums:
        yield n ** 2

def filtered(nums):
    for n in nums:
        if n > 1:
            yield n

result = list(filtered(squared(read_nums())))
print(result)

# Generator return value
def gen_with_return():
    yield 1
    yield 2
    return "done"

g = gen_with_return()
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration as e:
    print(f"Return: {e.value}")