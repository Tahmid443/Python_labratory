# 🐍 Python Exception Handling — Complete Revision Notes

> **Revision-focused notes based on the code in this `09.Exception Handling` folder.**
>
> This README explains Python exception handling from the basics to practical usage, including `try`, `except`, `else`, `finally`, `raise`, multiple exception handlers, resource cleanup, and the built-in exception classes demonstrated in the code.

---

## 📚 Table of Contents

1. [What is an Exception?](#1-what-is-an-exception)
2. [Why Exception Handling is Needed](#2-why-exception-handling-is-needed)
3. [Basic `try-except`](#3-basic-try-except)
4. [How `try` and `except` Work](#4-how-try-and-except-work)
5. [Handling Specific Exceptions](#5-handling-specific-exceptions)
6. [Multiple `except` Blocks](#6-multiple-except-blocks)
7. [The `else` Block](#7-the-else-block)
8. [The `finally` Block](#8-the-finally-block)
9. [`try-except-else-finally` Flow](#9-try-except-else-finally-flow)
10. [Nested `try-except`](#10-nested-try-except)
11. [Exception Handling for Files and Resources](#11-exception-handling-for-files-and-resources)
12. [Raising Exceptions with `raise`](#12-raising-exceptions-with-raise)
13. [Raising a Specific Exception](#13-raising-a-specific-exception)
14. [Exception Messages](#14-exception-messages)
15. [Built-in Exception Hierarchy](#15-built-in-exception-hierarchy)
16. [Built-in Exceptions in the Code](#16-built-in-exceptions-in-the-code)
17. [Important Exception Examples](#17-important-exception-examples)
18. [Syntax Errors vs Exceptions](#18-syntax-errors-vs-exceptions)
19. [`Exception` vs Specific Exceptions](#19-exception-vs-specific-exceptions)
20. [Exception Handling Best Practices](#20-exception-handling-best-practices)
21. [Common Mistakes](#21-common-mistakes)
22. [Quick Comparison Table](#22-quick-comparison-table)
23. [Revision Checklist](#23-revision-checklist)
24. [Ultra-Quick Revision](#24-ultra-quick-revision)

---

# 1. What is an Exception?

An **exception** is an event that occurs while a Python program is running that interrupts the normal flow of execution.

Example:

```python
x = 10 / 0
```

This causes:

```text
ZeroDivisionError
```

If the exception is not handled, Python stops the program and displays a traceback.

### Simple idea

```text
Normal program
      ↓
Something unexpected happens
      ↓
Exception is raised
      ↓
Python looks for a handler
      ↓
Handled → program can continue
```

---

# 2. Why Exception Handling is Needed

Without exception handling:

```python
print("Start")

x = 10 / 0

print("End")
```

The program stops at:

```python
10 / 0
```

So:

```text
Start
ZeroDivisionError
Program stops
```

With exception handling:

```python
print("Start")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

print("End")
```

Now the program can continue:

```text
Start
Cannot divide by zero
End
```

### Main purpose

Exception handling allows us to:

- prevent unexpected program crashes
- display meaningful error messages
- recover from expected runtime problems
- clean up resources
- separate normal logic from error-handling logic

---

# 3. Basic `try-except`

The fundamental structure is:

```python
try:
    # code that may cause an exception
except:
    # code that handles the exception
```

Example from the code:

```python
try:
    print(x)
except:
    print("An exception occurred")
```

Since `x` has not been defined, Python raises a `NameError`.

The `except` block catches it.

---

## General structure

```text
try
 ↓
Run risky code
 ↓
Exception?
 ├── No → continue
 └── Yes → matching except block
```

---

# 4. How `try` and `except` Work

Consider:

```python
try:
    print(x)
except:
    print("An exception occurred")

print("Program continues")
```

### Step-by-step

1. Python enters `try`.
2. It executes `print(x)`.
3. `x` is undefined.
4. Python raises `NameError`.
5. Python skips the remaining `try` code.
6. Python searches for a matching `except`.
7. The `except` block executes.
8. Program continues after the complete `try-except`.

---

## Important rule

If an exception occurs in the `try` block, Python does **not** continue executing the remaining statements in that `try` block.

Example:

```python
try:
    print("A")
    x = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
```

Output:

```text
A
C
```

`B` is never printed.

---

# 5. Handling Specific Exceptions

It is better to catch the specific exception you expect.

Example:

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
```

This is better than blindly using:

```python
except:
```

because the code clearly communicates which problem it expects.

---

## Why specific exceptions are better

Suppose:

```python
try:
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Now the program handles exactly the problem it knows how to recover from.

This makes debugging and maintenance easier.

---

# 6. Multiple `except` Blocks

Python allows multiple exception handlers.

The code demonstrates:

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
```

This means:

```text
try
 ↓
NameError?
 ├── Yes → first except
 └── No
      ↓
Other exception?
 └── second except
```

---

## Example with multiple specific exceptions

```python
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Different problems get different responses.

---

## Order matters

More specific exceptions should generally come before broader exceptions.

Correct:

```python
try:
    ...
except ZeroDivisionError:
    ...
except Exception:
    ...
```

Avoid:

```python
try:
    ...
except Exception:
    ...
except ZeroDivisionError:
    ...
```

The broad `Exception` handler can catch the `ZeroDivisionError` first, making the later handler unreachable for that exception.

---

# 7. The `else` Block

The `else` block runs **only when no exception occurs in the `try` block**.

Syntax:

```python
try:
    # risky code
except:
    # error
else:
    # no error
```

Example from the code:

```python
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
```

Since `print("Hello")` succeeds:

```text
Hello
Nothing went wrong
```

---

## Why use `else`?

It allows you to keep the successful path separate from the error-handling path.

Example:

```python
try:
    number = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Number:", number)
```

---

## Important rule

```text
Exception occurs
→ except runs
→ else does NOT run

No exception
→ except does NOT run
→ else runs
```

---

# 8. The `finally` Block

The `finally` block runs **regardless of whether an exception occurs**.

Syntax:

```python
try:
    ...
except:
    ...
finally:
    ...
```

Example:

```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
```

Even though `x` causes an exception, `finally` still runs.

---

## Main purpose of `finally`

`finally` is commonly used for **cleanup**.

Examples:

- closing files
- closing database connections
- releasing resources
- disconnecting network connections
- cleaning temporary resources

Think:

```text
finally → "This must happen at the end."
```

---

# 9. `try-except-else-finally` Flow

The complete structure is:

```python
try:
    # risky operation
except SomeError:
    # if exception happens
else:
    # if no exception happens
finally:
    # always execute
```

### Case 1 — No exception

```text
try
 ↓
success
 ↓
else
 ↓
finally
```

### Case 2 — Exception handled

```text
try
 ↓
exception
 ↓
except
 ↓
finally
```

### Case 3 — Exception not handled

```text
try
 ↓
exception
 ↓
no matching except
 ↓
finally
 ↓
exception propagates
```

This last case is important: `finally` can still run even when the exception is not handled by the current `except` blocks.

---

# 10. Nested `try-except`

The code contains a nested structure for file handling:

```python
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
```

There are two different operations that can fail:

```text
Opening the file
        ↓
Writing to the file
```

So there are two levels of error handling.

---

## Why nested handling can be useful

You may want different handling for different stages.

For example:

```text
Opening failed
→ handle opening error

Opening succeeded
→ writing failed
→ handle writing error

Regardless of writing result
→ close file
```

### But note

For normal file handling, Python's `with` statement is usually cleaner:

```python
with open("demofile.txt", "w") as f:
    f.write("Hello")
```

The context manager automatically handles closing the file.

---

# 11. Exception Handling for Files and Resources

The code demonstrates the important idea of resource cleanup.

```python
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
```

The critical line is:

```python
f.close()
```

inside `finally`.

Even if writing fails, the file should still be closed.

---

## Better modern Python approach

Prefer:

```python
with open("demofile.txt", "w") as f:
    f.write("Hello")
```

The `with` statement uses a context manager to handle cleanup automatically.

### Revision point

```text
finally → manual/general cleanup mechanism
with    → preferred context-manager approach for resources that support it
```

---

# 12. Raising Exceptions with `raise`

Python lets you deliberately generate an exception using:

```python
raise
```

Example from the code:

```python
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
```

If `x < 0`, Python raises:

```text
Exception: Sorry, no numbers below zero
```

---

## Why deliberately raise an exception?

Sometimes your program detects an invalid condition that Python itself would not automatically treat as an error.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

This makes your program enforce its own rules.

---

# 13. Raising a Specific Exception

You can choose the exception type.

The code demonstrates:

```python
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
```

Here the value is a string, but the program requires an integer.

So:

```text
TypeError
```

is appropriate.

---

## Common choices

### `ValueError`

Use when the type is appropriate but the value is invalid.

```python
age = -1

raise ValueError("Age cannot be negative")
```

---

### `TypeError`

Use when the type of an object is inappropriate.

```python
name = "Tahmid"

if not isinstance(name, int):
    raise TypeError("Expected an integer")
```

---

### `Exception`

A general exception can be raised:

```python
raise Exception("Something went wrong")
```

But in application code, a more specific exception is usually preferable when one fits the situation.

---

# 14. Exception Messages

You can attach a message:

```python
raise Exception("Sorry, no numbers below zero")
```

The message helps the developer or user understand what went wrong.

Example:

```python
raise TypeError("Only integers are allowed")
```

Compare:

```python
raise TypeError
```

with:

```python
raise TypeError("Only integers are allowed")
```

The second provides useful context.

---

## Catching the exception object

You can also write:

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

Here:

```text
e
```

contains the exception object/message.

---

# 15. Built-in Exception Hierarchy

Python's exceptions are organized in a hierarchy.

A simplified view:

```text
BaseException
│
├── KeyboardInterrupt
├── SystemExit
├── GeneratorExit
│
└── Exception
    │
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    │
    ├── AssertionError
    ├── AttributeError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    │
    ├── OSError
    ├── ReferenceError
    ├── RuntimeError
    ├── StopIteration
    ├── SyntaxError
    │   ├── IndentationError
    │   └── TabError
    │
    ├── TypeError
    ├── UnicodeError
    │   ├── UnicodeDecodeError
    │   ├── UnicodeEncodeError
    │   └── UnicodeTranslateError
    │
    └── ValueError
```

### Important concept

A child exception is also an instance of its parent category.

For example:

```text
ZeroDivisionError
      ↓
ArithmeticError
      ↓
Exception
      ↓
BaseException
```

Therefore:

```python
except ArithmeticError:
```

can catch a `ZeroDivisionError`.

---

# 16. Built-in Exceptions in the Code

The second Python file demonstrates many built-in exceptions.

Below is the revision guide for each one.

---

## 16.1 `ArithmeticError`

Base class for errors related to arithmetic operations.

Example:

```python
try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error")
```

`ZeroDivisionError` is a subclass of `ArithmeticError`.

Hierarchy:

```text
ArithmeticError
└── ZeroDivisionError
```

---

## 16.2 `AssertionError`

Raised when an `assert` statement fails.

Code:

```python
age = 15

assert age >= 18
```

Since the condition is false:

```text
AssertionError
```

is raised.

### Use

Assertions are useful for checking assumptions during development.

---

## 16.3 `AttributeError`

Occurs when an object does not have the requested attribute or method.

Code:

```python
text = "Hello"

text.append(" World")
```

Strings do not have a list-style `append()` method.

Therefore:

```text
AttributeError
```

---

# 16.4 `Exception`

`Exception` is a major general-purpose base class for many normal application exceptions.

Example:

```python
try:
    result = 10 / 0
except Exception:
    print("Something went wrong")
```

It can catch many exceptions derived from `Exception`.

### Best practice

Do not use a broad `except Exception:` when you can handle a specific exception more appropriately.

---

# 16.5 `EOFError`

Raised when `input()` encounters an end-of-file condition instead of receiving input.

Example:

```python
try:
    name = input("Enter your name: ")
except EOFError:
    print("Input ended unexpectedly")
```

---

# 16.6 `FloatingPointError`

Used for floating-point related errors in situations where Python or a numerical library raises this exception.

The code demonstrates it explicitly:

```python
raise FloatingPointError("Floating point error")
```

Then catches it:

```python
except FloatingPointError:
```

---

# 16.7 `GeneratorExit`

Raised inside a generator when its `close()` method is called.

The code:

```python
def my_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("GeneratorExit")
```

Then:

```python
g = my_generator()
next(g)
g.close()
```

Calling:

```python
g.close()
```

causes the generator to receive `GeneratorExit`.

---

# 16.8 `ImportError`

Occurs when an import operation cannot successfully import the requested name/module.

Code:

```python
from math import something_that_does_not_exist
```

This raises `ImportError`.

---

## `ImportError` vs `ModuleNotFoundError`

`ModuleNotFoundError` is a more specific subclass used when the requested module itself cannot be found.

Example:

```python
import module_that_does_not_exist
```

---

# 16.9 `IndentationError`

Occurs when Python code has invalid indentation.

Example:

```python
if True:
print("Hello")
```

Python requires indentation after the colon.

### Important

`IndentationError` is a subclass of `SyntaxError`.

Some syntax errors occur **before normal program execution begins**, so they cannot generally be caught by putting the malformed source inside a `try` block in that same source file.

---

# 16.10 `IndexError`

Occurs when an index is outside the valid range.

Code:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Valid indexes are:

```text
0, 1, 2
```

Index `5` does not exist.

Therefore:

```text
IndexError
```

---

# 16.11 `KeyError`

Occurs when a dictionary key is missing.

Code:

```python
student = {
    "name": "Tahmid",
    "age": 20
}

print(student["address"])
```

There is no `"address"` key.

Therefore:

```text
KeyError
```

### Safer alternative

```python
student.get("address")
```

returns `None` by default instead of raising `KeyError`.

---

# 16.12 `KeyboardInterrupt`

Raised when the user interrupts a running program, commonly with:

```text
Ctrl + C
```

Example:

```python
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted")
```

---

## Important

`KeyboardInterrupt` inherits directly from `BaseException`, not from the normal `Exception` branch.

That is why blindly using:

```python
except Exception:
```

does not catch it.

---

# 16.13 `LookupError`

A base class for errors involving invalid lookups.

Important subclasses:

```text
LookupError
├── IndexError
└── KeyError
```

Example:

```python
numbers = [10, 20, 30]

print(numbers[10])
```

can be caught by:

```python
except LookupError:
```

---

# 16.14 `MemoryError`

Raised when an operation cannot be completed because the Python process cannot allocate enough memory.

The code demonstrates it explicitly:

```python
raise MemoryError("Not enough memory")
```

Then:

```python
except MemoryError:
```

catches it.

### Note

Artificially raising `MemoryError` demonstrates the exception type; it does not actually exhaust the machine's memory.

---

# 16.15 `NameError`

Occurs when a local or global name is referenced but has not been defined.

Code:

```python
print(username)
```

If `username` does not exist:

```text
NameError
```

---

# 16.16 `NotImplementedError`

Used when a method is intentionally left for subclasses or implementations to provide.

Code:

```python
class Animal:
    def sound(self):
        raise NotImplementedError("sound() must be implemented")
```

Calling:

```python
animal.sound()
```

raises `NotImplementedError`.

### Common use

Abstract/base classes and methods that require subclass-specific implementation.

---

# 16.17 `OSError`

Represents operating-system-related errors.

Example:

```python
with open("unknown_file.txt", "r") as f:
    print(f.read())
```

If the file does not exist or another OS-level problem occurs, an `OSError` family exception may be raised.

Many file and operating-system exceptions are subclasses of `OSError`.

---

# 16.18 `OverflowError`

Occurs when a numerical operation produces a result too large for the available numeric representation in that operation.

The code demonstrates:

```python
import math

math.exp(1000)
```

which raises:

```text
OverflowError
```

---

# 16.19 `ReferenceError`

Associated with weak references.

A weak reference can refer to an object without keeping that object alive.

The code comments demonstrate the idea using:

```python
import weakref
```

When the referenced object has been destroyed, attempting to use the weak reference in an invalid way can result in `ReferenceError`.

### Important

The commented example is conceptual; checking:

```python
reference() is None
```

is the usual way to determine whether a weakly referenced object is gone.

---

# 16.20 `RuntimeError`

A general error that occurs during runtime when no more specific built-in exception is appropriate.

The code explicitly raises it:

```python
raise RuntimeError("Something went wrong")
```

---

# 16.21 `StopIteration`

Raised by an iterator when there are no more values to produce.

Code:

```python
numbers = iter([10, 20])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

The first two `next()` calls succeed.

The third has no value left, so:

```text
StopIteration
```

is raised.

---

## Generator connection

Python's `for` loop normally handles `StopIteration` internally.

For example:

```python
for x in numbers:
    print(x)
```

You usually do not manually catch `StopIteration` when using a `for` loop.

---

# 16.22 `SyntaxError`

Occurs when Python cannot parse the source code because the syntax is invalid.

Example:

```python
if True
    print("Hello")
```

The colon is missing.

This error occurs before normal execution of that source file.

---

## Important distinction

```text
SyntaxError
→ Python cannot parse the program

Runtime exception
→ program started, then something went wrong while running
```

---

# 16.23 `TabError`

Occurs when indentation contains inconsistent use of tabs and spaces.

For example, mixing tabs and spaces incorrectly in a block can trigger `TabError`.

It is related to Python's indentation rules and is a subclass of `IndentationError`.

---

# 16.24 `SystemError`

Indicates an internal error in the Python interpreter.

The code demonstrates it explicitly:

```python
raise SystemError("Internal system error")
```

Then catches it.

In normal application development, you generally should not manually raise `SystemError` unless you have a very specific reason.

---

# 16.25 `SystemExit`

Raised when Python is asked to terminate through:

```python
sys.exit()
```

Code:

```python
import sys

try:
    sys.exit()
except SystemExit:
    print("SystemExit")
```

Because `SystemExit` is raised, the `except` block can catch it.

### Important

Like `KeyboardInterrupt`, `SystemExit` inherits from `BaseException`, not from `Exception`.

---

# 16.26 `TypeError`

Occurs when an operation or function is used with an inappropriate type.

Code:

```python
result = "10" + 5
```

A string and integer cannot be directly added this way.

Therefore:

```text
TypeError
```

---

## Easy distinction

```text
TypeError
→ wrong TYPE

ValueError
→ right TYPE, wrong VALUE
```

Example:

```python
int("hello")
```

has a string input that is acceptable as a type to `int()`, but its content is not a valid integer representation, so it raises `ValueError`.

---

# 16.27 `UnboundLocalError`

A specialized form of `NameError`.

The code:

```python
x = 10

def test():
    try:
        print(x)
        x = 20
    except UnboundLocalError:
        print("UnboundLocalError")
```

Because `x` is assigned somewhere inside `test()`, Python treats `x` as a local variable throughout the function.

So:

```python
print(x)
```

tries to access the local `x` before it has been assigned.

This causes:

```text
UnboundLocalError
```

---

## Key concept

Assignment inside a function can make a name local:

```python
x = 10

def test():
    print(x)
    x = 20
```

Python sees the assignment and treats `x` as local to `test()`.

---

# 16.28 `UnicodeError`

Base class for Unicode-related encoding/decoding/translation errors.

Hierarchy:

```text
UnicodeError
├── UnicodeDecodeError
├── UnicodeEncodeError
└── UnicodeTranslateError
```

---

# 16.29 `UnicodeEncodeError`

Occurs when Python cannot encode a Unicode string into the requested encoding.

The code:

```python
text = "বাংলা"
text.encode("ascii")
```

ASCII cannot represent those Bengali characters, so:

```text
UnicodeEncodeError
```

is raised.

---

# 16.30 `UnicodeDecodeError`

Occurs when bytes cannot be decoded using the selected character encoding.

Code:

```python
data = b"\xff"
data.decode("utf-8")
```

The byte sequence is not valid UTF-8 in this context.

Therefore:

```text
UnicodeDecodeError
```

---

# 16.31 `UnicodeTranslateError`

Occurs when Unicode translation fails.

The code demonstrates it explicitly:

```python
raise UnicodeTranslateError(
    "translation",
    "text",
    0,
    1,
    "translation failed"
)
```

and catches it with:

```python
except UnicodeTranslateError:
```

---

# 16.32 `ValueError`

Occurs when a function receives an argument of the correct general type but an inappropriate value.

Code:

```python
number = int("hello")
```

The argument is a string, which `int()` can accept in principle, but `"hello"` does not represent a valid integer.

Therefore:

```text
ValueError
```

---

# 16.33 `ZeroDivisionError`

Occurs when dividing by zero.

Example:

```python
result = 10 / 0
```

raises:

```text
ZeroDivisionError
```

It is a subclass of:

```text
ArithmeticError
```

---

# 17. Important Exception Examples

## 17.1 `IndexError` vs `KeyError`

```python
numbers = [10, 20, 30]
numbers[5]
```

→ `IndexError`

```python
student = {"name": "Tahmid"}
student["age"]
```

→ `KeyError`

### Memory trick

```text
List index missing → IndexError
Dictionary key missing → KeyError
```

---

## 17.2 `TypeError` vs `ValueError`

### TypeError

Wrong kind/type of object:

```python
"10" + 5
```

### ValueError

Correct type category, invalid value:

```python
int("hello")
```

### Memory trick

```text
TYPE problem  → TypeError
VALUE problem → ValueError
```

---

## 17.3 `NameError` vs `UnboundLocalError`

```python
print(username)
```

when `username` was never defined:

```text
NameError
```

But:

```python
x = 10

def test():
    print(x)
    x = 20
```

causes:

```text
UnboundLocalError
```

because Python treats `x` as a local variable due to the assignment.

---

## 17.4 `IndexError` and `KeyError` under `LookupError`

```text
LookupError
├── IndexError
└── KeyError
```

So:

```python
except LookupError:
```

can catch either one.

---

## 17.5 `ZeroDivisionError` under `ArithmeticError`

```text
ArithmeticError
├── FloatingPointError
├── OverflowError
└── ZeroDivisionError
```

So:

```python
except ArithmeticError:
```

can catch `ZeroDivisionError`.

---

# 18. Syntax Errors vs Exceptions

This distinction is extremely important.

## Syntax Error

The source code itself is invalid.

Example:

```python
if True
    print("Hello")
```

Python cannot parse it.

```text
SyntaxError
```

---

## Runtime Exception

The source code is syntactically valid, but something goes wrong while executing it.

Example:

```python
x = 10 / 0
```

The program starts running and then raises:

```text
ZeroDivisionError
```

---

## Comparison

| Syntax Error | Runtime Exception |
|---|---|
| Invalid Python syntax | Problem during execution |
| Happens during parsing/compilation | Happens while running |
| Example: `SyntaxError` | Example: `ZeroDivisionError` |
| Program cannot normally begin executing that invalid source | Program has already started |

### Important

`IndentationError` and `TabError` are syntax-related exceptions.

---

# 19. `Exception` vs Specific Exceptions

You can write:

```python
try:
    ...
except:
    ...
```

or:

```python
try:
    ...
except Exception:
    ...
```

or:

```python
try:
    ...
except ValueError:
    ...
```

These are not equally precise.

---

## Broad handler

```python
except:
```

Catches almost all exceptions that derive from `BaseException`, including special exceptions such as `KeyboardInterrupt` and `SystemExit`.

This can be dangerous because it may hide interrupts or shutdown requests.

---

## `except Exception`

```python
except Exception:
```

Catches normal application/runtime exceptions under the `Exception` branch.

It does **not** catch:

```text
KeyboardInterrupt
SystemExit
GeneratorExit
```

because those are direct children of `BaseException`.

---

## Specific handler

```python
except ValueError:
```

is usually the best choice when you know what problem you expect.

### Preferred pattern

```python
try:
    number = int(input())
except ValueError:
    print("Please enter a valid number")
```

---

# 20. Exception Handling Best Practices

## 20.1 Catch specific exceptions

Prefer:

```python
except ValueError:
```

over:

```python
except:
```

when possible.

---

## 20.2 Do not silently ignore errors

Avoid:

```python
try:
    risky_operation()
except:
    pass
```

This can hide bugs.

---

## 20.3 Give useful error messages

Prefer:

```python
except ValueError:
    print("Please enter a valid integer.")
```

instead of:

```python
except ValueError:
    print("Error")
```

---

## 20.4 Use `finally` for cleanup

```python
try:
    resource = acquire_resource()
finally:
    release_resource()
```

---

## 20.5 Prefer `with` for context-managed resources

For files:

```python
with open("data.txt") as f:
    data = f.read()
```

This is usually cleaner than manually calling `close()`.

---

## 20.6 Do not use exceptions for ordinary control flow unnecessarily

Exceptions should normally represent exceptional situations, not replace simple conditional logic.

Bad idea:

```python
try:
    if_condition()
except:
    ...
```

when a normal `if` can clearly express the expected case.

---

## 20.7 Raise meaningful exceptions

Instead of:

```python
raise Exception("error")
```

choose a more specific type when appropriate:

```python
raise ValueError("Age cannot be negative")
```

---

# 21. Common Mistakes

## Mistake 1 — Catching everything blindly

```python
try:
    ...
except:
    ...
```

This can hide bugs and even catch interrupts such as `KeyboardInterrupt`.

Prefer specific exceptions.

---

## Mistake 2 — Putting too much code in `try`

Instead of:

```python
try:
    # 30 lines of unrelated code
except ValueError:
    ...
```

keep the `try` block focused on the operation that can reasonably raise the expected exception.

---

## Mistake 3 — Putting success logic in `except`

Wrong idea:

```python
try:
    operation()
except:
    print("Success")
```

Use `else` for successful execution:

```python
try:
    operation()
except SomeError:
    print("Failed")
else:
    print("Success")
```

---

## Mistake 4 — Forgetting `finally`

If a resource must be cleaned up regardless of success or failure, use:

```python
finally:
    cleanup()
```

or preferably a context manager when appropriate.

---

## Mistake 5 — Confusing `raise` with `except`

```text
raise  → create/propagate an exception
except → catch/handle an exception
```

---

## Mistake 6 — Raising the wrong exception type

For invalid value:

```python
ValueError
```

For wrong object type:

```python
TypeError
```

Choosing the correct type makes your code easier to understand and debug.

---

## Mistake 7 — Forgetting that `finally` runs even after an exception

```python
try:
    raise ValueError("Oops")
finally:
    print("Cleanup")
```

The cleanup line still executes.

---

# 22. Quick Comparison Table

| Exception | Typical Cause |
|---|---|
| `ArithmeticError` | General arithmetic error |
| `AssertionError` | `assert` condition fails |
| `AttributeError` | Missing attribute/method |
| `EOFError` | Unexpected end of input |
| `FloatingPointError` | Floating-point error |
| `GeneratorExit` | Generator is closed |
| `ImportError` | Import operation fails |
| `IndentationError` | Invalid indentation |
| `IndexError` | Invalid sequence index |
| `KeyError` | Missing dictionary key |
| `KeyboardInterrupt` | User interrupts program |
| `LookupError` | Invalid lookup |
| `MemoryError` | Memory allocation failure |
| `NameError` | Name is not defined |
| `NotImplementedError` | Required implementation is missing |
| `OSError` | Operating-system/file error |
| `OverflowError` | Numeric result too large |
| `ReferenceError` | Invalid weak reference |
| `RuntimeError` | General runtime problem |
| `StopIteration` | Iterator has no more values |
| `SyntaxError` | Invalid Python syntax |
| `TabError` | Incorrect tab/space indentation |
| `SystemError` | Internal interpreter error |
| `SystemExit` | Program termination requested |
| `TypeError` | Wrong type for an operation |
| `UnboundLocalError` | Local variable used before assignment |
| `UnicodeError` | General Unicode error |
| `UnicodeEncodeError` | String cannot be encoded |
| `UnicodeDecodeError` | Bytes cannot be decoded |
| `UnicodeTranslateError` | Unicode translation failure |
| `ValueError` | Invalid value |
| `ZeroDivisionError` | Division by zero |

---

# 23. Revision Checklist

Before moving forward, make sure you can explain:

- [ ] What is an exception?
- [ ] Why do we need exception handling?
- [ ] What is `try`?
- [ ] What is `except`?
- [ ] What is `else`?
- [ ] What is `finally`?
- [ ] What happens when an exception occurs inside `try`?
- [ ] How do multiple `except` blocks work?
- [ ] Why should specific exceptions usually come before broad exceptions?
- [ ] What does `raise` do?
- [ ] How do you raise a custom error message?
- [ ] Difference between `TypeError` and `ValueError`
- [ ] Difference between `IndexError` and `KeyError`
- [ ] Difference between `NameError` and `UnboundLocalError`
- [ ] Difference between `remove()`-style errors and exception handling generally
- [ ] What is `ArithmeticError`?
- [ ] What is `LookupError`?
- [ ] What is `UnicodeError`?
- [ ] What is `StopIteration`?
- [ ] What is `NotImplementedError`?
- [ ] What is `OSError`?
- [ ] What is `AssertionError`?
- [ ] What is `KeyboardInterrupt`?
- [ ] What is `SystemExit`?
- [ ] What is `GeneratorExit`?
- [ ] What is `SyntaxError`?
- [ ] What is `IndentationError`?
- [ ] What is `TabError`?
- [ ] Why is `finally` useful?
- [ ] Why is `with open(...)` often better for files?
- [ ] Difference between `except:` and `except Exception:`
- [ ] Why should you avoid silently swallowing exceptions?

---

# 24. Ultra-Quick Revision

## Basic syntax

```python
try:
    risky_code()

except SomeError:
    handle_error()

else:
    # runs only if no exception

finally:
    # runs regardless
```

---

## Raise an exception

```python
raise Exception("Something went wrong")
```

---

## Raise a specific exception

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Catch the exception object

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

---

## Multiple exceptions

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except Exception:
    ...
```

---

## Core exception families

```text
ArithmeticError
├── FloatingPointError
├── OverflowError
└── ZeroDivisionError
```

```text
LookupError
├── IndexError
└── KeyError
```

```text
NameError
└── UnboundLocalError
```

```text
UnicodeError
├── UnicodeDecodeError
├── UnicodeEncodeError
└── UnicodeTranslateError
```

```text
SyntaxError
└── IndentationError
    └── TabError
```

---

## Most important differences

```text
TypeError
→ wrong TYPE

ValueError
→ wrong VALUE

IndexError
→ invalid list/sequence index

KeyError
→ missing dictionary key

NameError
→ name does not exist

UnboundLocalError
→ local variable used before assignment

ZeroDivisionError
→ division by zero

AttributeError
→ object does not have requested attribute

ImportError
→ import operation failed

StopIteration
→ iterator has no more values
```

---

# 🎯 Final Mental Model

Think of Python exception handling as a safety system:

```text
                 PYTHON PROGRAM
                       │
                       ▼
                 ┌───────────┐
                 │    try    │
                 └─────┬─────┘
                       │
              ┌────────┴────────┐
              │                 │
          No error          Error occurs
              │                 │
              ▼                 ▼
           else            matching except
              │                 │
              └────────┬────────┘
                       ▼
                    finally
                       │
                       ▼
                 continue/exit
```

And remember:

```text
try     → test risky code
except  → handle an exception
else    → run when no exception happened
finally → run cleanup regardless
raise   → deliberately raise an exception
```

The most important practical rule is:

> **Catch specific exceptions, handle them meaningfully, and use `finally` or context managers to guarantee cleanup.**

Once these concepts are clear, Python's exception system becomes much easier to understand and use in real projects.
