# 10. Comprehensions and Functional Python

Comprehensions and functional programming tools help you write Python code that is concise, readable, and expressive.

This topic covers list, dictionary, and set comprehensions, `map()`, `filter()`, `reduce()`, `zip()`, `enumerate()`, sorting with custom keys, `any()`, `all()`, and the `operator` module.

## 📚 Table of Contents

1. [List Comprehensions](#1-list-comprehensions)
2. [Dictionary and Set Comprehensions](#2-dictionary-and-set-comprehensions)
3. [`map()`, `filter()`, and `reduce()`](#3-map-filter-and-reduce)
4. [`zip()` and `enumerate()`](#4-zip-and-enumerate)
5. [Sorting with `key`](#5-sorting-with-key)
6. [`any()` and `all()`](#6-any-and-all)
7. [The `operator` Module](#7-the-operator-module)
8. [Comprehensions vs Functional Tools](#8-comprehensions-vs-functional-tools)
9. [Common Mistakes](#9-common-mistakes)
10. [Competitive Programming Applications](#10-competitive-programming-applications)
11. [Practice Checklist](#11-practice-checklist)

---

## 1. List Comprehensions

A **list comprehension** creates a new list from an iterable, optionally filtering or transforming its elements.

### Basic syntax

```python
[expression for item in iterable if condition]
```

The `if condition` part is optional.

### 1.1 Basic comprehension

```python
squares = [x**2 for x in range(10)]

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Equivalent loop:

```python
squares = []

for x in range(10):
    squares.append(x**2)
```

### 1.2 Filtering with a condition

```python
evens = [x for x in range(20) if x % 2 == 0]

print(evens)
```

Only values satisfying the condition are included.

### 1.3 Using `if-else` in the expression

```python
labels = [
    "even" if x % 2 == 0 else "odd"
    for x in range(5)
]

print(labels)
# ['even', 'odd', 'even', 'odd', 'even']
```

**Important difference:**

- Filtering: `for x in values if condition`
- Conditional expression: `expression_if_true if condition else expression_if_false`

When using `if-else` to choose a value, the conditional expression comes before the `for` clause.

### 1.4 Nested comprehensions

```python
matrix = [
    [i * j for j in range(3)]
    for i in range(3)
]

print(matrix)
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

Flattening a nested list:

```python
flat = [x for row in matrix for x in row]

print(flat)
```

The nested loops follow the same order as ordinary loops:

```python
flat = []

for row in matrix:
    for x in row:
        flat.append(x)
```

### 1.5 Multiple conditions

```python
result = [
    x for x in range(100)
    if x % 2 == 0
    if x % 3 == 0
]

print(result)
```

Both conditions must be true. You could also combine them using `and`:

```python
result = [
    x for x in range(100)
    if x % 2 == 0 and x % 3 == 0
]
```

### 1.6 Transforming strings

```python
words = ["hello", "world"]

upper = [word.upper() for word in words]
lengths = [len(word) for word in words]

print(upper)
print(lengths)
```

Removing vowels from a string:

```python
s = "hello"

chars = [c for c in s if c not in "aeiou"]

print(chars)
print("".join(chars))
```

### 1.7 Calling functions

```python
import math

roots = [math.sqrt(x) for x in range(1, 6)]

print(roots)
```

Filtering with a function:

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


primes = [x for x in range(50) if is_prime(x)]

print(primes)
```

### When should you use list comprehensions?

Use them when you want to:

- Transform every element in a sequence.
- Filter elements based on conditions.
- Flatten simple nested iterables.
- Build a list without writing several lines of loop code.

Avoid deeply nested or complicated comprehensions if they reduce readability.

---

## 2. Dictionary and Set Comprehensions

Python supports comprehensions for dictionaries and sets as well as lists.

### 2.1 Dictionary comprehension

Syntax:

```python
{key_expression: value_expression for item in iterable}
```

Example:

```python
squares = {x: x**2 for x in range(5)}

print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 2.2 Transforming a dictionary

```python
prices = {
    "apple": 1.0,
    "banana": 0.5
}

discounted = {
    key: value * 0.9
    for key, value in prices.items()
}

print(discounted)
```

### 2.3 Filtering a dictionary

```python
cheap = {
    key: value
    for key, value in prices.items()
    if value < 1
}

print(cheap)
# {'banana': 0.5}
```

### 2.4 Swapping keys and values

```python
swapped = {value: key for key, value in prices.items()}

print(swapped)
```

If multiple original keys have the same value, the resulting dictionary keeps only the last value assigned to that new key.

### 2.5 Building a dictionary from two lists

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]

mapping = {
    key: value
    for key, value in zip(keys, values)
}

print(mapping)
# {'a': 1, 'b': 2, 'c': 3}
```

You can also write:

```python
mapping = dict(zip(keys, values))
```

### 2.6 Conditional values

```python
labels = {
    x: "even" if x % 2 == 0 else "odd"
    for x in range(5)
}

print(labels)
```

### 2.7 Set comprehension

Syntax:

```python
{expression for item in iterable if condition}
```

A set stores unique elements.

```python
evens = {x for x in range(20) if x % 2 == 0}

print(evens)
```

Unique word lengths:

```python
words = ["a", "bb", "ccc", "dd"]

unique_lengths = {len(word) for word in words}

print(unique_lengths)
# {1, 2, 3}
```

Unique characters:

```python
unique_chars = {
    c for c in "hello world"
    if c != " "
}

print(unique_chars)
```

The order in which set elements are displayed is not guaranteed.

### 2.8 Flattening into a set

```python
matrix = [
    [1, 2],
    [3, 4]
]

flat_set = {x for row in matrix for x in row}

print(flat_set)
# {1, 2, 3, 4}
```

### 2.9 Dictionary of word lengths

```python
text = "the quick brown fox"

word_lengths = {
    word: len(word)
    for word in text.split()
}

print(word_lengths)
```

### Comparison

| Comprehension | Result | Typical use |
|---|---|---|
| `[x for x in items]` | List | Ordered collection with duplicates |
| `{x for x in items}` | Set | Unique values |
| `{k: v for k, v in items}` | Dictionary | Key-value mapping |

---

## 3. `map()`, `filter()`, and `reduce()`

These tools apply functions to iterable data or combine values into a single result.

### 3.1 `map()`

`map(function, iterable)` applies a function to each element.

```python
nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, nums))

print(doubled)
# [2, 4, 6, 8, 10]
```

Using a named function:

```python
def square(x):
    return x**2


print(list(map(square, nums)))
```

### 3.2 Mapping multiple iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]

sums = list(map(lambda x, y: x + y, a, b))

print(sums)
# [11, 22, 33]
```

When multiple iterables are supplied, `map()` stops when the shortest iterable is exhausted.

### 3.3 `filter()`

`filter(function, iterable)` keeps elements for which the function returns a truthy value.

```python
nums = [1, 2, 3, 4, 5]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)
# [2, 4]
```

Passing `None` as the function filters out falsy values:

```python
mixed = [0, 1, "", "a", None, [], [1]]

truthy = list(filter(None, mixed))

print(truthy)
# [1, 'a', [1]]
```

### 3.4 Combining `map()` and `filter()`

```python
nums = [1, 2, 3, 4, 5]

result = list(
    map(
        lambda x: x**2,
        filter(lambda x: x % 2 == 0, nums)
    )
)

print(result)
# [4, 16]
```

The equivalent list comprehension is usually easier to read:

```python
result = [x**2 for x in nums if x % 2 == 0]

print(result)
```

### 3.5 `reduce()`

`reduce()` repeatedly combines elements to produce a single result. It is available from `functools`.

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, nums)

print(product)
# 120
```

Conceptually, it computes:

```text
((((1 * 2) * 3) * 4) * 5)
```

Summing values with `reduce()`:

```python
from functools import reduce
from operator import add

total = reduce(add, [1, 2, 3, 4])

print(total)
# 10
```

For ordinary summation, prefer the built-in `sum()`:

```python
total = sum([1, 2, 3, 4])
```

**Note:** Without an initial value, `reduce()` raises an error for an empty iterable. You can provide an initial value as the third argument.

### 3.6 Lazy evaluation

In Python 3, `map()` and `filter()` return iterators instead of immediately building lists.

```python
nums = [1, 2, 3]

m = map(str, nums)

print(m)        # A map object
print(list(m))  # ['1', '2', '3']
```

An iterator is consumed as you iterate over it. Once exhausted, it does not automatically restart.

### Quick comparison

| Tool | Purpose | Returns in Python 3 |
|---|---|---|
| `map()` | Transform elements | Iterator |
| `filter()` | Select elements | Iterator |
| `reduce()` | Combine elements | Single accumulated result |
| List comprehension | Transform and/or filter | List |

---

## 4. `zip()` and `enumerate()`

These functions are especially useful for iterating over collections.

### 4.1 `zip()`

`zip()` combines elements from multiple iterables by position.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

Output:

```text
Alice is 30
Bob is 25
Charlie is 35
```

### 4.2 Unequal iterable lengths

By default, `zip()` stops at the shortest iterable.

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# [(1, 'a'), (2, 'b')]
```

To preserve all elements, use `itertools.zip_longest()`:

```python
from itertools import zip_longest

result = zip_longest(
    [1, 2, 3],
    ["a", "b"],
    fillvalue="?"
)

print(list(result))
# [(1, 'a'), (2, 'b'), (3, '?')]
```

### 4.3 Unzipping

The unpacking operator `*` can reverse a zip operation.

```python
pairs = [
    (1, "a"),
    (2, "b"),
    (3, "c")
]

nums, letters = zip(*pairs)

print(nums)
print(letters)
```

For an empty `pairs` collection, `zip(*pairs)` produces no iterables to unpack, so handle that case separately if needed.

### 4.4 Creating a dictionary with `zip()`

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

mapping = dict(zip(names, ages))

print(mapping)
```

### 4.5 `enumerate()`

`enumerate()` provides an index and value while iterating.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

By default, indexing starts at zero.

To start at one:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

Convert to a list:

```python
print(list(enumerate(fruits)))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### 4.6 Combining `enumerate()` and `zip()`

```python
names = ["Alice", "Bob"]
ages = [30, 25]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index}: {name} ({age})")
```

### Why these functions matter

- `zip()` avoids manually coordinating multiple indexes.
- `enumerate()` avoids maintaining a separate counter.
- Both make iteration cleaner and reduce indexing mistakes.

---

## 5. Sorting with `key`

Python's `sorted()` and `list.sort()` allow a custom `key` function that determines how items are compared.

### 5.1 Basic sorting

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(sorted(nums))
print(sorted(nums, reverse=True))
```

- `sorted(iterable)` returns a new list.
- `list.sort()` sorts a list in place and returns `None`.

### 5.2 Sorting by length

```python
words = ["banana", "apple", "cherry"]

print(sorted(words, key=len))
```

The `key` function is applied to each item to obtain its sorting key.

### 5.3 Case-insensitive sorting

```python
words = ["banana", "Apple", "cherry"]

print(sorted(words, key=str.lower))
```

### 5.4 Sorting by the last character

```python
words = ["banana", "apple", "cherry"]

print(sorted(words, key=lambda word: word[-1]))
```

### 5.5 Sorting by multiple criteria

```python
data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 30)
]

result = sorted(data, key=lambda item: (item[1], item[0]))

print(result)
```

This sorts by age first, then name.

### 5.6 Stable sorting

Python sorting is stable: elements with equal sorting keys preserve their relative order.

```python
data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 30)
]

print(sorted(data, key=lambda item: item[1]))
```

Alice remains before Charlie because they have equal ages and Alice appeared first.

### 5.7 Sorting dictionaries

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

print(sorted(people, key=lambda person: person["age"]))
```

### 5.8 Using `itemgetter()` and `attrgetter()`

```python
from operator import itemgetter, attrgetter

data = [
    ("Alice", 30),
    ("Bob", 25)
]

print(sorted(data, key=itemgetter(1)))

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

print(sorted(people, key=itemgetter("age")))
```

For objects with attributes:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


points = [
    Point(1, 2),
    Point(3, 1),
    Point(2, 3)
]

print(sorted(points, key=attrgetter("y")))
```

### 5.9 Descending and mixed criteria

To sort by age descending and name ascending:

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30}
]

def score(person):
    return (-person["age"], person["name"])

print(sorted(people, key=score))
```

Negating a numeric field is useful when one criterion must be descending while another remains ascending.

### `sorted()` vs `list.sort()`

| Feature | `sorted()` | `list.sort()` |
|---|---|---|
| Input | Any iterable | A list |
| Creates a new list | Yes | No |
| Modifies the original list | No | Yes |
| Return value | Sorted list | `None` |
| Supports `key` and `reverse` | Yes | Yes |

---

## 6. `any()` and `all()`

These built-ins test conditions across an iterable.

### 6.1 `any()`

`any(iterable)` returns `True` if at least one element is truthy.

```python
print(any([False, True, False]))  # True
print(any([0, 0, 1]))             # True
print(any([]))                    # False
```

Common usage:

```python
nums = [2, 4, 6, 8]

print(any(x > 10 for x in nums))
# False
```

### 6.2 `all()`

`all(iterable)` returns `True` if every element is truthy.

```python
print(all([True, True, True]))  # True
print(all([1, 2, 3]))           # True
print(all([]))                  # True
```

The empty-iterable result for `all()` is `True` because there is no element that violates the condition.

Common usage:

```python
nums = [2, 4, 6, 8]

print(all(x % 2 == 0 for x in nums))
# True
```

### 6.3 Validation example

```python
def is_valid_user(user):
    return all([
        user.get("name"),
        user.get("age", 0) >= 18,
        user.get("email", "").count("@") == 1,
    ])


user = {
    "name": "Alice",
    "age": 30,
    "email": "a@b.com"
}

print(is_valid_user(user))
# True
```

This is a simple demonstration, not a complete email or user validation system.

### 6.4 Finding the first match

```python
def first_even(nums):
    return next(
        (x for x in nums if x % 2 == 0),
        None
    )


print(first_even([1, 3, 5, 4, 7]))  # 4
print(first_even([1, 3, 5]))        # None
```

`next()` returns the first generated value, or the supplied default if the iterator is exhausted.

### 6.5 Short-circuit evaluation

`any()` and `all()` stop as soon as the result is known.

```python
def check(n):
    print(f"Checking {n}")
    return n > 0


print(any(check(x) for x in [0, 1, 2]))
# Checks 0, then 1, then stops

print(all(check(x) for x in [1, 2, 0]))
# Checks 1, then 2, then 0, then stops
```

Generator expressions avoid constructing a temporary list and allow early termination.

### Comparison

| Function | Returns `True` when | Empty iterable |
|---|---|---|
| `any()` | At least one element is truthy | `False` |
| `all()` | Every element is truthy | `True` |

---

## 7. The `operator` Module

The `operator` module provides functions corresponding to many Python operators. It is useful when a function is required instead of an operator expression.

### 7.1 Arithmetic functions

```python
from operator import add, sub, mul, truediv

print(add(2, 3))       # 5
print(sub(5, 2))       # 3
print(mul(4, 3))       # 12
print(truediv(10, 2))  # 5.0
```

### 7.2 Using operators with `reduce()`

```python
from functools import reduce
from operator import add, mul

print(reduce(add, [1, 2, 3, 4]))
# 10

print(reduce(mul, [1, 2, 3, 4]))
# 24
```

For summation, `sum()` is usually simpler.

### 7.3 `itemgetter()`

`itemgetter()` retrieves one or more items from an object by index or key.

```python
from operator import itemgetter

data = [
    ("Alice", 30),
    ("Bob", 25)
]

data.sort(key=itemgetter(1))

print(data)
```

Getting multiple fields:

```python
records = [
    ("a", 1, "x"),
    ("b", 2, "y")
]

getter = itemgetter(0, 2)

print([getter(record) for record in records])
# [('a', 'x'), ('b', 'y')]
```

### 7.4 `attrgetter()`

`attrgetter()` retrieves object attributes.

```python
from operator import attrgetter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


points = [
    Point(1, 2),
    Point(3, 1)
]

print(sorted(points, key=attrgetter("y")))
```

### 7.5 `methodcaller()`

`methodcaller()` creates a callable that invokes a named method on an object.

```python
from operator import methodcaller

words = ["hello", "WORLD"]

upper = methodcaller("upper")

print([upper(word) for word in words])
# ['HELLO', 'WORLD']
```

It can also pass arguments to the method:

```python
replace_spaces = methodcaller("replace", " ", "_")

print(replace_spaces("hello world"))
# hello_world
```

### 7.6 Comparison operators

```python
from operator import lt, le, eq, ne, gt, ge

print(lt(1, 2))   # True: <
print(le(2, 2))   # True: <=
print(eq(1, 1))   # True: ==
print(ne(1, 2))   # True: !=
print(gt(3, 2))   # True: >
print(ge(3, 3))   # True: >=
```

### 7.7 Logical and sequence operators

```python
from operator import and_, or_, not_, concat, contains

print(and_(True, False))
print(or_(True, False))
print(not_(True))

print(concat("hello ", "world"))
print(contains([1, 2, 3], 2))
```

**Important:** `operator.and_()` and `operator.or_()` perform bitwise-style operator operations. They are not substitutes for the short-circuiting Boolean keywords `and` and `or` in expressions with side effects.

### Quick reference

| Function | Equivalent operation |
|---|---|
| `add(a, b)` | `a + b` |
| `sub(a, b)` | `a - b` |
| `mul(a, b)` | `a * b` |
| `truediv(a, b)` | `a / b` |
| `lt(a, b)` | `a < b` |
| `eq(a, b)` | `a == b` |
| `itemgetter(i)` | Retrieve `obj[i]` |
| `attrgetter("x")` | Retrieve `obj.x` |
| `methodcaller("upper")` | Call `obj.upper()` |

---

## 8. Comprehensions vs Functional Tools

The best choice depends on clarity and the operation you want to perform.

| Task | Recommended approach |
|---|---|
| Transform values with an expression | List comprehension |
| Filter and transform a list | List comprehension |
| Build a dictionary | Dictionary comprehension |
| Collect unique values | Set comprehension |
| Apply an existing function | `map()` can be useful |
| Filter with an existing predicate | `filter()` can be useful |
| Combine corresponding iterable values | `zip()` |
| Iterate with indexes | `enumerate()` |
| Sort by a field | `sorted(..., key=...)` |
| Test whether any condition holds | `any()` |
| Test whether all conditions hold | `all()` |
| Retrieve fields from tuples or objects | `itemgetter()` or `attrgetter()` |
| Accumulate a custom reduction | `functools.reduce()` when appropriate |

### Example comparison

Using `map()` and `filter()`:

```python
nums = [1, 2, 3, 4, 5]

result = list(
    map(
        lambda x: x * 2,
        filter(lambda x: x > 1, nums)
    )
)

print(result)
# [4, 6, 8, 10]
```

Using a list comprehension:

```python
result = [x * 2 for x in nums if x > 1]

print(result)
# [4, 6, 8, 10]
```

Both approaches are valid. Prefer the one that communicates the logic most clearly.

---

## 9. Common Mistakes

### Mistake 1: Confusing filtering with conditional expressions

Filtering:

```python
[x for x in range(10) if x % 2 == 0]
```

Choosing a value:

```python
["even" if x % 2 == 0 else "odd" for x in range(10)]
```

### Mistake 2: Forgetting that `map()` and `filter()` are lazy

```python
result = map(str, [1, 2, 3])

print(list(result))
```

The iterator is consumed by `list()`. Reusing the same exhausted iterator will not reproduce the original values.

### Mistake 3: Assuming `zip()` handles unequal lengths automatically

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# Only two pairs
```

Use `zip_longest()` when you need to preserve all values.

### Mistake 4: Modifying a list while iterating over it

Modifying a collection while iterating can lead to skipped or unexpected elements. When filtering a list, a comprehension is often safer:

```python
nums = [1, 2, 3, 4, 5]

evens = [x for x in nums if x % 2 == 0]
```

### Mistake 5: Forgetting that `sort()` returns `None`

Incorrect:

```python
nums = [3, 1, 2]
nums = nums.sort()
```

Correct:

```python
nums = [3, 1, 2]
nums.sort()

print(nums)
```

Or use:

```python
nums = sorted([3, 1, 2])
```

### Mistake 6: Writing unreadable nested comprehensions

A comprehension is not automatically better than a loop. Use ordinary loops when the logic becomes difficult to follow.

### Mistake 7: Forgetting empty iterable behavior

```python
print(any([]))  # False
print(all([]))  # True
```

These results are intentional and can matter in edge cases.

---

## 10. Competitive Programming Applications

These tools are extremely useful in competitive programming because they reduce boilerplate and make common operations concise.

### 10.1 Read and transform values

```python
nums = list(map(int, input().split()))

squares = [x * x for x in nums]

print(*squares)
```

### 10.2 Filter values

```python
nums = list(map(int, input().split()))

evens = [x for x in nums if x % 2 == 0]

print(*evens)
```

### 10.3 Sort by multiple criteria

Suppose each record contains a name and a score. Sort by score descending and name ascending.

```python
students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 90)
]

students.sort(key=lambda item: (-item[1], item[0]))

print(students)
```

### 10.4 Check conditions efficiently

```python
nums = [2, 4, 6, 8]

all_even = all(x % 2 == 0 for x in nums)
has_large = any(x > 10 for x in nums)

print(all_even)
print(has_large)
```

### 10.5 Build frequency dictionaries

```python
nums = [1, 2, 2, 3, 3, 3]

freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

print(freq)
```

For frequency counting, `collections.Counter` is another useful option.

### 10.6 Iterate over indexes and values

```python
nums = [10, 20, 30]

for i, value in enumerate(nums):
    print(i, value)
```

### 10.7 Iterate through two arrays together

```python
a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a, b):
    print(x + y)
