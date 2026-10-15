# 15. Debugging and Code Quality

Debugging is the process of finding, understanding, and fixing errors in a program. Code quality means writing code that is correct, readable, maintainable, and easy to test.

For competitive programming, debugging is especially important because a solution may compile and run but still produce the wrong answer for certain test cases.

## 📁 Project Structure

```text
15_Debugging_and_Code_Quality/
└── 01_debugging.py
```

## 🎯 Learning Objectives

By completing this module, you should understand how to:

- Identify and fix runtime errors and logical errors.
- Use `print()` statements for debugging.
- Pause execution with `breakpoint()` and `pdb`.
- Use assertions to check assumptions.
- Use the `logging` module to record program behavior.
- Debug loops, indexes, and calculations systematically.
- Improve code readability and reliability.
- Debug competitive programming solutions efficiently.

---

## 1. Types of Programming Errors

### 1.1 Syntax Errors

These occur when Python cannot parse your code.

```python
if x > 5
    print(x)
```

The colon is missing after the condition.

Correct version:

```python
if x > 5:
    print(x)
```

### 1.2 Runtime Errors

These occur while the program is running.

```python
x = 10 / 0
```

Output:

```text
ZeroDivisionError
```

Other examples include `IndexError`, `KeyError`, `TypeError`, and `ValueError`.

### 1.3 Logical Errors

The program runs but produces an incorrect result.

```python
def square(x):
    return x * 2  # Incorrect logic
```

Correct version:

```python
def square(x):
    return x * x
```

Logical errors are particularly important in competitive programming because they may only appear on specific test cases.

---

## 2. Method 1 — Print Debugging

Print debugging means displaying variable values and intermediate results to understand what your program is doing.

Your `debug_prints()` function demonstrates this technique.

```python
def debug_prints(nums):
    print(f"nums={nums}")

    result = []

    for i, n in enumerate(nums):
        print(f"Processing index {i}, value {n}")

        if n > 0:
            result.append(n * 2)

    print(f"result={result}")
    return result


print(debug_prints([1, -2, 3, -4]))
```

Expected debug information:

```text
nums=[1, -2, 3, -4]
Processing index 0, value 1
Processing index 1, value -2
Processing index 2, value 3
Processing index 3, value -4
result=[2, 6]
[2, 6]
```

### Why is print debugging useful?

- It shows the actual values of variables.
- It helps identify which iteration causes a problem.
- It lets you inspect intermediate results.
- It is simple and quick to use.

### Debugging a loop

Suppose you want to calculate the sum of all even numbers:

```python
nums = [2, 5, 8, 11]
total = 0

for n in nums:
    print(f"Before: n={n}, total={total}")

    if n % 2 == 0:
        total += n

    print(f"After: total={total}")

print("Final total:", total)
```

The expected final total is `10`.

**Tip:** Print the loop index, current value, and important state variables when debugging loops.

---

## 3. Method 2 — Debugging with `breakpoint()`

Python 3.7 and later provides the built-in `breakpoint()` function.

It pauses execution and normally opens the Python debugger (`pdb`) at that line.

```python
def breakpoint_demo(x):
    result = x * 2

    breakpoint()

    return result


print(breakpoint_demo(5))
```

When execution reaches `breakpoint()`, you can inspect variables and execute debugger commands.

### Useful `pdb` commands

| Command | Meaning |
|---|---|
| `n` | Execute the next line |
| `s` | Step into a function call |
| `c` | Continue execution until the next breakpoint |
| `p variable` | Print the value of a variable |
| `pp variable` | Pretty-print a variable |
| `l` | Show nearby source code |
| `where` | Show the current call stack |
| `q` | Quit the debugger |

For example, when execution pauses:

```text
(Pdb) p x
5
(Pdb) p result
10
(Pdb) n
(Pdb) c
```

Exact output depends on your program and execution environment.

### When should you use `breakpoint()`?

Use it when:

- A function produces an unexpected result.
- You need to inspect several variables at once.
- A loop behaves incorrectly.
- You want to follow execution one line at a time.

**Important:** Remove or disable debugging breakpoints before submitting a solution to an online judge. An interactive breakpoint can cause the program to pause or fail in a non-interactive environment.

---

## 4. Method 3 — Using `pdb.set_trace()`

The `pdb` module provides a debugger that can be started programmatically.

```python
import pdb

def pdb_demo():
    x = 1
    y = 2

    pdb.set_trace()

    return x + y
```

Calling `pdb.set_trace()` starts the debugger at that point.

This is similar to `breakpoint()` but explicitly uses the `pdb` module.

```python
import pdb

nums = [10, 20, 30]

for i, value in enumerate(nums):
    pdb.set_trace()
    print(i, value)
```

You can inspect `i` and `value` at every iteration.

### `breakpoint()` vs. `pdb.set_trace()`

- `breakpoint()` is the convenient built-in interface and can be configured through Python's breakpoint mechanism.
- `pdb.set_trace()` directly invokes the standard debugger.

For most everyday debugging, `breakpoint()` is a good default.

---

## 5. Method 4 — Assertions

An assertion checks whether a condition is true.

