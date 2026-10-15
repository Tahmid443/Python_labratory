# 19. Type Safety and Software Architecture in Python

This module introduces Python type annotations and essential software design patterns. Type annotations make code easier to understand and maintain, while design patterns provide reusable approaches to common software design problems.

## 📁 Project Structure

```text
19_Type_Safety_and_Architecture/
├── 01_type_annotations.py
└── 04_design_patterns/
    ├── decorator.py
    ├── factory.py
    ├── observer.py
    ├── singleton.py
    └── strategy.py
```

## 🎯 Learning Objectives

After completing this module, you should be able to:

- Add type annotations to variables, functions, and classes.
- Understand `Optional`, `Union`, `Callable`, `Sequence`, and other typing tools.
- Create type aliases and distinct types using `NewType`.
- Understand the difference between static type checking and runtime behavior.
- Explain and implement five design patterns:
  - Decorator
  - Factory
  - Observer
  - Singleton
  - Strategy
- Use abstract base classes to define interfaces.
- Choose appropriate abstractions without making code unnecessarily complicated.

---

# Part 1: Python Type Annotations

**File:** `01_type_annotations.py`

## 1. What Are Type Annotations?

Type annotations describe the expected types of variables, function parameters, and return values.

Python is dynamically typed, so annotations do not automatically enforce types at runtime. However, tools such as `mypy` and `pyright` can analyze annotated code and detect many potential type errors before execution.

### Basic Function Annotations

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
```

Here:

- `a: int` means `a` is expected to be an integer.
- `b: int` means `b` is expected to be an integer.
- `-> int` means the function is expected to return an integer.

For a function that returns no meaningful value, use `-> None`.

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

## 2. `Optional` and `Union`

### `Optional`

`Optional[T]` means that a value can be either type `T` or `None`. It is equivalent to `T | None`.

```python
from typing import Optional

def find_user(uid: int) -> Optional[dict]:
    users = {
        1: {"name": "Alice"},
        2: {"name": "Bob"}
    }

    return users.get(uid)

print(find_user(1))
print(find_user(100))
```

The function can return a dictionary or `None`.

**Important:** If a function returns an optional value, check for `None` before accessing its contents.

```python
user = find_user(1)

if user is not None:
    print(user["name"])
```

### `Union`

`Union` allows a value to have one of several specified types.

```python
from typing import Union

def to_int(value: Union[int, str]) -> int:
    return int(value)

print(to_int("123"))
print(to_int(456))
```

Modern Python supports the `|` syntax:

```python
def to_int(value: int | str) -> int:
    return int(value)
```

The `|` syntax for union types requires Python 3.10 or later.

## 3. Collection Type Annotations

Annotations can describe the element types of collections.

```python
from typing import List, Dict, Tuple

def process(items: List[int]) -> Dict[str, int]:
    return {"total": sum(items)}

def get_pair() -> Tuple[int, str]:
    return 1, "a"

print(process([10, 20, 30]))
print(get_pair())
```

Meaning:

| Annotation | Meaning |
|---|---|
| `List[int]` | A list containing integers |
| `Dict[str, int]` | A dictionary with string keys and integer values |
| `Tuple[int, str]` | A two-element tuple with an integer followed by a string |
| `Optional[int]` | An integer or `None` |
| `Union[int, str]` | An integer or a string |

For Python 3.9 and later, you can use built-in collection types directly:

```python
def process(items: list[int]) -> dict[str, int]:
    return {"total": sum(items)}
```

The older `List`, `Dict`, and `Tuple` forms are still useful to recognize when reading existing code.

## 4. `Callable`

`Callable` describes a function or other callable object.

```python
from typing import Callable

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

def square(number: int) -> int:
    return number * number

print(apply(square, 5))
```

`Callable[[int], int]` describes a callable that accepts an integer argument and returns an integer.

This is useful when passing functions as arguments, implementing callbacks, or creating function-based strategies.

## 5. `Any`

`Any` permits a value to have an unspecified type from the perspective of a static type checker.

```python
from typing import Any

def log(value: Any) -> None:
    print(value)

log(10)
log("Hello")
log([1, 2, 3])
```

Use `Any` when necessary, such as when dealing with untyped external data. Avoid using it everywhere because it weakens the benefits of static type checking.

## 6. `Sequence`

`Sequence` describes an ordered collection that supports operations such as indexing and iteration.

```python
from typing import Optional, Sequence

def first(items: Sequence[int]) -> Optional[int]:
    return items[0] if items else None