```

### Complexity reminders

- A simple comprehension over \(n\) elements usually takes \(O(n)\) time, excluding the cost of its expression.
- Sorting \(n\) elements generally takes \(O(n \log n)\) time.
- `any()` and `all()` may stop early, but their worst-case time is \(O(n)\).
- `zip()` and `enumerate()` produce iterators; they do not immediately build result lists.
- Creating a list from an iterator requires memory proportional to the number of collected elements.

Always consider the cost of the work performed inside a comprehension or callback.

---

## 11. Practice Checklist

### Beginner

- [ ] Create a list of squares from 1 to 20.
- [ ] Extract all even numbers from a list.
- [ ] Convert a list of strings to uppercase.
- [ ] Create a dictionary mapping numbers to their cubes.
- [ ] Find unique characters in a string using a set comprehension.
- [ ] Combine two lists using `zip()`.
- [ ] Print indexes and values using `enumerate()`.

### Intermediate

- [ ] Flatten a two-dimensional list.
- [ ] Filter a dictionary by its values.
- [ ] Use `map()` to transform numbers.
- [ ] Use `filter()` to select values satisfying a condition.
- [ ] Sort tuples by their second field.
- [ ] Sort records by multiple criteria.
- [ ] Use `any()` to check whether a list contains a negative value.
- [ ] Use `all()` to check whether every value satisfies a condition.
- [ ] Use `itemgetter()` to sort tuple records.

### Advanced

- [ ] Group values by a computed key.
- [ ] Find the first element satisfying a condition.
- [ ] Use `zip_longest()` to combine uneven collections.
- [ ] Implement a custom reduction with `reduce()`.
- [ ] Use `attrgetter()` to sort custom objects.
- [ ] Solve a small data-processing problem using comprehensions and built-ins.

---

## Final Notes

- Use list comprehensions for clear transformations and filtering.
- Use dictionary comprehensions for constructing or transforming mappings.
- Use set comprehensions when uniqueness matters.
- Use `map()` and `filter()` when they make the code clearer, especially with existing functions.
- Use `zip()` to process multiple iterables together.
- Use `enumerate()` instead of manually tracking indexes.
- Use `sorted()` with a `key` function for custom ordering.
- Use `any()` and `all()` to express Boolean conditions concisely.
- Use the `operator` module for reusable operator functions and attribute or item access.
- Prefer readable code over clever one-liners.

**Recommended learning order:** List comprehensions → Dictionary and set comprehensions → `map()` and `filter()` → `zip()` and `enumerate()` → Sorting with `key` → `any()` and `all()` → `operator` module.