```python
def assert_demo(nums):
    assert len(nums) > 0, "Empty list"
    return sum(nums) / len(nums)


print(assert_demo([1, 2, 3]))
```

Output:

```text
2.0
```

For an empty list:

```python
assert_demo([])
```

This raises:

```text
AssertionError: Empty list
```

### Assertion syntax

```python
assert condition
assert condition, "Error message"
```

Another example:

```python
def calculate_average(nums):
    assert len(nums) > 0, "The list must not be empty"

    return sum(nums) / len(nums)
```

### When should you use assertions?

Assertions are useful for checking internal assumptions, such as:

- A list should not be empty at a particular stage.
- An index should be within an expected range.
- An algorithm should preserve a particular invariant.
- A calculated result should satisfy a condition during development.

### Important limitation

Do not use assertions for essential input validation or program correctness checks that must always execute. Python can disable assertions when run with optimization (`python -O`).

For ordinary user input, use explicit validation:

```python
def calculate_average(nums):
    if not nums:
        raise ValueError("The list must not be empty")

    return sum(nums) / len(nums)
```

---

## 6. Method 5 — Logging

The `logging` module records diagnostic messages at different severity levels.

It is more flexible than using `print()` throughout a large program.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def logging_demo(x):
    logger.debug("Input: %s", x)

    result = x ** 2

    logger.debug("Result: %s", result)

    return result


print(logging_demo(5))
```

Output includes debug messages and the final result:

```text
DEBUG:__main__:Input: 5
DEBUG:__main__:Result: 25
25
```

The exact format can vary depending on the logging configuration.

### Logging levels

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed information for diagnosing problems |
| `INFO` | Confirmation of normal program events |
| `WARNING` | Something unexpected happened, but execution can continue |
| `ERROR` | An operation failed |
| `CRITICAL` | A serious failure may prevent continued execution |

Example:

```python
logger.debug("Current index: %s", i)
logger.info("Processing completed")
logger.warning("Unexpected input value")
logger.error("Failed to process the record")
```

### Why use `logger.debug("Value: %s", value)`?

Prefer parameterized logging:

```python
logger.debug("Value: %s", value)
```

Instead of:

```python
logger.debug(f"Value: {value}")
```

Parameterized logging lets the logging system defer string formatting when the message is filtered out.

### Logging exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")
```

`logger.exception()` includes exception information and is intended for use inside an exception handler.

### When should you use logging?

Logging is particularly useful for:

- Larger programs with multiple functions.
- Long-running scripts.
- Recording failures for later investigation.
- Debugging code where many print statements would clutter the output.

For short competitive programming solutions, temporary `print()` statements are often faster. Remove them before submission or send diagnostic output to standard error when appropriate.

---

## 7. Understanding the Bug in `buggy_function()`

Your original function contains a division-by-zero bug:

```python
def buggy_function(nums):
    total = 0

    for i, n in enumerate(nums):
        total += n / i

    return total
```

### Why does it fail?

`enumerate(nums)` starts its index at `0` by default.

On the first iteration:

```python
i = 0
n = nums[0]
```

Therefore:

```python
n / i
```

becomes division by zero and raises `ZeroDivisionError`.

### Fix 1 — Start indexing from 1

If the intended calculation is to divide each number by its one-based position:

```python
def fixed_function(nums):
    total = 0

    for i, n in enumerate(nums, start=1):
        total += n / i

    return total
```

For `[10, 20, 30]`, this calculates:

\[
10/1 + 20/2 + 30/3 = 30
\]

### Fix 2 — Skip the first element

If the first element should not be included in the calculation:

```python
def fixed_function(nums):
    total = 0

    for i, n in enumerate(nums):
        if i == 0:
            continue

        total += n / i

    return total
```

These fixes have different meanings. Choose the one that matches the intended algorithm rather than changing code just to eliminate the error.

**Competitive programming lesson:** Always inspect how indexes are initialized, especially when using division, array access, and nested loops.

---

## 8. A Systematic Debugging Workflow

When your solution fails, follow this process.

1. **Reproduce the problem.** Find an input that causes the failure.
2. **Read the error message.** Identify the exception type and traceback line.
3. **Check the variables.** Print their values or inspect them using `breakpoint()`.
4. **Trace the algorithm.** Verify the values of important variables after each iteration.
5. **Check boundary cases.** Try empty input, one element, zeros, negatives, duplicates, and maximum constraints.
6. **Form a hypothesis.** Explain why the result is wrong before changing the code.
7. **Make a small fix.** Change the specific cause rather than rewriting everything.
8. **Retest.** Confirm that the failing case and ordinary cases both work.
9. **Remove temporary diagnostics.** Ensure the final output matches the judge's expected format.

### Example: Finding an off-by-one error

Incorrect code:

```python
nums = [10, 20, 30]
for i in range(len(nums) - 1):
    print(nums[i])
```

This prints only the first two elements.

Correct code:

```python
for i in range(len(nums)):
    print(nums[i])
```

Or, more simply:

```python
for n in nums:
    print(n)
```

---

## 9. Common Debugging Mistakes

### Mistake 1: Printing too much information

