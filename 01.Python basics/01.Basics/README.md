# 🐍 Python Basics — Complete Revision Notes

This folder contains my **Python fundamentals** practice programs.  
The purpose of this README is to work as a **complete revision note**: instead of opening every `.py` file separately, I can come here to revise the concepts, syntax, examples, rules, and common mistakes.

> **Source files:** `01.output_comment.py` → `10.user_input.py`

---

## 📚 Table of Contents

1. [Output and Comments](#1-output-and-comments)
2. [Variables](#2-variables)
3. [Data Types](#3-data-types)
4. [Numbers](#4-numbers)
5. [Random Numbers](#5-random-numbers)
6. [Type Casting](#6-type-casting)
7. [Conditional Statements](#7-conditional-statements)
8. [Loops](#8-loops)
9. [Operators](#9-operators)
10. [User Input](#10-user-input)
11. [Important Differences](#11-important-differences)
12. [Common Mistakes](#12-common-mistakes)
13. [Quick Revision Sheet](#13-quick-revision-sheet)

---

# 1. Output and Comments

📄 **File:** `01.output_comment.py`

## 1.1 `print()`

The `print()` function is used to display information on the screen.

```python
print("Hello World")
print(10)
print(10 + 20)
```

Output:

```text
Hello World
10
30
```

### Printing variables

```python
name = "Taqi Tahmid"
print(name)
```

### Printing multiple values

```python
name = "Taqi Tahmid"
age = 20

print(name, age)
```

By default, `print()` separates multiple arguments with a space.

---

## 1.2 f-strings

An **f-string** allows variables and expressions to be inserted directly into a string.

```python
name = "Taqi Tahmid"
print(f"My name is {name}")
```

You can also put expressions inside `{}`:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

### Why use f-strings?

They are usually cleaner and easier to read than string concatenation.

```python
name = "Taqi"

# f-string
print(f"Hello {name}")
```

---

## 1.3 `end` parameter

Normally, `print()` ends with a newline.

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Using `end` changes what is printed at the end.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

The `end` value defaults to `"\n"`.

```python
print("A", end="\n")  # default
```

---

## 1.4 Comments

Comments are notes written inside source code for humans. Python ignores normal comments during execution.

### Single-line comment

```python
# This is a comment
print("Hello")
```

Comments are useful for:

- explaining code
- documenting logic
- making code easier to maintain
- temporarily disabling a line

---

## 1.5 Multi-line comments

Python does not have a dedicated multi-line comment syntax.

Triple-quoted strings are often used for multi-line documentation or notes:

```python
"""
This is a multi-line string.
It can contain multiple lines.
"""
```

If a triple-quoted string is not assigned to a variable, it does not normally affect the program's result, but technically it is a **string literal**, not a comment.

For actual documentation of functions/classes, use **docstrings**.

---

# 2. Variables

📄 **File:** `02.variables.py`

## 2.1 What is a variable?

A variable is a name that refers to an object/value.

```python
name = "Taqi"
age = 20
height = 5.6
```

Here:

- `name` refers to a string
- `age` refers to an integer
- `height` refers to a float

Python does not require you to declare the data type separately.

---

## 2.2 Variable naming rules

A variable name:

1. Must start with a letter or `_`.
2. Cannot start with a number.
3. Can contain letters, numbers and `_`.
4. Is case-sensitive.
5. Cannot be a Python keyword.

### Valid

```python
name = "Taqi"
_age = 20
student_name = "Rahim"
marks2 = 90
```

### Invalid

```python
2name = "Taqi"       # invalid
student-name = "A"   # invalid
class = 10           # invalid keyword
```

---

## 2.3 Case sensitivity

Python treats uppercase and lowercase names as different.

```python
age = 20
Age = 25
AGE = 30
```

These are three different variables.

---

## 2.4 Multiple assignment

Python allows multiple variables to be assigned in one statement.

```python
x, y, z = "apple", "orange", "mango"
```

Equivalent conceptually to:

```python
x = "apple"
y = "orange"
z = "mango"
```

---

## 2.5 Assigning the same value

The same value can be assigned to multiple variables:

```python
x = y = z = 100
```

Now all three names refer to `100`.

---

## 2.6 Unpacking

Values from an iterable can be unpacked into variables.

```python
marks = [90, 89, 85]

a, b, c = marks

print(a)
print(b)
print(c)
```

Output:

```text
90
89
85
```

The number of variables must match the number of values unless extended unpacking is used.

```python
a, *b = [1, 2, 3, 4]
```

Here:

```text
a = 1
b = [2, 3, 4]
```

---

## 2.7 Global and local variables

A variable created outside a function is generally a **global variable**.

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

The function can read the global `x`.

### Local variable

A variable created inside a function is local to that function.

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
```

Output:

```text
Python is fantastic
Python is awesome
```

The local `x` does not replace the global `x`.

---

## 2.8 `global` keyword

If you want to modify a global variable from inside a function, use `global`.

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print(x)
```

Output:

```text
fantastic
```

### Important

Simply reading a global variable does **not** require `global`.

---

# 3. Data Types

📄 **File:** `03.datatype.py`

Python has several built-in data types.

| Category | Types |
|---|---|
| Text | `str` |
| Numeric | `int`, `float`, `complex` |
| Sequence | `list`, `tuple`, `range` |
| Mapping | `dict` |
| Set | `set`, `frozenset` |
| Boolean | `bool` |
| Binary | `bytes`, `bytearray`, `memoryview` |
| None | `NoneType` |

---

## 3.1 Checking a type

Use `type()`.

```python
x = 5
print(type(x))
```

Output:

```text
<class 'int'>
```

Examples:

```python
print(type("Hello"))   # str
print(type(10))        # int
print(type(3.14))      # float
print(type(True))      # bool
```

---

## 3.2 String — `str`

Strings contain text.

```python
name = "Taqi"
country = 'Bangladesh'
```

Strings can be written using single or double quotes.

```python
"Hello"
'Hello'
```

---

## 3.3 Integer — `int`

Whole numbers:

```python
x = 10
y = -50
z = 100000000000
```

Python integers can be very large, limited mainly by available memory.

---

## 3.4 Float — `float`

Numbers containing a decimal point or represented using scientific notation.

```python
x = 10.5
y = -3.14
z = 35e3
```

`35e3` means:

```text
35 × 10³ = 35000
```

and its type is `float`.

---

## 3.5 Complex — `complex`

Complex numbers have a real part and an imaginary part.

```python
x = 3 + 4j
```

Here:

- real part = `3`
- imaginary part = `4`

```python
print(type(3 + 4j))
```

Output:

```text
<class 'complex'>
```

---

## 3.6 List

Lists store ordered, changeable collections.

```python
fruits = ["apple", "banana", "cherry"]
```

Lists are:

- ordered
- mutable
- allow duplicate values

---

## 3.7 Tuple

Tuples store ordered, immutable collections.

```python
numbers = (1, 2, 3)
```

---

## 3.8 Range

`range()` represents a sequence of numbers.

```python
numbers = range(5)
```

It is commonly used with loops.

---

## 3.9 Dictionary

Dictionaries store key-value pairs.

```python
student = {
    "name": "Taqi",
    "age": 20
}
```

---

## 3.10 Set

Sets store unordered collections of unique values.

```python
numbers = {1, 2, 3, 4}
```

---

## 3.11 Boolean

Boolean values are:

```python
True
False
```

Example:

```python
x = 10
print(x > 5)
```

Output:

```text
True
```

---

## 3.12 `None`

`None` represents the absence of a value.

```python
x = None
print(type(x))
```

Output:

```text
<class 'NoneType'>
```

---

# 4. Numbers

📄 **File:** `04.numbers.py`

Python has three main numeric types:

```text
int
float
complex
```

---

## 4.1 Integer

```python
x = 1
y = 35656222554887711
z = -3255522
```

Check the type:

```python
print(type(x))
```

---

## 4.2 Float

```python
x = 1.10
y = 1.0
z = -35.59
```

All are `float`.

---

## 4.3 Scientific notation

Python supports scientific notation using `e` or `E`.

```python
x = 35e3
y = 12e4
z = -87.7e100
```

Examples:

```text
35e3  = 35000.0
12e4  = 120000.0
```

These are **floats**, not complex numbers.

---

## 4.4 Complex numbers

```python
x = 1j
y = 3 + 4j
```

Example:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

---

## 4.5 Numeric conversion

```python
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)
```

Results:

```text
a = 1.0
b = 2
c = 1+0j
```

### Important

Converting a float to an integer using `int()` truncates the decimal part.

```python
int(2.9)    # 2
int(-2.9)   # -2
```

It does **not** perform normal mathematical rounding.

---

# 5. Random Numbers

📄 **File:** `05.random_number.py`

Python provides the `random` module for pseudo-random number generation.

```python
import random
```

> Random values generated by this module are generally suitable for games, simulations and ordinary programs, but **not for security-sensitive purposes**. For security-sensitive randomness, use the `secrets` module.

---

## 5.1 `random.random()`

Returns a random floating-point number in:

```text
0.0 <= number < 1.0
```

Example:

```python
import random

num = random.random()
print(num)
```

Possible output:

```text
0.384729...
```

---

## 5.2 `random.choice()`

Returns one random item from a non-empty sequence such as a list, tuple or string.

```python
numbers = [1, 2, 3, 4, 5]

print(random.choice(numbers))
```

String example:

```python
text = "striver"
print(random.choice(text))
```

---

## 5.3 `random.randrange()`

Generates a random integer from a range.

```python
random.randrange(20, 50, 3)
```

The general form is:

```python
random.randrange(start, stop, step)
```

The `stop` value is excluded.

Example:

```python
random.randrange(2, 10, 2)
```

Possible results:

```text
2, 4, 6, 8
```

---

## 5.4 `random.seed()`

`seed()` initializes the pseudo-random generator.

```python
random.seed(5)
print(random.random())
```

Using the same seed produces the same sequence of pseudo-random values.

```python
random.seed(5)
print(random.random())

random.seed(5)
print(random.random())
```

The two values will match.

### Why is this useful?

Useful for:

- testing
- debugging
- reproducible experiments
- simulations

---

## 5.5 `random.shuffle()`

Randomly rearranges a mutable sequence **in place**.

```python
items = ["A", "B", "C", "D"]

random.shuffle(items)

print(items)
```

The original list is modified.

### Important

`shuffle()` returns `None`.

```python
result = random.shuffle(items)
print(result)   # None
```

---

## 5.6 `random.uniform()`

Returns a random floating-point number between two values.

```python
random.uniform(5, 10)
```

Example:

```python
print(random.uniform(5, 10))
```

---

## 5.7 Useful random functions

| Function | Purpose |
|---|---|
| `random.random()` | Random float from `0.0` to less than `1.0` |
| `random.choice(seq)` | Random item |
| `random.randrange()` | Random integer from a range |
| `random.seed()` | Reproducible pseudo-random sequence |
| `random.shuffle()` | Shuffle a mutable sequence in place |
| `random.uniform(a, b)` | Random float in a specified interval |

---

# 6. Type Casting

📄 **File:** `06.casting.py`

**Type casting** means converting a value from one data type to another.

Common constructors:

```python
int()
float()
str()
```

---

## 6.1 `int()`

Converts a compatible value to an integer.

```python
x = int(1)
y = int(2.8)
z = int("3")
```

Results:

```text
1
2
3
```

### Important

```python
int("3")      # valid
int("3.5")    # ValueError
```

For a decimal string:

```python
int(float("3.5"))
```

gives:

```text
3
```

---

## 6.2 `float()`

Converts a compatible value to a floating-point number.

```python
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
```

Results:

```text
1.0
2.8
3.0
4.2
```

---

## 6.3 `str()`

Converts values into strings.

```python
x = str("s1")
y = str(2)
z = str(3.0)
```

Results:

```text
"s1"
"2"
"3.0"
```

---

## 6.4 Casting examples

```python
age = "20"

age = int(age)

print(age + 5)
```

Without conversion:

```python
age = "20"
print(age + 5)
```

This causes a `TypeError` because a string and integer cannot be added directly.

---

# 7. Conditional Statements

📄 **File:** `07.conditional_statement.py`

Conditional statements allow a program to make decisions.

---

## 7.1 `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

The block runs only when the condition is `True`.

---

## 7.2 `if-else`

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 7.3 `if-elif-else`

Used when there are multiple conditions.

```python
a = 33
b = 21

if a > b:
    print("a is greater")
elif a == b:
    print("They are equal")
else:
    print("b is greater")
```

Execution:

1. Python checks `if`.
2. If false, checks `elif`.
3. If all conditions are false, executes `else`.

---

## 7.4 Ternary conditional expression

Python provides a compact one-line conditional expression.

```python
x = 15
y = 20

max_value = x if x > y else y
```

General syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"
```

---

## 7.5 Default value pattern

A conditional expression can be useful for fallback values.

```python
username = ""

display_name = username if username else "Guest"
```

Since an empty string is falsy:

```text
display_name = "Guest"
```

---

## 7.6 `pass`

`pass` does nothing.

It is useful when a block is required syntactically but you do not want to implement it yet.

```python
age = 20

if age < 18:
    pass
else:
    print("Access granted")
```

Without `pass`, an empty block causes a syntax error.

---

# 7.7 `match-case`

`match-case` provides structural pattern matching and can be useful when comparing a value against multiple patterns.

```python
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
```

### Default case

Use `_` when no previous case matches.

```python
match day:
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Weekday")
```

`_` acts as a catch-all pattern in this context.

---

## 7.8 Combining values with `|`

Multiple patterns can be combined.

```python
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
```

---

## 7.9 `if` vs `match`

### Use `if` when:

- conditions involve comparisons
- ranges are important
- complex Boolean expressions are needed

### Use `match` when:

- matching specific patterns/values
- handling multiple structured cases
- pattern matching makes the code clearer

---

# 8. Loops

📄 **File:** `08.loops.py`

Loops repeat a block of code.

Python mainly provides:

```text
for
while
```

---

# 8.1 `for` loop

Used to iterate over an iterable.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
cherry
```

---

## 8.2 Looping through a string

Strings are iterable.

```python
for char in "banana":
    print(char)
```

Each character is processed one at a time.

---

## 8.3 `break`

`break` immediately terminates the loop.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    if fruit == "banana":
        break
```

Output:

```text
apple
banana
```

---

## 8.4 `continue`

`continue` skips the current iteration and moves to the next one.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue

    print(fruit)
```

Output:

```text
apple
cherry
```

### Remember

```text
break     → stop the entire loop
continue  → skip current iteration
```

---

# 8.5 `range()`

`range()` is commonly used to generate a sequence of numbers.

### `range(stop)`

```python
for x in range(6):
    print(x)
```

Produces:

```text
0 1 2 3 4 5
```

The stop value is excluded.

---

### `range(start, stop)`

```python
for x in range(2, 6):
    print(x)
```

Produces:

```text
2 3 4 5
```

---

### `range(start, stop, step)`

```python
for x in range(2, 30, 3):
    print(x)
```

Produces:

```text
2 5 8 11 14 17 20 23 26 29
```

General syntax:

```python
range(start, stop, step)
```

---

## 8.6 Negative step

`range()` can count backwards.

```python
for x in range(10, 0, -1):
    print(x)
```

Output:

```text
10 9 8 7 6 5 4 3 2 1
```

---

# 8.7 `for-else`

Python allows an `else` block after a `for` loop.

```python
for x in range(6):
    print(x)
else:
    print("Finally finished!")
```

The `else` block executes when the loop finishes normally.

### Important behavior

If the loop is terminated using `break`, the loop's `else` block does not execute.

```python
for x in range(6):
    if x == 3:
        break
else:
    print("Completed normally")
```

The `else` block is skipped.

---

# 8.8 Empty loop

A loop cannot have an empty body.

Use `pass` if necessary:

```python
for x in [0, 1, 2]:
    pass
```

---

# 8.9 `while` loop

A `while` loop repeats while its condition remains true.

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

### Important

Always make sure the loop condition can eventually become false.

Otherwise:

```python
while True:
    print("Infinite loop")
```

creates an infinite loop.

---

# 9. Operators

📄 **File:** `09.operators.py`

Operators perform operations on values.

---

# 9.1 Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `x + y` |
| `-` | Subtraction | `x - y` |
| `*` | Multiplication | `x * y` |
| `/` | Division | `x / y` |
| `%` | Modulus | `x % y` |
| `**` | Exponentiation | `x ** y` |
| `//` | Floor division | `x // y` |

### Examples

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a % b)    # 1
print(a ** b)   # 1000
print(a // b)   # 3
```

### `/` vs `//`

```python
10 / 3
```

gives approximately:

```text
3.333333...
```

While:

```python
10 // 3
```

gives:

```text
3
```

For negative numbers, floor division rounds toward negative infinity:

```python
-10 // 3
```

gives:

```text
-4
```

---

# 9.2 Assignment Operators

| Operator | Equivalent |
|---|---|
| `=` | `x = 5` |
| `+=` | `x = x + 3` |
| `-=` | `x = x - 3` |
| `*=` | `x = x * 3` |
| `/=` | `x = x / 3` |
| `%=` | `x = x % 3` |
| `//=` | `x = x // 3` |
| `**=` | `x = x ** 3` |
| `&=` | `x = x & 3` |
| `|=` | `x = x | 3` |
| `^=` | `x = x ^ 3` |
| `>>=` | `x = x >> 3` |
| `<<=` | `x = x << 3` |

Example:

```python
x = 10
x += 5

print(x)
```

Output:

```text
15
```

---

# 9.3 Walrus Operator `:=`

Python 3.8 introduced the assignment expression operator `:=`.

It allows a value to be assigned as part of an expression.

```python
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
```

Here:

```python
count := len(numbers)
```

both:

1. calculates `len(numbers)`
2. assigns it to `count`

and then the value is used in the condition.

### Use carefully

The walrus operator can make code shorter, but normal assignment is often clearer.

---

# 9.4 Ternary Operator

Python's conditional expression:

```python
num = 6

x = "WEEKEND!" if num > 5 else "Workday"
```

General form:

```python
result = value_if_true if condition else value_if_false
```

Nested conditional expressions are possible:

```python
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
```

However, deeply nested ternaries can reduce readability. Prefer `if-elif-else` when the logic becomes complicated.

---

# 9.5 Comparison Operators

Comparison operators return `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

Example:

```python
x = 10
y = 20

print(x < y)    # True
print(x == y)   # False
```

### `=` vs `==`

This is extremely important:

```python
x = 10
```

means assignment.

```python
x == 10
```

means comparison.

---

# 9.6 Logical Operators

| Operator | Meaning |
|---|---|
| `and` | True if both conditions are true |
| `or` | True if at least one condition is true |
| `not` | Reverses a Boolean result |

Examples:

```python
x = 7

print(x > 5 and x < 10)
print(x < 5 or x == 7)
print(not(x > 5))
```

---

## Truth table

### `and`

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### `or`

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### `not`

| A | not A |
|---|---|
| True | False |
| False | True |

---

# 9.7 Identity Operators

| Operator | Meaning |
|---|---|
| `is` | Same object |
| `is not` | Different objects |

Example:

```python
a = [1, 2]
b = a

print(a is b)
```

Output:

```text
True
```

### Important: `is` vs `==`

`==` checks whether values compare equal.

`is` checks whether two references point to the same object.

Use:

```python
a == b
```

for value equality.

Use:

```python
a is b
```

for object identity.

A common Python example is:

```python
if value is None:
    ...
```

---

# 9.8 Membership Operators

| Operator | Meaning |
|---|---|
| `in` | Value exists in a container |
| `not in` | Value does not exist |

Example:

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("mango" not in fruits)
```

Output:

```text
True
True
```

Membership also works with strings:

```python
print("py" in "python")
```

---

# 9.9 Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Name |
|---|---|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left shift |
| `>>` | Right shift |

---

## Bitwise AND

```python
5 & 3
```

Binary:

```text
5 = 101
3 = 011
---------
    001 = 1
```

So:

```python
5 & 3   # 1
```

---

## Bitwise OR

```text
5 = 101
3 = 011
---------
    111 = 7
```

Therefore:

```python
5 | 3   # 7
```

---

## Bitwise XOR

XOR returns `1` when the corresponding bits are different.

```text
5 = 101
3 = 011
---------
    110 = 6
```

Therefore:

```python
5 ^ 3   # 6
```

---

## Bitwise NOT

```python
~x
```

Python integers use signed integer semantics, so:

```python
~5
```

gives:

```text
-6
```

A useful identity is:

```text
~x = -(x + 1)
```

---

## Left shift

```python
5 << 1
```

Binary:

```text
101 << 1 = 1010
```

So:

```text
10
```

For non-negative integers, shifting left by one position is equivalent to multiplying by 2.

---

## Right shift

```python
10 >> 1
```

gives:

```text
5
```

For non-negative integers, shifting right by one position is equivalent to integer division by 2.

---

# 9.10 Operator Precedence

When multiple operators appear in an expression, Python follows precedence rules.

From higher to lower precedence:

| Priority | Operators |
|---:|---|
| 1 | `()` |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `|` |
| 10 | Comparisons, `is`, `is not`, `in`, `not in` |
| 11 | `not` |
| 12 | `and` |
| 13 | `or` |

Example:

```python
result = 2 + 3 * 4
```

First:

```text
3 * 4 = 12
```

Then:

```text
2 + 12 = 14
```

So:

```text
result = 14
```

### Best practice

Use parentheses when they make the intended logic clearer:

```python
result = (2 + 3) * 4
```

---

# 10. User Input

📄 **File:** `10.user_input.py`

The `input()` function allows a program to receive input from the user.

---

## 10.1 Basic input

```python
name = input()

print(f"Hello {name}")
```

The program waits for the user to type something and press Enter.

---

## 10.2 Input prompt

Instead of printing a separate question:

```python
print("Enter your age:")
age = input()
```

you can write:

```python
age = input("Enter your age: ")
```

---

## 10.3 Important: `input()` returns a string

This is one of the most important Python basics.

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters:

```text
20
```

the result is:

```text
<class 'str'>
```

Therefore, convert numeric input when needed.

---

## 10.4 Integer input

```python
age = int(input("Enter your age: "))
```

Now `age` is an integer.

---

## 10.5 Float input

```python
price = float(input("Enter price: "))
```

Now `price` is a float.

---

## 10.6 Mathematical operations with input

Incorrect:

```python
a = input("Enter a: ")
b = input("Enter b: ")

print(a + b)
```

If the user enters:

```text
10
20
```

the output is:

```text
1020
```

because both are strings.

Correct:

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(a + b)
```

Output:

```text
30
```

---

## 10.7 Using `math`

Your program imports Python's `math` module:

```python
import math
```

Then calculates a square root:

```python
x = input("Enter a number: ")
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")
```

### Cleaner version

Instead of converting later:

```python
x = float(input("Enter a number: "))
print(f"The square root is {math.sqrt(x)}")
```

---

## 10.8 Useful `math` functions

```python
import math

math.sqrt(25)       # 5.0
math.pow(2, 3)      # 8.0
math.ceil(3.2)      # 4
math.floor(3.8)     # 3
math.pi             # π
math.e              # Euler's number
```

---

# 11. Important Differences

## `=` vs `==` vs `is`

| Operator | Purpose |
|---|---|
| `=` | Assignment |
| `==` | Value comparison |
| `is` | Object identity |

Example:

```python
x = 10
x == 10
x is None
```

---

## `/` vs `//`

```python
10 / 3    # 3.333...
10 // 3   # 3
```

---

## `break` vs `continue` vs `pass`

| Keyword | Meaning |
|---|---|
| `break` | Terminates the loop |
| `continue` | Skips current iteration |
| `pass` | Does nothing; placeholder |

---

## `for` vs `while`

### `for`

Best when iterating over a collection or a known sequence.

```python
for x in range(10):
    print(x)
```

### `while`

Best when repetition depends on a condition.

```python
while condition:
    ...
```

---

## `random.choice()` vs `random.randrange()`

```python
random.choice([10, 20, 30])
```

selects an item from a sequence.

```python
random.randrange(10, 30, 2)
```

generates an integer from a numerical range.

---

# 12. Common Mistakes

## Mistake 1: Forgetting that `input()` returns `str`

```python
age = input("Age: ")
print(age + 5)   # TypeError
```

Correct:

```python
age = int(input("Age: "))
print(age + 5)
```

---

## Mistake 2: Using `=` instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Mistake 3: Confusing `is` and `==`

Do not normally use:

```python
a is b
```

when you mean value equality.

Use:

```python
a == b
```

---

## Mistake 4: Forgetting indentation

Python uses indentation to define blocks.

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 5: Infinite `while` loop

Wrong:

```python
i = 1

while i <= 5:
    print(i)
```

`i` never changes.

Correct:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## Mistake 6: Expecting `range(6)` to include 6

```python
range(6)
```

produces:

```text
0, 1, 2, 3, 4, 5
```

The stop value is excluded.

---

## Mistake 7: Expecting `int()` to round

```python
int(4.9)
```

returns:

```text
4
```

It truncates toward zero; it does not round to the nearest integer.

---

## Mistake 8: Assigning the result of `shuffle()`

Wrong:

```python
items = random.shuffle(items)
```

This makes `items` become `None`.

Correct:

```python
random.shuffle(items)
```

The list itself is modified.

---

## Mistake 9: Confusing scientific notation with complex numbers

This:

```python
35e3
```

is a `float`.

This:

```python
35j
```

is a `complex`.

---

# 13. Quick Revision Sheet

## Output

```python
print("Hello")
print("A", "B")
print("Hello", end=" ")
```

---

## Variables

```python
name = "Taqi"
age = 20

x, y, z = 1, 2, 3
```

Rules:

```text
✓ letters
✓ numbers after first character
✓ underscore
✗ cannot start with number
✗ cannot use keywords
✓ case-sensitive
```

---

## Data Types

```python
str
int
float
complex
list
tuple
range
dict
set
frozenset
bool
bytes
bytearray
memoryview
NoneType
```

Check type:

```python
type(value)
```

---

## Casting

```python
int()
float()
str()
```

---

## Conditions

```python
if condition:
    ...

elif condition:
    ...

else:
    ...
```

Ternary:

```python
x = a if condition else b
```

Match:

```python
match value:
    case 1:
        ...
    case _:
        ...
```

---

## Loops

```python
for x in iterable:
    ...
```

```python
while condition:
    ...
```

Control:

```python
break
continue
pass
```

Range:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

---

## Operators

### Arithmetic

```text
+  -  *  /  %  **  //
```

### Comparison

```text
==  !=  >  <  >=  <=
```

### Logical

```text
and  or  not
```

### Identity

```text
is  is not
```

### Membership

```text
in  not in
```

### Bitwise

```text
&  |  ^  ~  <<  >>
```

### Assignment

```text
=  +=  -=  *=  /=  %=  //=  **=
&= |= ^= >>= <<=
```

Walrus:

```text
:=
```

---

## User Input

```python
name = input("Enter name: ")
```

Remember:

```python
input()
```

returns a `str`.

Convert when necessary:

```python
age = int(input("Age: "))
price = float(input("Price: "))
```

---

# 🧠 Final Mental Model

When revising Python basics, remember this progression:

```text
OUTPUT
  ↓
VARIABLES
  ↓
DATA TYPES
  ↓
NUMBERS & CASTING
  ↓
OPERATORS
  ↓
USER INPUT
  ↓
CONDITIONS
  ↓
LOOPS
  ↓
RANDOM / MODULES
```

The fundamental programming flow is:

```text
Input
  ↓
Process
  ↓
Decision
  ↓
Repetition
  ↓
Output
```

Example:

```python
import math

number = float(input("Enter a number: "))

if number >= 0:
    result = math.sqrt(number)
    print(f"Square root = {result}")
else:
    print("Square root is not a real number")
```

This small program combines several fundamentals:

- module import
- user input
- type conversion
- variable
- conditional statement
- mathematical operation
- f-string
- output

---

# 🎯 What You Should Be Able to Do After This Chapter

Before moving to the next Python topic, make sure you can:

- [ ] Use `print()` and f-strings
- [ ] Write useful comments
- [ ] Create and name variables correctly
- [ ] Understand global and local variables
- [ ] Identify Python's basic data types
- [ ] Use `type()`
- [ ] Work with `int`, `float`, and `complex`
- [ ] Convert between common data types
- [ ] Generate random values
- [ ] Use `if`, `elif`, and `else`
- [ ] Use `match-case`
- [ ] Write `for` and `while` loops
- [ ] Use `break`, `continue`, and `pass`
- [ ] Use `range()`
- [ ] Understand operator categories
- [ ] Understand operator precedence
- [ ] Take input using `input()`
- [ ] Convert user input to numeric types
- [ ] Combine these concepts to solve small problems

---

## 📂 Related Practice Files

| # | File | Main Topics |
|---:|---|---|
| 01 | `01.output_comment.py` | `print()`, f-string, comments, `end` |
| 02 | `02.variables.py` | Variables, assignment, unpacking, scope |
| 03 | `03.datatype.py` | Built-in data types, `type()` |
| 04 | `04.numbers.py` | `int`, `float`, `complex`, numeric conversion |
| 05 | `05.random_number.py` | `random`, `choice`, `randrange`, `seed`, `shuffle`, `uniform` |
| 06 | `06.casting.py` | `int()`, `float()`, `str()` |
| 07 | `07.conditional_statement.py` | `if`, `elif`, `else`, ternary, `pass`, `match-case` |
| 08 | `08.loops.py` | `for`, `while`, `range`, `break`, `continue`, `pass` |
| 09 | `09.operators.py` | Arithmetic, assignment, comparison, logical, identity, membership, bitwise |
| 10 | `10.user_input.py` | `input()`, type conversion, `math.sqrt()` |

---

> **Revision tip:** Don't just read this README. After revising a topic, close the notes and try writing the examples yourself. Then modify them and create small problems from the same concept. That is where the actual Python skill develops.
