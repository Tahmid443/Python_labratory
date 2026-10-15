# 13 — Advanced Python

This folder covers important Python concepts that help you write safer, cleaner, more reusable, and more maintainable code.

These topics are especially useful when working with custom classes, object-oriented programming, large codebases, libraries, and advanced data structures.

## 📂 Project Structure

```text
13_Advanced_Python/
├── 01_shallow_deep_copy.py
├── 02_mutable_default_arguments.py
├── 03_context_managers.py
├── 04_custom_context_managers.py
├── 05_descriptors.py
├── 06_mro_and_super.py
├── 07_dunder_methods.py
├── 08_type_hints.py
├── 09_generics_and_protocols.py
├── 10_enum_and_namedtuple.py
└── 11_advanced_unpacking.py
```

---

## 1. Shallow Copy and Deep Copy

**File:** `01_shallow_deep_copy.py`

Copying creates a new reference or object depending on the operation. Understanding the difference is essential when working with nested lists, dictionaries, and custom objects.

### Assignment versus copying

```python
import copy

a = [1, 2, 3]

b = a                  # Same object
c = a.copy()           # Shallow copy
d = list(a)            # Shallow copy
e = a[:]               # Shallow copy
f = copy.deepcopy(a)   # Deep copy

b.append(4)

print(a)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3]
```

Assignment does not copy an object. It creates another reference to the same object.

### Shallow copy

A shallow copy creates a new outer object, but references to nested objects are shared.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0].append(99)

print(original)  # [[1, 2, 99], [3, 4]]
print(shallow)   # [[1, 2, 99], [3, 4]]
```

Both outer lists are different, but their first inner list is the same object.

### Deep copy

A deep copy recursively copies nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(99)

print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[1, 2, 99], [3, 4]]
```

Changing the copied inner list does not change the original.

### Custom copying

Python allows classes to customize their copying behavior using `__copy__()` and `__deepcopy__()`.

```python
import copy

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

node = Node(1, [Node(2), Node(3)])

duplicate = copy.deepcopy(node)
duplicate.children[0].value = 99

print(node.children[0].value)       # 2
print(duplicate.children[0].value)  # 99
```

### Comparison

| Operation | New outer object? | Nested mutable objects copied? |
|---|---|---|
| `b = a` | No | No |
| `a.copy()` | Yes | No |
| `list(a)` | Yes | No |
| `a[:]` | Yes | No |
| `copy.copy(a)` | Yes | No |
| `copy.deepcopy(a)` | Yes | Yes, recursively |

**Important:** Deep copying can be more expensive than shallow copying, particularly for large nested structures. It can also require special handling for objects such as files, sockets, and custom resource managers.

---

## 2. Mutable Default Arguments

**File:** `02_mutable_default_arguments.py`

A mutable default argument is an object such as a list, dictionary, or set used as a function's default parameter.

Python evaluates default argument expressions **once, when the function is defined**, not every time the function is called.

### The classic mistake

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]
print(add_item(3))  # [1, 2, 3]
```

All three calls reuse the same default list.

### The correct solution

Use `None` as a sentinel and create a new list inside the function.

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2]
```

The same principle applies to dictionaries and sets.

```python
def add_setting(key, settings=None):
    if settings is None:
        settings = {}

    settings[key] = True
    return settings

print(add_setting("debug"))  # {'debug': True}
print(add_setting("cache"))  # {'cache': True}
```

### When mutable defaults are acceptable

A mutable default is not automatically wrong. It can be intentional when shared state is part of the design, such as a persistent cache.

However, explicit cache objects, closures, or `functools.lru_cache` may make the intention clearer.

**Rule:** If a function should get a fresh mutable object on each call, use `None` and initialize the object inside the function.

---

## 3. Context Managers

**File:** `03_context_managers.py`

A context manager manages setup and cleanup around a block of code.

The `with` statement is commonly used to close files automatically, even if an exception occurs.

### Using `with`

```python
with open("test.txt", "w") as file:
    file.write("Hello, Python!")

with open("test.txt", "r") as file:
    print(file.read())
```

The file is closed automatically when the block exits.

### Without a context manager

```python
file = open("test.txt")

try:
    print(file.read())
finally:
    file.close()
```

The `finally` block ensures cleanup even if an exception is raised.

### The context manager protocol

A class-based context manager usually implements two methods:

- `__enter__()` — performs setup and returns the value assigned after `as`.
- `__exit__(exc_type, exc_value, traceback)` — performs cleanup and determines whether an exception should be suppressed.

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False

with Timer():
    sum(range(1_000_000))
```

Returning `False` means exceptions are not suppressed.

### Exception suppression

If `__exit__()` returns a truthy value, it suppresses an exception raised inside the `with` block.

```python
class SuppressValueError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return (
            exc_type is not None
            and issubclass(exc_type, ValueError)
        )

with SuppressValueError():
    int("abc")

print("Continued")
```

The `ValueError` is suppressed, so execution continues.

**Caution:** Suppress exceptions only when doing so is intentional. Otherwise, errors may go unnoticed.

### Multiple context managers

```python
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("A")
    b.write("B")
```

Both resources are managed automatically.

---

## 4. Custom Context Managers

**File:** `04_custom_context_managers.py`

You can create your own context managers using either a class or the `contextlib.contextmanager` decorator.

### Class-based implementation

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

        return False

with FileManager("test.txt", "w") as file:
    file.write("Hello!")
```

### Generator-based implementation

For simple setup and cleanup logic, `@contextmanager` is often more concise.

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    file = open(filename, mode)

    try:
        yield file
    finally:
        file.close()

with managed_file("test.txt", "r") as file:
    print(file.read())
```

The value yielded by the generator becomes the value after `as`. Cleanup belongs in the `finally` block.

### Timing utility

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()

    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")

with timer("Calculation"):
    sum(range(1_000_000))
```

### Exception suppression with `contextlib`

Python already provides a standard utility for this:

```python
from contextlib import suppress

with suppress(ValueError):
    int("abc")

print("Continued")
```

### Transaction-style cleanup

A database transaction context manager may commit on success and roll back on failure.

```python
from contextlib import contextmanager

@contextmanager
def transaction(connection):
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
```

The exact transaction behavior depends on the database driver and connection configuration.

### Temporary resources

Use standard-library utilities such as `tempfile.TemporaryDirectory()` when possible instead of manually creating and deleting temporary directories.

**Best practice:** Prefer built-in context managers and `contextlib` utilities when they already solve the problem.

---

## 5. Descriptors

**File:** `05_descriptors.py`

A descriptor is an object that defines one or more of the following methods:

- `__get__()` — controls attribute access.
- `__set__()` — controls attribute assignment.
- `__delete__()` — controls attribute deletion.

Descriptors are a foundation of Python's object model. Properties, methods, and many framework features use descriptor behavior.

### Validation descriptor

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be non-negative")

        setattr(obj, self.name, value)


class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


product = Product(10, 5)
print(product.total())  # 50

# product.price = -1  # ValueError
```

`__set_name__()` automatically tells the descriptor which attribute it manages.

The example accepts zero as well as positive values, so the error message correctly says *non-negative*.

### Type-checking descriptor

```python
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}"
            )

        setattr(obj, self.name, value)


class User:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Alice", 30)
print(user.name, user.age)
```

### Data and non-data descriptors

- A **data descriptor** defines `__set__()` or `__delete__()` in addition to attribute retrieval.
- A **non-data descriptor** defines `__get__()` but neither `__set__()` nor `__delete__()`.

Descriptors are useful for reusable validation, lazy attributes, computed values, and framework internals.

**Learning priority:** Understand what descriptors do and recognize their role in `property` and methods. Implementing custom descriptors is usually a later-stage topic.

---

## 6. MRO and `super()`

**File:** `06_mro_and_super.py`

MRO stands for **Method Resolution Order**. It determines the order Python uses to look up methods and attributes in an inheritance hierarchy.

Python uses the C3 linearization algorithm to construct the MRO.

### Basic inheritance

```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B -> " + super().greet()

class C(A):
    def greet(self):
        return "C -> " + super().greet()

class D(B, C):
    def greet(self):
        return "D -> " + super().greet()


print(D().greet())
print(D.__mro__)
```

Output:

```text
D -> B -> C -> A
```

The full MRO is:

```text
D -> B -> C -> A -> object
```

Although both `B` and `C` inherit from `A`, the shared ancestor is visited once in the cooperative method chain.

### What does `super()` do?

`super()` does not simply mean “call my direct parent.” It delegates to the next class in the MRO.

This is why `super()` works correctly in multiple inheritance.

### Cooperative multiple inheritance

```python
class Logger:
    def __init__(self, **kwargs):
        self.log = []
        super().__init__(**kwargs)

