from typing import Optional, List, Dict, Union, Callable

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def greet(name: str, times: int = 1) -> str:
    """
    Return a greeting repeated `times` times.

    Args:
        name:  Name of person.
        times: Number of repetitions.

    Returns:
        Greeting string.
    """
    return f"Hello, {name}! " * times

def process(items: List[int]) -> Optional[int]:
    """Return first positive or None."""
    for x in items:
        if x > 0:
            return x
    return None

def safe_div(a: float, b: float) -> Union[float, None]:
    if b == 0:
        return None
    return a / b

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

# Inspect annotations
print(add.__annotations__)
print(greet.__doc__)

# Type hints aren't enforced at runtime
print(add("hello", " world"))  # works, returns "hello world"

# Access docstring
help(greet)