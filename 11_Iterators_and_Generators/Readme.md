# 11. Iterators and Generators in Python

This folder covers **iterables, iterators, `iter()`, `next()`, generator functions, `yield`, `yield from`, generator expressions, and lazy evaluation**.

These concepts are important for writing memory-efficient Python programs, processing large datasets, building data pipelines, and solving competitive programming problems.

## 📁 Folder Structure

```text
11_Iterators_and_Generators/
├── 01_iterables_and_iterators.py
├── 02_iter_next.py
├── 03_generator_functions.py
├── 04_yield_from.py
├── 05_generator_expressions.py
└── 06_lazy_evaluation.py
```

## 📚 Table of Contents

1. [Iterables and Iterators](#1-iterables-and-iterators)
2. [`iter()` and `next()`](#2-iter-and-next)
3. [Generator Functions](#3-generator-functions)
4. [`yield from`](#4-yield-from)
5. [Generator Expressions](#5-generator-expressions)
6. [Lazy Evaluation](#6-lazy-evaluation)
7. [Iterators vs Generators vs Lists](#7-iterators-vs-generators-vs-lists)
8. [Time and Space Complexity](#8-time-and-space-complexity)
9. [Common Mistakes](#9-common-mistakes)
10. [Competitive Programming Applications](#10-competitive-programming-applications)
11. [Practice Checklist](#11-practice-checklist)

---

## 1. Iterables and Iterators

### 1.1 What Is an Iterable?

An **iterable** is an object that can provide its elements one at a time through iteration.

Common examples include:

- Lists
- Tuples
- Strings
- Sets
- Dictionaries
- Ranges
- File objects
- Generator objects

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Python obtains an iterator from the iterable to perform the loop.

### 1.2 What Is an Iterator?

An **iterator** is an object that produces values one at a time.

The iterator protocol consists of two methods:

- `__iter__()` returns an iterator.
- `__next__()` returns the next value.

When no values remain, `__next__()` raises `StopIteration`.

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

Calling `next(it)` again raises `StopIteration`.

### 1.3 Iterable vs Iterator

| Feature | Iterable | Iterator |
|---|---|---|
| Purpose | Provides an iterator | Produces values |
| `iter(obj)` | Usually creates an iterator | Returns the iterator itself |
| `next(obj)` | Not necessarily supported | Supported |
| Can restart? | Often, by creating a new iterator | Usually no; consumed values are not restored |
| Example | List, tuple, string | `iter(list)`, generator |

```python
numbers = [1, 2, 3]

print(hasattr(numbers, "__iter__"))  # True
print(hasattr(numbers, "__next__"))  # False

it = iter(numbers)

print(hasattr(it, "__iter__"))       # True
print(hasattr(it, "__next__"))       # True
```

**Important:** An iterable does not have to be an iterator. A list is iterable, but a list itself is not an iterator.

### 1.4 Creating a Custom Iterator

A custom iterator can define `__iter__()` and `__next__()`.

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


for number in CountDown(5):
    print(number, end=" ")

# Output: 5 4 3 2 1
```

Because the iterator returns itself from `__iter__()`, its state is shared. Once consumed, the same iterator does not automatically restart.

### 1.5 Creating a Custom Iterable

A custom iterable can create a fresh iterator each time `__iter__()` is called.

```python
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start

        while current < self.end:
            yield current
            current += 1


numbers = MyRange(1, 5)

print(list(numbers))  # [1, 2, 3, 4]
print(list(numbers))  # [1, 2, 3, 4]
```

Here, `__iter__()` is a generator function, so each call creates a new iterator.

**When to use:** Custom iterables are useful when you want an object to support repeated iteration without storing every generated value in a list.

---

## 2. `iter()` and `next()`

### 2.1 The `iter()` Function

`iter()` obtains an iterator from an iterable.

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
```

Every call to `next()` advances the iterator.

### 2.2 The `next()` Function

Syntax:

```python
next(iterator)
next(iterator, default)
```

Without a default value, calling `next()` after exhaustion raises `StopIteration`.

With a default value, it returns that value instead.

```python
it = iter([1, 2, 3])

print(next(it))             # 1
print(next(it))             # 2
print(next(it))             # 3
print(next(it, "default"))  # default
```

The default prevents `StopIteration` from propagating when the iterator is exhausted.

### 2.3 Manually Iterating Through Values

```python
it = iter("hello")

while True:
    try:
        character = next(it)
        print(character)
    except StopIteration:
        break
```

In ordinary Python code, prefer a `for` loop unless manual iterator control is needed.

```python
for character in "hello":
    print(character)
```

A `for` loop handles iterator exhaustion automatically.

### 2.4 Infinite Iterators

An infinite iterator continues producing values until you stop requesting them.

```python
def infinite():
    number = 0

    while True:
        yield number
        number += 1


it = infinite()

print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
```

Never convert an infinite iterator directly to a list:

```python
# Dangerous: never finishes
# values = list(infinite())
```

Use a finite number of calls or `itertools.islice()`.

```python
from itertools import islice

print(list(islice(infinite(), 5)))
# [0, 1, 2, 3, 4]
```

### 2.5 Understanding `enumerate()`

`enumerate()` returns an iterator that produces `(index, value)` pairs.

```python
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)
```

Output:

```text
0 a
1 b
2 c
```

You can specify the starting index:

```python
for index, letter in enumerate(letters, start=1):
    print(index, letter)
```

A simplified implementation:

```python
def my_enumerate(iterable, start=0):
    index = start

    for value in iterable:
        yield index, value
        index += 1
```

### 2.6 Understanding `zip()`

`zip()` combines elements from multiple iterables into tuples.

```python
numbers = [1, 2, 3]
letters = ["a", "b", "c"]

print(list(zip(numbers, letters)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

By default, `zip()` stops when the shortest iterable is exhausted.

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# [(1, 'a'), (2, 'b')]
```

A simplified implementation:

```python
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]

    while True:
        values = []

        for it in iterators:
            try:
                values.append(next(it))
            except StopIteration:
                return

        yield tuple(values)
```

The implementation stops when any iterator runs out of values.

**Competitive programming tip:** Use built-in `enumerate()` and `zip()` in normal solutions. Understanding their iterator behavior helps you avoid unnecessary list creation.

---

## 3. Generator Functions

### 3.1 What Is a Generator?

A **generator function** is a function that uses `yield` to produce values one at a time.

Unlike an ordinary function that returns and finishes, a generator pauses at each `yield` and resumes when the next value is requested.

```python
def simple_gen():
    yield 1
    yield 2
    yield 3


for value in simple_gen():
    print(value)
```

Output:

```text
1
2
3
```

Calling the function creates a generator object. The function body starts executing when the generator is advanced.

```python
def example():
    print("Started")
    yield 10


gen = example()
print("Created generator")
print(next(gen))
```

Output:

```text
Created generator
Started
10
```

### 3.2 `return` vs `yield`

| `return` | `yield` |
|---|---|
| Returns a final result | Produces a value and pauses |
| Ends the function | Suspends the generator |
| Does not preserve execution for another call | Preserves local state between yields |

```python
def normal_function():
    return 10


def generator_function():
    yield 10
    yield 20
```

`normal_function()` returns `10`.

`generator_function()` returns a generator object.

### 3.3 Fibonacci Generator

Generators are useful for sequences that can be calculated incrementally.

```python
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(10)))
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

The generator stores only the current pair of Fibonacci values instead of building the entire sequence internally.

### 3.4 Generator for Infinite Natural Numbers

```python
def naturals():
    number = 1

    while True:
        yield number
        number += 1
```

Take the first five values:

```python
from itertools import islice

print(list(islice(naturals(), 5)))
# [1, 2, 3, 4, 5]
```

The generator can continue indefinitely, but only the requested values are calculated.

### 3.5 Reading Large Files with a Generator

```python
def read_lines(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")
```

Usage:

```python
for line in read_lines("large_file.txt"):
    print(line)
```

This avoids loading the entire file into memory at once.

**Important:** The file remains open while the generator is suspended inside the `with` block. Exhausting the generator or closing it allows the context manager to close the file. If iteration stops early, explicitly close the generator when prompt cleanup is needed.

### 3.6 Chaining Generator Functions into a Pipeline

```python
def read_nums():
    for value in ["1", "2", "3"]:
        yield int(value)


def squared(numbers):
    for number in numbers:
        yield number ** 2


def filtered(numbers):
    for number in numbers:
        if number > 1:
            yield number


result = list(filtered(squared(read_nums())))

print(result)
# [4, 9]
```

Each stage produces values for the next stage instead of requiring a separate intermediate list.

### 3.7 Generator Return Values

A generator can use `return` to terminate and provide a final value through `StopIteration.value`.

```python
def gen_with_return():
    yield 1
    yield 2
    return "done"


gen = gen_with_return()

print(next(gen))  # 1
print(next(gen))  # 2

try:
    next(gen)
except StopIteration as error:
    print(error.value)  # done
```

This return value is not another item yielded by the generator and does not appear in `list(gen)`.

---

## 4. `yield from`

### 4.1 What Does `yield from` Do?

`yield from` delegates iteration to another iterable or generator.

Instead of writing a loop that yields every value manually, you can write:

```python
yield from iterable
```

### 4.2 Combining Generators

```python
def gen1():
    yield 1
    yield 2


def gen2():
    yield 3
    yield 4


def combined():
    yield from gen1()
    yield from gen2()


print(list(combined()))
# [1, 2, 3, 4]
```

This is a concise way to combine multiple sequences.

### 4.3 Flattening a Nested List

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = [1, [2, 3, [4, 5]], 6]

print(list(flatten(data)))
# [1, 2, 3, 4, 5, 6]
```

The function recursively processes nested lists and yields their values in order.

**Complexity:** For \(n\) total elements, the traversal takes \(O(n)\) time. Recursion uses stack space depending on nesting depth, and deeply nested structures can exceed Python's recursion limit.

### 4.4 Building a Chain Function

```python
def chain(*iterables):
    for iterable in iterables:
        yield from iterable


print(list(chain([1, 2], "ab", (True, False))))
# [1, 2, 'a', 'b', True, False]
```

The function yields each element from each iterable in order.

Python also provides `itertools.chain()` for this purpose.

### 4.5 Capturing a Subgenerator's Return Value

`yield from` can capture the return value of a delegated generator.

```python
def sub():
    yield 1
    yield 2
    return "sub done"


def main():
    result = yield from sub()
    print(f"Sub returned: {result}")
    yield 3


print(list(main()))
```

Output:

```text
Sub returned: sub done
[1, 2, 3]
```

The value returned by `sub()` is assigned to `result`; it is not yielded as an element.

### 4.6 Binary Tree Traversal with `yield from`

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node):
    if node is not None:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)


root = Node(2, Node(1), Node(3))

print(list(inorder(root)))
# [1, 2, 3]
```

This produces the inorder traversal: left subtree, current node, right subtree.

**DSA connection:** Generator-based traversal can yield nodes as they are visited. For binary search trees, inorder traversal yields values in sorted order when the tree satisfies the BST property.

---

## 5. Generator Expressions

### 5.1 What Is a Generator Expression?

A generator expression resembles a list comprehension but uses parentheses and evaluates lazily.

```python
# List comprehension: eager
squares_list = [x ** 2 for x in range(10)]

# Generator expression: lazy
squares_gen = (x ** 2 for x in range(10))
```

The list contains all computed values immediately. The generator expression computes each value as it is requested.

```python
gen = (x ** 2 for x in range(5))

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
```

### 5.2 Generator Expression with a Condition

```python
evens = (x for x in range(20) if x % 2 == 0)

print(list(evens))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### 5.3 Passing Generator Expressions to Functions

When a generator expression is the only argument to a function, the extra parentheses are unnecessary.

```python
print(sum(x ** 2 for x in range(10)))
print(any(x > 5 for x in range(10)))
print(all(x < 100 for x in range(10)))
print(max(len(word) for word in ["a", "bb", "ccc"]))
```

Results:

```text
285
True
True
3
```

This pattern is especially useful in competitive programming.

### 5.4 Nested Generator Expressions

```python
matrix = [
    [1, 2],
    [3, 4]
]

flat_gen = (value for row in matrix for value in row)

print(list(flat_gen))
# [1, 2, 3, 4]
```

This follows the same iteration order as the equivalent nested loops.

### 5.5 Chaining Transformations

```python
result = sum(
    x * 2
    for x in range(10)
    if x % 2 == 0
)

print(result)
# 40
```

Only even numbers are selected, and each selected number is doubled before being summed.

### 5.6 Measuring Memory Usage

```python
import sys

numbers_list = [x for x in range(100_000)]
numbers_gen = (x for x in range(100_000))

print(sys.getsizeof(numbers_list))
print(sys.getsizeof(numbers_gen))
```

A generator object typically occupies much less memory than a list containing all the generated values.

**Note:** `sys.getsizeof()` reports the shallow size of an object, not the total memory of everything it references. The exact output depends on the Python implementation and version.

### 5.7 When to Use a Generator Expression

Use a generator expression when:

- Processing a large sequence one value at a time.
- Computing a sum, maximum, minimum, or Boolean result.
- Passing data through a pipeline.
- You do not need indexing or repeated traversal.

Use a list comprehension when:

- You need to access elements by index.
- You need to iterate over the results multiple times.
- You need the complete collection immediately.

Remember that a generator is generally a **single-pass iterator**. After it is exhausted, it does not automatically restart.

---

## 6. Lazy Evaluation

### 6.1 What Is Lazy Evaluation?

**Lazy evaluation** means calculating a value only when it is needed.

Compare eager and lazy evaluation:

```python
def expensive(x):
    print(f"Computing {x}")
    return x * 2


print("Eager:")
result = [expensive(x) for x in range(3)]
print(result)

print("\nLazy:")
result = (expensive(x) for x in range(3))
print("Created")
print(next(result))
print(next(result))
print(next(result))
```

The list comprehension calls `expensive()` for every value immediately.

The generator expression delays each call until `next()` requests the corresponding value.

### 6.2 Why Lazy Evaluation Matters

Lazy evaluation can:

- Reduce peak memory usage.
- Avoid computing values that are never requested.
- Process large or streaming datasets.
- Support infinite sequences.
- Allow multiple transformations without intermediate lists.

However, laziness does not automatically make a program faster. Generator overhead can matter for small datasets, and consuming every value still requires the corresponding computations.

### 6.3 Infinite Prime Generator

```python
def primes():
    """Generate prime numbers indefinitely."""
    number = 2

    while True:
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number

        number += 1
```

Take the first ten prime numbers:

```python
from itertools import islice

print(list(islice(primes(), 10)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

The generator is infinite, but `islice()` limits the number of requested values.

This is a simple educational implementation. For larger prime-generation tasks, a sieve such as the Sieve of Eratosthenes is usually more efficient.

### 6.4 Lazy Pipelines

```python
def read_numbers():
    for number in range(10):
        yield number


pipeline = (
    number * 2
    for number in read_numbers()
    if number % 2 == 0
)

print(list(pipeline))
# [0, 4, 8, 12, 16]
```

Values pass through the pipeline one at a time:

1. Generate a number.
2. Keep it if it is even.
3. Multiply it by two.
4. Yield the result.

No intermediate list is needed.

### 6.5 Keeping the Last N Lines of a File

To obtain the final \(n\) lines without loading an entire file into memory:

```python
from collections import deque


def tail(path, n):
    if n < 0:
        raise ValueError("n must be non-negative")

    with open(path, encoding="utf-8") as file:
        return list(deque(file, maxlen=n))
```

`deque` retains only the most recent \(n\) lines while the file is read.

- Time complexity: \(O(L)\), where \(L\) is the total number of lines.
- Auxiliary storage: \(O(n)\) lines, excluding the returned list's reference storage.

When `n == 0`, the function returns an empty list.

### 6.6 Memory-Efficient Aggregation

```python
total = sum(x ** 2 for x in range(10_000_000))

print(total)
```

The generator expression avoids building a list of ten million squares.

The computation still takes \(O(n)\) time, but the generator itself uses \(O(1)\) auxiliary space for this expression, excluding the fixed-size running total and other implementation overhead.

### 6.7 `takewhile()` and `dropwhile()`

The `itertools` module provides useful lazy tools.

```python
from itertools import takewhile, dropwhile

print(list(takewhile(lambda x: x < 5, range(10))))
# [0, 1, 2, 3, 4]

print(list(dropwhile(lambda x: x < 5, range(10))))
# [5, 6, 7, 8, 9]
```

- `takewhile(predicate, iterable)` yields values while the predicate remains true, then stops permanently.
- `dropwhile(predicate, iterable)` skips values while the predicate is true, then yields the remaining values.

**Important:** These functions assume the intended stopping or skipping behavior is based on the initial sequence. `takewhile()` does not resume if a later value would satisfy the predicate again.

---

## 7. Iterators vs Generators vs Lists

| Feature | List | Iterator | Generator |
|---|---|---|---|
| Stores all results | Yes | Usually no | Usually no |
| Lazy production | No, for a constructed list | Often | Yes |
| Indexing | Yes | No, generally | No |
| Repeated traversal | Yes | Not after exhaustion | Not after exhaustion |
| Infinite sequences | No | Possible | Possible |
| Memory for \(n\) results | \(O(n)\) | Depends on implementation | Usually \(O(1)\) auxiliary state for simple generators |

A generator is a convenient way to create an iterator. An iterator is a protocol; a generator is one way to implement it.

Choose the data structure based on what the problem requires, not just because generators use less memory.

---

## 8. Time and Space Complexity

Let \(n\) be the number of values processed.

| Operation | Time Complexity | Additional Space |
|---|---:|---:|
| Create an iterator over a list | \(O(1)\) | \(O(1)\) |
| Consume all \(n\) list values | \(O(n)\) | \(O(1)\) iterator state |
| Generate \(n\) simple values | \(O(n)\) total | Often \(O(1)\) auxiliary state |
| Build a list of \(n\) values | \(O(n)\) | \(O(n)\) |
| Sum \(n\) generated values | \(O(n)\), excluding generation cost | Usually \(O(1)\) auxiliary space |
| Flatten \(n\) nested elements | \(O(n)\) | Depends on nesting depth and output storage |
| Read \(L\) file lines | \(O(L)\) | Depends on processing strategy |

These are typical complexities, not guarantees for every iterator. An iterator may perform expensive work per value or retain substantial internal state.

**Competitive programming reminder:** If you convert a generator to a list, you materialize the values and lose the main memory advantage of lazy iteration.

---

## 9. Common Mistakes

### Mistake 1: Calling `next()` on an Iterable Instead of Its Iterator

Incorrect:

```python
numbers = [1, 2, 3]

# next(numbers)  # TypeError
```

Correct:

```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
```

### Mistake 2: Reusing an Exhausted Iterator

```python
it = iter([1, 2, 3])

print(list(it))  # [1, 2, 3]
print(list(it))  # []
```

Create a new iterator when you need to traverse the iterable again:

```python
numbers = [1, 2, 3]

print(list(iter(numbers)))
print(list(iter(numbers)))
```

### Mistake 3: Trying to Convert an Infinite Generator to a List

```python
def naturals():
    number = 1

    while True:
        yield number
        number += 1


# Never finishes:
# list(naturals())
```

Use a limit:

```python
from itertools import islice

print(list(islice(naturals(), 5)))
```

### Mistake 4: Expecting a Generator Expression to Compute Immediately

```python
gen = (x * 2 for x in range(5))
print("Created")
```

The values have not all been computed yet. Advance the generator or consume it to obtain results.

### Mistake 5: Expecting `yield` to Return a List

```python
def numbers():
    yield 1
    yield 2
    yield 3


print(numbers())       # Generator object
print(list(numbers())) # [1, 2, 3]
```

### Mistake 6: Forgetting That `zip()` Stops at the Shortest Input

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# [(1, 'a'), (2, 'b')]
```

If you need to process unequal-length inputs differently, consider `itertools.zip_longest()`.

### Mistake 7: Accidentally Consuming a Generator

```python
gen = (x for x in range(5))

print(sum(gen))   # 10
print(list(gen))  # []
```

The first operation consumes the generator.

### Mistake 8: Assuming Laziness Automatically Improves Speed

Generators can reduce memory usage, but they do not eliminate computation. For small collections, a list comprehension may be simpler and sometimes faster.

---

## 10. Competitive Programming Applications

Iterators and generators are useful in competitive programming, particularly when processing streams of data or avoiding unnecessary intermediate collections.

### 10.1 Efficient Aggregation

```python
n = 10

total = sum(x * x for x in range(1, n + 1))
print(total)
```

Use a generator expression when values are needed only for a single aggregation.

### 10.2 Index and Value Together

```python
arr = [10, 20, 30, 40]

for index, value in enumerate(arr):
    print(index, value)
```

This is cleaner than maintaining an index manually.

### 10.3 Process Pairs with `zip()`

```python
a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a, b):
    print(x + y)
```

This avoids manual index-based pairing when the two sequences correspond element by element.

### 10.4 Process Input Tokens Lazily

For large competitive programming inputs, this common pattern reads all input at once and then creates an iterator over the tokens:

```python
import sys

data = iter(sys.stdin.buffer.read().split())

n = int(next(data))
arr = [int(next(data)) for _ in range(n)]

print(sum(arr))
```

The complete input and split tokens are still stored in memory. This is often fast, but it is not fully streaming.

For very large input where memory is a concern, process input line by line instead:

```python
import sys

total = 0

for line in sys.stdin.buffer:
    for token in line.split():
        total += int(token)

print(total)
```

Choose the approach according to the input size and memory limit.

### 10.5 Generate Values Without Storing Them All

```python
def squares(n):
    for number in range(1, n + 1):
        yield number * number


print(sum(squares(100)))
```

The values are generated as needed rather than stored in a list.

### 10.6 Useful `itertools` Functions

The standard library provides many iterator tools:

| Function | Purpose |
|---|---|
| `islice()` | Take a slice of an iterator |
| `chain()` | Combine iterables sequentially |
| `count()` | Generate an arithmetic sequence |
| `cycle()` | Repeat values from an iterable |
| `repeat()` | Repeat a value |
| `takewhile()` | Take values while a condition is true |
| `dropwhile()` | Skip values while a condition is true |
| `product()` | Cartesian product |
| `permutations()` | Generate permutations |
| `combinations()` | Generate combinations |
| `accumulate()` | Running accumulation |
| `zip_longest()` | Zip unequal-length iterables with a fill value |

Example:

```python
from itertools import accumulate

arr = [1, 2, 3, 4]

print(list(accumulate(arr)))
# [1, 3, 6, 10]
```

The `itertools` module is especially valuable in competitive programming because many of its tools are implemented efficiently in C.

---

## 11. Practice Checklist

Work through these tasks after studying the six Python files.

### Beginner

- [ ] Explain the difference between an iterable and an iterator.
- [ ] Use `iter()` and `next()` on a list and a string.
- [ ] Handle iterator exhaustion with `next(iterator, default)`.
- [ ] Write a generator that produces numbers from 1 to \(n\).
- [ ] Generate the first \(n\) Fibonacci numbers.
- [ ] Use `enumerate()` to print indices and values.
- [ ] Use `zip()` to combine two lists.

### Intermediate

- [ ] Implement a custom iterator class.
- [ ] Write a generator that yields even numbers.
- [ ] Flatten a nested list using `yield from`.
- [ ] Create a generator expression to filter and transform data.
- [ ] Build a pipeline that filters numbers and calculates their squares.
- [ ] Use `islice()` to obtain a finite part of an infinite generator.
- [ ] Demonstrate the difference between eager and lazy evaluation.

### Advanced

- [ ] Implement a generator for prime numbers.
- [ ] Write an inorder binary tree traversal as a generator.
- [ ] Read a large file without loading all its lines into memory.
- [ ] Implement a custom iterable that can be traversed repeatedly.
- [ ] Use `itertools` to solve a combinatorics problem.
- [ ] Explain the time and auxiliary-space complexity of a generator pipeline.

---

## Recommended Learning Order

Follow the files in this order:

1. `01_iterables_and_iterators.py` — Understand the iterator protocol.
2. `02_iter_next.py` — Learn how iteration advances and terminates.
3. `03_generator_functions.py` — Master `yield` and generator state.
4. `04_yield_from.py` — Delegate iteration and build recursive generators.
5. `05_generator_expressions.py` — Write compact, lazy expressions.
6. `06_lazy_evaluation.py` — Understand memory-efficient processing.

## Final Takeaways

- An **iterable** can provide an iterator.
- An **iterator** produces values through `__next__()`.
- `iter()` obtains an iterator; `next()` requests its next value.
- A **generator function** uses `yield` to produce values incrementally.
- `yield from` delegates iteration to another iterable or generator.
- A **generator expression** is the lazy counterpart of a list comprehension.
- Lazy evaluation can reduce memory usage and avoid unnecessary work.
- An exhausted iterator does not automatically restart.
- Infinite generators must be consumed with an explicit stopping condition.
- In competitive programming, built-in iteration tools and `itertools` can make solutions cleaner and more memory-efficient.

**Goal:** Understand not only how to use generators, but also when lazy iteration is useful and when a list is the better choice.