class Storage:
    def __init__(self, **kwargs):
        self.data = {}
        super().__init__(**kwargs)

class Service(Logger, Storage):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


service = Service("api")

print(service.name)
print(service.log)
print(service.data)
```

Each class participates in the initialization chain.

### Best practices

- Use `super()` consistently in cooperative inheritance hierarchies.
- Make constructors compatible with the keyword arguments passed through the hierarchy.
- Inspect `ClassName.__mro__` when behavior is unexpected.
- Avoid complex multiple inheritance unless it provides a clear design benefit.

---

## 7. Dunder Methods

**File:** `07_dunder_methods.py`

Dunder means **double underscore**. Dunder methods let custom objects participate in Python's built-in operations.

For example, `__add__()` supports `+`, while `__len__()` supports `len()`.

### Important dunder methods

| Method | Purpose |
|---|---|
| `__init__` | Initialize an instance |
| `__repr__` | Developer-oriented representation |
| `__str__` | Human-readable string |
| `__eq__` | Equality comparison |
| `__lt__` | Less-than comparison |
| `__add__` | Addition |
| `__sub__` | Subtraction |
| `__mul__` | Multiplication |
| `__rmul__` | Reflected multiplication |
| `__len__` | Length |
| `__getitem__` | Indexed access |
| `__iter__` | Iteration |
| `__contains__` | Membership testing |
| `__bool__` | Truth-value testing |
| `__abs__` | Absolute value |
| `__call__` | Calling an object like a function |
| `__hash__` | Hashing |
| `__enter__`, `__exit__` | Context manager protocol |

### Example: a vector class

```python
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, index):
        return (self.x, self.y)[index]


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)       # Vector(4, 6)
print(v1 - v2)       # Vector(-2, -2)
print(v1 * v2)       # 11 (dot product)
print(v1 * 3)        # Vector(3, 6)
print(3 * v1)        # Vector(3, 6)
print(abs(v1))       # 2.236...
print(list(v1))      # [1, 2]
print(v1[0])         # 1
```

### Important hashing rule

If two objects compare equal using `__eq__()`, they must have the same hash if they are hashable.

If a mutable object changes its hash-relevant fields after being placed in a set or used as a dictionary key, lookup behavior can break. For that reason, avoid defining a hash based on mutable state.

### Competitive programming relevance

Custom dunder methods can be useful for advanced data structures and clean object-oriented code. However, simple tuples, lists, dictionaries, and functions are often more convenient in contests.

---

## 8. Type Hints

**File:** `08_type_hints.py`

Type hints document the expected types of variables, parameters, and return values. Static type checkers can use them to identify potential mistakes.

**Type hints do not automatically enforce types at runtime.**

### Basic type hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def total(nums: list[int]) -> int:
    return sum(nums)

print(greet("Alice"))
print(total([1, 2, 3]))
```

### Optional values

```python
def lookup(data: dict[str, int], key: str) -> int | None:
    return data.get(key)
```

The result may be an integer or `None`.

For Python 3.10+, the union operator `|` is available. For older versions, use `Optional[int]` or `Union[int, None]` from `typing`.

### Common collection annotations

| Type | Meaning |
|---|---|
| `list[int]` | List of integers |
| `dict[str, int]` | Dictionary with string keys and integer values |
| `set[str]` | Set of strings |
| `tuple[int, int]` | Tuple containing two integers |
| `tuple[int, ...]` | Tuple containing zero or more integers |
| `int \| str` | Integer or string |
| `Any` | Any type; static checking is less restrictive |
| `Iterable[int]` | Iterable yielding integers |
| `Callable[[int], str]` | Callable accepting an integer and returning a string |

### Generic function

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T | None:
    return items[0] if items else None

print(first([10, 20, 30]))  # 10
print(first([]))            # None
```

The generic type variable allows the function to preserve the element type.

### Type aliases

```python
Vector = list[float]

def norm(values: Vector) -> float:
    return sum(x * x for x in values) ** 0.5
```

A type alias gives a descriptive name to a type expression.

### Runtime behavior

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet(42))  # Hello, 42
```

Python does not reject the integer merely because the annotation says `str`. A static type checker can warn about this mismatch.

