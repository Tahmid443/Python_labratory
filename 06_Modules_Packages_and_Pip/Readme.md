# 06. Modules, Packages, and Pip

## 📌 Overview

This section explains how to organize Python code into reusable modules and packages, import functionality from other files, use Python's standard library, and understand the basics of dependency management.

### Learning Objectives

By completing this section, you will learn how to:

- Import modules and specific functions.
- Use aliases and conditional imports.
- Understand `__name__ == "__main__"`.
- Explore useful Python standard-library modules.
- Create and import custom modules.
- Organize code into packages.
- Understand the role of `pip` in installing external libraries.

---

## 📂 Project Structure

```text
06_Modules_Packages_and_Pip/
├── 01_imports.py
├── 02_standard_library.py
├── 03_custom_modules.py
└── 04_packages.py
```

| File | Description |
|---|---|
| `01_imports.py` | Import statements, aliases, lazy imports, and the main guard |
| `02_standard_library.py` | Common built-in Python modules |
| `03_custom_modules.py` | Creating and using custom modules |
| `04_packages.py` | Package structure and submodule imports |

---

## 1. Imports in Python

**File:** `01_imports.py`

A module is a Python file containing reusable code, such as functions, classes, and variables. Importing a module lets another file use that code.

### 1.1 Import an Entire Module

```python
import math

print(math.pi)
print(math.sqrt(25))
```

When importing a whole module, access its members using the module name followed by a dot.

### 1.2 Import Specific Members

```python
from math import pi, sqrt

print(pi)
print(sqrt(25))
```

This allows you to use the imported members without writing `math.` each time.

### 1.3 Use an Alias

An alias provides a shorter or more convenient name.

```python
import math as m

print(m.e)
```

You can also alias individual members:

```python
from math import pi as PI

print(PI)
```

### 1.4 Import Everything

```python
# Avoid this in most projects.
# from math import *
```

Wildcard imports can make it difficult to identify where a name came from and may cause naming conflicts. Explicit imports are generally clearer.

### 1.5 Conditional Imports

Sometimes a program can use an optional third-party library if it is installed.

```python
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

print(HAS_NUMPY)
```

This is useful when a dependency is optional. If the program actually needs NumPy to function, declaring and installing the dependency is usually better than silently continuing without it.

### 1.6 The `__name__` Variable

Every Python module has a special variable called `__name__`.

- When a file runs directly, `__name__` is usually `"__main__"`.
- When a file is imported, `__name__` is normally the module's import name.

```python
def main():
    print("Program is running")

if __name__ == "__main__":
    main()
```

The main guard allows a file to be both executed as a script and imported without automatically running its main program.

### 1.7 Lazy Imports

An import placed inside a function is performed when execution reaches that import.

```python
def convert_to_json(data):
    import json
    return json.dumps(data)

print(convert_to_json({"ok": True}))
```

This can defer optional or expensive imports until they are needed. It is not necessary for every import, so use it when it provides a real benefit.

### 1.8 Relative Imports

Relative imports are commonly used inside packages.

```python
from . import utils
from .utils import helper
```

The leading dot refers to the current package. Relative imports generally require the module to run in a package context; running a package file directly can cause import errors.

---

## 2. Python Standard Library

**File:** `02_standard_library.py`

The standard library is a collection of modules included with Python. You can use these modules without installing them separately with `pip`.

### Common Modules

| Module | Purpose | Useful Examples |
|---|---|---|
| `os` | Operating-system interaction | `os.getcwd()` |
| `sys` | Python interpreter information | `sys.version` |
| `math` | Mathematical functions | `math.sqrt()`, `math.ceil()` |
| `random` | Pseudorandom values | `random.randint()` |
| `datetime` | Dates and times | `date.today()` |
| `json` | JSON serialization and parsing | `json.dumps()`, `json.loads()` |
| `re` | Regular expressions | `re.findall()` |
| `collections` | Specialized containers | `Counter`, `deque` |
| `itertools` | Efficient iterator tools | `chain()`, `combinations()` |
| `functools` | Higher-order function utilities | `reduce()`, `lru_cache` |
| `pathlib` | Filesystem paths | `Path.cwd()` |

### 2.1 `math`

```python
import math

print(math.sqrt(16))  # 4.0
print(math.floor(3.7))  # 3
print(math.ceil(3.2))  # 4
```

Useful for mathematical calculations. For competitive programming, also learn `math.gcd()`, `math.lcm()`, and `math.factorial()`.

### 2.2 `random`

```python
import random

print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

random.seed(42)
print(random.random())
```

`randint(a, b)` includes both endpoints. A fixed seed can make pseudorandom results reproducible, which is useful for testing.

Do not use `random` for passwords, tokens, or other security-sensitive values; use the `secrets` module instead.

### 2.3 `datetime`

```python
from datetime import date, datetime, timedelta

print(date.today())
print(datetime.now())
print(date.today() + timedelta(days=7))
```

