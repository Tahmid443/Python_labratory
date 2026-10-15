from functools import wraps
import time

# Without wraps - metadata lost
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}"

print(greet.__name__)   # "wrapper" - wrong!
print(greet.__doc__)    # None - wrong!

# With wraps - metadata preserved
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet2(name):
    """Greet someone."""
    return f"Hello, {name}"

print(greet2.__name__)   # "greet2"
print(greet2.__doc__)    # "Greet someone."

# Other functools
from functools import lru_cache, cached_property, partial

@lru_cache(maxsize=128)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))
print(fib.cache_info())

# partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5), cube(3))

# reduce
from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))