**Best practice:** Use type hints to improve readability and tooling, but validate external or untrusted input explicitly.

---

## 9. Generics and Protocols

**File:** `09_generics_and_protocols.py`

Generics let classes and functions work with multiple types while preserving useful type information.

Protocols describe behavior that an object must provide, without requiring it to inherit from a particular base class.

### Generic class

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")

        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")

        return self._items[-1]


stack: Stack[int] = Stack()
stack.push(10)
stack.push(20)

print(stack.pop())   # 20
print(stack.peek())  # 10
```

`Stack[int]` tells a static type checker that the stack is intended to store integers. This annotation does not, by itself, enforce that rule at runtime.

### Protocols: structural typing

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

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
```

Neither `Circle` nor `Square` needs to inherit from `Drawable`. They satisfy the protocol because they provide the required method.

### Runtime-checkable protocols

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Circle"

print(isinstance(Circle(), Drawable))  # True
```

Runtime-checkable protocols provide limited structural checks. They do not perform full static type validation of method signatures.

### Type variables with constraints

```python
StrOrBytes = TypeVar("StrOrBytes", str, bytes)

def concat(a: StrOrBytes, b: StrOrBytes) -> StrOrBytes:
    return a + b

print(concat("Hello, ", "world"))
print(concat(b"Hello, ", b"world"))
```

The constrained type variable allows either strings or bytes while keeping the two arguments and return type consistent.

### When to use these concepts

- **Generics:** Reusable stacks, queues, trees, containers, and utility functions.
- **Protocols:** Describing the required behavior of interchangeable objects.
- **Type variables:** Preserving relationships between input and output types.

These concepts are particularly valuable when building libraries and large applications.

---

## 10. Enum and Named Tuple

**File:** `10_enum_and_namedtuple.py`

`Enum` provides named symbolic constants. `namedtuple` creates tuple-like objects whose fields can be accessed by name.

### Enum

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)   # RED
print(Color.RED.value)  # 1

print(Color(1))         # Color.RED
```

Members are accessed by name, while calling the enum class with a value retrieves the corresponding member.

### Automatic values

```python
from enum import Enum, auto

class Day(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()

print(Day.MON)
```

Use `auto()` when the specific underlying values are not important.

### IntEnum

```python
from enum import IntEnum

class Size(IntEnum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

print(Size.SMALL == 1)       # True
print(Size.SMALL < Size.MEDIUM)  # True
```

`IntEnum` members can compare with integers. Ordinary `Enum` members generally do not compare equal to their underlying values.

### Flags and bitmasks

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

permissions = Permission.READ | Permission.WRITE

print(Permission.READ in permissions)  # True
```

`Flag` is useful when values represent combinations of independent options.

### Named tuples

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

point = Point(3, 4)

print(point.x, point.y)  # 3 4
print(point[0], point[1])  # 3 4

x, y = point
print(x, y)
```

A named tuple supports both named field access and ordinary tuple unpacking.

### Default values

```python
from collections import namedtuple

Point3D = namedtuple(
    "Point3D",
    ["x", "y", "z"],
    defaults=[0]
)

print(Point3D(1, 2))  # Point3D(x=1, y=2, z=0)
```

Defaults apply to the rightmost fields, so `z` defaults to zero.

### Modern alternative: dataclasses

For many new applications, `dataclasses.dataclass` is a convenient alternative when you want named fields and additional class behavior. Named tuples remain useful when tuple behavior, immutability, and unpacking are desirable.

---

## 11. Advanced Unpacking

**File:** `11_advanced_unpacking.py`

Unpacking assigns values from an iterable to variables. Extended unpacking uses `*` to collect multiple values into a list.

### Basic unpacking

```python
a, b, c = [10, 20, 30]

print(a, b, c)  # 10 20 30
```

The number of target variables must match the number of values unless extended unpacking is used.

### Nested unpacking

```python
(a, b), c = (1, 2), 3

print(a, b, c)  # 1 2 3
```

Nested unpacking follows the structure of the input.

### Star unpacking

```python
first, *rest = [1, 2, 3, 4, 5]
print(first, rest)  # 1 [2, 3, 4, 5]

*initial, last = [1, 2, 3, 4, 5]
print(initial, last)  # [1, 2, 3, 4] 5

a, *middle, z = [1, 2, 3, 4, 5]
print(a, middle, z)  # 1 [2, 3, 4] 5
```

