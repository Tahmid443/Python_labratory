# 14 — Python Standard Library

Python's standard library provides powerful tools for mathematics, dates, file systems, data structures, iteration, functional programming, logging, command-line applications, and operating-system tasks.

Learning these modules helps you write solutions faster without unnecessarily reinventing functionality that Python already provides.

## 📂 Project Structure

```text
14_Standard_Library/
├── 01_math_random.py
├── 02_datetime.py
├── 03_os_pathlib.py
├── 04_sys.py
├── 05_collections.py
├── 06_itertools.py
├── 07_functools.py
├── 08_logging.py
├── 09_argparse.py
├── 10_subprocess.py
└── 11_shutil_and_tempfile.py
```

---

## 1. `math` and `random`

**File:** `01_math_random.py`

### The `math` module

The `math` module provides mathematical constants and functions.

```python
import math

print(math.pi)
print(math.e)

print(math.sqrt(25))          # 5.0
print(math.floor(3.8))         # 3
print(math.ceil(3.2))          # 4
print(math.factorial(5))       # 120

print(math.gcd(12, 18))        # 6
print(math.lcm(4, 6))          # 12
print(math.isqrt(26))          # 5

print(math.log(100, 10))       # 2.0
print(math.sin(math.pi / 2))   # 1.0
```

Important functions:

| Function | Purpose |
|---|---|
| `math.sqrt(x)` | Square root |
| `math.isqrt(x)` | Integer square root |
| `math.floor(x)` | Round down |
| `math.ceil(x)` | Round up |
| `math.factorial(n)` | Factorial |
| `math.gcd(a, b)` | Greatest common divisor |
| `math.lcm(a, b)` | Least common multiple |
| `math.log(x)` | Natural logarithm by default |
| `math.log2(x)` | Base-2 logarithm |
| `math.log10(x)` | Base-10 logarithm |
| `math.isclose(a, b)` | Approximate floating-point comparison |
| `math.hypot(x, y)` | Euclidean distance from the origin |

### Floating-point precision

Floating-point calculations can produce small rounding errors.

```python
import math

print(0.1 + 0.2 == 0.3)          # False
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

For numerical comparisons, use an appropriate tolerance rather than assuming exact equality.

Python's built-in `round()` uses round-half-to-even behavior for exact halfway cases in the represented value.

### The `random` module

The `random` module generates pseudorandom values.

```python
import random

random.seed(42)

print(random.random())             # Float in [0.0, 1.0)
print(random.randint(1, 10))       # Both endpoints included
print(random.randrange(0, 10, 2))  # 0, 2, 4, 6, or 8
print(random.uniform(1, 5))

print(random.choice(["A", "B", "C"]))
print(random.choices(["A", "B", "C"], k=5))
print(random.sample(range(100), 5))
```

- `random.choice()` selects one element.
- `random.choices()` samples with replacement and can support weights.
- `random.sample()` samples without replacement.
- `random.shuffle()` shuffles a mutable sequence in place.
- `random.seed()` makes pseudorandom sequences reproducible for a given compatible environment and execution pattern.

Example of weighted selection:

```python
import random

outcomes = ["win", "lose"]
result = random.choices(outcomes, weights=[1, 9], k=10)

print(result)
```

### Security warning: use `secrets` for secrets

The `random` module is not suitable for generating passwords, authentication tokens, or cryptographic keys.

```python
import secrets

print(secrets.token_hex(16))
print(secrets.token_urlsafe(16))
print(secrets.randbelow(100))
print(secrets.choice("abcdef"))
```

**Competitive programming priority:** Learn `gcd`, `isqrt`, logarithms, `ceil`, and basic `random` usage. For most mathematical contest problems, `math` is much more important than `random`.

---

## 2. `datetime`

**File:** `02_datetime.py`

The `datetime` module handles dates, times, durations, formatting, and timezone-aware timestamps.

### Main classes

| Class | Purpose |
|---|---|
| `date` | Calendar date |
| `time` | Time of day |
| `datetime` | Date and time together |
| `timedelta` | Duration or difference |
| `timezone` | Fixed UTC offset |

### Getting the current date and time

```python
from datetime import datetime, date