Use `date` for calendar dates, `datetime` for date-and-time values, and `timedelta` to represent durations.

### 2.4 `json`

```python
import json

data = {"name": "Alice", "score": 95}

text = json.dumps(data)
print(text)

parsed = json.loads(text)
print(parsed["score"])
```

- `json.dumps()` converts a Python object into a JSON string.
- `json.loads()` parses a JSON string into a Python object.

JSON is commonly used for APIs, configuration, and data exchange.

### 2.5 `collections`

```python
from collections import Counter, defaultdict, deque

print(Counter("hello"))

counts = defaultdict(int)
counts["apple"] += 1
print(counts["apple"])

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
```

Important tools:

- `Counter`: counts occurrences of elements.
- `defaultdict`: provides a default value for missing keys.
- `deque`: supports efficient additions and removals at both ends.

For competitive programming, `Counter` and `deque` are especially useful.

### 2.6 `itertools`

```python
from itertools import chain, combinations

print(list(chain([1, 2], [3, 4])))
print(list(combinations([1, 2, 3], 2)))
```

`chain()` combines iterables without manually concatenating them. `combinations()` generates selections of a specified size without regard to order.

Other useful tools include `permutations()`, `product()`, `accumulate()`, and `islice()`.

**Important:** Many `itertools` functions produce iterators. Converting them to a list is convenient for small examples, but may consume substantial memory for large results.

### 2.7 `functools`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
```

`lru_cache` caches function results and can speed up repeated calculations. It is particularly useful for recursive dynamic programming when the arguments are hashable.

### 2.8 `pathlib`

```python
from pathlib import Path

current_directory = Path.cwd()
print(current_directory)

file_path = current_directory / "data.txt"
print(file_path)
```

`pathlib` provides an object-oriented way to work with filesystem paths and is often more convenient than manually joining path strings.

---

## 3. Creating Custom Modules

**File:** `03_custom_modules.py`

A custom module is a Python file that you create to store reusable functions, classes, and variables.

### 3.1 Example Module

Suppose you create a file named `myutils.py`:

```python
# myutils.py

PI = 3.14159

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def add(self, a, b):
        return a + b
```

### 3.2 Import Your Module

Place `main.py` in the same directory:

```python
# main.py

import myutils

print(myutils.add(2, 3))
print(myutils.PI)

calculator = myutils.Calculator()
print(calculator.add(4, 5))
```

You can also import specific members:

```python
from myutils import add, PI

print(add(10, 20))
print(PI)
```

Python searches for modules in locations that include the current import context and directories listed in `sys.path`. Ensure your module is located where Python can find it.

### 3.3 Understanding the Demonstration in This File

The supplied `03_custom_modules.py` demonstrates module creation dynamically using `types.ModuleType` and `exec()`.

This is useful for understanding how Python represents modules, but it is not the normal way to organize a project. Creating an ordinary `.py` file and importing it is simpler and easier to maintain.

**Security warning:** Never pass untrusted input to `exec()` or use `eval()` to evaluate arbitrary user-provided expressions. Both can execute code. The `Calculator` example in the demonstration uses `eval()`, so it should not be copied into a real application that accepts untrusted input.

---

## 4. Python Packages

**File:** `04_packages.py`

A package organizes related Python modules into a directory structure. Packages help keep larger projects maintainable.

### 4.1 Typical Package Structure

```text
myproject/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── math/
    │   ├── __init__.py
    │   ├── basic.py
    │   └── advanced.py
    └── utils/
        ├── __init__.py
        └── helpers.py
```

Here:

- `mypackage` is the top-level package.
- `math` and `utils` are subpackages.
- `basic.py`, `advanced.py`, and `helpers.py` are modules.
- `__init__.py` can mark a regular package and define its initialization behavior.

Modern Python also supports namespace packages without `__init__.py`, but explicit `__init__.py` files are still common in ordinary projects.

### 4.2 Example Module

```python
# mypackage/math/basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Import a function from this module:

```python
from mypackage.math.basic import add, subtract

print(add(2, 3))
print(subtract(5, 2))
```

You can also import the module itself:

```python
from mypackage.math import basic

print(basic.add(2, 3))
```

### 4.3 What Does `__init__.py` Do?

The `__init__.py` file can:

- Initialize package-level state.
- Expose selected functions and classes.
- Define the package's public interface.
- Run package initialization code when the package is imported.

For example:

```python
# mypackage/math/__init__.py

from .basic import add, subtract
```

Then:

```python
from mypackage.math import add, subtract

print(add(2, 3))
```

### 4.4 Understanding the Package Demonstration

The supplied `04_packages.py` creates module objects dynamically and registers them in `sys.modules`.

This demonstrates Python's module system, but it does not reproduce a normal on-disk package structure. For practical learning, create the folders and `.py` files shown above, then import them using their package paths.

---

## 5. What Is `pip`?

`pip` is Python's package installer. It installs third-party packages that are not included in the Python standard library.

