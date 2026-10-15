import math
import random

# math
print(math.pi, math.e)
print(math.sqrt(16))
print(math.floor(3.7), math.ceil(3.2), round(3.5))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.log(100, 10))
print(math.sin(math.pi / 2))
print(math.isclose(0.1 + 0.2, 0.3))

# Constants
print(math.inf, math.nan)

# random - pseudo-random
random.seed(42)
print(random.random())           # [0, 1)
print(random.randint(1, 10))     # inclusive
print(random.randrange(0, 10, 2))
print(random.uniform(1.0, 5.0))
print(random.choice(["a", "b", "c"]))
print(random.choices(["a", "b", "c"], k=5))
print(random.sample(range(100), 5))

# Shuffle in place
deck = list(range(10))
random.shuffle(deck)
print(deck)

# Weighted
print(random.choices(["win", "lose"], weights=[1, 9], k=10))

# Cryptographic random
import secrets
print(secrets.token_hex(8))
print(secrets.token_urlsafe(16))
print(secrets.randbelow(100))
print(secrets.choice("abcdef"))