print(first([10, 20, 30]))
print(first([]))
print(first((5, 6, 7)))
```

A sequence annotation allows compatible types such as lists and tuples without requiring a specific mutable list.

Use `Sequence[T]` when a function only needs to read a sequence. Use `list[T]` when the function specifically requires a list or needs list-specific operations.

## 7. Class Type Annotations

Annotations can describe the attributes and methods of a class.

```python
class User:
    name: str
    age: int
    email: str | None

    def __init__(
        self,
        name: str,
        age: int,
        email: str | None = None
    ) -> None:
        self.name = name
        self.age = age
        self.email = email

    def greet(self) -> str:
        return f"Hello, {self.name}"

user = User("Alice", 25)
print(user.greet())
```

The attribute annotations document the intended types of the object's fields. The constructor initializes those fields.

Annotations do not automatically validate values supplied to the constructor.

## 8. Type Aliases

A type alias gives a descriptive name to an existing type.

```python
Vector = list[float]
Matrix = list[Vector]

def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))

v1 = [1.0, 2.0, 3.0]
v2 = [4.0, 5.0, 6.0]

print(dot(v1, v2))
```

Type aliases are useful when a type becomes long or represents a meaningful concept.

**Note:** The example assumes both vectors have compatible lengths. `zip()` stops at the shorter input, so a production implementation should validate dimensions if unequal lengths are invalid.

## 9. `NewType`

`NewType` creates a distinct static type based on an existing type.

```python
from typing import NewType

UserId = NewType("UserId", int)

def get_user(uid: UserId) -> str:
    return f"User ID: {uid}"

uid = UserId(101)

print(get_user(uid))
```

`UserId` is useful for distinguishing values that share the same underlying type but have different meanings.

For example:

```python
UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)
```

A static type checker can distinguish `UserId` and `OrderId` even though both are based on integers.

`NewType` does not create a new runtime class or validate values at runtime. It is primarily a static type-checking tool.

## 10. Type Annotations Are Not Runtime Enforcement

Consider:

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add("a", "b"))
```

The second call returns `"ab"` at runtime even though the argument and return annotations specify integers.

Python normally does not reject the call just because the annotations do not match.

Use a static type checker to catch this kind of mismatch.

For example, install `mypy`:

```bash
python -m pip install mypy
```

Run it on the file:

```bash
mypy 01_type_annotations.py
```

Type checkers may report issues in your code, depending on the checker, its configuration, and the annotations available.

---

# Part 2: Design Patterns

Design patterns are reusable approaches to recurring software design problems. They are not mandatory structures that every program must follow.

The right pattern is the one that makes the code easier to understand, test, and extend.

## 11. Abstract Base Classes

Several patterns in this project use `ABC` and `abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...
```

An abstract base class defines methods that concrete subclasses are expected to implement.

You generally cannot instantiate a class while it still has unimplemented abstract methods.

```python
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(circle.area())
```

Abstract base classes can make contracts between components clearer.

---

## 12. Decorator Pattern

**File:** `04_design_patterns/decorator.py`

### What Is the Decorator Pattern?

The Decorator pattern adds responsibilities to an object by wrapping it inside another object that follows the same interface.

Instead of creating a separate class for every combination of features, you can combine decorators dynamically.

The project demonstrates a coffee-ordering system.

### Base Component

```python
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        ...

    @abstractmethod
    def description(self) -> str:
        ...
```

`Coffee` defines the common interface for every coffee object.

### Concrete Component

```python
class Espresso(Coffee):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Espresso"
```

An espresso is the basic object that can be decorated.

### Base Decorator

```python
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee
```

The decorator stores another `Coffee` object. Since it also implements the `Coffee` interface, it can be wrapped by another decorator.

### Concrete Decorators

```python
class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def description(self) -> str:
        return self._coffee.description() + ", Milk"


class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.3

    def description(self) -> str:
        return self._coffee.description() + ", Sugar"
```

Each decorator adds one feature and adjusts the cost or description.

### Combining Decorators

```python
coffee = Espresso()
print(coffee.description(), coffee.cost())

coffee = Milk(coffee)
print(coffee.description(), coffee.cost())

coffee = Sugar(Milk(Espresso()))
print(coffee.description(), coffee.cost())
```

Expected results:

```text
Espresso 2.0
Espresso, Milk 2.5
Espresso, Milk, Sugar 2.8
```

The nested object structure is:

```text
Sugar
└── Milk
    └── Espresso
```

Each wrapper delegates to the wrapped object and adds its own behavior.

### When to Use It

- Adding optional features to objects.
- Combining behaviors at runtime.
- Avoiding many subclasses for different feature combinations.
- Wrapping objects without changing their underlying class.

### Important Distinction

The **Decorator design pattern** wraps objects.

