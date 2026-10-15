# 08. Exception Handling in Python

## 📌 Overview

Exception handling allows a Python program to respond to runtime errors without crashing unexpectedly. It helps you handle invalid input, missing files, division by zero, failed conversions, and other exceptional situations.

### Learning Objectives

By completing this section, you will learn how to:

- Handle exceptions using `try` and `except`.
- Catch multiple types of exceptions.
- Use `else` and `finally` correctly.
- Raise exceptions with `raise`.
- Re-raise exceptions and chain their causes.
- Define custom exception classes.
- Use assertions for debugging and internal checks.
- Write safer and more reliable Python programs.

---

## 📂 Project Structure

```text
08_Exception_Handling/
├── 01_try_except.py
├── 02_multiple_exceptions.py
├── 03_else_finally.py
├── 04_raise.py
├── 05_custom_exceptions.py
└── 06_assertions.py
```

| File | Description |
|---|---|
| `01_try_except.py` | Basic exception handling and accessing exception details |
| `02_multiple_exceptions.py` | Handling multiple exception types |
| `03_else_finally.py` | Using `else` and `finally` blocks |
| `04_raise.py` | Raising, re-raising, and chaining exceptions |
| `05_custom_exceptions.py` | Creating application-specific exceptions |
| `06_assertions.py` | Assertions, invariants, and debugging |

---

## 1. Basic Exception Handling

**File:** `01_try_except.py`

An exception is an event that interrupts the normal flow of a program when an error or exceptional condition occurs.

Common examples include:

- `ValueError`: A value has an inappropriate format, such as `int("abc")`.
- `TypeError`: An operation receives an incompatible type.
- `ZeroDivisionError`: Division by zero.
- `IndexError`: A sequence index is out of range.
- `KeyError`: A dictionary key does not exist.
- `FileNotFoundError`: A requested file cannot be found.

### 1.1 The `try` and `except` Blocks

```python
try:
    number = int("abc")
except ValueError:
    print("Could not convert the value to an integer.")
```

- `try` contains code that may raise an exception.
- `except` handles a matching exception if it occurs.

If the conversion succeeds, the `except` block is skipped.

### 1.2 Accessing Exception Details

```python
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Error: {error}")
```

Using `as error` stores the exception object in a variable. This lets you inspect or log its message.

### 1.3 Catching a General Exception

```python
try:
    data = {}
    print(data["missing"])
except Exception as error:
    print(f"{type(error).__name__}: {error}")
```

`Exception` catches most ordinary application errors.

However, avoid catching every exception without a good reason. Catch the specific errors you expect whenever possible so that unexpected bugs are not hidden.

### 1.4 Handling Errors Inside Functions

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None
```

Returning `None` is one possible design choice. In a larger application, you might instead raise the exception or return a structured result, depending on what callers need to know.

### 1.5 Re-Raising an Exception

```python
try:
    try:
        int("abc")
    except ValueError:
        print("Inner handler")
        raise
except ValueError as error:
    print(f"Outer handler: {error}")
```

A bare `raise` inside an exception handler re-raises the currently handled exception, preserving its traceback.

This is useful when a function needs to log or perform local cleanup but still wants the calling code to handle the error.

---

## 2. Handling Multiple Exceptions

**File:** `02_multiple_exceptions.py`

A single operation may fail in different ways. Python allows you to handle each expected exception separately.

### 2.1 Multiple `except` Blocks

```python
def process(data):
    try:
        number = int(data)
        return 100 / number
    except ValueError:
        return "Not a number"
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(process("10"))
print(process("abc"))
print(process("0"))
```

Each `except` block handles a different type of error.

### 2.2 Handling Multiple Types in One Block

```python
def parse_integer(value):
    try:
        return int(value)
    except (ValueError, TypeError) as error:
        print(f"Conversion failed: {error}")
        return None

print(parse_integer("42"))
print(parse_integer("abc"))
print(parse_integer(None))
```

Use a tuple of exception classes when the same recovery behavior applies to multiple exception types.

### 2.3 Exception Order Matters

```python
try:
    int("abc")