Only one starred target is allowed at each unpacking level.

### Unpacking in function calls

```python
def add_four(a, b, c, d):
    return a + b + c + d

first = [1, 2]
second = [3, 4]

print(add_four(*first, *second))  # 10
```

The `*` operator expands positional arguments.

The `**` operator expands dictionary entries into keyword arguments.

```python
def greet(name, language):
    return f"{name} speaks {language}"

data = {"name": "Alice", "language": "English"}

print(greet(**data))
```

### Dictionary merging

```python
defaults = {"host": "localhost", "port": 8080}
overrides = {"port": 9090}

config = {**defaults, **overrides}

print(config)
# {'host': 'localhost', 'port': 9090}
```

When the same key appears more than once, the value from the rightmost mapping wins.

### Unpacking in loops

```python
pairs = [(1, "a"), (2, "b")]

for number, letter in pairs:
    print(number, letter)

for index, (number, letter) in enumerate(pairs):
    print(index, number, letter)
```

### Ignoring values

```python
first, _, third = (10, 20, 30)

print(first, third)  # 10 30
```

The underscore is a conventional name for a value you do not intend to use. It is still an ordinary variable.

### Swapping values

```python
a = 10
b = 20

a, b = b, a

print(a, b)  # 20 10
```

No temporary variable is required.

### Returning multiple values

```python
def statistics(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

minimum, maximum, average = statistics([1, 2, 3, 4, 5])

print(minimum, maximum, average)
```

Technically, the function returns a tuple, which can be unpacked into separate variables.

**Competitive programming tip:** Master tuple unpacking, `enumerate()`, `zip()`, starred assignment, and dictionary merging. They make Python solutions shorter and often easier to read.

---

## 12. Time and Space Complexity

Complexity depends on the operation and the size and structure of the data. These are general guidelines rather than guarantees for every custom object.

| Operation | Typical cost | Notes |
|---|---|---|
| Assignment `b = a` | \(O(1)\) | Creates another reference |
| Shallow copy of a list | \(O(n)\) | Copies the outer list's references |
| Deep copy | Depends on object graph | May traverse many nested objects |
| Append to a Python list | Amortized \(O(1)\) | Occasional resizing can cost \(O(n)\) |
| List indexing | \(O(1)\) | Ordinary list |
| Dictionary lookup | Average \(O(1)\) | Worst cases can be slower |
| Set membership | Average \(O(1)\) | Depends on hashing |
| Tuple unpacking | \(O(n)\) | Generally consumes the input values |
| Iterating over \(n\) elements | \(O(n)\) | Visits each element once |
| Context manager overhead | Usually \(O(1)\) | Excludes setup, cleanup, and work inside |

Type hints and protocols mainly improve clarity and static analysis; they do not automatically change algorithmic complexity.

---

## 13. Common Mistakes

### Mistake 1: Confusing assignment with copying

```python
a = [[1, 2]]
b = a
b[0].append(3)

print(a)  # [[1, 2, 3]]
```

**Fix:** Use an appropriate shallow or deep copy when independent data is required.

### Mistake 2: Reusing a mutable default unintentionally

```python
def collect(value, items=[]):
    items.append(value)
    return items
```

**Fix:** Use `items=None` and create a new list inside the function.

### Mistake 3: Suppressing every exception

A context manager that suppresses all exceptions can hide programming errors.

**Fix:** Suppress only the specific exception types that are intentionally handled.

### Mistake 4: Assuming `super()` always calls the direct parent

**Fix:** Understand and inspect the MRO, especially in multiple inheritance.

### Mistake 5: Defining equality without considering hashing

Equal hashable objects must have equal hashes. Mutable hash-relevant state is especially dangerous for dictionary keys and set elements.

**Fix:** Design equality and hashing together, and avoid hashing mutable objects based on changing fields.

### Mistake 6: Assuming annotations validate input

```python
def square(x: int) -> int:
    return x * x
```

Annotations help type checkers, but runtime validation is not automatic.

**Fix:** Validate untrusted input explicitly.

### Mistake 7: Forgetting that `*rest` creates a list

Extended unpacking collects the remaining values into a list. For very large inputs, consider whether that allocation is necessary.

---

## 14. Competitive Programming Applications

For competitive programming, prioritize the parts of this folder that improve correctness, implementation speed, and your understanding of Python's behavior.

### High-priority concepts