now = datetime.now()
today = date.today()

print(now)
print(today)

print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
```

### Creating and parsing dates

```python
from datetime import datetime

d = datetime(2026, 10, 15, 10, 30)
print(d)

text = "2026-10-15 10:30:00"
parsed = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")

print(parsed)
```

`strptime()` converts a string into a date/time object using a specified format.

### Formatting dates

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%A, %B %d, %Y"))
print(now.isoformat())
```

Common format directives:

| Directive | Meaning |
|---|---|
| `%Y` | Four-digit year |
| `%m` | Month number |
| `%d` | Day of month |
| `%H` | Hour, 24-hour clock |
| `%M` | Minute |
| `%S` | Second |
| `%A` | Full weekday name |
| `%B` | Full month name |
| `%w` | Weekday number, Sunday is 0 |

### Date arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()

tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)

print(tomorrow)
print(last_week)

difference = tomorrow - now
print(difference.days)
print(difference.total_seconds())
```

### Timezones

```python
from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)

print(utc_now)
print(utc_now.isoformat())
```

A timezone-aware datetime includes timezone information. A naive datetime does not.

Avoid casually mixing naive and aware datetime objects in arithmetic or comparisons.

**Best practice:** Use timezone-aware UTC timestamps for applications that need consistent time handling across locations.

---

## 3. `os` and `pathlib`

**File:** `03_os_pathlib.py`

These modules help you work with directories, file paths, environment variables, and filesystem metadata.

### Current working directory and environment variables

```python
import os

print(os.getcwd())
print(os.name)
print(os.environ.get("HOME"))
```

Environment variable names differ between operating systems. For example, Windows commonly uses `USERPROFILE` for a user's profile directory.

### Using `os.path`

```python
import os

path = "/home/user/data.txt"

print(os.path.basename(path))  # data.txt
print(os.path.dirname(path))   # /home/user
print(os.path.splitext(path))  # ('/home/user/data', '.txt')
print(os.path.abspath("."))
print(os.path.exists(path))
```

### Modern path handling with `pathlib`

`pathlib.Path` provides an object-oriented way to work with paths and is often easier to read.

```python
from pathlib import Path

path = Path("data") / "input.txt"

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.exists())
print(path.is_file())
print(path.is_dir())
```

The `/` operator joins path components.

### Reading and writing files

```python
from pathlib import Path

path = Path("example.txt")

path.write_text("Hello, Python!", encoding="utf-8")
content = path.read_text(encoding="utf-8")

print(content)
```

For large files, prefer streaming with `open()` rather than loading the entire file into memory.

### Creating directories

```python
from pathlib import Path

directory = Path("data/reports")
directory.mkdir(parents=True, exist_ok=True)
```

- `parents=True` creates missing parent directories.
- `exist_ok=True` avoids an error if the directory already exists.

### Iterating over files

```python
from pathlib import Path

for path in Path(".").glob("*.py"):
    print(path)

for path in Path(".").iterdir():
    print(path)
```

`glob()` matches a pattern, while `iterdir()` lists the immediate contents of a directory.

**Best practice:** Prefer `pathlib` for new Python code unless you specifically need an `os` or `os.path` feature.

---

## 4. `sys`

**File:** `04_sys.py`

The `sys` module provides access to Python interpreter settings, command-line arguments, streams, and runtime information.

### Python and platform information

```python
import sys

print(sys.version)
print(sys.version_info)
print(sys.platform)
print(sys.maxsize)
```

### Command-line arguments

```python
import sys

print(sys.argv)
```

If you execute:

```bash
python app.py Alice 25
```

Then `sys.argv` contains the script name followed by the provided arguments.

### Standard streams

```python
import sys