except ValueError:
    print("Invalid value")
except Exception:
    print("Another error")
```

Place specific exceptions before general ones.

Incorrect ordering:

```python
try:
    int("abc")
except Exception:
    print("Generic error")
except ValueError:
    print("Invalid value")
```

The second handler is unreachable for `ValueError`, because the first handler already catches it.

**Rule:** Catch the most specific expected exceptions first and broader exceptions later.

---

## 3. The `else` and `finally` Blocks

**File:** `03_else_finally.py`

Python provides two additional blocks for controlling the flow of exception handling.

### 3.1 The `else` Block

The `else` block runs only when the `try` block completes without raising an exception.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Division successful")
        return result

print(divide(10, 2))
print(divide(10, 0))
```

Use `else` to keep code that should run only after successful execution outside the `try` block.

### 3.2 The `finally` Block

The `finally` block runs when control leaves the `try` statement, whether an exception occurred or not.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero")
        return None
    finally:
        print("Cleanup complete")
```

Typical uses include releasing resources and performing cleanup.

### 3.3 Understanding the Complete Flow

| Block | When It Runs |
|---|---|
| `try` | Executes the code being monitored |
| `except` | Runs when a matching exception occurs |
| `else` | Runs if the `try` block succeeds without an exception |
| `finally` | Runs when control exits the statement, including on exceptions |

### 3.4 Resource Cleanup

For ordinary file operations, a context manager is generally simpler than manually closing the file in `finally`.

```python
def read_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""
```

The `with` statement automatically closes the file, even if reading raises an exception.

### 3.5 `finally` and `return`

```python
def example():
    try:
        return 1
    finally:
        print("Cleanup runs before the function returns")

print(example())
```

Output:

```text
Cleanup runs before the function returns
1
```

Avoid returning a value from `finally`. Such a return can override a return from `try` or `except`, and can suppress a pending exception.

---

## 4. Raising Exceptions

**File:** `04_raise.py`

The `raise` statement lets you signal that an operation cannot continue under the current conditions.

### 4.1 Raising an Exception Explicitly

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(25))
```

Calling `set_age(-5)` raises a `ValueError`.

Use an appropriate built-in exception class when an input or operation violates the function's requirements.

### 4.2 Re-Raising an Exception

```python
def process(data):
    try:
        return int(data)
    except ValueError:
        print("Logging conversion error")
        raise

try:
    process("abc")
except ValueError:
    print("Error handled by the caller")
```

The bare `raise` preserves the original exception and traceback.

### 4.3 Exception Chaining With `raise ... from`

Sometimes a lower-level error occurs while performing a higher-level operation. You can raise a more meaningful exception while preserving the original cause.

```python
def load_number(text):
    try:
        return int(text)
    except ValueError as error:
        raise RuntimeError("Could not process the number") from error

try:
    load_number("abc")
except RuntimeError as error:
    print(error)
    print("Original cause:", error.__cause__)
```

Here:

- `ValueError` is the original cause.
- `RuntimeError` describes the higher-level failure.
- `from error` explicitly links the two exceptions.

This is helpful when building APIs or applications that need clear error messages without losing diagnostic information.

### 4.4 Validate Inputs With Exceptions

```python
def check_positive(number):
    if number <= 0:
        raise ValueError("Expected a positive number")
    return number
```

Use explicit exceptions for conditions that callers must handle or that must be enforced in production.

---

## 5. Custom Exceptions

**File:** `05_custom_exceptions.py`

Custom exceptions let you define errors specific to your application. They are useful when built-in exception types do not clearly describe the problem.

### 5.1 Defining a Custom Exception

```python
class AppError(Exception):
    """Base exception for the application."""
    pass

class NotFoundError(AppError):
    """Raised when a requested record is missing."""
    pass
```

Custom exceptions should generally inherit from `Exception` directly or from an application-specific base class that inherits from it.

### 5.2 Adding Details to an Exception

```python
class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")
```

This exception stores structured information:

- `field`: the field that failed validation.
- `message`: a description of the validation failure.

### 5.3 Using Custom Exceptions

```python
def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValidationError("age", "must be an integer")

    if age < 0:
        raise ValidationError("age", "must be non-negative")

    if age > 150:
        raise ValidationError("age", "is outside the accepted range")

    return age
```

The explicit `bool` check matters because `bool` is a subclass of `int` in Python. Without it, `True` and `False` would pass an ordinary `isinstance(age, int)` check.

Handle the custom exception:

```python
try:
    validate_age(-5)
except ValidationError as error:
    print(error.field)
    print(error.message)
```

### 5.4 Handling Missing Records

```python
class NotFoundError(AppError):
    pass

def find_user(users, user_id):
    if user_id not in users:
        raise NotFoundError(f"User {user_id} not found")
    return users[user_id]

try:
    find_user({1: "Alice"}, 2)
except NotFoundError as error:
    print(error)
```

### 5.5 Why Use Custom Exceptions?

Custom exceptions make error handling more expressive.

For example, a caller can distinguish between:

- `ValidationError`: the supplied data is invalid.
- `NotFoundError`: the requested record does not exist.
- `AppError`: a general application-specific failure.

This makes it easier to handle different failures without inspecting error-message strings.

---

## 6. Assertions

**File:** `06_assertions.py`

An assertion checks whether a condition is true. If the condition is false, Python raises an `AssertionError`.

Assertions are primarily intended for debugging and checking internal assumptions.

### 6.1 Basic Assertion

```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

print(divide(10, 2))
```

If `b` is zero, the assertion fails.

### 6.2 Postconditions

A postcondition describes something that should be true after an operation completes.

```python
def sort_numbers(numbers):
    result = sorted(numbers)
    assert result == sorted(result)
    return result
```

The example demonstrates the general idea, although the assertion is redundant because `result` is already produced by `sorted()`.

A more useful check would verify a property such as preserving the input elements:

```python
def sort_numbers(numbers):
    result = sorted(numbers)
    assert len(result) == len(numbers)
    assert sorted(result) == sorted(numbers)
    return result
```

### 6.3 Invariants

An invariant is a condition that should remain true throughout an object's valid states.

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)
        assert self._items[-1] == value

    def pop(self):
        assert not self.is_empty(), "Pop from an empty stack"
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0
```

Assertions can help detect mistakes during development, but the `pop()` assertion is not a reliable public-input validation mechanism.

### 6.4 Assertions Can Be Disabled

Python can disable assertions when run with optimization:

```bash
python -O script.py
```

Therefore, do not rely on `assert` to enforce important production requirements.

### 6.5 Assertion vs. Explicit Validation

Use assertions for internal assumptions:

```python
assert len(items) > 0, "Internal assumption failed"
```

Use explicit exceptions for input validation and conditions that must always be enforced:

```python
def production_divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b
```

**Key rule:** If a condition must remain enforced when Python runs with `-O`, do not use an assertion for it.

---

## 7. Common Exception Handling Patterns

### Pattern 1: Handle Only Expected Errors

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    print("You entered:", number)
```

### Pattern 2: Preserve the Original Exception

```python
try:
    result = int("invalid")
except ValueError:
    # Perform any necessary logging or cleanup.
    raise
```

### Pattern 3: Convert a Low-Level Error Into a Meaningful One

```python
def parse_score(text):
    try:
        return int(text)
    except ValueError as error:
        raise ValueError("Score must be an integer") from error
```

This example raises the same exception type with a more meaningful message and keeps the original cause.

### Pattern 4: Keep `try` Blocks Focused

Prefer:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid number")

