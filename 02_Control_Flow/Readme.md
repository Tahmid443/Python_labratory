# 02. Control Flow in Python — Complete Notes

Control flow determines the order in which a program executes its statements. It allows a program to make decisions, repeat instructions, skip iterations, and stop execution when necessary.

This chapter covers conditional statements, loops, loop control statements, and practical problem-solving techniques.

## Table of Contents

1. [Conditional Statements](#1-conditional-statements)
2. [Nested Conditions](#2-nested-conditions)
3. [For Loops](#3-for-loops)
4. [While Loops](#4-while-loops)
5. [Break, Continue, and Pass](#5-break-continue-and-pass)
6. [Loop Else](#6-loop-else)
7. [Practice Programs](#7-practice-programs)
8. [Common Mistakes](#8-common-mistakes)
9. [Time Complexity](#9-time-complexity)
10. [Practice Problems](#10-practice-problems)

---

## 1. Conditional Statements

**File:** `01_if_elif_else.py`

Conditional statements allow a program to execute different blocks of code depending on whether conditions are true or false.

### 1.1 The `if` Statement

The `if` statement executes a block when its condition evaluates to `True`.

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

Output:

```text
You are an adult.
```

Syntax:

```python
if condition:
    # Code executed when condition is True
```

Python uses indentation to define blocks. Four spaces per indentation level is the standard convention.

### 1.2 The `if-else` Statement

Use `else` to specify what happens when the condition is false.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

The modulo operator `%` returns the remainder after division. An integer is even if its remainder when divided by two is zero.

### 1.3 The `if-elif-else` Statement

Use `elif` when several mutually exclusive conditions need to be checked in sequence.

```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(grade(85))
```

Output:

```text
B
```

**How it works:**

1. Python checks `score >= 90`.
2. If false, it checks `score >= 80`.
3. If true, it returns `"B"`.
4. The remaining conditions are skipped.

Only the first matching branch executes.

**Important:** The order of conditions matters. Check more restrictive conditions before broader ones.

### 1.4 Checking Positive, Negative, or Zero

```python
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))
print(check_number(-3))
print(check_number(0))
```

Output:

```text
Positive
Negative
Zero
```

The three conditions cover all possible real-number cases.

### 1.5 The Ternary Conditional Expression

A conditional expression is a compact way to choose between two values.

Syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
def is_adult(age):
    return "Adult" if age >= 18 else "Minor"

print(is_adult(20))
print(is_adult(15))
```

Output:

```text
Adult
Minor
```

This is useful for simple decisions. Use a regular `if-else` statement when the logic becomes complicated.

### 1.6 Truthy and Falsy Values

Conditions do not have to contain explicit comparisons.

```python
name = "Alice"

if name:
    print("Name is not empty.")
```

Common falsy values include:

- `False`
- `None`
- `0` and `0.0`
- `""`
- `[]`
- `{}`
- `set()`

Most other values are truthy.

---

## 2. Nested Conditions

**File:** `02_nested_conditions.py`

A nested condition is an `if`, `elif`, or `else` statement inside another conditional block.

Nested conditions are useful when a decision depends on multiple stages of validation.

### 2.1 Basic Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("You are underage.")
```

Output:

```text
Entry allowed.
```

The inner condition is evaluated only if the outer condition is true.

### 2.2 Classifying a Triangle

A valid triangle must satisfy all three triangle inequalities:

\[
a+b>c,\qquad a+c>b,\qquad b+c>a
\]

After checking validity, classify the triangle by its sides:

- **Equilateral:** All three sides are equal.
- **Isosceles:** Exactly two sides are equal, or at least two are equal under the common inclusive definition.
- **Scalene:** All three sides are different.

```python
def classify_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"

    return "Not a triangle"
```

The supplied function assumes positive side lengths. A more defensive implementation validates them first:

```python
def classify_triangle(a, b, c):
    if min(a, b, c) <= 0:
        return "Not a triangle"

    if not (a + b > c and a + c > b and b + c > a):
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
```

### 2.3 Nested Conditions for Login Logic

```python
def login(username, password, is_admin=False):
    if username and password:
        if len(password) >= 8:
            if is_admin:
                return "Admin access granted"
            return "User access granted"

        return "Password too short"

    return "Missing credentials"
```

The program performs several checks:

1. Check that both credentials are non-empty.
2. Check the password length.
3. Choose the response based on the admin flag.

**Security note:** This is only a control-flow demonstration. Real authentication requires password verification, secure credential storage, and authorization checks.

### 2.4 Nested Conditions vs. Logical Operators

Sometimes nested conditions can be simplified.

Nested form:

```python
if age >= 18:
    if has_id:
        print("Entry allowed.")
```

Combined form:

```python
if age >= 18 and has_id:
    print("Entry allowed.")
```

Use `and` when both conditions must be true. Use nesting when the second decision should happen only after the first succeeds or when each stage needs its own response.

---

## 3. For Loops

**File:** `03_for_loops.py`

A `for` loop iterates over the items of an iterable, such as a list, tuple, string, set, dictionary, or range.

### 3.1 Basic `for` Loop

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

`range(5)` generates the integers from `0` through `4`. The stop value `5` is excluded.

### 3.2 Understanding `range()`

General syntax:

```python
range(start, stop, step)
```

- `start`: First value; defaults to `0`.
- `stop`: Exclusive upper boundary.
- `step`: Increment or decrement; defaults to `1`.

Examples:

```python
for i in range(1, 6):
    print(i, end=" ")

print()

for i in range(1, 10, 2):
    print(i, end=" ")

print()

for i in range(5, 0, -1):
    print(i, end=" ")
```

Output:

```text
1 2 3 4 5
1 3 5 7 9
5 4 3 2 1
```

A negative step produces a descending sequence when the starting and stopping values are appropriate.

### 3.3 Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Python assigns each element to `fruit` in sequence.

This is generally preferable to manually accessing each element by index when the index is unnecessary.

### 3.4 Iterating with an Index Using `enumerate()`

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:

```text
0: apple
1: banana
2: cherry
```

To start counting from `1`:

```python
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Use `enumerate()` instead of manually maintaining a counter when both the index and element are needed.

### 3.5 Iterating Over a Dictionary

Iterating directly over a dictionary produces its keys.

```python
person = {"name": "Alice", "age": 30}

for key in person:
    print(key, person[key])
```

To access keys and values together, use `.items()`:

```python
for key, value in person.items():
    print(f"{key} = {value}")
```

### 3.6 Nested Loops

A nested loop is a loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end="\t")
    print()
```

The outer loop runs three times. For each outer iteration, the inner loop runs three times.

Therefore, the inner loop executes \(3\times3=9\) times.

Nested loops are useful for:

- Multiplication tables.
- Matrix operations.
- Pattern printing.
- Comparing pairs of elements.

### 3.7 Pattern Printing

```python
for i in range(1, 5):
    print("*" * i)
```

Output:

```text
*
**
***
****
```

The string repetition operator repeats `"*"` exactly `i` times.

---

## 4. While Loops

**File:** `04_while_loops.py`

A `while` loop repeats a block as long as its condition remains true.

### 4.1 Basic `while` Loop

```python
count = 0

while count < 5:
    print(count, end=" ")
    count += 1
```

Output:

```text
0 1 2 3 4
```

Execution process:

1. Check whether `count < 5`.
2. Execute the loop body if true.
3. Increase `count` by one.
4. Return to the condition.
5. Stop when the condition becomes false.

### 4.2 Infinite Loops and `break`

```python
n = 1

while True:
    if n > 5:
        break

    print(n, end=" ")
    n += 1
```

Output:

```text
1 2 3 4 5
```

`while True` creates a loop whose condition is always true. A `break` statement is needed to exit this loop.

Be careful: forgetting the exit condition can produce an infinite loop.

### 4.3 Calculating Factorial

For a non-negative integer \(n\):

\[
n!=n(n-1)(n-2)\cdots 1
\]

By convention, \(0!=1\).

```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")

    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result

print(factorial(5))
```

Output:

```text
120
```

Dry run for `factorial(4)`:

| Iteration | `n` | `result` |
|---|---:|---:|
| Initial | 4 | 1 |
| 1 | 3 | 4 |
| 2 | 2 | 12 |
| 3 | 1 | 24 |
| 4 | 0 | 24 |

Time complexity: \(O(n)\).

Space complexity: \(O(1)\), excluding the space needed to represent the growing integer result.

### 4.4 Generating Fibonacci Numbers

The Fibonacci sequence starts with:

\[
0,1,1,2,3,5,8,13,\ldots
\]

Each term after the first two is the sum of the previous two terms.

```python
def fib(n):
    a, b = 0, 1

    while n > 0:
        a, b = b, a + b
        n -= 1

    return a
```

This function returns the \(n\)-th Fibonacci number using zero-based indexing.

Examples:

```python
print(fib(0))  # 0
print(fib(1))  # 1
print(fib(5))  # 5
print(fib(10)) # 55
```

The assignment `a, b = b, a + b` updates both values using the values on the right-hand side before assignment.

Time complexity: \(O(n)\) arithmetic operations. The integers grow in size, so their arithmetic cost also grows for large `n`.

### 4.5 The Collatz Sequence

For a positive integer \(n\), repeatedly apply these rules:

- If \(n\) is even, replace it with \(n//2\).
- If \(n\) is odd and greater than `1`, replace it with \(3n+1\).
- Stop when \(n=1\).

```python
def collatz(n):
    if n < 1:
        raise ValueError("n must be positive")

    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps
```

Example:

```python
print(collatz(6))
```

Sequence:

```text
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

The sequence takes eight steps to reach `1`.

The Collatz conjecture states that this process eventually reaches `1` for every positive integer. This remains an unproven mathematical conjecture.

---

## 5. Break, Continue, and Pass

**File:** `05_break_continue_pass.py`

These statements change how Python executes a block of code.

### 5.1 `break`

`break` immediately terminates the nearest enclosing loop.

```python
for i in range(10):
    if i == 5:
        break

    print(i, end=" ")
```

Output:

```text
0 1 2 3 4
```

The loop ends when `i` becomes `5`, so `5` is not printed.

### 5.2 `continue`

`continue` skips the rest of the current iteration and moves to the next iteration.

```python
for i in range(10):
    if i % 2 == 0:
        continue

    print(i, end=" ")
```

Output:

```text
1 3 5 7 9
```

Even numbers are skipped.

### 5.3 `pass`

`pass` does nothing. It serves as a placeholder when Python syntax requires a statement.

```python
def future_function():
    pass

class EmptyClass:
    pass
```

It is useful when developing a program gradually.

**Remember:**

| Statement | Purpose |
|---|---|
| `break` | Exit the nearest enclosing loop |
| `continue` | Skip to the next iteration |
| `pass` | Do nothing |

### 5.4 Searching with Early Exit

```python
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n

    return None
```

Example:

```python
print(find_first_even([1, 3, 5, 4, 7]))
```

Output:

```text
4
```

The function stops as soon as it finds an even number. Here, `return` exits the function itself, which also terminates the loop.

### 5.5 Skipping Invalid Values

```python
def process(values):
    total = 0

    for value in values:
        if not isinstance(value, (int, float)):
            continue

        total += value

    return total
```

Example:

```python
print(process([1, "a", 2, None, 3]))
```

Output:

```text
6
```

The function skips values that are neither integers nor floats. Since `bool` is a subclass of `int`, Boolean values also pass this particular check.

---

## 6. Loop Else

**File:** `06_loop_else.py`

Python allows `else` to be attached to a `for` or `while` loop.

The loop's `else` block executes if the loop finishes normally without encountering a `break`.

This is different from the `else` block associated with an `if` statement.

### 6.1 `for-else`

```python
for i in range(5):
    print(i)
else:
    print("Loop completed.")
```

The message is printed because the loop finishes without `break`.

Now consider:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed.")
```

The `else` block does not execute because the loop terminates through `break`.

**Important:** `continue` does not prevent the loop's `else` block from executing. Only a `break` that exits that loop prevents it.

### 6.2 Finding a Prime Number

A prime number is an integer greater than `1` with exactly two positive divisors: `1` and itself.

The following function finds the first prime number in an iterable:

```python
def find_prime(numbers):
    for n in numbers:
        if n < 2:
            continue

        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                break
        else:
            return n

    return None
```

Example:

```python
print(find_prime([4, 6, 8, 9, 11, 15]))
```

Output:

```text
11
```

How it works:

1. Skip numbers less than `2`.
2. Try dividing each remaining number by integers starting at `2`.
3. Stop checking the candidate when a divisor is found.
4. If the inner loop completes without `break`, the candidate is prime.
5. Return the first prime found.

Why check divisors only up to the square root?

If a composite number \(n\) has a factor greater than \(\sqrt n\), it must also have a corresponding factor smaller than \(\sqrt n\).

This reduces the divisor-checking time to \(O(\sqrt n)\) per candidate.

### 6.3 `while-else`

```python
def search(items, target):
    i = 0

    while i < len(items):
        if items[i] == target:
            print(f"Found at {i}")
            break

        i += 1
    else:
        print("Not found")
```

Example:

```python
search([1, 2, 3, 4], 3)
search([1, 2, 3, 4], 10)
```

Output:

```text
Found at 2
Not found
```

The first call finds the target and executes `break`. The second reaches the end without `break`, so the `else` block runs.

---

## 7. Practice Programs

**File:** `07_practice.py`

This file combines conditionals, loops, functions, and arithmetic.

### 7.1 FizzBuzz

Print numbers from `1` to `n` with the following rules:

- Multiples of `3`: print `Fizz`.
- Multiples of `5`: print `Buzz`.
- Multiples of both `3` and `5`: print `FizzBuzz`.
- Otherwise, print the number.

```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```

**Why check divisibility by 15 first?**

Because a number divisible by both `3` and `5` is divisible by `15`. If you check divisibility by `3` first, multiples of `15` will print `Fizz` instead of `FizzBuzz`.

Time complexity: \(O(n)\).

### 7.2 Checking Whether a Number Is Prime

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
```

Examples:

```python
print(is_prime(2))   # True
print(is_prime(9))   # False
print(is_prime(17))  # True
```

The function returns `False` immediately when it finds a divisor.

Time complexity: \(O(\sqrt n)\) for \(n\ge2\).

### 7.3 Listing Prime Numbers

```python
def print_primes(limit):
    return [
        n for n in range(2, limit + 1)
        if is_prime(n)
    ]
```

Example:

```python
print(print_primes(30))
```

Output:

```text
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

This returns a list; it does not directly print each prime.

For a limit \(L\), the simple implementation performs roughly \(O(L\sqrt L)\) trial-division work in the worst-case upper-bound analysis.

For much larger limits, the Sieve of Eratosthenes is usually more efficient.

### 7.4 Multiplication Table

```python
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()
```

The format specifier `:4` reserves a field width of four characters, helping align the output.

There are two nested loops, each running `n` times.

Time complexity: \(O(n^2)\).

### 7.5 Pyramid Pattern

```python
def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
```

For `pyramid(5)`, the output is:

```text
    *
   ***
  *****
 *******
*********
```

At row `i`:

- Leading spaces: `n - i`
- Stars: `2 * i - 1`

This creates a centered pyramid with an odd number of stars on every row.

The number of characters printed across all rows is \(O(n^2)\).

---

## 8. Common Mistakes

### Mistake 1: Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

### Mistake 2: Using `=` Instead of `==`

Incorrect:

```python
# if x = 5:
#     print("Equal")
```

Correct:

```python
if x == 5:
    print("Equal")
```

`=` assigns a value, while `==` compares values.

### Mistake 3: Off-by-One Errors in `range()`

```python
for i in range(1, 5):
    print(i)
```

This prints `1`, `2`, `3`, and `4`, not `5`.

Use `range(1, 6)` when you want to include `5`.

### Mistake 4: Forgetting to Update a `while` Loop Variable

Incorrect:

```python
# count = 0
# while count < 5:
#     print(count)
```

The condition never becomes false because `count` is never updated.

Correct:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Mistake 5: Confusing `break` and `continue`

- `break` terminates the nearest enclosing loop.
- `continue` skips the current iteration and proceeds to the next one.

### Mistake 6: Misunderstanding Loop `else`

A loop's `else` block is not simply an alternative that runs when the loop's body does not execute. It runs when the loop terminates normally without `break`.

### Mistake 7: Checking Prime Numbers Incorrectly

Numbers below `2` are not prime. Also, checking divisors only up to `int(n ** 0.5)` requires including the square-root boundary when it is an integer.

The expression `range(2, int(n ** 0.5) + 1)` handles this boundary correctly for ordinary-sized positive integers.

---

## 9. Time Complexity

Time complexity describes how the amount of work grows as the input size increases.

| Operation | Typical time complexity |
|---|---|
| Single conditional check | \(O(1)\) |
| Loop over `n` elements | \(O(n)\) |
| Two nested loops of size `n` | \(O(n^2)\) |
| Factorial loop | \(O(n)\) arithmetic operations |
| Fibonacci loop | \(O(n)\) arithmetic operations |
| Trial-division prime check | \(O(\sqrt n)\) |
| FizzBuzz up to `n` | \(O(n)\) |
| Multiplication table of size `n × n` | \(O(n^2)\) |

These estimates count elementary operations. For arbitrary-precision integers, arithmetic operations can become more expensive as the numbers grow.

---

## 10. Practice Problems

Solve these problems without copying the implementations above.

### Beginner

- [ ] Check whether an integer is positive, negative, or zero.
- [ ] Check whether a number is even or odd.
- [ ] Find the largest of three numbers.
- [ ] Assign a grade based on a score.
- [ ] Check whether a year is a leap year.
- [ ] Check whether a character is a vowel or consonant.

### Loops

- [ ] Print integers from `1` to `n`.
- [ ] Print integers from `n` down to `1`.
- [ ] Calculate the sum of the first `n` positive integers.
- [ ] Calculate the factorial of `n`.
- [ ] Print a multiplication table.
- [ ] Count the digits of an integer.
- [ ] Reverse an integer.
- [ ] Find the sum of the digits of an integer.

### Problem-Solving

- [ ] Print FizzBuzz from `1` to `n`.
- [ ] Check whether a number is prime.
- [ ] Print all primes up to `n`.
- [ ] Find the first even number in a list.
- [ ] Search for an element and report its index.
- [ ] Print a right-angled triangle pattern.
- [ ] Print a centered pyramid.
- [ ] Use `for-else` to detect whether a list contains a target.
- [ ] Find all divisors of a positive integer.
- [ ] Find the greatest common divisor of two integers.

---

## Final Revision Checklist

Before moving to the next chapter, make sure you can:

- [ ] Write `if`, `elif`, and `else` statements.
- [ ] Use nested conditions and logical operators.
- [ ] Explain how `range()` works.
- [ ] Iterate over lists, strings, and dictionaries.
- [ ] Use `enumerate()` to access indexes and values.
- [ ] Write `while` loops with correct termination conditions.
- [ ] Explain the difference between `break`, `continue`, and `pass`.
- [ ] Explain the behavior of `for-else` and `while-else`.
- [ ] Solve basic problems using loops and conditions.
- [ ] Analyze the time complexity of simple loops.

**Next topic:** Functions and Recursion — parameters, return values, scope, recursive calls, and base cases.

**Study strategy:** For every loop, trace the variable values manually. For every condition, test normal cases, boundary cases, and invalid inputs. Dry-running code is one of the best ways to build strong problem-solving skills for competitive programming.
