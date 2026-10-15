from typing import Optional, Union, List, Dict, Tuple, Callable, Any, Iterable, Sequence

# Function annotations
def add(a: int, b: int) -> int:
    return a + b

# Optional (can be None)
def find_user(uid: int) -> Optional[dict]:
    users = {1: {"name": "Alice"}}
    return users.get(uid)

# Union (or |)
def to_int(x: Union[int, str]) -> int:
    return int(x)

def to_int_modern(x: int | str) -> int:
    return int(x)

# Collections
def process(items: List[int]) -> Dict[str, int]:
    return {"total": sum(items)}

def get_pair() -> Tuple[int, str]:
    return 1, "a"

# Callable
def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

# Any - escape hatch
def log(x: Any) -> None:
    print(x)

# Sequence (read-only, covariant)
def first(items: Sequence[int]) -> Optional[int]:
    return items[0] if items else None

# Class annotations
class User:
    name: str
    age: int
    email: Optional[str] = None

    def __init__(self, name: str, age: int, email: Optional[str] = None) -> None:
        self.name = name
        self.age = age
        self.email = email

    def greet(self) -> str:
        return f"Hello, {self.name}"

# Type aliases
Vector = List[float]
Matrix = List[Vector]

def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))

# NewType (distinct types)
from typing import NewType
UserId = NewType("UserId", int)

def get_user(uid: UserId) -> User:
    return User("Alice", 30)

# Runtime check (annotations not enforced)
print(add(1, 2))
# print(add("a", "b"))  # works at runtime