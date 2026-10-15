from functools import (
    wraps, lru_cache, cache, cached_property,
    partial, partialmethod, reduce, singledispatch
)

# wraps
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logged
def greet(name):
    """Say hi."""
    return f"Hi {name}"

print(greet("Alice"))
print(greet.__name__, greet.__doc__)

# lru_cache
@lru_cache(maxsize=128)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
print(fib.cache_info())
fib.cache_clear()

# cache (unbounded)
@cache
def square(x):
    print("computing")
    return x * x

square(4); square(4)

# partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(4), cube(2))

# reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))

# singledispatch
@singledispatch
def describe(x):
    return f"Unknown: {x}"

@describe.register(int)
def _(x):
    return f"Int: {x}"

@describe.register(str)
def _(x):
    return f"String: {x}"

print(describe(1))
print(describe("hi"))
print(describe(1.5))