sys.stdout.write("Normal output\n")
sys.stderr.write("Error or diagnostic output\n")
```

- `sys.stdout` is standard output.
- `sys.stderr` is standard error.
- `sys.stdin` is standard input.

### Recursion limit

```python
import sys

print(sys.getrecursionlimit())
```

You can change the recursion limit with `sys.setrecursionlimit()`, but setting it too high can crash the interpreter. Do not raise it casually to solve recursion problems.

### Memory-related inspection

```python
import sys

values = [1, 2, 3]

print(sys.getsizeof(values))
print(sys.getsizeof(42))
print(sys.getrefcount(values))
```

`sys.getsizeof()` reports the shallow size of an object, not necessarily the total memory consumed by everything it references. `getrefcount()` is implementation-dependent and includes a temporary reference in CPython.

### Module information

```python
import sys

print(sys.path)
print(sys.modules.get("math"))
```

- `sys.path` influences where Python searches for modules.
- `sys.modules` contains modules already loaded in the current interpreter.

### Exiting a program

```python
import sys

sys.exit(0)
```

A status code of `0` conventionally indicates success. Nonzero values conventionally indicate an error.

**Competitive programming priority:** Understand `sys.stdin`, `sys.stdout`, `sys.argv`, and `sys.setrecursionlimit()`. For fast input, `sys.stdin.buffer.readline` is often useful.

---

## 5. `collections`

**File:** `05_collections.py`

The `collections` module contains specialized data structures that often simplify common algorithms.

### `Counter`

`Counter` counts occurrences of hashable elements.

```python
from collections import Counter

counts = Counter("hello")

print(counts)
print(counts["l"])           # 2
print(counts.most_common(2))
```

It is particularly useful for frequency counting.

```python
from collections import Counter

nums = [1, 2, 1, 3, 2, 1]
frequency = Counter(nums)

print(frequency[1])  # 3
```

### `defaultdict`

A `defaultdict` automatically creates a default value when a missing key is accessed.

```python
from collections import defaultdict

groups = defaultdict(list)

groups["fruit"].append("apple")
groups["fruit"].append("banana")
groups["vegetable"].append("carrot")

print(dict(groups))
```

Counting with `defaultdict(int)`:

```python
from collections import defaultdict

counts = defaultdict(int)

for char in "hello":
    counts[char] += 1

print(dict(counts))
```

### `deque`

A double-ended queue supports efficient additions and removals from either end.

```python
from collections import deque

queue = deque([1, 2, 3])

queue.append(4)
queue.appendleft(0)

print(queue.popleft())
print(queue.pop())
print(queue)
```

Typical endpoint append and pop operations are \(O(1)\).

Use `deque` for BFS queues and sliding-window algorithms. Removing the first element of a regular list with `pop(0)` takes \(O(n)\).

### Fixed-size deque

```python
from collections import deque

recent = deque(maxlen=3)

for value in range(5):
    recent.append(value)

print(recent)  # deque([2, 3, 4], maxlen=3)
```

When full, adding an element to one end discards an element from the opposite end.

### `namedtuple`

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(3, 4)

print(p.x, p.y)
print(p[0], p[1])
```

This provides named fields while retaining tuple behavior.

### `ChainMap`

`ChainMap` searches multiple mappings in order.

```python
from collections import ChainMap

defaults = {"color": "red", "size": "M"}
user = {"color": "blue"}

config = ChainMap(user, defaults)

print(config["color"])  # blue
print(config["size"])   # M
```

The first mapping containing a key takes precedence. `ChainMap` combines views of the mappings rather than copying them into a new dictionary.

### `OrderedDict`

```python
from collections import OrderedDict

data = OrderedDict()
data["b"] = 2
data["a"] = 1

data.move_to_end("b")
print(data)
```

Regular dictionaries preserve insertion order in modern Python. `OrderedDict` remains useful when its additional operations, such as `move_to_end()` and specialized order-sensitive equality, are needed.

### Competitive programming priority

