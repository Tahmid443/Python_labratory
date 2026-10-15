def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hi, {name}"

print(greet("Alice"))

# With parameters
def retry(max_attempts=3, delay=0.1):
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def flaky():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

# Rate limiter
def rate_limit(calls_per_second):
    import time
    min_interval = 1.0 / calls_per_second
    def decorator(func):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(2)
def api_call(x):
    return x

for i in range(3):
    api_call(i)
print("Done")