### 5.1 Check Your Python and pip Versions

```bash
python --version
python -m pip --version
```

Using `python -m pip` helps ensure that `pip` is associated with the Python interpreter you intend to use.

### 5.2 Install a Package

```bash
python -m pip install requests
```

### 5.3 Upgrade a Package

```bash
python -m pip install --upgrade requests
```

### 5.4 Uninstall a Package

```bash
python -m pip uninstall requests
```

### 5.5 List Installed Packages

```bash
python -m pip list
```

### 5.6 Use a Virtual Environment

A virtual environment isolates project dependencies from other Python projects.

Create one:

```bash
python -m venv .venv
```

Activate it on Windows Command Prompt:

```bat
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Then install packages inside the environment:

```bash
python -m pip install requests
```

A common dependency workflow is to maintain a `requirements.txt` file:

```bash
python -m pip freeze > requirements.txt
```

Another environment can install the listed dependencies with:

```bash
python -m pip install -r requirements.txt
```

For reproducible projects, review dependency versions and avoid recording unrelated packages from a shared environment.

---

## 6. Module vs. Package vs. Library

| Term | Meaning | Example |
|---|---|---|
| Module | A unit of Python code, commonly a `.py` file | `myutils.py` |
| Package | A way to organize related modules | `mypackage/` |
| Library | A broader collection of reusable code | Python's standard library or Requests |
| `pip` | A tool for installing Python packages | `python -m pip install requests` |

The terms *package* and *library* are sometimes used informally in overlapping ways, but they are not exactly the same thing.

---

## 7. Common Mistakes to Avoid

1. **Using wildcard imports:** `from module import *` can create naming conflicts.
2. **Naming files after standard-library modules:** Names such as `random.py`, `json.py`, or `collections.py` can shadow the real modules.
3. **Running package modules incorrectly:** Relative imports may fail when a package file is executed directly. Run it in the appropriate package context.
4. **Using `eval()` or `exec()` with untrusted input:** These functions can execute arbitrary code.
5. **Installing packages into the wrong environment:** Use the intended interpreter and virtual environment.
6. **Confusing standard-library modules with third-party packages:** Modules such as `math`, `json`, and `itertools` normally do not need to be installed with `pip`.
7. **Importing a module before it is available on the import path:** Check your directory structure and module names.

---

## 8. Competitive Programming Notes

For Python competitive programming, prioritize these standard-library tools:

| Tool | Typical Use |
|---|---|
| `math.gcd()` | Greatest common divisor |
| `math.lcm()` | Least common multiple |
| `collections.Counter` | Frequency counting |
| `collections.defaultdict` | Grouping and counting |
| `collections.deque` | Queues and BFS |
| `heapq` | Priority queues and heaps |
| `bisect` | Binary search on sorted lists |
| `itertools` | Combinations, permutations, products |
| `functools.lru_cache` | Memoization for dynamic programming |
| `sys.stdin` | Fast input for large test cases |

Example: frequency counting

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]
frequency = Counter(numbers)

print(frequency[3])  # 3
```

Example: greatest common divisor

```python
from math import gcd

print(gcd(24, 36))  # 12
```

Example: fast input

```python
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

print(sum(numbers))
```

**Competitive programming tip:** Learn how to use the standard library effectively before implementing every utility from scratch. However, understand the underlying algorithms and complexities so you can choose the right tool.

---

## 9. Key Takeaways

- Modules let you reuse code across Python files.
- `import` and `from ... import ...` provide different ways to access module members.
- `__name__ == "__main__"` separates direct script execution from importing.
- Python's standard library includes powerful tools for mathematics, data structures, iteration, dates, and files.
- Custom modules help separate responsibilities and reduce duplicated code.
- Packages organize modules into a hierarchy.
- `pip` installs third-party packages, while virtual environments isolate dependencies.
- Avoid unsafe dynamic execution and be careful not to shadow standard-library module names.

---

## 10. Practice Checklist

- [ ] Import a module using `import`.
- [ ] Import specific functions and assign aliases.
- [ ] Write a script that uses the `__main__` guard.
- [ ] Experiment with `math`, `json`, and `datetime`.
- [ ] Use `Counter`, `defaultdict`, and `deque`.
- [ ] Generate combinations with `itertools`.
- [ ] Create a custom module and import it from another file.
- [ ] Build a package with at least two submodules.
- [ ] Create and activate a virtual environment.
- [ ] Install and uninstall a third-party package using `pip`.
- [ ] Solve a competitive programming problem using a standard-library module.

## ▶️ Running the Examples

From the project directory, run each file with Python:

```bash
python 01_imports.py
python 02_standard_library.py
python 03_custom_modules.py
python 04_packages.py
```

For the package examples, remember that the supplied scripts simulate modules dynamically. The real-world examples in this README use ordinary Python files and directories.

**Recommended learning order:** Imports → Standard Library → Custom Modules → Packages → `pip` and Virtual Environments.