1. `Counter` — frequency counting.
2. `defaultdict` — grouping and graph adjacency lists.
3. `deque` — BFS and sliding windows.
4. `namedtuple` — optional named records.
5. `ChainMap` and `OrderedDict` — specialized applications.

---

## 6. `itertools`

**File:** `06_itertools.py`

`itertools` provides efficient iterator-building tools. Many of its functions are lazy, meaning they produce values as needed rather than creating an entire list immediately.

### Infinite iterators

```python
import itertools as it

print(list(it.islice(it.count(10), 5)))
# [10, 11, 12, 13, 14]

print(list(it.islice(it.cycle("AB"), 6)))
# ['A', 'B', 'A', 'B', 'A', 'B']

print(list(it.repeat("x", 3)))
# ['x', 'x', 'x']
```

`count()` and `cycle()` can be infinite. Limit them with tools such as `islice()` when you need a finite result.

### Cartesian product

```python
import itertools as it

print(list(it.product("AB", repeat=2)))
# [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
```

For inputs of sizes \(n\) and \(m\), the product produces \(n \times m\) combinations.

### Permutations and combinations

```python
import itertools as it

print(list(it.permutations("ABC", 2)))
print(list(it.combinations("ABC", 2)))
print(list(it.combinations_with_replacement("AB", 2)))
```

- `permutations()` considers different orders distinct.
- `combinations()` selects items without considering order.
- `combinations_with_replacement()` allows repeated selections.

Be careful: combinatorial outputs can grow extremely quickly.

### Chaining iterables

```python
import itertools as it

print(list(it.chain([1, 2], "ab", [3, 4])))
# [1, 2, 'a', 'b', 3, 4]

print(list(it.chain.from_iterable([[1, 2], [3, 4]])))
# [1, 2, 3, 4]
```

### Iterator slicing

```python
import itertools as it

print(list(it.islice(range(100), 5)))
print(list(it.islice(range(100), 10, 20, 2)))
```

`islice()` selects a portion of an iterator without requiring the entire iterable to be materialized.

### Grouping consecutive equal keys

```python
import itertools as it

data = [
    ("a", 1),
    ("a", 2),
    ("b", 3),
    ("b", 4),
]

for key, group in it.groupby(data, key=lambda item: item[0]):
    print(key, list(group))
```

Important: `groupby()` groups consecutive elements with equal keys. It does not automatically group all equal keys throughout an unsorted sequence. Sort by the same key first when global grouping is required.

### Running totals and products

```python
import itertools as it
import operator

nums = [1, 2, 3, 4]

print(list(it.accumulate(nums)))
# [1, 3, 6, 10]

print(list(it.accumulate(nums, operator.mul)))
# [1, 2, 6, 24]
```

### Filtering iterators

```python
import itertools as it

print(list(it.compress("ABCD", [1, 0, 1, 0])))
# ['A', 'C']

print(list(it.takewhile(lambda x: x < 3, range(10))))
# [0, 1, 2]

print(list(it.dropwhile(lambda x: x < 3, range(10))))
# [3, 4, 5, 6, 7, 8, 9]
```

`takewhile()` stops at the first failed condition. It does not resume later even if subsequent values would satisfy the condition.

### Pairwise iteration

```python
import itertools as it

print(list(it.pairwise([1, 2, 3, 4])))
# [(1, 2), (2, 3), (3, 4)]
```

`pairwise()` is available in Python 3.10 and later.

### Chunking an iterable

```python
import itertools as it

def chunks(iterable, size):
    if size <= 0:
        raise ValueError("size must be positive")

    iterator = iter(iterable)

    while chunk := list(it.islice(iterator, size)):
        yield chunk

print(list(chunks(range(10), 3)))
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

The function returns chunks lazily, although each individual chunk is materialized as a list.

**Competitive programming priority:** Learn `product`, `permutations`, `combinations`, `accumulate`, `chain`, `islice`, and `pairwise`. Always estimate the output size before using combinatorial functions.

---

## 7. `functools`

**File:** `07_functools.py`

The `functools` module provides utilities for decorators, caching, partial application, reductions, and function dispatch.

### `wraps`

When writing decorators, `functools.wraps` preserves useful metadata from the original function.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@logged
def greet(name):
    """Say hello."""
    return f"Hello, {name}"

print(greet("Alice"))
print(greet.__name__)
print(greet.__doc__)
```

