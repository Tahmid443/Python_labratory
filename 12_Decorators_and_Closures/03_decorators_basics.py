# Function decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")

# Equivalent to:
# greet = my_decorator(greet)

# Timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1000000)

# Logging decorator
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

add(2, 3)

# Multiple decorators
@timer
@log
def demo():
    return "done"

demo()