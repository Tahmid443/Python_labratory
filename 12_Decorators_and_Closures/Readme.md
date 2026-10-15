# 12. Decorators and Closures in Python

This folder covers **nested functions, closures, decorators, decorators with arguments, `functools.wraps`, and practical decorator patterns**.

These concepts help you write reusable, modular Python code. They are useful for logging, measuring execution time, caching results, validating inputs, retrying failed operations, and understanding how frameworks such as Flask use decorators.

## 📁 Folder Structure

```text
12_Decorators_and_Closures/
├── 01_nested_functions.py
├── 02_closures.py
├── 03_decorators_basics.py
├── 04_decorators_with_arguments.py
├── 05_functools_wraps.py
└── 06_practical_decorators.py
```

## 📚 Table of Contents

1. [Nested Functions](#1-nested-functions)
2. [Closures](#2-closures)
3. [Decorators Basics](#3-decorators-basics)
4. [Decorators with Arguments](#4-decorators-with-arguments)
5. [`functools.wraps`](#5-functoolswraps)
6. [Useful `functools` Tools](#6-useful-functools-tools)
7. [Practical Decorators](#7-practical-decorators)
8. [Common Mistakes](#8-common-mistakes)
9. [Time and Space Complexity](#9-time-and-space-complexity)
10. [Competitive Programming Applications](#10-competitive-programming-applications)
11. [Practice Checklist](#11-practice-checklist)

---

## 1. Nested Functions

**File:** `01_nested_functions.py`

### 1.1 What Is a Nested Function?

A nested function is a function defined inside another function.

```python
def outer():
    print("Outer start")

    def inner():
        print("Inner")

    inner()
    inner()
    print("Outer end")


outer()
```

Output:

```text
Outer start
Inner
Inner
Outer end
```

The `inner()` function is defined inside `outer()`. It is available within the enclosing function's scope.

### 1.2 Returning a Nested Function

A function can return another function as a value.

```python
def make_adder(n):
    def add(x):
        return x + n

    return add


add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))   # 8
print(add10(3))  # 13
```

Here:

- `make_adder(5)` returns a function that adds 5.
- `make_adder(10)` returns a function that adds 10.
- Each returned function retains access to its enclosing variable `n`.

This example introduces the concept of a **closure**, which is explained in the next section.

### 1.3 Multiple Levels of Nesting

```python
def a():
    def b():
        def c():
            return "deep"

        return c()

    return b()


print(a())  # deep
```

Nested functions can access names from their enclosing scopes, subject to Python's scope rules.

Deep nesting is possible, but excessive nesting can make code difficult to read.

### 1.4 Returning Multiple Functions

```python
def make_ops():
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    return add, sub, mul


add, sub, mul = make_ops()

print(add(2, 3))  # 5
print(sub(5, 2))  # 3
print(mul(4, 3))  # 12
```

Python returns a tuple containing the three function objects, which can be unpacked into separate variables.

**Key takeaway:** Functions are first-class objects in Python. They can be assigned to variables, passed to other functions, and returned from functions.

---

## 2. Closures

**File:** `02_closures.py`

### 2.1 What Is a Closure?

A **closure** is a function that retains access to variables from its enclosing scope even after the enclosing function has finished executing.

```python
def outer(x):
    def inner(y):
        return x + y

    return inner


f = outer(10)

print(f(5))   # 15
print(f(20))  # 30
```

Although `outer()` has already returned, `inner()` can still access `x`.

Closures are useful when you want to preserve state without creating a class.

### 2.2 Closures with Mutable State: `nonlocal`

The `nonlocal` keyword allows a nested function to reassign a variable defined in an enclosing function scope.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3
```

The variable `count` persists between calls to `increment()`.

Without `nonlocal`, the assignment `count += 1` would treat `count` as a local variable in `increment()`, causing an `UnboundLocalError` when Python tries to read it before assigning it.

### 2.3 Closure Variables and the Late-Binding Problem

Consider this example:

```python
def make_multipliers():
    funcs = []

    for i in range(3):
        funcs.append(lambda x: x * i)

    return funcs


for f in make_multipliers():
    print(f(10), end=" ")

# Output: 20 20 20
```

Why does this happen?

The lambdas capture access to the variable `i`, not a separate snapshot of its value for each iteration. When the returned functions are called, the loop has finished and `i` is `2`.

### 2.4 Fixing Late Binding with Default Arguments

```python
def make_multipliers_fixed():
    funcs = []

    for i in range(3):
        funcs.append(lambda x, i=i: x * i)

    return funcs


for f in make_multipliers_fixed():
    print(f(10), end=" ")

# Output: 0 10 20
```

The default argument `i=i` captures the current value of `i` when each lambda is created.

Another option is to use a nested function:

```python
def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply


multipliers = [make_multiplier(i) for i in range(3)]

print([f(10) for f in multipliers])
# [0, 10, 20]
```

### 2.5 Inspecting a Closure

```python
def outer(x):
    def inner(y):
        return x + y

    return inner


f = outer(10)

print(f.__closure__[0].cell_contents)  # 10
```

`__closure__` exposes the closure cells associated with a function. The order of cells corresponds to the function's free-variable metadata, so avoid assuming that a particular index always represents a particular variable in arbitrary functions.

This attribute is mainly useful for debugging and learning.

### 2.6 Closures for Memoization

Memoization stores results so repeated calls with the same arguments can reuse previous computations.

```python
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
```

The `cache` dictionary persists because `wrapper()` retains access to it through a closure.

**Important limitations:**

- The arguments used as dictionary keys must be hashable.
- This implementation handles positional arguments only.
- The cache grows as new argument combinations are encountered.
- It does not implement cache expiration or eviction.
- Recursive calls to `fib()` use the decorated function name, so they benefit from the cache.

For standard memoization, Python's `functools.lru_cache` is often the better choice.

---

## 3. Decorators Basics

**File:** `03_decorators_basics.py`

### 3.1 What Is a Decorator?

A **decorator** is a callable that takes another callable and returns a callable, usually to extend or modify its behavior.

Decorators are commonly used for:

- Logging function calls
- Measuring execution time
- Caching results
- Checking permissions
- Validating arguments
- Retrying failed operations

### 3.2 Creating Your First Decorator

```python
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
```

Output:

```text
Before greet
Hello, Alice
After greet
```

The syntax:

```python
@my_decorator
def greet(name):
    ...
```

is equivalent to:

```python
def greet(name):
    ...


greet = my_decorator(greet)
```

The decorator replaces the name `greet` with the callable returned by `my_decorator`.

### 3.3 Understanding `*args` and `**kwargs`

Decorators often need to work with functions that accept different arguments.

- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

This allows the wrapper to forward the original arguments without knowing the wrapped function's signature in advance.

### 3.4 A Timing Decorator

```python
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.4f}s")

        return result

    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


slow_sum(1_000_000)
```

`time.perf_counter()` is appropriate for measuring elapsed duration. It is generally preferable to `time.time()` for benchmarking.

This decorator measures successful execution. If the wrapped function raises an exception, the timing output will not be printed by this version.

### 3.5 A Logging Decorator

```python
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    return a + b


print(add(2, 3))
```

The decorator logs the call before executing the original function.

Be careful when logging sensitive arguments, such as passwords, authentication tokens, or private information.

### 3.6 Applying Multiple Decorators

```python
@timer
@log
def demo():
    return "done"


demo()
```

Decorators are applied from the bottom upward. This is equivalent to:

```python
demo = timer(log(demo))
```

Therefore:

1. `log` decorates the original `demo`.
2. `timer` decorates the result.
3. Calling `demo()` executes the outer timing wrapper, which invokes the logging wrapper.

The order matters because decorators may change behavior.

---

## 4. Decorators with Arguments

**File:** `04_decorators_with_arguments.py`

A regular decorator accepts the function being decorated.

A **decorator factory** accepts configuration and returns a decorator.

This adds an extra function level:

```text
Decorator factory
       ↓
    Decorator
       ↓
     Wrapper
       ↓
Original function
```

### 4.1 Repeating a Function

```python
from functools import wraps


def repeat(times):
    def decorator(func):
        @wraps(func)
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
# ['Hi, Alice', 'Hi, Alice', 'Hi, Alice']
```

Here, `repeat(3)` configures the decorator to call the function three times.

**Design consideration:** This implementation returns a list of results, changing the original function's return behavior. That is acceptable when intentional, but decorators should preserve the original contract when possible.

### 4.2 A Retry Decorator

```python
import time
from functools import wraps


def retry(max_attempts=3, delay=0.1):
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    if delay < 0:
        raise ValueError("delay cannot be negative")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator


@retry(max_attempts=3, delay=0.1)
def flaky():
    import random

    if random.random() < 0.7:
        raise ValueError("Random failure")

    return "Success"
```

The wrapper retries the operation after an exception and re-raises the last exception if every attempt fails.

**Use retries carefully:**

- Retry only failures that may be temporary.
- Do not blindly retry operations that can cause duplicate side effects.
- For network operations, use sensible timeouts and consider exponential backoff.
- Catch specific exception types where possible.
- Avoid using retries to hide programming errors.

### 4.3 A Rate-Limiting Decorator

A simple rate limiter can enforce a minimum interval between calls.

```python
import time
from functools import wraps


def rate_limit(calls_per_second):
    if calls_per_second <= 0:
        raise ValueError("calls_per_second must be positive")

    min_interval = 1.0 / calls_per_second

    def decorator(func):
        last_called = [None]

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.monotonic()

            if last_called[0] is not None:
                elapsed = now - last_called[0]

                if elapsed < min_interval:
                    time.sleep(min_interval - elapsed)

            result = func(*args, **kwargs)
            last_called[0] = time.monotonic()

            return result

        return wrapper

    return decorator


@rate_limit(2)
def api_call(value):
    return value
```

This is a simple, sequential rate limiter. It spaces successful calls by at least the configured interval, but it is not a complete concurrent or distributed rate-limiting system.

`time.monotonic()` is used because it measures elapsed time without being affected by wall-clock adjustments.

---

## 5. `functools.wraps`

**File:** `05_functools_wraps.py`

### 5.1 The Problem Without `wraps`

```python
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@bad_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}"


print(greet.__name__)  # wrapper
print(greet.__doc__)   # None
```

The decorated function's name and docstring now belong to the wrapper.

This can make debugging, documentation, and introspection more confusing.

### 5.2 Preserving Metadata with `@wraps`

```python
from functools import wraps


def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@good_decorator
def greet2(name):
    """Greet someone."""
    return f"Hello, {name}"


print(greet2.__name__)  # greet2
print(greet2.__doc__)   # Greet someone.
```

`@wraps(func)` copies important metadata from the original function to the wrapper and sets `__wrapped__` to the wrapped callable.

**Best practice:** Use `@wraps(func)` in almost every custom function decorator.

### 5.3 Why Metadata Matters

Preserving metadata helps:

- Debugging and readable tracebacks
- Documentation tools
- Introspection
- Frameworks that inspect functions
- Accessing the wrapped function through `__wrapped__`

`wraps` preserves important metadata, but it does not make the wrapper's actual Python code or runtime calling behavior identical to the original function.

---

## 6. Useful `functools` Tools

Python's `functools` module provides utilities for higher-order functions and callable behavior.

### 6.1 `lru_cache`

`lru_cache` caches results and can significantly speed up recursive functions with repeated subproblems.

```python
from functools import lru_cache


@lru_cache(maxsize=128)
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(50))
print(fib.cache_info())
```

`cache_info()` reports cache statistics, including hits, misses, the maximum cache size, and the current number of stored entries.

For many dynamic programming problems, caching overlapping subproblems can turn an exponential recursive solution into a polynomial-time solution.

For Fibonacci, memoization reduces the time complexity from \(O(2^n)\) for the naive recursive algorithm to \(O(n)\) with caching.

Important considerations:

- Arguments must be hashable.
- Cached values are reused, so functions with side effects may not behave as expected.
- A bounded cache may evict older entries.
- `lru_cache` does not automatically understand the mathematical meaning of the function; it caches calls according to their arguments.

### 6.2 `cached_property`

`cached_property` computes a property and stores the resulting value on the instance after the first successful access.

```python
from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Calculating area")
        return 3.141592653589793 * self.radius ** 2


circle = Circle(5)

print(circle.area)  # Calculates
print(circle.area)  # Uses cached value
```

This is useful for expensive calculations that are repeatedly accessed on an object.

**Important:** If the underlying data changes, the cached value may become stale. You can delete the cached attribute to calculate it again:

```python
del circle.area
print(circle.area)
```

### 6.3 `partial`

`functools.partial` creates a new callable with some arguments already supplied.

```python
from functools import partial


def power(base, exp):
    return base ** exp


square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))  # 25
print(cube(3))    # 27
```

This is useful when you want to configure a function once and reuse it with fewer arguments.

### 6.4 `reduce`

`reduce()` applies a binary function cumulatively to the items of an iterable.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print(total)  # 10
```

For summation, `sum(numbers)` is usually clearer and preferable.

`reduce()` is useful when the operation genuinely involves combining elements step by step into a single result.

---

## 7. Practical Decorators

**File:** `06_practical_decorators.py`

This section brings together the decorator patterns introduced earlier.

### 7.1 Timing

```python
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__}: {elapsed:.4f}s")

    return wrapper
```

The `finally` block measures elapsed time whether the wrapped function succeeds or raises an exception.

For serious benchmarking, run repeated measurements and account for environment noise.

### 7.2 Logging

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Calling %s", func.__name__)
        return func(*args, **kwargs)

    return wrapper
```

Using the logging module makes it easier to configure log levels and output destinations than relying exclusively on `print()`.

### 7.3 Retry

```python
import time
from functools import wraps


def retry(times=3, exceptions=(Exception,), delay=0.5):
    if times < 1:
        raise ValueError("times must be at least 1")

    if delay < 0:
        raise ValueError("delay cannot be negative")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == times:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator
```

Example:

```python
@retry(times=3, exceptions=(TimeoutError,), delay=0.2)
def request_data():
    # Replace with a real operation that can time out.
    return "data"
```

The exception tuple limits which failures trigger another attempt. Choose exception types according to the operation being retried.

### 7.4 Cache

```python
from functools import wraps


def cache(func):
    store = {}

    @wraps(func)
    def wrapper(*args):
        if args not in store:
            store[args] = func(*args)

        return store[args]

    return wrapper
```

This is a small educational memoization decorator. Because it uses `args` as dictionary keys, all positional arguments must be hashable. It does not handle keyword arguments or provide eviction.

For general-purpose caching, prefer `functools.cache` or `functools.lru_cache`.

### 7.5 Validate Types

```python
import inspect
from functools import wraps


def validate_types(**expected):
    def decorator(func):
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)

            for name, expected_type in expected.items():
                if name in bound.arguments:
                    value = bound.arguments[name]

                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"{name} must be "
                            f"{expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorator
```

Usage:

```python
@validate_types(a=int, b=int)
def add(a, b):
    return a + b


print(add(1, 2))  # 3

# add(1, "2")  # TypeError
```

**Python detail:** `isinstance(True, int)` is `True` because `bool` is a subclass of `int`. If exact type matching is required, compare with `type(value) is expected_type` instead.

Runtime type validation is a design choice; Python does not require every function argument to be checked this way.

### 7.6 Count Function Calls

```python
from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    return f"Hi {name}"


greet("Alice")
greet("Bob")
greet("Charlie")

print(greet.calls)  # 3
```

The wrapper stores a counter as an attribute. This is convenient for simple debugging and learning.

For concurrent programs, this simple increment is not a thread-safe counting mechanism.

---

## 8. Common Mistakes

### Mistake 1: Forgetting to Return the Result

Incorrect:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper
```

The wrapper implicitly returns `None`, even if the original function returns a value.

Correct:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

### Mistake 2: Forgetting `@wraps`

Without `@wraps(func)`, the decorated function may expose the wrapper's name and docstring instead of the original function's metadata.

### Mistake 3: Confusing Decorators with Decorator Factories

A basic decorator receives the function:

```python
@my_decorator
def greet():
    pass
```

A decorator factory receives configuration and returns a decorator:

```python
@repeat(3)
def greet():
    pass
```

The second form has an additional function-call level.

### Mistake 4: Using Mutable Global State Unnecessarily

Closures can retain state without requiring a global variable. However, shared closure state can still introduce concurrency issues and unexpected coupling if it is not designed carefully.

### Mistake 5: Catching Every Exception During Retries

Blindly retrying all exceptions can hide bugs and repeat operations that have already produced side effects. Retry only appropriate, preferably transient, failures.

### Mistake 6: Using a Cache with Unhashable Arguments

This fails because lists cannot be dictionary keys:

```python
# cache[[1, 2, 3]] = "result"  # TypeError
```

If a custom cache must support such arguments, you need an explicit, reliable key strategy. Do not assume converting every argument to a tuple is always sufficient.

### Mistake 7: Overusing Decorators

Decorators are powerful, but they can obscure control flow when stacked excessively. Use them when the shared behavior is clear and the added abstraction improves readability.

---

## 9. Time and Space Complexity

The exact cost depends on the wrapped function and the decorator's implementation.

| Pattern | Typical Additional Cost |
|---|---|
| Simple wrapper | \(O(1)\) time and space per call, excluding the original function |
| Timing decorator | \(O(1)\) timing overhead per call |
| Logging decorator | Depends on logging configuration and output |
| Call counter | \(O(1)\) time and space for the counter |
| Memoization cache | Expected \(O(1)\) dictionary lookup per call, plus computation on cache misses |
| `lru_cache` | Cache lookup overhead; memory bounded by `maxsize` when configured |
| Retry decorator | Up to `times` executions of the original function |
| Type-validation decorator | Depends on signature binding and the number of validated arguments |

### Memoization Example

For the Fibonacci recurrence:

\[
F(n)=F(n-1)+F(n-2)
\]

- Naive recursive Fibonacci: \(O(2^n)\) time as a common upper-bound description.
- Memoized Fibonacci: \(O(n)\) time and \(O(n)\) cache space.

The cache improves performance because each distinct input is computed once rather than repeatedly.

---

## 10. Competitive Programming Applications

Decorators and closures are useful for understanding Python's execution model, but they are not necessary in every contest solution.

### 10.1 Memoization for Dynamic Programming

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def ways(n):
    if n <= 1:
        return 1

    return ways(n - 1) + ways(n - 2)
```

This is a simple recurrence example. It counts ways to reach step `n` when each move advances one or two steps.

- Time complexity: \(O(n)\).
- Cache space: \(O(n)\).

For larger `n`, recursive depth may become a problem. An iterative DP solution avoids recursion depth concerns.

### 10.2 Timing a Solution During Practice

```python
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f"Elapsed: {elapsed:.6f}s")
        return result

    return wrapper
```

Use timing while experimenting locally. Remove debug output from submissions unless the judge explicitly expects it.

### 10.3 Closures for Configurable Behavior

```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

Closures can create reusable functions with a fixed configuration.

### 10.4 When Not to Use Decorators in Contests

Avoid unnecessary decorator complexity when:

- A direct function call is clearer.
- A wrapper makes debugging harder.
- The task is small enough that abstraction adds no value.
- The decorator introduces extra behavior or unexpected side effects.

For competitive programming, **correctness, clarity, and predictable performance** are more important than using advanced Python features unnecessarily.

---

## 11. Practice Checklist

### Beginner

- [ ] Write a nested function that returns the square of a number.
- [ ] Create an adder closure with a configurable offset.
- [ ] Implement a counter using `nonlocal`.
- [ ] Explain why lambdas in a loop may share the final loop variable.
- [ ] Write a basic decorator that prints before and after a function call.
- [ ] Preserve the original function's return value in a wrapper.
- [ ] Use `@wraps` to preserve function metadata.

### Intermediate

- [ ] Create a timing decorator using `time.perf_counter()`.
- [ ] Implement a decorator that logs function calls.
- [ ] Build a decorator factory that repeats a function a fixed number of times.
- [ ] Implement a configurable retry decorator.
- [ ] Create a call-counting decorator.
- [ ] Use `lru_cache` to optimize a recursive problem.
- [ ] Explain the difference between a decorator and a decorator factory.

### Advanced

- [ ] Build a cache decorator supporting positional and keyword arguments.
- [ ] Implement a type-validation decorator using `inspect.signature`.
- [ ] Explain late binding and fix it using a closure or default argument.
- [ ] Stack two decorators and explain their execution order.
- [ ] Design a retry decorator that supports selected exceptions and exponential backoff.
- [ ] Identify concurrency and memory issues in stateful decorators.
- [ ] Compare a closure-based implementation with a class-based implementation.

---

## Recommended Learning Order

1. `01_nested_functions.py` — Learn nested scopes and first-class functions.
2. `02_closures.py` — Understand captured variables and retained state.
3. `03_decorators_basics.py` — Build your first function decorators.
4. `04_decorators_with_arguments.py` — Learn decorator factories.
5. `05_functools_wraps.py` — Preserve metadata and explore standard utilities.
6. `06_practical_decorators.py` — Combine the patterns into reusable tools.

## Final Takeaways

- Nested functions are defined inside other functions.
- Closures retain access to variables from enclosing scopes.
- `nonlocal` allows reassignment of a variable in an enclosing function scope.
- Decorators wrap callables to add reusable behavior.
- Decorator factories allow configurable decorators.
- `functools.wraps` preserves important function metadata.
- `lru_cache` is useful for memoization and dynamic programming.
- Retry and rate-limiting decorators need careful handling of exceptions, timing, and side effects.
- Keep decorators readable and use them when they provide a clear benefit.

**Goal:** Understand how closures preserve state, how decorators transform functions, and how to use these tools to write clean, reusable Python code.