A Python **function decorator** wraps or modifies the behavior of a callable, commonly using `@decorator`.

They share the general idea of wrapping behavior, but they are not the same implementation technique.

---

## 13. Factory Pattern

**File:** `04_design_patterns/factory.py`

### What Is the Factory Pattern?

The Factory pattern centralizes object creation so that client code does not need to know every detail about constructing concrete objects.

The project uses shapes as an example.

### Base Class and Concrete Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2
```

Both shapes implement the same interface but use different area calculations.

### Simple Factory

```python
class ShapeFactory:
    @staticmethod
    def create(kind: str, **kwargs) -> Shape:
        if kind == "circle":
            return Circle(kwargs["r"])

        if kind == "square":
            return Square(kwargs["s"])

        raise ValueError(f"Unknown shape: {kind}")
```

Usage:

```python
shape = ShapeFactory.create("circle", r=5)
print(f"{shape.area():.2f}")
```

The client chooses the requested shape, while the factory handles the construction.

### Registration-Based Factory

A registration-based factory stores creator functions in a dictionary.

```python
class Factory:
    _creators = {}

    @classmethod
    def register(cls, name: str):
        def decorator(creator):
            cls._creators[name] = creator
            return creator

        return decorator

    @classmethod
    def create(cls, name: str, *args, **kwargs):
        try:
            creator = cls._creators[name]
        except KeyError:
            raise ValueError(f"Unknown type: {name}") from None

        return creator(*args, **kwargs)
```

Register a creator:

```python
@Factory.register("circle")
def make_circle(radius: float) -> Circle:
    return Circle(radius)

shape = Factory.create("circle", 3)
print(shape.area())
```

This lets you register additional object creators without adding another conditional branch to the factory.

### When to Use It

- Object creation involves multiple steps.
- Client code should not depend on concrete constructors.
- The program supports multiple interchangeable implementations.
- A registry of available implementations is useful.

### Common Mistake

A factory is not automatically necessary for every class. If an object can be created simply with `MyClass(...)`, adding a factory may create needless complexity.

---

## 14. Observer Pattern

**File:** `04_design_patterns/observer.py`

### What Is the Observer Pattern?

The Observer pattern allows one object to notify multiple interested objects when an event or state change occurs.

The object that produces the event does not need to know the internal details of every listener.

### Event Emitter

```python
from collections.abc import Callable
from typing import Any

class EventEmitter:
    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable[..., Any]]] = {}

    def on(self, event: str, callback: Callable[..., Any]) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def off(self, event: str, callback: Callable[..., Any]) -> None:
        listeners = self._listeners.get(event, [])

        if callback in listeners:
            listeners.remove(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)
```

This implementation provides three basic operations:

- `on()`: Register a listener.
- `off()`: Remove a listener.
- `emit()`: Notify listeners associated with an event.

### Usage

```python
emitter = EventEmitter()

def on_user_created(name: str) -> None:
    print(f"Welcome, {name}!")

def log_event(name: str) -> None:
    print(f"[LOG] User {name} created")

emitter.on("user_created", on_user_created)
emitter.on("user_created", log_event)

emitter.emit("user_created", "Alice")
```

Output:

```text
Welcome, Alice!
[LOG] User Alice created
```

### Classic Observer Implementation

The project also demonstrates a subject that stores observer objects.

```python
class Observer:
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(f"{self.name}: {message}")


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)
```

Usage:

```python
subject = Subject()

subject.attach(Observer("A"))
subject.attach(Observer("B"))

subject.notify("Hello")
```

Output:

```text
A: Hello
B: Hello
```

### When to Use It

- Event-driven systems.
- Notification systems.
- User-interface event handling.
- Logging and monitoring.
- Applications where several components react to one event.

### Design Considerations

- Decide what happens when a listener raises an exception.
- Consider whether duplicate registrations should be allowed.
- Avoid modifying the listener collection unexpectedly during notification.
- Consider listener cleanup to avoid retaining objects unnecessarily.

---

## 15. Singleton Pattern

**File:** `04_design_patterns/singleton.py`

### What Is the Singleton Pattern?

The Singleton pattern aims to ensure that a class has only one instance accessible through a shared creation mechanism.

The project demonstrates a singleton using `__new__()`.

### Basic Singleton

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0

        return cls._instance
```

Usage:

```python
a = Singleton()
b = Singleton()

a.value = 42

print(b.value)  # 42
print(a is b)   # True
```

Both variables refer to the same object.

### Thread-Safe Creation

If multiple threads can create the object simultaneously, protect the creation step with a lock.

```python
import threading

class SafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance
```

The lock protects instance creation.