- **Shallow and deep copying:** Avoid accidental changes to nested data.
- **Mutable defaults:** Prevent state from leaking between function calls.
- **Type hints:** Document expected inputs and return values.
- **Advanced unpacking:** Write clean code for tuples, graph edges, and paired values.
- **Dunder methods:** Understand how Python objects interact with built-in operations.
- **Enums and named tuples:** Represent fixed states and structured records when appropriate.

### Example: graph edges

```python
edges = [
    (0, 1, 5),
    (1, 2, 3),
    (2, 3, 7),
]

for u, v, weight in edges:
    print(u, v, weight)
```

Tuple unpacking is common when processing graph edges, coordinate pairs, and weighted relationships.

### Example: counting with a dictionary

```python
def frequency_count(nums: list[int]) -> dict[int, int]:
    freq = {}

    for value in nums:
        freq[value] = freq.get(value, 0) + 1

    return freq


print(frequency_count([1, 2, 1, 3, 2, 1]))
# {1: 3, 2: 2, 3: 1}
```

Type hints make the expected data structure clearer without changing the counting algorithm.

### Lower-priority concepts for contests

Custom descriptors, sophisticated multiple inheritance, and elaborate context managers are useful Python knowledge, but most competitive programming problems do not require implementing them.

Focus first on algorithms, data structures, complexity analysis, and Python's standard containers.

---

## 15. Practice Checklist

Mark each topic when you can explain it and implement a small example without copying the solution.

- [ ] Explain assignment, shallow copy, and deep copy.
- [ ] Demonstrate how nested mutable objects are shared.
- [ ] Fix a mutable default argument bug.
- [ ] Explain when default argument expressions are evaluated.
- [ ] Use `with open(...)` safely.
- [ ] Implement a simple class-based context manager.
- [ ] Implement a generator-based context manager using `@contextmanager`.
- [ ] Explain `__enter__()` and `__exit__()`.
- [ ] Describe the descriptor protocol.
- [ ] Explain how `property` relates to descriptors.
- [ ] Inspect the MRO of a multiple-inheritance class.
- [ ] Explain how `super()` follows the MRO.
- [ ] Implement `__repr__()` and `__eq__()` in a custom class.
- [ ] Explain the relationship between equality and hashing.
- [ ] Add useful type hints to functions and classes.
- [ ] Create a generic stack.
- [ ] Explain structural typing using a protocol.
- [ ] Define and use an enum.
- [ ] Create and unpack a named tuple.
- [ ] Use nested and starred unpacking.
- [ ] Merge dictionaries using `**`.
- [ ] Recognize which concepts are useful in competitive programming.

---

## 16. Mini Projects

### Project 1: Safe configuration loader

Build a configuration utility that:

- Starts with a dictionary of default settings.
- Applies user overrides using dictionary unpacking.
- Uses type hints for its public functions.
- Avoids shared mutable defaults.

### Project 2: Validated product model

Create a `Product` class that:

- Stores a name, price, and quantity.
- Uses a descriptor or property to validate values.
- Implements `__repr__()`.
- Calculates the total price.
- Rejects invalid values.

### Project 3: Resource timer

Create a context manager that:

- Starts a timer on entry.
- Measures elapsed time on exit.
- Prints the result even if the managed block raises an exception.
- Does not accidentally suppress exceptions.

### Project 4: Generic stack

Implement a stack with:

- `push()`
- `pop()`
- `peek()`
- `is_empty()`
- A generic type annotation.

Test empty-stack behavior and document its operation complexities.

---

## 17. Recommended Learning Order

Follow this order to build understanding gradually:

1. Shallow copy and deep copy
2. Mutable default arguments
3. Advanced unpacking
4. Type hints
5. Enums and named tuples
6. Dunder methods
7. Context managers
8. Custom context managers
9. MRO and `super()`
10. Generics and protocols
11. Descriptors

The first six topics are especially useful for everyday Python programming. The remaining topics deepen your understanding of Python's object model and help when designing reusable classes and libraries.

---

## Final Goal

By completing this folder, you should be able to reason about object identity and copying, avoid common function-definition pitfalls, manage resources safely, understand Python's method resolution rules, design custom objects with appropriate special methods, and use type annotations to communicate your intentions clearly.

For competitive programming, use these concepts where they make your solutions safer or clearer—but always keep algorithmic efficiency and simplicity as your primary goals.
