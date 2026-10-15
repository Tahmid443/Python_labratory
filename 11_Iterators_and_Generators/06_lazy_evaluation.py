# Generators are lazy - compute on demand
def expensive(x):
    print(f"Computing {x}")
    return x * 2

# Eager - all computed
print("Eager:")
result = [expensive(x) for x in range(3)]
print(result)

print("\nLazy:")
result = (expensive(x) for x in range(3))
print("Created")
print(next(result))
print(next(result))
print(next(result))

# Infinite streams
def primes():
    """Infinite prime generator"""
    n = 2
    while True:
        is_prime = True
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1

from itertools import islice
print(list(islice(primes(), 10)))

# Pipeline (memory efficient)
def read_numbers():
    for i in range(10):
        yield i

pipeline = (
    x * 2
    for x in read_numbers()
    if x % 2 == 0
)

print(list(pipeline))

# Generator for large files
def tail(path, n):
    from collections import deque
    with open(path) as f:
        return list(deque(f, maxlen=n))

# Memory efficient sum
total = sum(x ** 2 for x in range(10000000))
print(total)

# Take while / drop while
from itertools import takewhile, dropwhile
print(list(takewhile(lambda x: x < 5, range(10))))
print(list(dropwhile(lambda x: x < 5, range(10))))