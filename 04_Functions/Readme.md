# 04. Python Functions — Complete Notes

Functions are reusable blocks of code designed to perform specific tasks. They help organize programs, reduce repetition, improve readability, and make complex problems easier to solve.

In competitive programming, functions are especially useful for implementing algorithms, separating logic into smaller parts, testing solutions, and understanding recursion.

## Table of Contents

1. [Defining Functions](#1-defining-functions)
2. [Parameters and Arguments](#2-parameters-and-arguments)
3. [The Return Statement](#3-the-return-statement)
4. [Scope and Namespace](#4-scope-and-namespace)
5. [Default Arguments](#5-default-arguments)
6. [`*args` and `**kwargs`](#6-args-and-kwargs)
7. [Lambda Functions](#7-lambda-functions)
8. [Recursion Basics](#8-recursion-basics)
9. [First-Class Functions](#9-first-class-functions)
10. [Annotations and Docstrings](#10-annotations-and-docstrings)
11. [Function Complexity](#11-function-complexity)
12. [Common Mistakes](#12-common-mistakes)
13. [Practice Problems](#13-practice-problems)

---

## 1. Defining Functions

**File:** `01_defining_functions.py`

A function is a named block of code that can be executed whenever it is called.

### 1.1 Basic Function Syntax

```python
def greet():
    print("Hello!")

greet()
greet()
```

Output:

```text
Hello!
Hello!
```

Explanation:

- `def` defines a function.
- `greet` is the function name.
- `()` contains parameters, if any.
- The indented block is the function body.
- `greet()` calls the function.

Defining a function does not execute its body. The body runs when the function is called.

### 1.2 Functions with Parameters

Parameters allow a function to receive input.

```python
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")
greet_name("Bob")
```

Output:

```text
Hello, Alice!
Hello, Bob!
```

Here, `name` is a parameter, while `"Alice"` and `"Bob"` are arguments.

### 1.3 Functions with Return Values

A function can calculate a value and return it using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

The returned value can be stored, printed, passed to another function, or used in an expression.

```python
print(add(2, 3) * 2)
```

Output:

```text
10
```

### 1.4 Returning Multiple Values

Python functions can return multiple values by returning a tuple.

```python
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([1, 5, 3, 9, 2])

print(low)
print(high)
```

Output:

```text
1
9
```

The statement `return min(nums), max(nums)` is effectively returning a tuple:

```python
return (min(nums), max(nums))
```

This is useful when an algorithm needs to produce several related results.

### 1.5 Docstrings

A docstring describes what a function does.

```python
def area(radius):
    """Return the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2

print(area.__doc__)
print(area(5))
```

Output:

```text
Return the area of a circle given its radius.
78.53981633974483
```

A docstring is different from a comment. Python stores a function's docstring in its `__doc__` attribute, making it available to documentation tools and `help()`.

### 1.6 Nested Functions

A function can be defined inside another function.

```python
def outer():
    def inner():
        return "Hello from inner!"

    return inner()

print(outer())
```

Nested functions are useful for organizing helper logic and implementing closures.

### 1.7 Functions Are Objects

In Python, functions are objects and can be assigned to variables.

```python
def add(a, b):
    return a + b

f = add

print(f(2, 3))
```

Output:

```text
5
```

Both `add` and `f` refer to the same function. Assigning a function to another variable does not execute it.

**Key takeaway:** Functions can receive inputs, perform operations, return results, and be passed around like other objects.

---

## 2. Parameters and Arguments

**File:** `02_parameters_arguments.py`

Parameters define what inputs a function accepts. Arguments are the actual values supplied when calling it.

### 2.1 Positional Arguments

Arguments are matched to parameters by position.

```python
def subtract(a, b):
    return a - b

print(subtract(10, 3))
```

Output:

```text
7
```

The first argument becomes `a`, and the second becomes `b`.

### 2.2 Keyword Arguments

Arguments can also be matched by parameter name.

```python
def subtract(a, b):
    return a - b

print(subtract(b=3, a=10))
```

Output:

```text
7
```

Keyword arguments can be supplied in a different order because their parameter names identify the destination.

### 2.3 Mixing Positional and Keyword Arguments

Positional arguments must come before keyword arguments.

```python
def power(base, exp):
    return base ** exp

print(power(2, exp=3))
print(power(base=2, exp=3))
```

Both calls return `8`.

Incorrect:

```python
# power(base=2, 3)
```

This raises `SyntaxError` because a positional argument follows a keyword argument.

### 2.4 Positional-Only Parameters

Python 3.8 introduced `/` in function parameter lists.

Parameters before `/` must be passed positionally.

```python
def add(a, b, /, c):
    return a + b + c

print(add(1, 2, 3))
print(add(1, 2, c=3))
```

Both calls return `6`.

This call is invalid:

```python
# add(a=1, b=2, c=3)
```

Here, `a` and `b` are positional-only, while `c` can be positional or keyword-based.

### 2.5 Keyword-Only Parameters

Parameters after a bare `*` must be supplied using their names.

```python
def calculate(a, *, b, c):
    return a + b + c

print(calculate(1, b=2, c=3))
```

Output:

```text
6
```

The following call is invalid:

```python
# calculate(1, 2, 3)
```

Keyword-only parameters make function calls more explicit and readable.

### 2.6 Combining Parameter Types

```python
def calculate(a, b, /, c, *, d):
    return a + b + c + d

print(calculate(1, 2, 3, d=4))
```

Output:

```text
10
```

The parameter rules are:

- `a` and `b`: positional-only.
- `c`: positional or keyword.
- `d`: keyword-only.

### 2.7 Parameter Categories at a Glance

| Syntax | Meaning |
|---|---|
| `def f(a, b):` | Regular parameters |
| `def f(a, /):` | Positional-only |
| `def f(*, a):` | Keyword-only |
| `def f(*args):` | Variable positional arguments |
| `def f(**kwargs):` | Variable keyword arguments |

**Competitive programming tip:** Most contest solutions primarily use regular positional parameters. Still, understanding keyword-only and positional-only parameters helps you write robust, reusable Python code.

---

## 3. The Return Statement

**File:** `03_return_statement.py`

The `return` statement ends the current function call and optionally sends a result back to the caller.

### 3.1 Returning a Single Value

```python
def square(x):
    return x * x

result = square(5)
print(result)
```

Output:

```text
25
```

### 3.2 Functions That Return `None`

A function that reaches the end without executing a `return` statement returns `None` implicitly.

```python
def log(msg):
    print(f"[LOG] {msg}")

result = log("Program started")
print(result)
```

Output:

```text
[LOG] Program started
None
```

The function prints a message but does not return that message.

### 3.3 Returning Multiple Values

```python
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

low, high, average = stats([1, 2, 3, 4, 5])

print(low, high, average)
```

Output:

```text
1 5 3.0
```

The function returns a tuple containing the minimum, maximum, and average.

This function assumes the list is non-empty. An empty list would cause an error, so production code should decide how to handle empty input.

### 3.4 Early Return

An early return exits a function as soon as the answer is known.

```python
def is_even(n):
    if n % 2 != 0:
        return False

    return True

print(is_even(4))
print(is_even(7))
```

Output:

```text
True
False
```

A shorter implementation is:

```python
def is_even(n):
    return n % 2 == 0
```

Early returns often reduce unnecessary nesting and make functions easier to read.

### 3.5 `return` vs. `print`

This is one of the most important concepts in Python.

```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(1, 2)
y = add_return(1, 2)

print("x =", x)
print("y =", y)
```

Output:

```text
3
x = None
y = 3
```

`add_print()` displays the result but returns `None`. `add_return()` provides the result for later use.

In competitive programming, functions that implement algorithms should generally return results, leaving printing to the caller.

### 3.6 Returning `None` When No Result Exists

```python
def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n

    return None

print(find_first_even([1, 3, 8, 9]))
print(find_first_even([1, 3, 5]))
```

Output:

```text
8
None
```

The explicit `return None` documents what happens when no even number is found.

**Important:** `None` is a value, not the same as `0`, `False`, or an empty string.

---

## 4. Scope and Namespace

**File:** `04_scope_and_namespace.py`

A namespace maps names to objects. Scope determines where a name can be accessed.

Python follows the **LEGB rule** when resolving ordinary variable names.

### 4.1 The LEGB Rule

| Scope | Meaning |
|---|---|
| L — Local | Names inside the current function |
| E — Enclosing | Names in enclosing functions |
| G — Global | Names defined at module level |
| B — Built-in | Names provided by Python, such as `len` and `print` |

Python searches these scopes in order when resolving a name.

### 4.2 Global Scope

A variable defined at module level is global to that module.

```python
x = 10

def read_global():
    print(x)

read_global()
```

Output:

```text
10
```

A function can read a global variable without declaring it `global`.

### 4.3 Modifying Global Variables

To reassign a module-level variable from inside a function, use `global`.

```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)
```

Output:

```text
20
```

Without `global`, assigning to `x` inside the function normally creates a local variable instead.

Global state can make programs harder to test and reason about. Prefer passing values as arguments and returning results when practical.

### 4.4 Local Scope

Variables created inside a function are local to that function unless another mechanism is used.

```python
def local_demo():
    y = 5
    print(y)

local_demo()
```

Output:

```text
5
```

Trying to access `y` outside the function raises `NameError` because that name is not defined in the surrounding scope.

### 4.5 Enclosing Scope and `nonlocal`

Nested functions can access variables from enclosing functions.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter = outer()

print(counter())
print(counter())
print(counter())
```

Output:

```text
1
2
3
```

`nonlocal` tells Python that `count` refers to a binding in an enclosing function scope rather than a new local variable.

This is useful when building closures that maintain state.

### 4.6 Local Variables Can Shadow Global Variables

```python
name = "global"

def show():
    name = "local"
    print(name)

show()
print(name)
```

Output:

```text
local
global
```

The local `name` is separate from the global `name`.

### 4.7 Built-in Names

Python provides built-in functions such as `len()`, `sum()`, `min()`, and `max()`.

```python
def print_len(items):
    print(len(items))

print_len([1, 2, 3])
```

Avoid naming your variables or functions after important built-ins.

For example, using `list` as a variable name can hide the built-in `list()` constructor in the current scope.

### 4.8 Prefer Explicit Inputs and Outputs

Instead of relying on global variables:

```python
def better_add(a, b, c=0):
    return a + b + c
```

This function makes its dependencies explicit and is easier to reuse and test.

---

## 5. Default Arguments

**File:** `05_default_arguments.py`

Default arguments let parameters use predefined values when callers omit those arguments.

### 5.1 Basic Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
```

Output:

```text
Hello, Alice!
Hi, Bob!
```

If `greeting` is omitted, its default value is used.

### 5.2 Default Parameters Must Follow Required Parameters

Valid:

```python
def calculate(a, b=2, c=3):
    return a + b + c

print(calculate(1))
print(calculate(1, 5))
print(calculate(1, 5, 10))
```

Output:

```text
6
9
16
```

Invalid:

```python
# def calculate(a=1, b):
#     return a + b
```

A required positional parameter cannot follow a default positional parameter.

### 5.3 The Mutable Default Argument Trap

Default argument expressions are evaluated once when the function is defined, not every time the function is called.

Consider this example:

```python
def bad_append(item, items=[]):
    items.append(item)
    return items

print(bad_append(1))
print(bad_append(2))
print(bad_append(3))
```

Output:

```text
[1]
[1, 2]
[1, 2, 3]
```

All calls reuse the same default list.

This behavior is often a bug when each call is expected to start with a fresh list.

### 5.4 The Correct Pattern: Use `None`

```python
def good_append(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(good_append(1))
print(good_append(2))
```

Output:

```text
[1]
[2]
```

The function creates a new list when no list is provided.

If a caller passes an existing list, the function intentionally modifies that list.

### 5.5 When Defaults Are Safe

Immutable defaults such as integers, strings, and `None` are generally safe:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

The problem is not the use of defaults itself. It is unintentionally sharing a mutable object between calls.

---

## 6. `*args` and `**kwargs`

**File:** `06_args_kwargs.py`

Use `*args` and `**kwargs` when a function needs to accept a variable number of positional or keyword arguments.

The names `args` and `kwargs` are conventional; the important part is the `*` and `**` syntax.

### 6.1 `*args`: Variable Positional Arguments

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
```

Output:

```text
6
15
```

Inside the function, `args` is a tuple containing the additional positional arguments.

A call with no extra positional arguments gives an empty tuple.

### 6.2 `**kwargs`: Variable Keyword Arguments

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=30, city="Dhaka")
```

Output:

```text
name = Alice
age = 30
city = Dhaka
```

Inside the function, `kwargs` is a dictionary of additional keyword arguments.

### 6.3 Combining Parameters, `*args`, and `**kwargs`

```python
def full(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

full(1, 2, 3, 4, x=10, y=20)
```

Output:

```text
a = 1, b = 2
args = (3, 4)
kwargs = {'x': 10, 'y': 20}
```

The first two positional arguments fill `a` and `b`. Remaining positional arguments go into `args`, while additional keyword arguments go into `kwargs`.

### 6.4 Unpacking Arguments at the Call Site

A list or tuple can be expanded into positional arguments using `*`.

```python
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]

print(add3(*nums))
```

Output:

```text
6
```

A dictionary can be expanded into keyword arguments using `**`.

```python
opts = {"a": 1, "b": 2, "c": 3}

print(add3(**opts))
```

Output:

```text
6
```

The dictionary keys must match accepted parameter names unless the function accepts arbitrary keyword arguments.

### 6.5 When Should You Use Them?

Use `*args` and `**kwargs` when variable arguments genuinely make an interface more useful, such as wrappers and flexible utility functions.

For a simple algorithm with a fixed number of inputs, regular parameters are usually clearer.

---

## 7. Lambda Functions

**File:** `07_lambda_functions.py`

A lambda expression creates a small anonymous function. Its body is a single expression whose result becomes the return value.

### 7.1 Basic Lambda

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Equivalent regular function:

```python
def square(x):
    return x ** 2
```

Prefer `def` when the function needs a descriptive name, multiple statements, or more complex logic.

### 7.2 Multiple Parameters

```python
add = lambda a, b: a + b

print(add(2, 3))
```

Output:

```text
5
```

### 7.3 Conditional Expressions

```python
max_of = lambda a, b: a if a > b else b

print(max_of(3, 5))
```

Output:

```text
5
```

A lambda can contain a conditional expression, but it cannot contain ordinary statements such as `return`, `for`, or `while` in its body.

### 7.4 Lambda with `sorted()`

One of the most common uses is supplying a sorting key.

```python
words = ["banana", "apple", "cherry"]

print(sorted(words, key=lambda word: len(word)))
```

Output:

```text
['apple', 'banana', 'cherry']
```

The key function determines the value used for comparisons.

Sorting by the second element of each tuple:

```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
]

students.sort(key=lambda student: student[1])
print(students)
```

### 7.5 Lambda with `map()`

`map()` applies a function to each item of an iterable.

```python
nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
print(doubled)
```

Output:

```text
[2, 4, 6, 8]
```

A list comprehension is often easier to read:

```python
doubled = [x * 2 for x in nums]
```

### 7.6 Lambda with `filter()`

`filter()` keeps elements for which the function returns a truthy value.

```python
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

Output:

```text
[2, 4, 6]
```

Equivalent comprehension:

```python
evens = [x for x in nums if x % 2 == 0]
```

### 7.7 Lambda with `reduce()`

`reduce()` combines elements into one result by repeatedly applying a two-argument function.

```python
from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)
print(total)
```

Output:

```text
10
```

For summation, `sum(nums)` is simpler and generally preferable. `reduce()` is useful when the combining operation is more specialized.

### 7.8 When Not to Use Lambda

Avoid complicated expressions:

```python
# Hard to read:
# lambda x: (x ** 2 + 1 if x > 0 else -x) * 3
```

Prefer a regular function:

```python
def transform(x):
    if x > 0:
        return (x ** 2 + 1) * 3
    return -x * 3
```

**Rule of thumb:** Use a lambda for short expressions, especially as a sorting key. Use `def` for more complex logic.

---

## 8. Recursion Basics

**File:** `08_recursion_basics.py`

Recursion occurs when a function calls itself to solve a smaller version of the same problem.

Recursive solutions usually contain:

1. **Base case:** A condition that stops recursion.
2. **Recursive case:** A call to the same function with a smaller or simpler problem.
3. **Progress:** Each recursive step must move toward a base case.

### 8.1 Factorial

For a non-negative integer \(n\):

\[
n! =
\begin{cases}
1 & n = 0 \\
n \times (n-1)! & n > 0
\end{cases}
\]

Implementation:

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

Call sequence:

```text
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
120
```

Time complexity: \(O(n)\).

Auxiliary call-stack space: \(O(n)\).

### 8.2 Fibonacci Sequence

The mathematical recurrence is:

\[
F(n) =
\begin{cases}
n & n \leq 1 \\
F(n-1) + F(n-2) & n > 1
\end{cases}
\]

Recursive implementation:

```python
def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

This implementation is easy to understand but inefficient because it repeatedly calculates the same values.

Time complexity is exponential, approximately \(O(2^n)\), and recursion depth is \(O(n)\).

A more efficient version uses iteration:

```python
def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a

print(fib(10))
```

This returns the 10th Fibonacci number in \(O(n)\) time and \(O(1)\) auxiliary space.

### 8.3 Recursive Sum of a List

```python
def sum_list(nums):
    if not nums:
        return 0

    return nums[0] + sum_list(nums[1:])

print(sum_list([1, 2, 3, 4]))
```

Output:

```text
10
```

The base case is an empty list. Each recursive call adds the first element to the sum of the remaining elements.

This particular implementation copies a slice at each call, so it can take \(O(n^2)\) total time and \(O(n)\) stack space.

An index-based version avoids repeated slicing:

```python
def sum_list(nums, i=0):
    if i == len(nums):
        return 0

    return nums[i] + sum_list(nums, i + 1)
```

This version takes \(O(n)\) time and \(O(n)\) stack space.

### 8.4 Reversing a String Recursively

```python
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
```

Output:

```text
olleh
```

The recursive call reverses the substring without its first character, then places the first character at the end.

Because slicing and string concatenation create new strings, this implementation takes \(O(n^2)\) time in typical analyses and \(O(n)\) stack space.

For ordinary string reversal, `s[::-1]` is usually more efficient and simpler.

### 8.5 Recursive Binary Search

Binary search finds a target in a **sorted** sequence by repeatedly reducing the search interval by half.

```python
def binary_search(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1

    if lo > hi:
        return -1

    mid = (lo + hi) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)

    return binary_search(arr, target, lo, mid - 1)


print(binary_search([1, 3, 5, 7, 9], 7))
```

Output:

```text
3
```

The function returns the index of the target or `-1` if the target is absent.

Complexity:

- Time: \(O(\log n)\).
- Auxiliary call-stack space: \(O(\log n)\).

**Important:** The input must be sorted for binary search to work correctly.

### 8.6 Tower of Hanoi

The Tower of Hanoi problem moves `n` disks from one peg to another, using an auxiliary peg, without placing a larger disk on a smaller one.

```python
def hanoi(n, src, dst, aux):
    if n <= 0:
        return

    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return

    hanoi(n - 1, src, aux, dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n - 1, aux, dst, src)


hanoi(3, "A", "C", "B")
```

The recurrence for the minimum number of moves is:

\[
T(n) = 2T(n-1) + 1
\]

Therefore, the number of moves is \(2^n - 1\), and the time complexity is \(O(2^n)\).

### 8.7 Recursion and Python's Call Stack

Each recursive call adds a stack frame. Python limits recursion depth, so deep recursion can raise `RecursionError`.

Python does not optimize tail recursion into constant-stack execution.

In competitive programming:

- Use recursion for trees, divide-and-conquer, backtracking, and naturally recursive problems.
- Consider iterative solutions for deep linear recursion.
- Avoid increasing the recursion limit unless you understand the stack and environment constraints.

---

## 9. First-Class Functions

**File:** `09_first_class_functions.py`

In Python, functions are first-class objects. This means functions can be:

- Assigned to variables.
- Passed as arguments.
- Returned from other functions.
- Stored in lists, tuples, or dictionaries.

A function that receives or returns other functions is often called a higher-order function.

### 9.1 Assigning Functions to Variables

```python
def greet(name):
    return f"Hello, {name}"

say_hi = greet

print(say_hi("Alice"))
```

The variable `say_hi` refers to the same function object as `greet`.

### 9.2 Passing Functions as Arguments

```python
def apply(func, value):
    return func(value)

def greet(name):
    return f"Hello, {name}"

print(apply(greet, "Bob"))
print(apply(str.upper, "hello"))
```

Output:

```text
Hello, Bob
HELLO
```

Notice that `greet` is passed without parentheses. Writing `greet("Bob")` would call it immediately instead of passing the function itself.

### 9.3 Returning Functions

```python
def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
```

Output:

```text
10
15
```

`make_multiplier()` returns a function that remembers the value of `n`.

### 9.4 Closures

A closure is a function that retains access to variables from its enclosing lexical scope even after the enclosing function has returned.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply

double = make_multiplier(2)

print(double(10))
```

The returned `multiply` function retains access to `n`, whose value is `2`.

Closures are useful for callbacks, decorators, and functions that maintain private state.

### 9.5 Storing Functions in a Dictionary

```python
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
}

print(ops["add"](3, 4))
print(ops["sub"](10, 4))
```

Output:

```text
7
6
```

This pattern can implement a simple operation dispatcher.

For more complicated operations, named functions are often clearer.

### 9.6 Higher-Order Functions

A higher-order function can accept other functions or return a function.

```python
def compose(f, g):
    return lambda x: f(g(x))

add1 = lambda x: x + 1
double = lambda x: x * 2

combined = compose(add1, double)

print(combined(5))
```

Output:

```text
11
```

The result is:

\[
f(g(5)) = 2 \times 5 + 1 = 11
\]

### 9.7 Built-in Higher-Order Functions

```python
nums = [1, 2, 3, 4]

print(list(map(str, nums)))
print(list(filter(lambda x: x > 2, nums)))
```

Output:

```text
['1', '2', '3', '4']
[3, 4]
```

`map()` transforms elements, while `filter()` selects elements based on a predicate.

For straightforward transformations and filtering, list comprehensions are often more readable.

---

## 10. Annotations and Docstrings

**File:** `10_annotations_and_docstrings.py`

Type annotations document the expected types of parameters and return values. Docstrings explain the purpose and behavior of functions.

### 10.1 Basic Type Annotations

```python
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

print(add(2, 3))
```

Here:

- `a: int` suggests that `a` should be an integer.
- `b: int` suggests that `b` should be an integer.
- `-> int` documents the expected return type.

Python does not enforce these annotations automatically at runtime.

For example:

```python
print(add("hello", " world"))
```

This works and returns `"hello world"` because the `+` operator supports concatenating strings.

Type checkers can use annotations to detect many mistakes before execution.

### 10.2 Documenting Function Arguments and Results

```python
def greet(name: str, times: int = 1) -> str:
    """
    Return a greeting repeated `times` times.

    Args:
        name: Name of the person.
        times: Number of repetitions.

    Returns:
        The repeated greeting string.
    """
    return f"Hello, {name}! " * times

print(greet("Alice", 2))
```

Docstrings are available through `function.__doc__` and `help(function)`.

### 10.3 Optional Results

A function that returns an integer or `None` can be annotated using `Optional[int]`.

```python
from typing import Optional

def first_positive(items: list[int]) -> Optional[int]:
    for x in items:
        if x > 0:
            return x

    return None
```

`Optional[int]` means `int | None`.

The modern syntax, available in Python 3.10 and later, is:

```python
def first_positive(items: list[int]) -> int | None:
    for x in items:
        if x > 0:
            return x

    return None
```

### 10.4 Union Types

A union indicates that a value may have one of several types.

```python
def safe_div(a: float, b: float) -> float | None:
    if b == 0:
        return None

    return a / b
```

The function returns a floating-point result or `None` if division by zero is requested.

### 10.5 Callable Types

A callable annotation describes a function or other callable object.

```python
from collections.abc import Callable

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

print(apply(lambda n: n * 2, 5))
```

The annotation `Callable[[int], int]` describes a callable that accepts an integer and returns an integer.

### 10.6 Built-in Generic Types

In modern Python, built-in collection types can be used directly in annotations:

```python
def total(nums: list[int]) -> int:
    return sum(nums)

def lookup(data: dict[str, int], key: str) -> int | None:
    return data.get(key)
```

This syntax is supported in Python 3.9 and later for built-in generic types. Use compatible syntax if your project targets an older Python version.

### 10.7 Inspecting Annotations

```python
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

print(add.__annotations__)
print(add.__doc__)
help(add)
```

Annotations and docstrings provide useful information for developers and tools, but they do not automatically validate every call.

---

## 11. Function Complexity

Understanding complexity helps you choose the right algorithm for a competitive programming problem.

| Example | Time complexity | Auxiliary space |
|---|---:|---:|
| Add two numbers | \(O(1)\) | \(O(1)\) |
| Find minimum or maximum in a list | \(O(n)\) | \(O(1)\) |
| Iterative factorial | \(O(n)\) | \(O(1)\) |
| Recursive factorial | \(O(n)\) | \(O(n)\) |
| Naive recursive Fibonacci | Exponential, approximately \(O(2^n)\) | \(O(n)\) stack |
| Iterative Fibonacci | \(O(n)\) | \(O(1)\) |
| Binary search | \(O(\log n)\) | \(O(\log n)\) for recursive implementation |
| Tower of Hanoi | \(O(2^n)\) | \(O(n)\) stack |

The actual complexity depends on the operations performed inside the function. Defining or calling a simple function does not automatically make its work constant-time.

---

## 12. Common Mistakes

### Mistake 1: Confusing `print()` with `return`

Incorrect when a caller needs the result:

```python
def square(x):
    print(x * x)

result = square(5)
```

`result` becomes `None`.

Correct:

```python
def square(x):
    return x * x

result = square(5)
```

### Mistake 2: Forgetting the Base Case in Recursion

A recursive function without a reachable stopping condition may continue until Python raises `RecursionError`.

Always identify the smallest valid problem before writing the recursive case.

### Mistake 3: Using Mutable Default Arguments

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Correct:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

### Mistake 4: Modifying Globals Unnecessarily

Excessive global state makes functions harder to test and reuse. Prefer arguments and return values.

### Mistake 5: Passing a Function Call Instead of a Function

```python
def apply(func, x):
    return func(x)

def double(x):
    return x * 2

print(apply(double, 5))    # Correct
```

`double` is the function object. `double(5)` is the result of calling it.

### Mistake 6: Overusing Lambda Functions

A short lambda is useful for a sorting key, but complicated logic should be written using `def`.

### Mistake 7: Assuming Type Hints Enforce Types

Annotations document intended types and support static analysis. They do not automatically reject incompatible arguments at runtime.

### Mistake 8: Ignoring Recursion Limits

Deep recursion may fail even when the algorithm is logically correct. Consider an iterative solution when the recursion depth may be large.

---

## 13. Practice Problems

Try solving these problems using functions. Each function should have a clear purpose, appropriate parameters, and a meaningful return value.

### Beginner: Function Basics

- [ ] Write a function that returns the square of a number.
- [ ] Write a function that returns the maximum of three numbers.
- [ ] Write a function that checks whether a number is even.
- [ ] Write a function that returns the sum of a list.
- [ ] Write a function that counts vowels in a string.
- [ ] Write a function that returns the minimum and maximum of a list.
- [ ] Write a function that checks whether a string is a palindrome.
- [ ] Write a function that converts Celsius to Fahrenheit.

### Intermediate: Parameters and Scope

- [ ] Write a greeting function with a default greeting.
- [ ] Create a function that accepts any number of integers and returns their sum.
- [ ] Create a function that accepts keyword arguments and returns them as a dictionary.
- [ ] Write a function that safely divides two numbers.
- [ ] Create a closure that multiplies a number by a configurable factor.
- [ ] Write a function that applies another function to every element of a list.
- [ ] Write a function with type annotations and a useful docstring.

### Recursion

- [ ] Calculate factorial recursively.
- [ ] Calculate the sum of the first `n` natural numbers.
- [ ] Calculate the nth Fibonacci number.
- [ ] Reverse a string recursively.
- [ ] Find the sum of digits of an integer recursively.
- [ ] Find the greatest common divisor (GCD) recursively.
- [ ] Implement binary search recursively.
- [ ] Solve the Tower of Hanoi problem.
- [ ] Generate all subsets of a list using recursion.

### Competitive Programming Challenges

- [ ] Implement fast exponentiation.
- [ ] Implement recursive and iterative binary search.
- [ ] Calculate GCD and least common multiple (LCM).
- [ ] Generate all permutations of a sequence.
- [ ] Generate all subsets of a sequence.
- [ ] Solve the Fibonacci problem using memoization.
- [ ] Implement merge sort using recursion.
- [ ] Implement quicksort using recursion.

---

## Final Revision Checklist

Before moving to the next chapter, make sure you can:

- [ ] Define and call functions.
- [ ] Distinguish parameters from arguments.
- [ ] Use positional, keyword, positional-only, and keyword-only arguments.
- [ ] Explain the difference between `print()` and `return`.
- [ ] Return multiple values and handle `None`.
- [ ] Explain local, enclosing, global, and built-in scopes.
- [ ] Avoid mutable default argument bugs.
- [ ] Use `*args` and `**kwargs`.
- [ ] Write and use lambda expressions.
- [ ] Explain recursion, base cases, and recursive cases.
- [ ] Analyze recursive time and space complexity.
- [ ] Pass functions as arguments and return functions.
- [ ] Understand closures and higher-order functions.
- [ ] Write useful type annotations and docstrings.

**Next topic:** Python modules, packages, and exception handling.

**Study strategy:** First understand every example in these files. Then implement the practice problems without looking at the solutions. For competitive programming, prioritize return values, parameter handling, recursion, binary search, GCD, and divide-and-conquer algorithms.