This example illustrates thread-safe creation in the ordinary case. Subclasses, initialization behavior, and other lifecycle requirements may need additional design.

### Pythonic Alternative: Module-Level Instance

Python modules are normally initialized once per interpreter and reused through the import system. A module-level object can therefore provide shared configuration without a custom singleton class.

```python
class _Config:
    def __init__(self) -> None:
        self.debug = False

config = _Config()
```

Other modules can import `config` and use the same module-level instance.

### When to Use It

Potential examples include:

- Shared configuration.
- A carefully managed process-wide registry.
- A resource that genuinely requires one shared instance.

### Disadvantages

- Global shared state can make tests harder to isolate.
- Dependencies become less explicit.
- Initialization and lifecycle management can become complicated.
- A singleton in one process is not automatically shared across multiple processes.

**Practical advice:** Prefer passing dependencies explicitly when possible. A module-level instance may be simpler than implementing a custom singleton.

---

## 16. Strategy Pattern

**File:** `04_design_patterns/strategy.py`

### What Is the Strategy Pattern?

The Strategy pattern defines interchangeable algorithms behind a common interface.

The caller can select an algorithm without changing the code that uses it.

The project demonstrates this concept using sorting algorithms.

### Strategy Interface

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        ...
```

Every concrete strategy implements the `sort()` method.

### Bubble Sort Strategy

```python
class BubbleSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        arr = data[:]
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr
```

The method copies the input before sorting, so it does not modify the original list.

Bubble sort has \(O(n^2)\) average and worst-case time complexity in this implementation.

### Quick Sort Strategy

```python
class QuickSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data[:]

        pivot = data[0]

        smaller = [x for x in data[1:] if x < pivot]
        greater_or_equal = [
            x for x in data[1:] if x >= pivot
        ]

        return (
            self.sort(smaller)
            + [pivot]
            + self.sort(greater_or_equal)
        )
```

This is a simple recursive demonstration, not an optimal general-purpose sorting implementation.

Its worst-case time complexity can be \(O(n^2)\), and its recursion depth can become large for unfavorable inputs. Python's built-in `sorted()` is usually preferable for practical sorting.

### Context Class

```python
class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self.strategy.sort(data)
```

The `Sorter` delegates sorting to whichever strategy it receives.

### Using Different Strategies

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]

print(Sorter(BubbleSort()).sort(data))
print(Sorter(QuickSort()).sort(data))
```

Both strategies expose the same interface, so the caller can switch between them without changing the calling code.

### Function-Based Strategy

Python functions are first-class objects. A strategy can often be represented with a function instead of a class.

```python
def sort_desc(data: list[int]) -> list[int]:
    return sorted(data, reverse=True)

def sort_by_len(data: list[str]) -> list[str]:
    return sorted(data, key=len)

strategies = {
    "desc": sort_desc,
    "len": sort_by_len
}

print(strategies["desc"]([1, 3, 2]))
print(strategies["len"](["pear", "fig", "banana"]))
```

Function-based strategies are often simpler when each algorithm has no additional state.

### When to Use It

- Multiple algorithms solve the same problem.
- Behavior needs to be selected at runtime.
- You want to test algorithms independently.
- You want to avoid large conditional blocks that select different behaviors.

---

# Part 3: Comparing the Five Patterns

## 17. Quick Comparison

| Pattern | Main purpose | Example from this project |
|---|---|---|
| Decorator | Add behavior by wrapping an object | Adding milk or sugar to coffee |
| Factory | Centralize object creation | Creating circles or squares |
| Observer | Notify registered listeners | User-created events |
| Singleton | Share a single instance | Shared configuration |
| Strategy | Switch between algorithms | Bubble sort and quick sort |

## 18. How to Choose a Pattern

Ask yourself what problem you are trying to solve:

- **Need to add optional behavior to an object?** Consider Decorator.
- **Need to centralize construction logic?** Consider Factory.
- **Need to notify several components about an event?** Consider Observer.
- **Need a single shared instance?** Consider Singleton, but check whether dependency injection or a module-level instance is simpler.
- **Need to switch between interchangeable algorithms?** Consider Strategy.

Do not select a pattern simply because it is a well-known pattern. Select it because it addresses a real design problem.

---

# Part 4: Common Mistakes

## 19. Type Annotation Mistakes

### Mistake 1: Assuming Annotations Validate Values

```python
def square(number: int) -> int:
    return number * number
```

This annotation does not prevent callers from passing an unexpected value at runtime.

**Solution:** Use a static type checker and explicit runtime validation where untrusted data requires it.

### Mistake 2: Ignoring `None`

A function annotated with `str | None` may return `None`. Accessing string methods without checking can raise an exception.

