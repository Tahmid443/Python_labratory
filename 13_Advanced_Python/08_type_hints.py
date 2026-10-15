from typing import List, Dict, Set, Tuple, Optional, Union, Callable, Any, Iterable

# Basic
def greet(name: str) -> str:
    return f"Hello, {name}"

# Collections
def total(nums: List[int]) -> int:
    return sum(nums)

def lookup(m: Dict[str, int], k: str) -> Optional[int]:
    return m.get(k)

# Union (or | in 3.10+)
def parse(x: Union[int, str]) -> int:
    return int(x)

def parse2(x: int | str) -> int:   # 3.10+
    return int(x)

# Tuple
def point() -> Tuple[int, int]:
    return (1, 2)

def variadic() -> Tuple[int, ...]:
    return (1, 2, 3)

# Callable
def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

# Any
def log(x: Any) -> None:
    print(x)

# Iterable
def process(items: Iterable[int]) -> List[int]:
    return [x * 2 for x in items]

# Type aliases
Vector = List[float]

def norm(v: Vector) -> float:
    return sum(x ** 2 for x in v) ** 0.5

# Class methods
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, {self.name}"

# Generic function
from typing import TypeVar
T = TypeVar("T")

def first(lst: List[T]) -> Optional[T]:
    return lst[0] if lst else None

# New syntax 3.12
# def greet(name: str) -> str: ...
# type Vector = list[float]

# Type hints are NOT enforced at runtime
print(greet(42))   # works, but type-checker warns