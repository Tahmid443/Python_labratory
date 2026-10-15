# 01. Python Fundamentals — Complete Notes 🐍

This chapter covers the fundamental concepts of Python programming, from printing output and declaring variables to data types, type conversion, operators, strings, and basic programming exercises.

These concepts form the foundation for learning Data Structures and Algorithms (DSA) and Competitive Programming.

## Table of Contents

1. [Hello World and Output](#1-hello-world-and-output)
2. [Comments and Docstrings](#2-comments-and-docstrings)
3. [Variables and Naming Conventions](#3-variables-and-naming-conventions)
4. [Python Data Types](#4-python-data-types)
5. [Type Conversion](#5-type-conversion)
6. [Input and Output](#6-input-and-output)
7. [Operators](#7-operators)
8. [String Basics](#8-string-basics)
9. [Basic Programming Exercises](#9-basic-programming-exercises)
10. [Important Python Concepts](#10-important-python-concepts)
11. [Practice Problems](#11-practice-problems)

---

## 1. Hello World and Output

**File:** `01_hello_world.py`

### 1.1 The `print()` Function

The `print()` function displays information on the screen.

```python
print("Hello, World!")
print("Welcome to Python!")
print(100)
print(10 + 20)
```

Output:

```text
Hello, World!
Welcome to Python!
100
30
```

The `print()` function can display strings, numbers, variables, and expressions.

### 1.2 Printing Multiple Values

You can pass multiple arguments to `print()`, separated by commas.

```python
print("Python", "is", "awesome")
```

Output:

```text
Python is awesome
```

By default, `print()` separates multiple arguments with a space.

### 1.3 The `sep` Parameter

The `sep` parameter specifies the separator between printed arguments.

```python
print("Python", "is", "awesome", sep="-")
print(10, 20, 30, sep=" | ")
```

Output:

```text
Python-is-awesome
10 | 20 | 30
```

### 1.4 The `end` Parameter

By default, `print()` ends with a newline character (`\n`). The `end` parameter changes what is printed at the end.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Another example:

```python
print("A", end="-")
print("B", end="-")
print("C")
```

Output:

```text
A-B-C
```

**Competitive programming tip:** Understanding `print()` is useful when formatting output exactly as required by a problem.

---

## 2. Comments and Docstrings

**File:** `02_comments.py`

Comments explain code to human readers. Python ignores ordinary comments during execution.

### 2.1 Single-Line Comments

Use `#` to write a comment.

```python
# This is a comment
print("Hello")  # This is also a comment
```

Comments are useful for explaining logic, assumptions, and non-obvious decisions.

### 2.2 Multiline Comments

Python does not have a dedicated multiline-comment syntax. You can write consecutive comments:

```python
# This is the first line.
# This is the second line.
# This is the third line.
```

Triple-quoted strings are also commonly used for multiline text, but they are not technically comments.

### 2.3 Docstrings

A docstring documents a module, class, or function. It is written as a string literal at the beginning of the relevant definition.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(2, 3))
```

Output:

```text
5
```

You can access a function's docstring using:

```python
print(add.__doc__)
```

Output:

```text
Return the sum of two numbers.
```

### 2.4 Writing Good Comments

Prefer comments that explain **why** something is necessary rather than repeating what the code already says.

```python
# Adjust the index because the input positions start from 1.
index = position - 1
```

Avoid unnecessary comments that merely restate simple operations.

### 2.5 The Main Guard

```python
if __name__ == "__main__":
    print("This file is running directly.")
```

This block executes when the file is run directly, rather than imported as a module.

---

## 3. Variables and Naming Conventions

**File:** `03_variables.py`

### 3.1 What Is a Variable?

A variable is a name that refers to an object in Python.

```python
name = "Alice"
age = 20
height = 5.6
is_student = True
```

Here, `name`, `age`, `height`, and `is_student` refer to objects of different types.

Python is dynamically typed, meaning you do not need to declare a variable's type explicitly.

```python
x = 10
print(x)

x = "Hello"
print(x)
```

Output:

```text
10
Hello
```

### 3.2 Multiple Assignment

You can assign values to multiple variables in one statement.

```python
x, y, z = 1, 2, 3
print(x, y, z)
```

Output:

```text
1 2 3
```

### 3.3 Assigning the Same Value

```python
a = b = c = 0
print(a, b, c)
```

All three names initially refer to the same object, which is safe here because integers are immutable.

### 3.4 Swapping Variables

Python supports swapping without a temporary variable.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output:

```text
20 10
```

This is particularly useful in sorting algorithms.

### 3.5 Naming Rules

Valid variable names:

```python
first_name = "John"
age2 = 20
_private_value = 100
```

Invalid variable names:

```python
# 2age = 20       # Cannot start with a digit
# first-name = "" # Hyphens are not allowed
# class = "A"     # Reserved keyword
```

### 3.6 Naming Conventions

Following PEP 8 makes Python code more readable.

| Purpose | Convention | Example |
|---|---|---|
| Variables | `snake_case` | `first_name` |
| Functions | `snake_case` | `calculate_sum()` |
| Constants | `UPPER_CASE` | `MAX_SIZE` |
| Classes | `PascalCase` | `StudentRecord` |

Python does not enforce constants through uppercase naming; it is a convention indicating that a value should not be reassigned.

---

## 4. Python Data Types

**File:** `04_data_types.py`

A data type describes the kind of object a variable refers to and the operations supported by that object.

### 4.1 Numeric Types

**Integer (`int`)**

Represents whole numbers.

```python
age = 20
negative = -15
large_number = 10 ** 100

print(type(age))
```

Python integers have arbitrary precision, subject to available memory.

**Floating-point (`float`)**

Represents numbers with fractional parts.

```python
price = 19.99
temperature = -2.5
```

Floating-point values are usually stored with finite binary precision. Therefore, some decimal calculations may not be exact.

**Complex (`complex`)**

Represents numbers with real and imaginary parts.

```python
z = 2 + 3j

print(z.real)
print(z.imag)
```

Output:

```text
2.0
3.0
```

### 4.2 String (`str`)

Strings represent text.

```python
name = "Python"
message = 'Hello World'
```

Strings are immutable sequences of Unicode characters.

### 4.3 Boolean (`bool`)

Boolean values represent truth values.

```python
is_valid = True
is_finished = False
```

The two Boolean values are `True` and `False`, with capital initial letters.

### 4.4 None (`NoneType`)

`None` represents the absence of a value.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

It is commonly used to represent missing values or the absence of a meaningful result.

### 4.5 Collection Types

**List (`list`)** — ordered and mutable.

```python
numbers = [10, 20, 30]
numbers.append(40)
```

**Tuple (`tuple`)** — ordered and immutable.

```python
coordinates = (10, 20)
```

**Set (`set`)** — stores unique elements.

```python
unique_numbers = {1, 2, 2, 3}
print(unique_numbers)
```

Output:

```text
{1, 2, 3}
```

Sets do not guarantee a particular iteration order.

**Dictionary (`dict`)** — stores key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 20
}

print(student["name"])
```

Output:

```text
Alice
```

### 4.6 Checking Data Types

Use `type()` to inspect an object's type.

```python
x = 42
print(type(x))
```

Output:

```text
<class 'int'>
```

Use `isinstance()` to check whether an object belongs to a type or its subclasses.

```python
print(isinstance(42, int))       # True
print(isinstance(3.14, int))    # False
print(isinstance(True, int))    # True
```

**Important:** In Python, `bool` is a subclass of `int`. This explains why `isinstance(True, int)` returns `True`.

---

## 5. Type Conversion

**File:** `05_type_conversion.py`

Type conversion changes a value from one type to another.

There are two main forms: implicit conversion and explicit conversion.

### 5.1 Implicit Conversion

Python automatically converts certain values when an operation requires it.

```python
result = 5 + 3.14

print(result)
print(type(result))
```

Output:

```text
8.14
<class 'float'>
```

Here, the integer participates in an operation that produces a floating-point result.

### 5.2 Explicit Conversion

You can explicitly convert values using functions such as `int()`, `float()`, `str()`, and `bool()`.

```python
text = "42"

number = int(text)
decimal = float(text)

print(number)
print(decimal)
```

Output:

```text
42
42.0
```

Common conversions:

| Function | Purpose | Example |
|---|---|---|
| `int(x)` | Convert to integer when valid | `int("25")` |
| `float(x)` | Convert to floating point | `float("3.5")` |
| `str(x)` | Convert to string representation | `str(100)` |
| `bool(x)` | Convert to Boolean | `bool(1)` |
| `list(x)` | Create a list from an iterable | `list("abc")` |
| `tuple(x)` | Create a tuple from an iterable | `tuple([1, 2])` |
| `set(x)` | Create a set from an iterable | `set([1, 1, 2])` |

### 5.3 Converting Numbers to Strings

```python
number = 100
print("Number: " + str(number))
```

Output:

```text
Number: 100
```

Alternatively, use an f-string:

```python
print(f"Number: {number}")
```

### 5.4 Truthiness and Boolean Conversion

Values such as `0`, `0.0`, `""`, `[]`, `{}`, `set()`, and `None` are false-like.

Most other objects are true-like.

```python
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False
print(bool(1))       # True
print(bool("hello")) # True
```

An empty collection is false-like, but a collection containing elements is true-like.

### 5.5 Handling Conversion Errors

Invalid conversions may raise a `ValueError`.

```python
try:
    number = int("hello")
except ValueError:
    print("Invalid integer input.")
```

This is useful when processing input that may not contain a valid number.

### 5.6 Rounding and Truncation

```python
print(round(3.14159, 2))
print(int(3.99))
```

Output:

```text
3.14
3
```

`round()` rounds a number according to Python's rounding rules. `int()` truncates the fractional part toward zero.

For example:

```python
print(int(-3.99))
```

Output:

```text
-3
```

Do not confuse truncation with mathematical floor, which rounds toward negative infinity.

---

## 6. Input and Output

**File:** `06_input_output.py`

### 6.1 Basic Output

Use `print()` to display information.

```python
print("Hello", "World", sep=", ", end="!\n")
```

Output:

```text
Hello, World!
```

### 6.2 Formatted Output with f-Strings

F-strings allow expressions and variables to be embedded inside strings.

```python
name = "Alice"
age = 20

print(f"Name: {name}, Age: {age}")
```

Output:

```text
Name: Alice, Age: 20
```

You can also format numeric values.

```python
pi = 3.14159265
print(f"Pi = {pi:.2f}")
```

Output:

```text
Pi = 3.14
```

The `.2f` format specifies two digits after the decimal point.

### 6.3 Reading User Input

The `input()` function reads a line of text and returns it as a string.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Even when the user types a number, `input()` returns a string.

### 6.4 Converting Input to Numbers

```python
age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1}.")
```

For decimal input:

```python
height = float(input("Enter your height: "))
```

### 6.5 Reading Multiple Values

Suppose the user enters two integers on one line:

```text
10 20
```

Read them using:

```python
a, b = map(int, input().split())
print(a + b)
```

Explanation:

1. `input()` reads a line.
2. `.split()` separates the line into whitespace-delimited strings.
3. `map(int, ...)` converts the strings to integers.
4. Multiple assignment stores the resulting integers in `a` and `b`.

This is a common pattern in competitive programming.

### 6.6 Reading a List of Integers

```python
numbers = list(map(int, input().split()))
print(numbers)
```

Input:

```text
1 2 3 4 5
```

Output:

```text
[1, 2, 3, 4, 5]
```

### 6.7 Fast Input for Competitive Programming

For problems with large input, Python programmers often use:

```python
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
```

This can be faster than the built-in `input()` for large inputs.

**Note:** If you use `sys.stdin.readline()` to read text, it generally retains the trailing newline. Use `.strip()` when necessary, but avoid stripping blindly if whitespace is meaningful.

---

## 7. Operators

**File:** `07_operators.py`

Operators perform operations on values and variables.

### 7.1 Arithmetic Operators

Let `a = 10` and `b = 3`.

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `a + b` | 13 |
| `-` | Subtraction | `a - b` | 7 |
| `*` | Multiplication | `a * b` | 30 |
| `/` | True division | `a / b` | 3.333... |
| `//` | Floor division | `a // b` | 3 |
| `%` | Modulo | `a % b` | 1 |
| `**` | Exponentiation | `a ** b` | 1000 |

**Important distinction:**

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(-7 // 2)  # -4
```

Floor division rounds down toward negative infinity, not toward zero.

The modulo operator returns the remainder according to Python's division rules:

```python
print(7 % 3)    # 1
print(-7 % 3)   # 2
```

### 7.2 Comparison Operators

Comparison operators return Boolean results.

```python
a = 5
b = 3

print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True
print(a >= 5)  # True
print(b <= 3)  # True
```

Common operators:

- `==` — equal to
- `!=` — not equal to
- `>` — greater than
- `<` — less than
- `>=` — greater than or equal to
- `<=` — less than or equal to

Do not confuse `=` (assignment) with `==` (comparison).

### 7.3 Logical Operators

Python has three main logical operators.

**`and`** — true when both operands are true-like.

```python
print(True and False)  # False
```

**`or`** — true when at least one operand is true-like.

```python
print(True or False)  # True
```

**`not`** — reverses a truth value.

```python
print(not True)  # False
```

Example:

```python
age = 20

if age >= 18 and age <= 60:
    print("Eligible")
```

Python also supports chained comparisons:

```python
if 18 <= age <= 60:
    print("Eligible")
```

### 7.4 Assignment Operators

Assignment operators update variables.

```python
x = 5

x += 3   # x = x + 3
x -= 1   # x = x - 1
x *= 2   # x = x * 2
x //= 3  # x = x // 3
x **= 2  # x = x ** 2

print(x)
```

These operators are frequently used in loops, counters, and algorithm implementations.

### 7.5 Identity Operators

The operators `is` and `is not` test whether two references point to the same object.

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print(a == c)  # True
```

- `is` checks object identity.
- `==` checks value equality.

Use `is None` to check whether a value is `None`:

```python
result = None

if result is None:
    print("No result")
```

### 7.6 Membership Operators

`in` and `not in` check whether a value belongs to a collection or appears in a sequence.

```python
print(2 in [1, 2, 3])         # True
print(4 not in [1, 2, 3])     # True
print("py" in "python")       # True
```

Membership testing in a list generally requires linear time, while set and dictionary membership are typically average-case constant time.

This difference is important in DSA.

### 7.7 Bitwise Operators

Bitwise operators manipulate the binary representation of integers.

Consider:

```text
5 = 101
3 = 011
```

**AND (`&`)** — a bit is set if both corresponding bits are set.

```python
print(5 & 3)  # 1
```

**OR (`|`)** — a bit is set if either corresponding bit is set.

```python
print(5 | 3)  # 7
```

**XOR (`^`)** — a bit is set if the corresponding bits differ.

```python
print(5 ^ 3)  # 6
```

**NOT (`~`)** — inverts the integer's bits according to Python's integer representation rules.

```python
print(~5)  # -6
```

For Python integers, `~n` equals `-n - 1`.

**Left shift (`<<`)** — shifts bits to the left.

```python
print(5 << 1)  # 10
```

**Right shift (`>>`)** — shifts bits to the right.

```python
print(5 >> 1)  # 2
```

Bitwise operations are useful in competitive programming problems involving masks, subsets, and low-level integer operations.

---

## 8. String Basics

**File:** `08_string_basics.py`

A string (`str`) is an immutable sequence of Unicode characters.

### 8.1 Creating Strings

Strings can use single quotes, double quotes, or triple quotes.

```python
s1 = "Hello"
s2 = 'World'
s3 = """A multiline
string"""
```

Triple-quoted strings can span multiple lines.

### 8.2 String Concatenation

The `+` operator joins strings.

```python
first = "Hello"
second = "World"

print(first + ", " + second)
```

Output:

```text
Hello, World
```

### 8.3 String Repetition

The `*` operator repeats a string.

```python
print("ab" * 3)
```

Output:

```text
ababab
```

### 8.4 String Length

Use `len()` to get the number of Unicode code points in a string.

```python
s = "Python"
print(len(s))
```

Output:

```text
6
```

### 8.5 String Indexing

Python uses zero-based indexing.

```python
s = "Python"

print(s[0])   # P
print(s[1])   # y
print(s[-1])  # n
print(s[-2])  # o
```

Positive indexing starts at zero. Negative indexing starts from the end, with `-1` referring to the last character.

### 8.6 String Slicing

General syntax:

```python
string[start:stop:step]
```

The `start` index is included, while the `stop` index is excluded.

```python
s = "Python"

print(s[1:4])  # yth
print(s[:3])   # Pyt
print(s[2:])   # thon
print(s[::2])  # Pto
print(s[::-1]) # nohtyP
```

Slicing is useful for extracting substrings and reversing strings.

### 8.7 Iterating Over Strings

```python
s = "Python"

for ch in s:
    print(ch)
```

This processes one character at a time.

### 8.8 String Immutability

Strings cannot be modified in place.

```python
s = "Python"

# s[0] = "J"  # Raises TypeError

s = "J" + s[1:]
print(s)
```

Output:

```text
Jython
```

The second example creates a new string and reassigns the variable.

### 8.9 Escape Sequences

Escape sequences represent special characters.

| Sequence | Meaning |
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
print("Quote: \"Hello\"")
```

### 8.10 Raw Strings

A raw string treats most backslashes as literal characters.

```python
path = r"C:\Users\name"
print(path)
```

Raw strings are useful for Windows paths and regular expressions. A raw string literal cannot end with an odd number of backslashes.

### 8.11 Useful String Methods

```python
s = "  Hello Python  "

print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("Python", "World"))
print(s.split())
```

Common methods:

- `lower()` — returns a lowercase string.
- `upper()` — returns an uppercase string.
- `strip()` — removes leading and trailing whitespace.
- `replace(old, new)` — replaces occurrences of a substring.
- `split()` — splits a string into a list.
- `find(sub)` — returns the first matching index, or `-1`.
- `startswith(prefix)` — checks the beginning of a string.
- `endswith(suffix)` — checks the end of a string.

**Important:** String methods generally return new strings because strings are immutable.

---

## 9. Basic Programming Exercises

**File:** `09_basic_exercises.py`

These exercises combine the concepts covered in this chapter.

### 9.1 Calculate the Area of a Circle

Formula:

\[
A = \pi r^2
\]

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(5))
```

The function uses `math.pi` and the exponentiation operator.

### 9.2 Convert Celsius to Fahrenheit

Formula:

\[
F = \frac{9}{5}C + 32
\]

```python
def c_to_f(celsius):
    return (celsius * 9 / 5) + 32

print(c_to_f(25))
```

Output:

```text
77.0
```

### 9.3 Swap Two Values

```python
def swap(a, b):
    return b, a

x, y = swap(10, 20)
print(x, y)
```

Output:

```text
20 10
```

Python packs the returned values into a tuple, which can then be unpacked.

### 9.4 Sum the Digits of an Integer

```python
def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print(sum_digits(12345))
```

Output:

```text
15
```

The function converts the absolute value to a string, converts each character back to an integer, and sums the digits.

### 9.5 Reverse an Integer

```python
def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

print(reverse_number(12345))
print(reverse_number(-123))
```

Output:

```text
54321
-321
```

This implementation preserves the sign but does not preserve leading zeros in the reversed result.

### 9.6 Check Even or Odd

```python
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(7))
```

An integer is even when its remainder after division by two is zero.

### 9.7 Find the Maximum of Three Numbers

```python
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(10, 25, 15))
```

Output:

```text
25
```

The built-in `max()` function returns the largest value.

### 9.8 Calculate BMI

Formula:

\[
BMI = \frac{\text{weight in kilograms}}{(\text{height in metres})^2}
\]

```python
def bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("Height must be positive.")

    return weight_kg / (height_m ** 2)

print(f"{bmi(70, 1.75):.2f}")
```

Output:

```text
22.86
```

The validation prevents division by zero and rejects negative heights.

---

## 10. Important Python Concepts

### 10.1 Mutable vs Immutable Objects

| Mutable | Immutable |
|---|---|
| `list` | `int` |
| `dict` | `float` |
| `set` | `bool` |
| | `str` |
| | `tuple` (when its elements are immutable) |

Mutable objects can be modified after creation. Immutable objects cannot be changed in place.

### 10.2 Common Errors

| Error | Typical cause |
|---|---|
| `SyntaxError` | Invalid Python syntax |
| `NameError` | Using a name that has not been defined |
| `TypeError` | Performing an unsupported operation for a type |
| `ValueError` | A value has the correct general type but is invalid for the operation |
| `IndexError` | Accessing an invalid sequence index |
| `ZeroDivisionError` | Dividing by zero |

Learning to read error messages is an important programming skill.

### 10.3 Complexity Awareness

Some common operations have different time costs:

| Operation | Typical time complexity |
|---|---|
| List indexing | \(O(1)\) |
| List append | Amortized \(O(1)\) |
| List membership (`x in list`) | \(O(n)\) |
| Set membership | Average \(O(1)\) |
| Dictionary key lookup | Average \(O(1)\) |
| String slicing of length \(k\) | \(O(k)\) |

These are typical complexities, not guarantees for every possible implementation or input.

Understanding these differences will help when studying DSA.

---

## 11. Practice Problems

Try solving these independently before checking online solutions.

### Beginner Level

- [ ] Print your name, age, and country on separate lines.
- [ ] Read two integers and print their sum, difference, product, and quotient.
- [ ] Convert a temperature from Celsius to Fahrenheit.
- [ ] Swap two variables without using a third variable.
- [ ] Check whether a number is positive, negative, or zero.
- [ ] Determine whether an integer is even or odd.
- [ ] Calculate the area and circumference of a circle.
- [ ] Find the largest of three numbers.

### Strings

- [ ] Count the characters in a string.
- [ ] Reverse a string using slicing.
- [ ] Check whether a string is a palindrome.
- [ ] Count the vowels in a string.
- [ ] Convert a string to uppercase and lowercase.
- [ ] Count the number of words in a sentence.
- [ ] Remove leading and trailing whitespace.
- [ ] Count how many times a given character appears.

### Numbers and Logic

- [ ] Calculate the sum of the digits of an integer.
- [ ] Reverse an integer while preserving its sign.
- [ ] Determine whether a number is divisible by both 3 and 5.
- [ ] Convert seconds into hours, minutes, and seconds.
- [ ] Calculate the factorial of a non-negative integer.
- [ ] Check whether a number is prime.
- [ ] Find the greatest common divisor of two integers.

### Competitive Programming Preparation

- [ ] Read an integer `n` and then read `n` integers.
- [ ] Find the sum and maximum of a list of integers.
- [ ] Count the even and odd numbers in a list.
- [ ] Find the second-largest distinct value in a list.
- [ ] Remove duplicates from a list.
- [ ] Understand the difference between list, tuple, set, and dictionary.
- [ ] Solve five beginner problems using only input, output, variables, operators, and strings.

---

## Final Revision Checklist

Before moving on to conditional statements and loops, make sure you can:

- [ ] Use `print()` with `sep` and `end`.
- [ ] Explain comments, docstrings, and the main guard.
- [ ] Create variables and follow Python naming conventions.
- [ ] Identify Python's built-in data types.
- [ ] Convert values safely between types.
- [ ] Read one or multiple values from input.
- [ ] Use arithmetic, comparison, logical, identity, membership, and bitwise operators.
- [ ] Index, slice, iterate over, and reverse strings.
- [ ] Write reusable functions for simple mathematical problems.
- [ ] Recognize common exceptions and debug basic errors.

**Next topic:** Conditional Statements and Loops — `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, and `range()`.

**Study strategy:** Read the explanation, run the corresponding Python file, modify the examples, and solve the practice problems without copying solutions. Understanding the logic matters more than memorizing the syntax.