result = number * 2
```

over wrapping a large amount of unrelated code in one `try` block. Smaller blocks make it easier to understand exactly which operation might fail.

---

## 8. Common Mistakes to Avoid

1. **Catching every exception unnecessarily:** Prefer specific exception types.
2. **Putting general handlers first:** Place specific handlers before `except Exception`.
3. **Using exceptions for ordinary control flow:** Use normal conditions when they express the situation more clearly.
4. **Swallowing errors silently:** If you handle an exception, provide meaningful recovery, reporting, or logging.
5. **Returning from `finally`:** This can override a return value or suppress an exception.
6. **Using `assert` for production validation:** Assertions may be disabled with `-O`.
7. **Raising vague exceptions:** Choose a suitable exception type and provide a useful message.
8. **Losing the original cause:** Use `raise NewError(...) from error` when translating an exception.
9. **Creating custom exceptions for everything:** Use built-in exceptions when they already describe the problem adequately.
10. **Ignoring cleanup:** Prefer context managers for files and other supported resources.

---

## 9. Competitive Programming Notes

In competitive programming, exceptions are most useful for understanding runtime failures and writing reusable utilities. Most contest solutions should validate input according to the problem's guarantees rather than wrapping every operation in a broad `try`/`except`.

Important points:

- `ValueError` can occur when converting an invalid string to an integer.
- `IndexError` often indicates an invalid list or string index.
- `KeyError` can occur when accessing a missing dictionary key.
- `ZeroDivisionError` occurs when dividing by zero.
- `try`/`except` should not be used to hide algorithmic bugs.
- `assert` can help during local debugging, but do not depend on it for required validation.
- When debugging, read the traceback to identify the operation and line that caused the error.

Example: safe integer parsing

```python
def parse_integer(text):
    try:
        return int(text)
    except ValueError:
        return None

value = parse_integer("123")
print(value)
```

For contest input that is guaranteed to contain valid integers, direct parsing is usually sufficient:

```python
n = int(input())
```

---

## 10. Key Takeaways

- `try` contains code that may raise an exception.
- `except` handles matching exceptions.
- `else` runs when the `try` block succeeds.
- `finally` is used for cleanup and runs when control exits the statement.
- `raise` explicitly signals an error.
- Bare `raise` re-raises the currently handled exception.
- `raise ... from ...` preserves the relationship between an error and its cause.
- Custom exceptions represent application-specific failures.
- Assertions check internal assumptions and are not a substitute for production validation.
- Good exception handling makes programs more reliable without hiding genuine bugs.

---

## 11. Practice Checklist

- [ ] Handle an invalid integer conversion.
- [ ] Handle division by zero.
- [ ] Catch multiple exception types in one function.
- [ ] Explain why specific exceptions should come before general exceptions.
- [ ] Demonstrate when `else` and `finally` execute.
- [ ] Re-raise an exception after logging a message.
- [ ] Chain a `ValueError` into a more meaningful exception.
- [ ] Create a custom `ValidationError` class.
- [ ] Create a custom `NotFoundError` class.
- [ ] Use assertions to check an internal invariant.
- [ ] Explain why assertions should not enforce production input validation.
- [ ] Write a function that validates a user's input and raises appropriate exceptions.

---

## 12. Mini Project: Input Validator

Build a small Python program that validates user records.

**Requirements:**

1. Accept a username, age, and email address.
2. Raise `ValidationError` if the username is empty.
3. Raise `ValidationError` if the age is not an integer or is negative.
4. Raise `ValidationError` if the email does not meet your chosen basic format requirements.
5. Handle validation errors without crashing the program.
6. Keep validation logic in separate functions.
7. Use clear exception messages.

Example exception structure:

```python
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

def validate_username(username):
    if not username.strip():
        raise ValidationError("Username cannot be empty")
    return username

def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValidationError("Age must be an integer")
    if age < 0:
        raise ValidationError("Age cannot be negative")
    return age
```

This project combines functions, conditional logic, custom exceptions, and reliable input validation.

---

## ▶️ Running the Examples

From the `08_Exception_Handling` directory, run:

```bash
python 01_try_except.py
python 02_multiple_exceptions.py
python 03_else_finally.py
python 04_raise.py
python 05_custom_exceptions.py
python 06_assertions.py
```

**Recommended learning order:** Basic `try`/`except` → Multiple Exceptions → `else`/`finally` → `raise` → Custom Exceptions → Assertions.