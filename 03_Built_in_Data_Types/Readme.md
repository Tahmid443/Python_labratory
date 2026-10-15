# 03. Python Built-in Data Types — Complete Notes

Python provides several built-in data types for storing, organizing, and manipulating data. Understanding these types is essential for writing efficient programs and solving Data Structures and Algorithms (DSA) and competitive programming problems.

This chapter covers strings, lists, tuples, sets, dictionaries, ranges, mutability, unpacking, and comprehensions.

## Table of Contents

1. [Strings](#1-strings)
2. [String Methods](#2-string-methods)
3. [Lists](#3-lists)
4. [Tuples](#4-tuples)
5. [Sets](#5-sets)
6. [Dictionaries](#6-dictionaries)
7. [Range](#7-range)
8. [Mutability and Immutability](#8-mutability-and-immutability)
9. [Unpacking](#9-unpacking)
10. [Comprehensions](#10-comprehensions)
11. [Data Types Comparison](#11-data-types-comparison)
12. [Common Mistakes](#12-common-mistakes)
13. [Practice Problems](#13-practice-problems)

---

## 1. Strings

**File:** `01_strings.py`

A string (`str`) is an immutable sequence of Unicode characters. Strings are commonly used to store names, sentences, symbols, and other textual data.

### 1.1 Creating Strings

```python
s1 = "Hello, World!"
s2 = 'Python'
s3 = """This is a
multiline string."""

print(s1)
print(s2)
print(s3)
```

Single and double quotes can both define strings. Triple quotes are useful for multiline strings and docstrings.

### 1.2 Indexing

Python uses zero-based indexing.

```python
s = "Python"

print(s[0])   # P
print(s[1])   # y
print(s[-1])  # n
print(s[-2])  # o
```

Positive indexes start from the beginning, while negative indexes start from the end.

For a string of length `n`, valid indexes range from `-n` through `n - 1`.

### 1.3 Slicing

Slicing extracts a portion of a sequence.

Syntax:

```python
sequence[start:stop:step]
```

The `stop` index is excluded.

```python
s = "Python"

print(s[0:3])   # Pyt
print(s[2:])    # thon
print(s[:4])    # Pyth
print(s[::2])   # Pto
print(s[::-1])  # nohtyP
```

Important slicing patterns:

| Expression | Meaning |
|---|---|
| `s[:]` | Copy the sequence's contents into a new string |
| `s[:n]` | First `n` characters |
| `s[n:]` | Characters from index `n` onward |
| `s[-n:]` | Last `n` characters |
| `s[::-1]` | Reverse the string |
| `s[::2]` | Every second character |

Slicing takes \(O(k)\) time for a result containing `k` characters.

### 1.4 String Concatenation and Repetition

```python
print("Hello" + " " + "World")
print("Python " * 3)
print("-" * 20)
```

The `+` operator joins strings, while `*` repeats a string.

### 1.5 Membership

Use `in` and `not in` to test whether a substring exists.

```python
s = "Hello, World!"

print("World" in s)       # True
print("Python" not in s)  # True
```

String membership is case-sensitive.

### 1.6 Iterating Over a String

```python
for ch in "Python":
    print(ch)
```

Each iteration assigns one character to `ch`.

### 1.7 Escape Sequences

| Escape | Meaning |
|---|---|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

Example:

```python
print("Hello\nWorld")
print("Name:\tAlice")
print("Path: C:\\Users\\Alice")
```

### 1.8 Raw Strings and f-Strings

A raw string treats most backslashes as literal characters:

```python
path = r"C:\Users\Alice"
print(path)
```

An f-string embeds expressions directly inside a string:

```python
name = "Alice"
age = 20

print(f"{name} is {age} years old.")
print(f"Next year: {age + 1}")
print(f"Pi: {3.14159:.2f}")
```

**Important:** Raw strings cannot end with an odd number of backslashes because the final backslash would escape the closing quote.

### 1.9 String Immutability

Strings cannot be changed in place.

```python
s = "hello"

# s[0] = "H"  # TypeError

s = "H" + s[1:]
print(s)  # Hello
```

The second example creates a new string and reassigns `s`.

---

## 2. String Methods

**File:** `02_string_methods.py`

Python provides built-in methods for searching, transforming, splitting, validating, and formatting strings.

String methods generally return new strings rather than modifying the original string.

### 2.1 Case Conversion

```python
s = "hello, WORLD!"

print(s.upper())       # HELLO, WORLD!
print(s.lower())       # hello, world!
print(s.title())       # Hello, World!
print(s.capitalize())  # Hello, world!
print(s.swapcase())    # HELLO, world!
```

| Method | Purpose |
|---|---|
| `upper()` | Convert letters to uppercase |
| `lower()` | Convert letters to lowercase |
| `title()` | Capitalize the beginning of words |
| `capitalize()` | Capitalize the first character |
| `swapcase()` | Reverse the case of letters |

### 2.2 Removing Whitespace

```python
s = "  Python  "

print(s.strip())   # "Python"
print(s.lstrip())  # "Python  "
print(s.rstrip())  # "  Python"
```

- `strip()` removes whitespace from both ends.
- `lstrip()` removes whitespace from the left.
- `rstrip()` removes whitespace from the right.

These methods can also accept a set of characters to remove. They do not remove an exact substring as a unit.

### 2.3 Searching and Counting

```python
s = "Hello, World!"

print(s.find("World"))      # 7
print(s.rfind("l"))         # 10
print(s.count("l"))         # 3
print(s.startswith("Hello"))  # True
print(s.endswith("!"))       # True
```

| Method | Purpose |
|---|---|
| `find(sub)` | Return the first index or `-1` |
| `rfind(sub)` | Return the last matching index or `-1` |
| `count(sub)` | Count non-overlapping occurrences |
| `startswith(prefix)` | Check the beginning |
| `endswith(suffix)` | Check the ending |

Unlike `find()`, `index()` raises `ValueError` when the substring is absent.

### 2.4 Replacing Text

```python
s = "I like Java"

print(s.replace("Java", "Python"))
```

Output:

```text
I like Python
```

To limit replacements:

```python
s = "cat cat cat"
print(s.replace("cat", "dog", 1))
```

Output:

```text
dog cat cat
```

### 2.5 Splitting and Joining

`split()` converts a string into a list.

```python
text = "apple,banana,cherry"
fruits = text.split(",")

print(fruits)
```

Output:

```text
['apple', 'banana', 'cherry']
```

`join()` combines strings using a separator.

```python
print(" - ".join(fruits))
```

Output:

```text
apple - banana - cherry
```

For competitive programming, reading multiple integers often looks like this:

```python
numbers = list(map(int, input().split()))
```

`split()` creates strings, `map(int, ...)` converts them to integers, and `list()` collects the results.

### 2.6 Checking String Contents

```python
print("hello".isalpha())  # True
print("123".isdigit())    # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True
print("".isalpha())       # False
```

Common methods:

- `isalpha()`: all characters are alphabetic.
- `isdigit()`: all characters are digits according to Unicode's digit classification.
- `isalnum()`: all characters are alphanumeric.
- `isspace()`: all characters are whitespace.

These methods return `False` for empty strings.

### 2.7 Formatting Strings

```python
print("{} is {}".format("Alice", 20))
print("{name} is {age}".format(name="Bob", age=25))
```

For modern Python, f-strings are usually more readable:

```python
name = "Alice"
age = 20

print(f"{name} is {age}")
```

### 2.8 Padding and Alignment

```python
print("5".zfill(3))       # 005
print("hi".center(10, "*"))
print("hi".ljust(10, "."))
print("hi".rjust(10, "."))
```

- `zfill(width)` pads with zeros on the left.
- `center(width, fillchar)` centers the string.
- `ljust(width, fillchar)` aligns left.
- `rjust(width, fillchar)` aligns right.

### 2.9 Useful String Problem-Solving Patterns

Reverse a string:

```python
def reverse_string(s):
    return s[::-1]
```

Check a palindrome:

```python
def is_palindrome(s):
    return s == s[::-1]
```

Count vowels:

```python
def count_vowels(s):
    return sum(ch.lower() in "aeiou" for ch in s)
```

Time complexity for reversing a string of length `n`: \(O(n)\).

---

## 3. Lists

**File:** `03_lists.py`

A list is an ordered, mutable collection. It can contain duplicate values and elements of different types.

### 3.1 Creating Lists

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4]]
empty = []

from_range = list(range(5))
```

Lists are commonly used for arrays and sequences in Python programming.

### 3.2 Accessing and Slicing

```python
nums = [10, 20, 30, 40, 50]

print(nums[0])     # 10
print(nums[-1])    # 50
print(nums[1:4])   # [20, 30, 40]
```

Accessing an element by index takes \(O(1)\) time. Slicing takes \(O(k)\) time for `k` copied elements.

### 3.3 Modifying Elements

```python
nums = [10, 20, 30]
nums[0] = 100

print(nums)
```

Output:

```text
[100, 20, 30]
```

Lists are mutable, so their elements can be reassigned.

### 3.4 Adding Elements

```python
nums = [1, 2, 3]

nums.append(4)          # Add one element
nums.insert(0, 0)       # Insert at index 0
nums.extend([5, 6, 7])  # Add multiple elements

print(nums)
```

Important differences:

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]
```

`append()` adds one object. `extend()` adds the elements from an iterable.

### 3.5 Removing Elements

```python
nums = [10, 20, 30, 40]

nums.remove(20)  # Remove the first matching value
last = nums.pop()  # Remove and return the last element
del nums[0]        # Delete by index

print(nums)
print(last)
```

| Operation | Behavior | Typical complexity |
|---|---|---|
| `append(x)` | Add at the end | Amortized \(O(1)\) |
| `pop()` | Remove last element | \(O(1)\) |
| `pop(i)` | Remove at index | \(O(n)\) |
| `insert(i, x)` | Insert at index | \(O(n)\) |
| `remove(x)` | Remove first matching value | \(O(n)\) |
| `clear()` | Remove all elements | \(O(n)\) |

`remove()` raises `ValueError` if the value is absent. `pop()` raises `IndexError` when the list is empty or the specified index is invalid.

### 3.6 Common List Operations

```python
nums = [1, 2, 3, 4, 5]

print(len(nums))
print(3 in nums)
print(sum(nums))
print(min(nums))
print(max(nums))
```

For a list of `n` elements:

- `len(nums)`: \(O(1)\)
- `sum(nums)`: \(O(n)\)
- `min(nums)` and `max(nums)`: \(O(n)\)
- Membership testing with `in`: \(O(n)\) in the worst case.

### 3.7 Sorting Lists

```python
nums = [3, 1, 4, 1, 5, 9]

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted([3, 1, 4]))
```

`sort()` modifies the existing list and returns `None`.

`sorted()` returns a new sorted list and works with any iterable whose elements can be ordered.

Both use Python's Timsort algorithm, with \(O(n\log n)\) worst-case time complexity.

Custom sorting:

```python
words = ["apple", "kiwi", "banana"]
words.sort(key=len)

print(words)
```

The list is sorted by word length.

### 3.8 Reversing Lists

```python
nums = [1, 2, 3]

nums.reverse()
print(nums)

nums = [1, 2, 3]
print(nums[::-1])
```

`reverse()` modifies the list in place. Slicing creates a new list.

### 3.9 Copying Lists

```python
original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]
```

For a flat list, `.copy()` creates a shallow copy. Nested lists require additional care, as explained in Section 8.

---

## 4. Tuples

**File:** `04_tuples.py`

A tuple is an ordered, immutable collection. Tuples allow duplicate values and can contain different data types.

### 4.1 Creating Tuples

```python
t = (1, 2, 3)
single = (1,)
empty = ()
```

A single-element tuple requires a trailing comma.

```python
not_a_tuple = (1)
print(type(not_a_tuple))  # <class 'int'>
```

Parentheses alone do not create a tuple; the comma does.

### 4.2 Accessing Elements

```python
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
print(t[1:3]) # (20, 30)
```

Tuples support indexing, slicing, iteration, and membership tests.

### 4.3 Unpacking Tuples

```python
point = (10, 20)
x, y = point

print(x, y)
```

Python assigns each element to the corresponding variable.

The number of variables must match the number of unpacked elements unless starred unpacking is used.

### 4.4 Immutability

```python
t = (1, 2, 3)

# t[0] = 100  # TypeError
```

Tuple elements cannot be reassigned, inserted, or removed.

However, a tuple can contain mutable objects, such as lists. Those inner objects can still change.

### 4.5 Tuple Methods

Tuples provide two primary methods:

```python
t = (1, 2, 2, 3)

print(t.count(2))  # 2
print(t.index(3))  # 3
```

- `count(x)`: count occurrences of `x`.
- `index(x)`: return the first matching index.

### 4.6 Concatenation and Membership

```python
print((1, 2) + (3, 4))
print((1, 2) * 2)
print(2 in (1, 2, 3))
```

Concatenation and repetition create new tuples.

### 4.7 Swapping Variables

```python
x, y = 10, 20
x, y = y, x

print(x, y)  # 20 10
```

Python's multiple assignment makes a temporary variable unnecessary.

### 4.8 Named Tuples

Named tuples provide named fields while preserving tuple-like behavior.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x)
print(p.y)
```

They are useful when a small record benefits from named fields.

---

## 5. Sets

**File:** `05_sets.py`

A set is a mutable collection of unique, hashable elements. Sets are useful for deduplication, membership testing, and mathematical set operations.

Sets do not provide positional indexing, and their iteration order should not be relied upon for a particular arrangement.

### 5.1 Creating Sets

```python
s = {1, 2, 3}
empty = set()

nums = set([1, 2, 2, 3, 3])
print(nums)  # {1, 2, 3}
```

Use `set()` for an empty set. `{}` creates an empty dictionary.

### 5.2 Adding and Removing Elements

```python
s = {1, 2, 3}

s.add(4)
s.discard(1)
s.remove(2)

print(s)
```

- `add(x)`: add an element.
- `discard(x)`: remove an element if present.
- `remove(x)`: remove an element or raise `KeyError` if absent.
- `pop()`: remove and return an arbitrary element.
- `clear()`: remove all elements.

### 5.3 Set Operations

Let:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

**Union:** All elements from either set.

```python
print(a | b)
# {1, 2, 3, 4, 5, 6}
```

**Intersection:** Elements shared by both sets.

```python
print(a & b)
# {3, 4}
```

**Difference:** Elements in `a` but not in `b`.

```python
print(a - b)
# {1, 2}
```

**Symmetric difference:** Elements belonging to exactly one of the sets.

```python
print(a ^ b)
# {1, 2, 5, 6}
```

Equivalent methods include `union()`, `intersection()`, `difference()`, and `symmetric_difference()`.

### 5.4 Subsets and Supersets

```python
a = {1, 2, 3, 4}

print({1, 2}.issubset(a))       # True
print(a.issuperset({1, 2}))     # True
print({1, 2}.isdisjoint({5, 6})) # True
```

A set is a subset if every one of its elements belongs to the other set.

### 5.5 Frozen Sets

A `frozenset` is an immutable set.

```python
fs = frozenset([1, 2, 3])
print(fs)
```

Because it is immutable, a frozenset can be used as an element of another set or as a dictionary key, provided its elements are hashable.

### 5.6 Removing Duplicates

```python
nums = [1, 2, 2, 3, 3, 3]

unique = set(nums)
print(unique)
```

Converting back to a list:

```python
print(list(set(nums)))
```

This does not preserve the original order. To preserve first-occurrence order, use:

```python
unique = list(dict.fromkeys(nums))
print(unique)  # [1, 2, 3]
```

### 5.7 Sets in Competitive Programming

Checking whether an item exists in a set takes \(O(1)\) average time and \(O(n)\) worst-case time under pathological hashing conditions.

For example:

```python
seen = set()

for x in [1, 2, 3, 2, 4]:
    if x in seen:
        print("Duplicate:", x)
    else:
        seen.add(x)
```

Sets are especially useful for detecting duplicates and tracking visited states in graph algorithms.

---

## 6. Dictionaries

**File:** `06_dictionaries.py`

A dictionary (`dict`) stores key-value pairs. Keys must be hashable, while values can be of any type.

Dictionaries preserve insertion order in modern Python.

### 6.1 Creating Dictionaries

```python
person = {"name": "Alice", "age": 30}
empty = {}

from_pairs = dict([("a", 1), ("b", 2)])
```

A dictionary maps each key to a value.

### 6.2 Accessing Values

```python
person = {"name": "Alice", "age": 30}

print(person["name"])
print(person.get("age"))
print(person.get("city", "Unknown"))
```

Difference:

- `person[key]` raises `KeyError` if the key is absent.
- `person.get(key)` returns `None` by default if absent.
- `person.get(key, default)` returns the provided default if absent.

### 6.3 Adding and Updating Values

```python
person = {"name": "Alice", "age": 30}

person["city"] = "Dhaka"
person["age"] = 31

print(person)
```

Assigning to an existing key replaces its value. Assigning to a new key adds a new entry.

### 6.4 Removing Entries

```python
person = {"name": "Alice", "age": 30, "city": "Dhaka"}

del person["city"]
age = person.pop("age")

print(person)
print(age)
```

- `del d[key]`: delete a key.
- `d.pop(key)`: remove a key and return its value.
- `d.pop(key, default)`: return the default if the key is absent.
- `d.clear()`: remove all entries.

### 6.5 Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30}

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)
```

- `keys()`: dictionary keys.
- `values()`: dictionary values.
- `items()`: key-value pairs.

These methods return dynamic view objects rather than lists.

### 6.6 Checking Whether a Key Exists

```python
person = {"name": "Alice", "age": 30}

print("name" in person)  # True
print("city" in person)  # False
```

Membership testing on a dictionary checks its keys, not its values.

### 6.7 Updating and Merging Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = {**d1, **d2}
print(merged)
```

Output:

```text
{'a': 1, 'b': 3, 'c': 4}
```

When keys overlap, the value from the later dictionary wins.

Alternatively:

```python
d1.update(d2)
```

This updates `d1` in place.

### 6.8 Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}

print(squares)
```

Output:

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 6.9 Nested Dictionaries

```python
users = {
    "alice": {"age": 30, "city": "Dhaka"},
    "bob": {"age": 25, "city": "Chittagong"},
}

print(users["alice"]["city"])
```

Nested dictionaries can represent structured records, configuration data, and grouped information.

### 6.10 `dict.fromkeys()`

```python
keys = ["a", "b", "c"]
defaults = dict.fromkeys(keys, 0)

print(defaults)
```

Output:

```text
{'a': 0, 'b': 0, 'c': 0}
```

**Important:** If the default is a mutable object, every key references the same object.

Avoid this pattern:

```python
# Avoid sharing one list between all keys.
bad = dict.fromkeys(["a", "b"], [])
```

Instead, create a separate list for each key:

```python
good = {key: [] for key in ["a", "b"]}
```

### 6.11 Frequency Counting

A common competitive programming technique is counting how many times each value occurs.

```python
nums = [1, 2, 2, 3, 3, 3]
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

print(freq)
```

Output:

```text
{1: 1, 2: 2, 3: 3}
```

This takes \(O(n)\) average time for `n` elements.

A convenient alternative is `collections.Counter`:

```python
from collections import Counter

print(Counter(nums))
```

---

## 7. Range

**File:** `07_range.py`

A `range` object represents an arithmetic progression of integers. It is commonly used in loops and is memory-efficient because it does not store every integer separately.

### 7.1 The Three Forms

```python
print(list(range(5)))
# [0, 1, 2, 3, 4]

print(list(range(2, 7)))
# [2, 3, 4, 5, 6]

print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]
```

General syntax:

```python
range(start, stop, step)
```

The `stop` value is excluded. The `step` cannot be zero.

### 7.2 Counting Backward

```python
print(list(range(5, 0, -1)))
# [5, 4, 3, 2, 1]
```

A negative step is useful for reverse iteration.

### 7.3 Range Is Memory-Efficient

```python
r = range(1_000_000)

print(r[500])
print(len(r))
print(5 in r)
```

A range stores the information needed to represent the sequence rather than a million separate integer objects.

Indexing and length calculation are \(O(1)\). Membership testing for integers in a range is also \(O(1)\).

### 7.4 Summation

```python
print(sum(range(101)))
```

Output:

```text
5050
```

This computes the sum of integers from `0` through `100`.

### 7.5 Nested Ranges

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
```

Each pair represents one combination of the two loop variables.

Two loops over ranges of size `n` and `m` produce \(O(nm)\) iterations.

---

## 8. Mutability and Immutability

**File:** `08_mutability_immutability.py`

Mutability describes whether an object can be modified after creation.

### 8.1 Common Mutable and Immutable Types

| Immutable | Mutable |
|---|---|
| `int` | `list` |
| `float` | `dict` |
| `bool` | `set` |
| `str` | `bytearray` |
| `tuple` | Custom mutable objects |
| `frozenset` | |

`None` is also immutable.

A tuple is immutable as a container, but it can reference mutable objects.

### 8.2 Immutable Objects

```python
s = "hello"
s2 = s

s += " world"

print(s)
print(s2)
```

Output:

```text
hello world
hello
```

The concatenation creates a new string and reassigns `s`. It does not change the original string referenced by `s2`.

### 8.3 Mutable Objects and References

```python
lst = [1, 2, 3]
lst2 = lst

lst.append(4)

print(lst)
print(lst2)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Both variables refer to the same list object.

Conceptually:

```text
lst  ──┐
       ├──> [1, 2, 3, 4]
lst2 ──┘
```

Assignment does not automatically copy a mutable object.

### 8.4 Shallow Copy

```python
original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]
```

The two lists are separate outer objects.

However, `.copy()` creates only a shallow copy, so nested mutable objects are still shared.

### 8.5 Shallow Copy vs. Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()
deep = copy.deepcopy(original)

original[0].append(99)

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)
```

Output:

```text
Original: [[1, 2, 99], [3, 4]]
Shallow: [[1, 2, 99], [3, 4]]
Deep: [[1, 2], [3, 4]]
```

- A shallow copy duplicates the outer container.
- A deep copy recursively copies nested objects where supported.

Deep copying is useful when nested mutable structures must be independent, although it can require additional time and memory.

### 8.6 Equality vs. Identity

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

- `==` compares values for equality.
- `is` checks whether both references point to the same object.

Use `is None` to check for `None`:

```python
value = None

if value is None:
    print("No value")
```

Do not use `is` as a general replacement for `==`.

### 8.7 Tuples Containing Mutable Objects

```python
t = ([1, 2], [3, 4])

t[0].append(99)
print(t)
```

Output:

```text
([1, 2, 99], [3, 4])
```

The tuple's references cannot be reassigned, but the list they reference remains mutable.

---

## 9. Unpacking

**File:** `09_unpacking.py`

Unpacking assigns elements from an iterable to multiple variables in one statement.

### 9.1 Basic Unpacking

```python
a, b, c = (10, 20, 30)

print(a, b, c)
```

The iterable must provide the expected number of values unless starred unpacking is used.

### 9.2 Starred Unpacking

```python
first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

The starred variable collects the remaining elements into a list.

More examples:

```python
*start, last = [1, 2, 3, 4]
print(start, last)

first, *rest = [10, 20, 30]
print(first, rest)
```

There can be at most one starred target at a given unpacking level.

### 9.3 Swapping Variables

```python
a, b = 10, 20
a, b = b, a

print(a, b)
```

Python evaluates the right-hand side before assigning the results.

### 9.4 Nested Unpacking

```python
(a, b), c = (1, 2), 3

print(a, b, c)
```

Nested unpacking is useful when working with pairs, coordinates, and structured results.

### 9.5 Unpacking in Function Calls

The `*` operator expands an iterable into positional arguments.

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]

print(add(*nums))
```

Output:

```text
6
```

The `**` operator expands a dictionary into keyword arguments.

```python
def greet(name, age):
    return f"{name} is {age}"

info = {"name": "Alice", "age": 30}

print(greet(**info))
```

Output:

```text
Alice is 30
```

Dictionary keys must match the function's accepted parameter names unless the function supports arbitrary keyword arguments.

### 9.6 Merging Iterables and Dictionaries

```python
a = [1, 2]
b = [3, 4]

print([*a, *b])
```

Dictionary merging:

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = {**d1, **d2}
print(merged)
```

Later dictionary entries override earlier values for duplicate keys.

### 9.7 Ignoring Values

```python
_, second, _ = (10, 20, 30)

print(second)
```

An underscore is a conventional variable name used when a value is intentionally ignored. It is not a special syntax for discarding values.

---

## 10. Comprehensions

**File:** `10_comprehensions.py`

Comprehensions provide a concise way to build collections from iterables.

They can include transformations, filtering conditions, and nested iteration.

### 10.1 List Comprehension

Traditional loop:

```python
squares = []

for x in range(10):
    squares.append(x ** 2)
```

Equivalent comprehension:

```python
squares = [x ** 2 for x in range(10)]

print(squares)
```

General syntax:

```python
[expression for item in iterable]
```

### 10.2 List Comprehension with a Condition

```python
evens = [x for x in range(20) if x % 2 == 0]

print(evens)
```

General syntax:

```python
[expression for item in iterable if condition]
```

Only elements satisfying the condition are included.

### 10.3 Conditional Expressions in Comprehensions

```python
labels = [
    "even" if x % 2 == 0 else "odd"
    for x in range(5)
]

print(labels)
```

Output:

```text
['even', 'odd', 'even', 'odd', 'even']
```

Remember the distinction:

- `expression if condition` at the end filters elements.
- `value_if_true if condition else value_if_false` inside the expression chooses a value for each element.

### 10.4 Nested List Comprehensions

```python
matrix = [
    [i * j for j in range(3)]
    for i in range(3)
]

print(matrix)
```

Output:

```text
[[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

The outer comprehension creates rows. The inner comprehension creates each row's values.

### 10.5 Flattening a Nested List

```python
matrix = [[1, 2], [3, 4], [5, 6]]

flat = [x for row in matrix for x in row]

print(flat)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

Read the comprehension in loop order:

1. Iterate through each `row`.
2. Iterate through each `x` in that row.
3. Add `x` to the resulting list.

### 10.6 Set Comprehension

```python
words = ["a", "bb", "ccc", "dd"]

unique_lengths = {len(word) for word in words}

print(unique_lengths)
```

Set comprehensions automatically remove duplicate results.

### 10.7 Dictionary Comprehension

```python
square_map = {x: x ** 2 for x in range(5)}

print(square_map)
```

General syntax:

```python
{key_expression: value_expression for item in iterable}
```

### 10.8 Generator Expressions

```python
gen = (x ** 2 for x in range(5))

print(sum(gen))
```

Output:

```text
30
```

Unlike a list comprehension, a generator expression produces values lazily as they are requested.

This is often more memory-efficient when processing a large iterable without needing to store every result.

A generator is generally consumed as it is iterated, so reusing it may require creating a new generator.

### 10.9 When Not to Use Comprehensions

Avoid comprehensions when the logic becomes too complicated or involves multiple side effects.

Less readable:

```python
# Avoid complicated nested expressions.
```

Often clearer:

```python
result = []

for row in matrix:
    for value in row:
        if value > 0:
            result.append(value)
```

Choose readability over brevity.

---

## 11. Data Types Comparison

| Type | Ordered | Mutable | Duplicates | Indexing |
|---|---|---|---|---|
| `str` | Yes | No | Yes | Yes |
| `list` | Yes | Yes | Yes | Yes |
| `tuple` | Yes | No | Yes | Yes |
| `set` | No positional order | Yes | No | No |
| `frozenset` | No positional order | No | No | No |
| `dict` | Yes, insertion order | Yes | Keys must be unique | By key |
| `range` | Yes | No | Values follow the specified progression | Yes |

### Which Type Should You Use?

- **String:** Text processing and character operations.
- **List:** Ordered, changeable collections and arrays.
- **Tuple:** Fixed records and immutable sequences.
- **Set:** Unique values, duplicate detection, and membership testing.
- **Dictionary:** Key-value mappings, frequency counts, and lookups.
- **Range:** Memory-efficient integer sequences.
- **Generator:** Lazy processing when results need not be stored all at once.

### Average Operation Complexity

| Operation | Typical average complexity |
|---|---:|
| List indexing | \(O(1)\) |
| List append | Amortized \(O(1)\) |
| List membership | \(O(n)\) |
| Tuple indexing | \(O(1)\) |
| Set membership | \(O(1)\) |
| Dictionary key lookup | \(O(1)\) |
| String search | \(O(n)\) |
| Sorting a list | \(O(n\log n)\) |

These are typical complexities, not guarantees for every possible input or implementation.

---

## 12. Common Mistakes

### Mistake 1: Trying to Modify a String

Incorrect:

```python
# s = "hello"
# s[0] = "H"
```

Correct:

```python
s = "H" + "hello"[1:]
```

Strings are immutable.

### Mistake 2: Confusing `append()` and `extend()`

```python
a = [1, 2]
a.append([3, 4])

print(a)  # [1, 2, [3, 4]]
```

Use `extend()` when the intention is to add each element separately.

### Mistake 3: Forgetting the Tuple Comma

```python
a = (5,)
b = (5)

print(type(a))  # tuple
print(type(b))  # int
```

### Mistake 4: Using `{}` for an Empty Set

```python
empty_dict = {}
empty_set = set()
```

### Mistake 5: Assuming a Set Preserves List Order

```python
nums = [3, 1, 2, 1]
unique = list(set(nums))
```

This removes duplicates but does not promise to preserve the original order. Use `dict.fromkeys()` if first-occurrence order matters.

### Mistake 6: Using a Dictionary Value When Checking a Key

```python
person = {"name": "Alice"}

print("name" in person)  # True
print("Alice" in person) # False
```

Dictionary membership checks keys.

### Mistake 7: Assuming Assignment Creates a Copy

```python
a = [1, 2]
b = a

b.append(3)

print(a)  # [1, 2, 3]
```

Use `a.copy()` or another suitable copying method when independent data is required.

### Mistake 8: Forgetting That `sort()` Returns `None`

```python
nums = [3, 1, 2]

nums.sort()
print(nums)
```

Do not write `nums = nums.sort()` if you intend to keep the sorted list.

### Mistake 9: Using a Mutable Default with `dict.fromkeys()`

```python
# Both keys refer to the same list.
bad = dict.fromkeys(["x", "y"], [])
```

Use a dictionary comprehension to create a separate mutable value for each key.

### Mistake 10: Overusing Comprehensions

If a comprehension becomes difficult to read, rewrite it as a normal loop.

---

## 13. Practice Problems

Try solving the following problems independently before checking your solutions.

### Beginner: Strings

- [ ] Reverse a string.
- [ ] Check whether a string is a palindrome.
- [ ] Count vowels and consonants.
- [ ] Count the occurrences of a character.
- [ ] Count the words in a sentence.
- [ ] Remove spaces from a string.
- [ ] Check whether two strings are anagrams.
- [ ] Find the first non-repeating character.

### Beginner: Lists and Tuples

- [ ] Find the largest and smallest list elements.
- [ ] Calculate the sum and average of a list.
- [ ] Remove duplicates from a list.
- [ ] Find the second-largest distinct element.
- [ ] Rotate a list by `k` positions.
- [ ] Merge two sorted lists.
- [ ] Find common elements in two lists.
- [ ] Split a list into chunks of a given size.

### Beginner: Sets and Dictionaries

- [ ] Find the union and intersection of two sets.
- [ ] Find elements that occur in only one of two lists.
- [ ] Count the frequency of each number in a list.
- [ ] Find the most frequent element.
- [ ] Group words by their first character.
- [ ] Find duplicate elements using a set.
- [ ] Check whether two lists contain the same unique values.

### Intermediate: Comprehensions and Unpacking

- [ ] Generate squares of even numbers from `1` to `n`.
- [ ] Flatten a two-dimensional list.
- [ ] Build a dictionary mapping numbers to their squares.
- [ ] Transpose a matrix using a comprehension.
- [ ] Extract the first, middle, and last elements using unpacking.
- [ ] Merge multiple lists using unpacking.
- [ ] Create a word-frequency dictionary using a comprehension or loop.

### Competitive Programming Challenge

- [ ] Two Sum: find two indices whose values add up to a target.
- [ ] Find the first duplicate in an array.
- [ ] Find the longest substring without repeating characters.
- [ ] Find the majority element in a list.
- [ ] Group anagrams together.
- [ ] Find the frequency of each character in a string.
- [ ] Find the intersection of two arrays.
- [ ] Find the longest consecutive sequence using a set.

---

## Final Revision Checklist

Before moving to the next chapter, make sure you can:

- [ ] Index and slice strings, lists, and tuples.
- [ ] Use common string methods.
- [ ] Explain the differences between lists, tuples, sets, and dictionaries.
- [ ] Add, remove, search, and sort list elements.
- [ ] Perform set union, intersection, difference, and symmetric difference.
- [ ] Use dictionaries for frequency counting and fast lookups.
- [ ] Explain the behavior of `range()`.
- [ ] Distinguish mutable objects from immutable objects.
- [ ] Explain references, shallow copies, and deep copies.
- [ ] Use basic and starred unpacking.
- [ ] Write list, set, dictionary, and generator comprehensions.
- [ ] Estimate the time complexity of common operations.

**Next topic:** Functions and Recursion — function arguments, return values, scope, recursion, base cases, and recursive problem-solving.

**Study strategy:** Practice each operation directly in Python, then solve small problems without looking at the notes. For competitive programming, pay particular attention to list operations, sets, dictionaries, string processing, and time complexity.