**Solution:** Check whether the value is `None` before using it as a string.

### Mistake 3: Using `Any` Everywhere

Excessive `Any` annotations can hide type mismatches.

**Solution:** Prefer specific types and introduce `Any` only at boundaries where the type is genuinely unknown.

### Mistake 4: Confusing `NewType` with Runtime Validation

`UserId = NewType("UserId", int)` does not check that a value is a valid user ID.

**Solution:** Validate external values separately if they have constraints beyond being integers.

## 20. Design Pattern Mistakes

- Using Factory classes when direct construction is sufficient.
- Creating a Singleton for data that could be passed as a dependency.
- Using inheritance when a simple function would be easier to understand.
- Building an Observer system without considering listener errors or cleanup.
- Applying Decorator when a straightforward function or composition would be clearer.
- Choosing a Strategy abstraction for an algorithm that never changes.

Good architecture balances flexibility with simplicity.

---

# Part 5: Practice Checklist

## Type Annotations

- [ ] Annotate function parameters and return values.
- [ ] Use `Optional` or `T | None`.
- [ ] Use `Union` or `|` for multiple accepted types.
- [ ] Annotate lists, dictionaries, and tuples.
- [ ] Use `Callable` for function arguments.
- [ ] Use `Sequence` for read-only sequence interfaces.
- [ ] Create a type alias.
- [ ] Use `NewType` to distinguish IDs.
- [ ] Annotate class attributes and methods.
- [ ] Run a static type checker on a sample file.

## Decorator Pattern

- [ ] Implement a base component.
- [ ] Implement two concrete decorators.
- [ ] Wrap an object with one decorator.
- [ ] Combine multiple decorators.
- [ ] Verify that behavior and cost change as expected.

## Factory Pattern

- [ ] Implement a base class and two concrete classes.
- [ ] Create objects through a factory.
- [ ] Handle unknown factory names.
- [ ] Implement a registration-based factory.

## Observer Pattern

- [ ] Register event listeners.
- [ ] Notify multiple listeners.
- [ ] Remove a listener.
- [ ] Handle an unknown event.
- [ ] Decide how callback exceptions should be handled.

## Singleton Pattern

- [ ] Create two references to the same instance.
- [ ] Verify identity with `is`.
- [ ] Understand thread-safe creation.
- [ ] Compare a custom singleton with a module-level instance.

## Strategy Pattern

- [ ] Define a common strategy interface.
- [ ] Implement two different strategies.
- [ ] Inject a strategy into a context object.
- [ ] Switch strategies without changing the context.
- [ ] Implement a strategy using a plain function.

---

# Part 6: Mini Projects

## Project 1: Typed Student Management System

Create a student management program with:

- A `Student` class.
- Typed attributes for name, student ID, and marks.
- A function that finds a student by ID.
- A function that returns an optional result.
- A type alias for a list of students.
- Static type checking.

## Project 2: Extensible Notification System

Use the Observer pattern to implement a notification system.

Requirements:

- Register multiple listeners.
- Emit a notification event.
- Remove listeners.
- Handle callback failures deliberately.
- Add type annotations to callbacks and event data.

## Project 3: Payment Strategy System

Implement interchangeable payment strategies such as:

- Cash payment.
- Card payment.
- Mobile payment.

Requirements:

- Define a shared payment interface.
- Implement each payment method separately.
- Select a strategy at runtime.
- Test each strategy independently.

## Project 4: Configurable Shape Factory

Build a shape factory that can create different shapes from a configuration.

Requirements:

- Support circles and squares.
- Give each shape an `area()` method.
- Reject unknown shape names.
- Use type annotations for the factory interface.
- Add a new shape without rewriting the client code.

---

# Part 7: Recommended Learning Order

1. Function and class type annotations.
2. `Optional`, `Union`, and modern union syntax.
3. Collection types, `Callable`, and `Sequence`.
4. Type aliases and `NewType`.
5. Static type checking with `mypy` or `pyright`.
6. Abstract base classes and interfaces.
7. Decorator pattern.
8. Factory pattern.
9. Observer pattern.
10. Singleton pattern.
11. Strategy pattern.
12. Mini projects combining type safety and design patterns.

## ✅ Final Goal

By completing this module, you should be able to make Python code more explicit through type annotations and structure larger programs using common design patterns.

For competitive programming, focus primarily on writing correct algorithms, understanding complexity, and using Python's built-in data structures. Type annotations and design patterns become especially valuable when developing larger projects, reusable libraries, and maintainable applications.

**Remember:** Good architecture is not about using the most patterns. It is about making the code easier to understand, test, and change.