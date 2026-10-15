from functools import wraps
import time
import logging

logging.basicConfig(level=logging.INFO)

# 1. Timing
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper

# 2. Logging
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

# 3. Retry
def retry(times=3, exceptions=(Exception,), delay=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# 4. Cache
def cache(func):
    store = {}
    @wraps(func)
    def wrapper(*args):
        if args not in store:
            store[args] = func(*args)
        return store[args]
    return wrapper

# 5. Validate types
def validate_types(**expected):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            for name, typ in expected.items():
                if name in bound.arguments:
                    val = bound.arguments[name]
                    if not isinstance(val, typ):
                        raise TypeError(f"{name} must be {typ.__name__}, got {type(val).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 6. Count calls
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Usage
@timer
@log_calls
def compute(n):
    return sum(i ** 2 for i in range(n))

@validate_types(a=int, b=int)
def add(a, b):
    return a + b

@count_calls
def greet(name):
    return f"Hi {name}"

compute(100000)
print(add(1, 2))
# add(1, "2")   # TypeError
greet("a"); greet("b"); greet("c")
print(f"greet called {greet.calls} times")