### `lru_cache`

`lru_cache` memoizes function results using a least-recently-used eviction policy.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(30))
print(fib.cache_info())
```

Without caching, the straightforward recursive Fibonacci implementation repeats many computations. With caching, each distinct argument is evaluated once.

For \(n\) Fibonacci values, the time complexity becomes \(O(n)\), with \(O(n)\) cached entries and recursion depth \(O(n)\).

Arguments must be hashable. Cached results should also be treated carefully if they are mutable objects.

### `cache`

```python
from functools import cache

@cache
def square(n):
    print("Computing...")
    return n * n

print(square(4))
print(square(4))
```

The second call reuses the cached result.

`cache` is an unbounded cache, equivalent in effect to `lru_cache(maxsize=None)`. Use it only when the number of distinct keys is reasonably bounded.

### `partial`

`partial()` creates a callable with some arguments pre-filled.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(2))    # 8
```

### `reduce`

`reduce()` repeatedly combines values into a single result.

```python
from functools import reduce
from operator import mul

nums = [1, 2, 3, 4]

print(reduce(mul, nums, 1))  # 24
```

For sums, Python's built-in `sum()` is generally clearer than `reduce()`.

### `singledispatch`

`singledispatch` selects an implementation based on the type of the first argument.

```python
from functools import singledispatch

@singledispatch
def describe(value):
    return f"Unknown: {value}"

@describe.register(int)
def _(value):
    return f"Integer: {value}"

@describe.register(str)
def _(value):
    return f"String: {value}"

print(describe(10))
print(describe("hello"))
print(describe(1.5))
```

### Competitive programming priority

Memoization with `lru_cache` can be especially useful for recursive dynamic programming. Make sure cache keys are hashable, and be mindful of recursion depth and memory consumption.

---

## 8. `logging`

**File:** `08_logging.py`

The `logging` module records diagnostic messages at different severity levels. It is more flexible than using `print()` for debugging a larger application.

### Logging levels

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed diagnostic information |
| `INFO` | Normal application events |
| `WARNING` | Something unexpected or potentially problematic |
| `ERROR` | An operation failed |
| `CRITICAL` | A severe failure |

### Basic logging

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Unexpected condition")
logger.error("Operation failed")
logger.critical("Critical failure")
```

`basicConfig()` generally configures the root logger only if it has not already been configured by the process.

### Logging exceptions

```python
import logging

logger = logging.getLogger(__name__)

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")
```

`logger.exception()` should be called from an exception handler. It logs the message with exception information.

### Logging to a file

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

### Best practices

- Use `logging.getLogger(__name__)` in each module.
- Choose appropriate logging levels.
- Prefer structured logging configuration over scattered `print()` statements.
- Avoid logging passwords, tokens, and sensitive information.
- Use lazy formatting:

```python
logger.info("User %s logged in", "alice")
```

**Competitive programming note:** Ordinary contest solutions generally use `print()` for required output. Logging is more relevant to debugging local tools and larger applications. Avoid sending debug messages to standard output when the judge expects exact output.

---

## 9. `argparse`

**File:** `09_argparse.py`

`argparse` builds command-line interfaces. It parses command-line arguments and provides automatic help and error messages.

### Basic example

```python
import argparse

parser = argparse.ArgumentParser(description="Greeting program")

parser.add_argument("name", help="Name of the person")
parser.add_argument("--age", type=int, default=0)
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

if args.verbose:
    print(vars(args))