Printing every variable in a large program can make the important information hard to find.

**Better:** Print only the state relevant to the suspected problem.

### Mistake 2: Fixing symptoms instead of causes

If a division-by-zero error occurs, adding an arbitrary value to the denominator may hide the real problem.

**Better:** Determine whether the index, input, or mathematical formula is incorrect.

### Mistake 3: Testing only one example

A solution can pass a normal example but fail on edge cases.

**Better:** Test the smallest, largest, empty, duplicated, and unusual inputs permitted by the problem.

### Mistake 4: Leaving debug output in the final solution

Online judges often expect exact output. Extra messages can cause a Wrong Answer verdict.

**Better:** Remove temporary debugging prints before submission.

### Mistake 5: Using assertions as mandatory validation

Assertions may be disabled in optimized Python execution.

**Better:** Use explicit conditions and exceptions for checks that must always happen.

### Mistake 6: Forgetting that `breakpoint()` pauses execution

A solution that pauses for interactive debugging is unsuitable for an ordinary online judge submission.

**Better:** Remove breakpoints or configure debugging appropriately before submitting.

---

## 10. Debugging in Competitive Programming

Competitive programming introduces a few additional challenges:

- **Wrong Answer (WA):** The program runs, but the algorithm is incorrect.
- **Runtime Error (RE):** The program raises an exception or terminates unexpectedly.
- **Time Limit Exceeded (TLE):** The algorithm or implementation is too slow.
- **Memory Limit Exceeded (MLE):** The program uses too much memory.

### What to investigate

| Verdict | What to check |
|---|---|
| Wrong Answer | Algorithm logic, conditions, edge cases, integer or floating-point behavior |
| Runtime Error | Index bounds, division by zero, recursion depth, invalid conversions |
| Time Limit Exceeded | Time complexity, unnecessary loops, repeated computations, input/output |
| Memory Limit Exceeded | Large data structures, unnecessary copies, excessive recursion |

### Useful habits

- Test the smallest valid input first.
- Check whether your loop boundaries are inclusive or exclusive.
- Verify that every variable is initialized correctly.
- Compare intermediate values against a hand-calculated example.
- Estimate time complexity before optimizing.
- Use a brute-force solution for small inputs when testing a more efficient algorithm.
- Test random small cases and compare both solutions when possible.

For competitive programming, the most important skill is not adding more print statements; it is building a clear hypothesis about where the algorithm goes wrong.

---

## 11. Practice Checklist

Use this checklist to assess your progress.

- [ ] Identify syntax errors, runtime errors, and logical errors.
- [ ] Use `print()` to trace a loop.
- [ ] Inspect variables with `breakpoint()`.
- [ ] Use common `pdb` commands.
- [ ] Write assertions for internal assumptions.
- [ ] Explain why assertions should not replace essential validation.
- [ ] Configure logging and use different severity levels.
- [ ] Find and fix an off-by-one error.
- [ ] Debug a division-by-zero error.
- [ ] Test edge cases systematically.
- [ ] Remove debugging statements before submitting a solution.
- [ ] Diagnose a deliberately incorrect competitive programming solution.

---

## 12. Mini Project — Debug and Validate a List Analyzer

Build a function that returns the sum, average, minimum, and maximum of a list of numbers. It should reject empty input and include useful logging.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def analyze_numbers(nums):
    # Validate input
    if not nums:
        raise ValueError("The list must not be empty")

    logger.debug("Analyzing %d numbers", len(nums))

    total = sum(nums)
    average = total / len(nums)

    result = {
        "sum": total,
        "average": average,
        "minimum": min(nums),
        "maximum": max(nums),
    }

    logger.debug("Analysis result: %s", result)

    return result


if __name__ == "__main__":
    numbers = [4, 8, -2, 10]

    print(analyze_numbers(numbers))
```

Expected result:

```python
{
    "sum": 20,
    "average": 5.0,
    "minimum": -2,
    "maximum": 10
}
```

### Test cases

```python
print(analyze_numbers([5]))
print(analyze_numbers([1, 2, 3, 4]))
print(analyze_numbers([-5, -2, -9]))

# Should raise ValueError
print(analyze_numbers([]))
```

### Challenges

1. Add validation that all values are numbers.
2. Write tests for lists containing zero and duplicate values.
3. Deliberately introduce a bug and use `breakpoint()` to find it.
4. Add a test that verifies the expected dictionary for a known input.
5. Separate validation, calculation, and output into distinct functions.

---

## 13. Suggested Learning Order

1. Understand syntax, runtime, and logical errors.
2. Practice print debugging.
3. Learn `breakpoint()` and basic `pdb` commands.
4. Use assertions for internal assumptions.
5. Learn logging for larger programs.
6. Practice boundary-case testing.
7. Debug common array, string, loop, and recursion mistakes.
8. Apply systematic testing to competitive programming problems.

## Final Takeaway

Good programmers do not merely write code that works on one example. They write code whose behavior they understand, test it against difficult cases, and investigate failures methodically.

**Your goal:** Given a failing program, be able to explain what went wrong, why it happened, and how to fix it without introducing another bug.