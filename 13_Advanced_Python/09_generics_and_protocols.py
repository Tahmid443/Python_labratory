from typing import TypeVar, Generic, Protocol, runtime_checkable

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Empty")
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

s: Stack[int] = Stack()
s.push(1)
print(s.pop())

# Generic function
def first(lst: list[T]) -> T:
    return lst[0]

# Protocol (structural typing)
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Circle"

class Square:
    def draw(self) -> str:
        return "Square"

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())
render(Square())
print(isinstance(Circle(), Drawable))

# Bound typevar
from typing import SupportsInt
def to_int(x: SupportsInt) -> int:
    return int(x)

# Constrained typevar
StrOrBytes = TypeVar("StrOrBytes", str, bytes)
def concat(a: StrOrBytes, b: StrOrBytes) -> StrOrBytes:
    return a + b