print(f"Hello, {args.name}!")
```

Run it from a terminal:

```bash
python app.py Alice --age 30 --verbose
```

### Common argument options

| Option | Purpose |
|---|---|
| Positional argument | Required argument identified by position |
| `type=int` | Converts an argument to an integer |
| `default=value` | Supplies a default value |
| `action="store_true"` | Creates a Boolean flag |
| `choices=[...]` | Restricts allowed values |
| `nargs="+"` | Accepts one or more values |
| `help="..."` | Documents an argument |

### Example with choices

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--format",
    choices=["json", "text"],
    default="text",
)

args = parser.parse_args()
print(args.format)
```

### Keep parsing separate from application logic

A good structure is to place parser construction in a function and call `parse_args()` inside `main()`.

```python
def main():
    parser = build_parser()
    args = parser.parse_args()
    # Perform the requested task here.

if __name__ == "__main__":
    main()
```

For testing, consider passing an explicit argument list to `parse_args([...])` rather than modifying `sys.argv` globally.

**Best practice:** Use `argparse` when building scripts with command-line options. It is unnecessary for most standard online judge submissions.

---

## 10. `subprocess`

**File:** `10_subprocess.py`

The `subprocess` module runs external programs and lets Python interact with their input, output, and exit status.

### Running a command

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('hello')"],
    capture_output=True,
    text=True,
    check=True,
)

print(result.stdout)
print(result.returncode)
```

Using `sys.executable` runs the current Python interpreter.

### Important options

- `capture_output=True` captures standard output and standard error.
- `text=True` returns text strings rather than bytes.
- `check=True` raises `CalledProcessError` if the command exits with a nonzero status.
- `timeout=...` limits how long the operation may run.

### Handling failures

```python
import subprocess

try:
    subprocess.run(
        ["some-command-that-may-fail"],
        check=True,
        timeout=5,
    )
except subprocess.CalledProcessError as error:
    print("Exit code:", error.returncode)
except subprocess.TimeoutExpired:
    print("Command timed out")
except FileNotFoundError:
    print("Executable not found")
```

### Avoid shell injection

Prefer passing a list of arguments:

```python
import subprocess

subprocess.run(["echo", "hello"], check=True)
```

Avoid building shell command strings from untrusted input:

```python
# Avoid with untrusted input:
# subprocess.run(user_input, shell=True)
```

With `shell=True`, shell interpretation introduces additional security risks if untrusted data is included.

### Streaming with `Popen`

`Popen` provides more control over processes and their streams. It is useful when you need interactive input, streaming output, or process pipelines.

```python
import subprocess
import sys

process = subprocess.Popen(
    [sys.executable, "-c", "print('a'); print('b')"],
    stdout=subprocess.PIPE,
    text=True,
)

output, _ = process.communicate()
print(output)
print(process.returncode)
```

For straightforward commands, `subprocess.run()` is usually the preferred interface.

**Safety rule:** Never assume a command is safe just because it is being run from Python. Validate arguments, avoid unnecessary shell interpretation, and handle failures and timeouts.

---

## 11. `shutil` and `tempfile`

**File:** `11_shutil_and_tempfile.py`

`shutil` provides high-level file operations, while `tempfile` creates temporary files and directories safely.

### Copying files

```python
import shutil
from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)

    source = root / "source.txt"
    destination = root / "copy.txt"

    source.write_text("Hello", encoding="utf-8")
    shutil.copy(source, destination)

    print(destination.read_text(encoding="utf-8"))
```

Useful functions:

| Function | Purpose |
|---|---|
| `shutil.copy()` | Copy file contents and basic file permissions |
| `shutil.copy2()` | Copy file contents and attempt to preserve metadata |
| `shutil.copytree()` | Copy a directory tree |
| `shutil.move()` | Move a file or directory |
| `shutil.rmtree()` | Remove a directory tree |
| `shutil.disk_usage()` | Report disk usage |
| `shutil.which()` | Find an executable in the search path |

### Temporary directories

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "data.txt"
    path.write_text("temporary data", encoding="utf-8")

    print(path.read_text(encoding="utf-8"))

# The temporary directory is cleaned up after the block.
```

### Temporary files

```python
import tempfile

with tempfile.NamedTemporaryFile(
    mode="w+",
    suffix=".txt",
    encoding="utf-8",
) as file:
    file.write("Hello")
    file.seek(0)
    print(file.read())
```

Temporary-file behavior can differ across operating systems, particularly when reopening a file by name while it remains open. Use the appropriate `tempfile` options for your platform and use case.

### Finding executables

```python
import shutil

print(shutil.which("python"))
```

`which()` returns the executable path if found, or `None` otherwise.

### Important safety warning

`shutil.rmtree()` recursively deletes a directory tree. Use it only on a directory you have verified is safe to remove. Do not build destructive paths from untrusted input without careful validation.

Prefer `TemporaryDirectory()` when temporary resources should be cleaned up automatically.

---

## 12. Time and Space Complexity

The exact complexity depends on the input size, implementation, and operation. These are useful general guidelines.

| Operation | Typical complexity | Notes |
|---|---|---|
| `Counter(iterable)` | \(O(n)\) average | Counts \(n\) hashable elements |
| `defaultdict` insertion or lookup | Average \(O(1)\) | Hash-table operations |
| `deque.append()` / `popleft()` | \(O(1)\) | Endpoint operations |
| `list.pop(0)` | \(O(n)\) | Remaining elements shift |
| `itertools.chain()` | Lazy iteration | Visits each yielded item |
| `itertools.accumulate()` | \(O(n)\) | Produces running results |
| `itertools.combinations()` | \(O(\binom{n}{r})\) outputs | Output size grows rapidly |
| `itertools.permutations()` | \(O(P(n,r))\) outputs | \(P(n,r)=n!/(n-r)!\) |
| `lru_cache` lookup | Average \(O(1)\) | Excludes the wrapped function's computation |
| `Path.read_text()` | \(O(n)\) | Reads the whole file of size \(n\) |
| `shutil.copy()` | \(O(n)\) | Copies \(n\) bytes |
| `datetime` arithmetic | Usually \(O(1)\) | Fixed-size date/time values |

For lazy iterators, remember that creating the iterator may be inexpensive, but consuming all its results still costs time and may require memory if you convert everything to a list.

---

## 13. Common Mistakes

### Mistake 1: Using `random` for security-sensitive tokens

**Fix:** Use `secrets` for tokens, passwords, and security-sensitive random values.

### Mistake 2: Treating floating-point results as exact

**Fix:** Use `math.isclose()` with an appropriate tolerance when approximate equality is intended.

### Mistake 3: Confusing naive and timezone-aware datetimes

**Fix:** Keep timezone handling explicit and use aware UTC timestamps where appropriate.

### Mistake 4: Using `list.pop(0)` as a queue

**Fix:** Use `collections.deque` for efficient removals from the left.

### Mistake 5: Materializing huge iterator outputs

```python
# Can consume enormous amounts of memory:
# results = list(itertools.permutations(items))
```

**Fix:** Iterate lazily or limit the output to the amount you actually need.

### Mistake 6: Assuming `groupby()` groups every matching key globally

**Fix:** Sort by the grouping key first if equal keys must be collected into a single group.

### Mistake 7: Catching subprocess failures too late

**Fix:** Use `check=True` when a nonzero exit code should be treated as an error, and handle timeouts where appropriate.

### Mistake 8: Using `shell=True` with untrusted input

**Fix:** Prefer an argument list and validate inputs.

### Mistake 9: Accidentally deleting important files

**Fix:** Prefer managed temporary directories and verify paths before recursive deletion.

---

## 14. Competitive Programming Priority

Not every standard-library module is equally useful in contests.

### Learn first

- `math`: GCD, LCM, integer square root, floor, ceiling.
- `collections.Counter`: frequency counting.
- `collections.defaultdict`: graph adjacency lists and grouping.
- `collections.deque`: BFS and sliding windows.
- `itertools`: combinations, permutations, products, and accumulation.
- `functools.lru_cache`: memoization for recursive dynamic programming.
- `sys.stdin.buffer.readline`: fast input for large input files.

### Learn when needed

- `datetime`: date and time problems.
- `pathlib` and `os`: file-based tasks and scripting.
- `sys.argv` and `argparse`: command-line tools.
- `logging`: debugging larger applications.
- `subprocess`, `shutil`, and `tempfile`: automation and system utilities.

### Example: fast input

```python
import sys

input = sys.stdin.buffer.readline

n = int(input())
nums = list(map(int, input().split()))

print(sum(nums))
```

Use this pattern when input is large and the problem requires fast parsing. For small problems, ordinary `input()` is usually sufficient.

### Example: frequency counting

```python
from collections import Counter

nums = [1, 2, 1, 3, 2, 1]
freq = Counter(nums)

print(freq[1])  # 3
print(freq[2])  # 2
```

### Example: BFS queue

```python
from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}

queue = deque([0])
visited = {0}

while queue:
    node = queue.popleft()
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

The queue uses efficient endpoint operations, and marking nodes as visited when enqueuing prevents duplicate queue entries.

---

## 15. Practice Checklist

- [ ] Use common `math` functions without looking up every example.
- [ ] Explain the difference between `random` and `secrets`.
- [ ] Parse and format a datetime string.
- [ ] Calculate durations using `timedelta`.
- [ ] Use timezone-aware UTC datetimes.
- [ ] Navigate paths with `pathlib`.
- [ ] Read and write files safely.
- [ ] Explain `sys.argv`, standard streams, and the recursion limit.
- [ ] Count elements using `Counter`.
- [ ] Group elements with `defaultdict`.
- [ ] Implement a BFS using `deque`.
- [ ] Generate combinations and permutations with `itertools`.
- [ ] Explain why `groupby()` groups consecutive equal keys.
- [ ] Use `accumulate()` for prefix sums.
- [ ] Apply `lru_cache` to a recursive function.
- [ ] Use `partial()` and understand `reduce()`.
- [ ] Configure a logger with appropriate levels.
- [ ] Build a command-line interface with `argparse`.
- [ ] Run an external command safely with `subprocess`.
- [ ] Use `TemporaryDirectory()` to manage temporary files.
- [ ] Identify the time and space costs of the tools you use.

---

## 16. Mini Projects

### Project 1: File statistics tool

Create a program that:

- Accepts a file path using `argparse`.
- Reads the file using `pathlib`.
- Counts words and characters.
- Uses `Counter` to identify frequent words.
- Reports errors clearly.

### Project 2: Random quiz generator

Create a quiz application that:

- Selects questions using `random`.
- Tracks scores using dictionaries or `Counter`.
- Supports reproducible practice sessions with a seed.
- Uses `secrets` only if you need security-sensitive randomness.

### Project 3: Directory backup utility

Build a tool that:

- Accepts source and destination paths.
- Uses `pathlib` to inspect paths.
- Copies files using `shutil`.
- Logs operations using `logging`.
- Handles errors without deleting the source data.

### Project 4: Combinatorics explorer

Create a program that:

- Accepts a list of values.
- Generates combinations of a chosen size.
- Calculates running totals with `itertools.accumulate()`.
- Displays only a limited number of results to avoid excessive memory use.

---

## 17. Recommended Learning Order

Follow this order:

1. `math` and `random`
2. `collections`
3. `itertools`
4. `functools`
5. `sys`
6. `os` and `pathlib`
7. `datetime`
8. `logging`
9. `argparse`
10. `shutil` and `tempfile`
11. `subprocess`

The first four are especially useful for competitive programming. The remaining modules are important for general Python development, automation, and practical scripting.

---

## Final Goal

After completing this folder, you should know when to use Python's standard library instead of implementing functionality from scratch. You should be comfortable with efficient data structures, lazy iteration, memoization, mathematical utilities, filesystem operations, and safe process execution.

For competitive programming, prioritize tools that simplify algorithms and improve performance. For real-world Python development, also practice logging, command-line interfaces, path handling, and resource management.
