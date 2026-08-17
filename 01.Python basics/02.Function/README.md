# 🐍 Python Functions --- Complete Revision Notes

This folder contains my Python practice programs for **Functions and
Function Arguments**.

This README is written as a **revision notebook**. It explains the
concepts used in the source files, gives syntax and examples, highlights
important rules, and points out common mistakes.

> **Practice files:** `01.functions.py`, `02.arguments.py`

------------------------------------------------------------------------

## 📚 Table of Contents

1.  [What is a Function?](#1-what-is-a-function)
2.  [Defining and Calling a
    Function](#2-defining-and-calling-a-function)
3.  [Function Naming Rules](#3-function-naming-rules)
4.  [Return Values](#4-return-values)
5.  [The `return` Statement](#5-the-return-statement)
6.  [`None` as a Default Return
    Value](#6-none-as-a-default-return-value)
7.  [Empty Functions and `pass`](#7-empty-functions-and-pass)
8.  [Parameters and Arguments](#8-parameters-and-arguments)
9.  [Number of Arguments](#9-number-of-arguments)
10. [Default Parameter Values](#10-default-parameter-values)
11. [Positional Arguments](#11-positional-arguments)
12. [Keyword Arguments](#12-keyword-arguments)
13. [Mixing Positional and Keyword
    Arguments](#13-mixing-positional-and-keyword-arguments)
14. [Passing Different Data Types](#14-passing-different-data-types)
15. [Returning Different Data Types](#15-returning-different-data-types)
16. [Positional-Only Arguments](#16-positional-only-arguments)
17. [Keyword-Only Arguments](#17-keyword-only-arguments)
18. [Combining Positional-Only and
    Keyword-Only](#18-combining-positional-only-and-keyword-only)
19. [Why Functions Matter](#19-why-functions-matter)
20. [Common Mistakes](#20-common-mistakes)
21. [Quick Revision Sheet](#21-quick-revision-sheet)
22. [Practice Files](#22-practice-files)

------------------------------------------------------------------------

# 1. What is a Function?

A **function** is a reusable block of code that performs a particular
task.

Instead of writing the same code repeatedly, we can put it inside a
function and call that function whenever we need it.

Example:

``` python
def greet():
    print("Hello from a function")
```

The function does not run merely because it was defined.

It runs when we call it:

``` python
greet()
```

### Basic idea

``` text
Define function
      ↓
   def name():
      ↓
Call function
      ↓
   name()
      ↓
Code executes
```

Functions are one of the most important ideas in programming because
they help us:

-   reuse code
-   avoid repetition
-   organize large programs
-   make code easier to read
-   test individual pieces of logic
-   divide a large problem into smaller problems

------------------------------------------------------------------------

# 2. Defining and Calling a Function

📄 **File:** `01.functions.py`

A Python function is defined using the `def` keyword.

## Syntax

``` python
def function_name():
    # function body
```

Example:

``` python
def my_function():
    print("Hello from a function")
```

To execute it:

``` python
my_function()
```

------------------------------------------------------------------------

## 2.1 Function definition

``` python
def my_function():
    print("Hello from a function")
```

This creates the function.

Python stores the function so it can be called later.

------------------------------------------------------------------------

## 2.2 Function call

``` python
my_function()
```

A function call tells Python to execute the function body.

------------------------------------------------------------------------

## 2.3 Calling a function multiple times

One major advantage of functions is reuse.

``` python
def greet():
    print("Hello")

greet()
greet()
greet()
```

Output:

``` text
Hello
Hello
Hello
```

Instead of writing:

``` python
print("Hello")
print("Hello")
print("Hello")
```

we can define the behavior once and reuse it.

------------------------------------------------------------------------

# 3. Function Naming Rules

Function names follow the same general rules as variable names.

## Valid names

``` python
def my_function():
    pass

def calculate_sum():
    pass

def _helper():
    pass

def student2():
    pass
```

## Rules

### Rule 1 --- Start with a letter or underscore

Valid:

``` python
def hello():
    pass

def _hello():
    pass
```

Invalid:

``` python
def 2hello():
    pass
```

------------------------------------------------------------------------

### Rule 2 --- Can contain letters, numbers and underscores

``` python
def student_1():
    pass
```

But the name cannot start with a number.

------------------------------------------------------------------------

### Rule 3 --- Names are case-sensitive

These are different:

``` python
def myFunction():
    pass

def myfunction():
    pass
```

Python treats them as two different names.

------------------------------------------------------------------------

### Rule 4 --- Don't use Python keywords

Avoid names such as:

``` python
def class():
    pass
```

because `class` is a Python keyword.

------------------------------------------------------------------------

## Naming best practice

Use descriptive names:

``` python
def calculate_average():
    pass
```

is much better than:

``` python
def ca():
    pass
```

For normal Python functions, `snake_case` is the conventional style.

------------------------------------------------------------------------

# 4. Return Values

📄 **File:** `01.functions.py`

A function can send a value back to the code that called it using
`return`.

Example:

``` python
def get_greeting():
    return "Hello from a function"
```

Now we can store the returned value:

``` python
message = get_greeting()

print(message)
```

Output:

``` text
Hello from a function
```

------------------------------------------------------------------------

## 4.1 Why use `return`?

`print()` displays a value.

`return` sends a value back to the caller.

Compare:

``` python
def add(a, b):
    print(a + b)
```

and:

``` python
def add(a, b):
    return a + b
```

With `print()`:

``` python
result = add(5, 3)
```

`result` becomes `None`.

With `return`:

``` python
result = add(5, 3)
print(result)
```

Output:

``` text
8
```

### Important distinction

``` text
print() → displays information
return  → gives information back to the caller
```

A returned value can be:

-   stored in a variable
-   used in another expression
-   passed to another function
-   compared
-   returned from another function

Example:

``` python
def add(a, b):
    return a + b

result = add(5, 3) * 2
print(result)
```

Output:

``` text
16
```

------------------------------------------------------------------------

# 5. The `return` Statement

A function can return almost any Python object.

``` python
def add(a, b):
    return a + b
```

Once Python reaches `return`, the function immediately finishes.

Example:

``` python
def test():
    print("Before return")
    return 10
    print("After return")
```

Calling:

``` python
test()
```

produces:

``` text
Before return
```

The second `print()` is unreachable because execution has already
returned.

------------------------------------------------------------------------

## 5.1 Returning an expression

You do not need to calculate the result beforehand.

``` python
def multiply(a, b):
    return a * b
```

------------------------------------------------------------------------

## 5.2 Returning a Boolean

``` python
def is_even(n):
    return n % 2 == 0
```

Then:

``` python
print(is_even(10))
```

Output:

``` text
True
```

------------------------------------------------------------------------

## 5.3 Returning multiple values

Python can return multiple values using tuple packing:

``` python
def calculate(a, b):
    return a + b, a - b
```

Then:

``` python
sum_value, difference = calculate(10, 3)
```

Conceptually, the function returns:

``` python
(13, 7)
```

------------------------------------------------------------------------

# 6. `None` as a Default Return Value

If a function does not explicitly return a value, Python returns `None`.

Example:

``` python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

``` text
Hello
None
```

This is an important distinction.

A function can produce output with `print()` while still returning
`None`.

------------------------------------------------------------------------

## `None` means no meaningful returned value

``` python
result = greet()
```

does not mean the function failed.

It means the function did not explicitly return a value.

------------------------------------------------------------------------

# 7. Empty Functions and `pass`

Python does not allow an empty function body.

This is invalid:

``` python
def my_function():
```

Python requires an indented statement.

If you want to create a placeholder function, use `pass`.

``` python
def my_function():
    pass
```

`pass` means:

> Do nothing.

It is useful while designing a program and planning to implement the
function later.

Example:

``` python
def calculate_result():
    pass
```

Later you can replace it with the actual implementation.

------------------------------------------------------------------------

# 8. Parameters and Arguments

📄 **File:** `02.arguments.py`

Information can be passed into a function.

Example:

``` python
def my_function(fname):
    print(fname + " Refsnes")
```

Calling:

``` python
my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

produces different results because different values are passed into the
function.

------------------------------------------------------------------------

# 8.1 Parameter

A **parameter** is the variable listed in the function definition.

``` python
def my_function(name):
    print("Hello", name)
```

Here:

``` text
name → parameter
```

------------------------------------------------------------------------

# 8.2 Argument

An **argument** is the actual value passed when the function is called.

``` python
my_function("Emil")
```

Here:

``` text
"Emil" → argument
```

### Easy memory trick

``` text
Definition → parameter
Call       → argument
```

Example:

``` python
def add(a, b):
    return a + b
```

`a` and `b` are parameters.

``` python
add(10, 20)
```

`10` and `20` are arguments.

------------------------------------------------------------------------

# 9. Number of Arguments

By default, the number of arguments passed to a function must match the
number of required parameters.

Example:

``` python
def my_function(fname, lname):
    print(fname + " " + lname)
```

Correct:

``` python
my_function("Emil", "Refsnes")
```

Incorrect:

``` python
my_function("Emil")
```

This causes a `TypeError` because one required argument is missing.

Also incorrect:

``` python
my_function("Emil", "Refsnes", "Extra")
```

because too many arguments were supplied.

------------------------------------------------------------------------

## Important rule

If a function has:

``` python
def function(a, b):
```

then a normal call needs two values:

``` python
function(10, 20)
```

unless defaults or special argument handling change the requirements.

------------------------------------------------------------------------

# 10. Default Parameter Values

A parameter can have a default value.

``` python
def my_function(name="friend"):
    print("Hello", name)
```

Now the function can be called with or without an argument.

``` python
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
```

Output:

``` text
Hello Emil
Hello Tobias
Hello friend
Hello Linus
```

------------------------------------------------------------------------

## 10.1 Why use default parameters?

They make parameters optional.

Example:

``` python
def greet(name="Guest"):
    print(f"Hello {name}")
```

Then:

``` python
greet()
```

uses:

``` text
Guest
```

while:

``` python
greet("Tahmid")
```

uses:

``` text
Tahmid
```

------------------------------------------------------------------------

## 10.2 Default values are used when an argument is omitted

If an argument is provided, it replaces the default:

``` python
def greet(name="Guest"):
    print(name)

greet("Tahmid")
```

Output:

``` text
Tahmid
```

------------------------------------------------------------------------

# 11. Positional Arguments

When arguments are passed without parameter names, they are **positional
arguments**.

Example:

``` python
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
```

Call:

``` python
my_function("dog", "Buddy")
```

Mapping happens by position:

``` text
animal → "dog"
name   → "Buddy"
```

------------------------------------------------------------------------

## 11.1 Order matters

``` python
my_function("dog", "Buddy")
```

is not equivalent to:

``` python
my_function("Buddy", "dog")
```

The second call maps:

``` text
animal → "Buddy"
name   → "dog"
```

Therefore, positional arguments must be supplied in the correct order.

------------------------------------------------------------------------

# 12. Keyword Arguments

Keyword arguments use:

``` text
parameter=value
```

syntax.

Example:

``` python
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
```

Call:

``` python
my_function(animal="dog", name="Buddy")
```

Here Python matches arguments by parameter name rather than position.

------------------------------------------------------------------------

## 12.1 Advantages of keyword arguments

They can make calls:

-   clearer
-   easier to read
-   less dependent on parameter order

Example:

``` python
create_student(name="Tahmid", age=20, department="CSE")
```

The meaning of each value is immediately visible.

------------------------------------------------------------------------

# 13. Mixing Positional and Keyword Arguments

You can combine positional and keyword arguments.

Example:

``` python
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
```

Call:

``` python
my_function("dog", name="Buddy", age=5)
```

Mapping:

``` text
animal → "dog"       positional
name   → "Buddy"     keyword
age    → 5           keyword
```

------------------------------------------------------------------------

## Important rule

**Positional arguments must come before keyword arguments.**

Correct:

``` python
my_function("dog", name="Buddy", age=5)
```

Incorrect:

``` python
my_function(animal="dog", "Buddy", 5)
```

This causes a `SyntaxError`.

------------------------------------------------------------------------

# 14. Passing Different Data Types

Functions can receive many kinds of Python objects as arguments.

The data type is preserved.

For example, a list can be passed to a function:

``` python
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]

my_function(my_fruits)
```

Output:

``` text
apple
banana
cherry
```

------------------------------------------------------------------------

## 14.1 Strings

``` python
def show(value):
    print(value)

show("Python")
```

------------------------------------------------------------------------

## 14.2 Numbers

``` python
def square(n):
    return n * n

print(square(5))
```

------------------------------------------------------------------------

## 14.3 Lists

``` python
def show_items(items):
    for item in items:
        print(item)
```

------------------------------------------------------------------------

## 14.4 Dictionaries

``` python
def show_student(student):
    print(student["name"])

show_student({
    "name": "Tahmid",
    "age": 20
})
```

The key idea is:

> Python functions can receive objects of many different types.

------------------------------------------------------------------------

# 15. Returning Different Data Types

A function can return any Python object.

Your source file demonstrates returning a list:

``` python
def my_function():
    return ["apple", "banana", "cherry"]
```

Then:

``` python
fruits = my_function()

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output:

``` text
apple
banana
cherry
```

------------------------------------------------------------------------

## Possible return types

A function can return:

``` python
int
float
str
bool
list
tuple
dict
set
None
```

and other Python objects.

Examples:

``` python
def get_number():
    return 10
```

``` python
def get_name():
    return "Tahmid"
```

``` python
def get_list():
    return [1, 2, 3]
```

``` python
def get_student():
    return {"name": "Tahmid", "age": 20}
```

------------------------------------------------------------------------

# 16. Positional-Only Arguments

Python allows you to require certain arguments to be passed
**positionally**.

Use `/` in the function definition.

Example:

``` python
def my_function(name, /):
    print("Hello", name)
```

Correct:

``` python
my_function("Emil")
```

Incorrect:

``` python
my_function(name="Emil")
```

The second call raises a `TypeError` because `name` has been declared
positional-only.

------------------------------------------------------------------------

## 16.1 What does `/` mean?

Everything before `/` is positional-only.

Example:

``` python
def function(a, b, /):
    pass
```

Both `a` and `b` must be passed positionally:

``` python
function(10, 20)
```

This is not allowed:

``` python
function(a=10, b=20)
```

------------------------------------------------------------------------

## 16.2 Why use positional-only arguments?

They can be useful when:

-   parameter names are considered an implementation detail
-   you want a simpler public API
-   you want to prevent keyword usage
-   you want freedom to rename parameters later without breaking
    keyword-based callers

------------------------------------------------------------------------

# 17. Keyword-Only Arguments

You can require arguments to be passed using keywords.

Use `*` before the keyword-only parameters.

Example:

``` python
def my_function(*, name):
    print("Hello", name)
```

Correct:

``` python
my_function(name="Emil")
```

Incorrect:

``` python
my_function("Emil")
```

The second call raises a `TypeError`.

------------------------------------------------------------------------

## 17.1 What does `*` mean?

Parameters after `*` are keyword-only.

Example:

``` python
def function(*, name, age):
    pass
```

Call:

``` python
function(name="Tahmid", age=20)
```

You must provide the parameter names.

------------------------------------------------------------------------

# 18. Combining Positional-Only and Keyword-Only

Python allows both rules in the same function.

Your source demonstrates:

``` python
def my_function(a, b, /, *, c, d):
    return a + b + c + d
```

The structure is:

``` text
a, b → positional-only
c, d → keyword-only
```

Correct call:

``` python
result = my_function(5, 10, c=15, d=20)

print(result)
```

Output:

``` text
50
```

------------------------------------------------------------------------

## 18.1 Understanding the syntax

``` python
def my_function(a, b, /, *, c, d):
```

Break it into sections:

``` text
a, b
 ↑
 positional-only
```

``` text
/
 ↑
 ends positional-only section
```

``` text
*
 ↑
 begins keyword-only section
```

``` text
c, d
 ↑
 keyword-only
```

------------------------------------------------------------------------

## 18.2 Valid calls

``` python
my_function(5, 10, c=15, d=20)
```

Also:

``` python
my_function(1, 2, c=3, d=4)
```

------------------------------------------------------------------------

## 18.3 Invalid calls

This is invalid:

``` python
my_function(a=5, b=10, c=15, d=20)
```

because `a` and `b` are positional-only.

This is also invalid:

``` python
my_function(5, 10, 15, 20)
```

because `c` and `d` are keyword-only.

------------------------------------------------------------------------

# 19. Why Functions Matter

Functions become increasingly important as programs get larger.

Imagine writing a program that calculates student results.

Without functions, you might have repeated code for:

``` text
input
calculate total
calculate average
calculate grade
print result
```

Functions allow you to separate the tasks:

``` python
def calculate_total(marks):
    ...

def calculate_average(total, count):
    ...

def calculate_grade(average):
    ...

def display_result(...):
    ...
```

Now each function has a focused responsibility.

------------------------------------------------------------------------

## 19.1 Reusability

Instead of:

``` python
print("Hello")
print("Hello")
print("Hello")
```

use:

``` python
def greet():
    print("Hello")

greet()
greet()
greet()
```

------------------------------------------------------------------------

## 19.2 Readability

Compare:

``` python
total = calculate_total(marks)
```

with a long block of calculation code.

A well-named function makes the program easier to understand.

------------------------------------------------------------------------

## 19.3 Maintainability

If the calculation changes, you can update the function in one place.

------------------------------------------------------------------------

## 19.4 Testing

Small functions are easier to test independently.

``` python
def add(a, b):
    return a + b
```

You can test:

``` python
print(add(2, 3))
print(add(10, 20))
```

------------------------------------------------------------------------

# 20. Common Mistakes

## Mistake 1: Defining a function but never calling it

``` python
def greet():
    print("Hello")
```

This only defines the function.

To execute:

``` python
greet()
```

------------------------------------------------------------------------

## Mistake 2: Forgetting parentheses when calling

Wrong:

``` python
greet
```

Correct:

``` python
greet()
```

The first expression refers to the function object; the second calls it.

------------------------------------------------------------------------

## Mistake 3: Confusing parameters and arguments

``` python
def greet(name):
    ...
```

`name` is a parameter.

``` python
greet("Tahmid")
```

`"Tahmid"` is an argument.

------------------------------------------------------------------------

## Mistake 4: Wrong number of arguments

``` python
def add(a, b):
    return a + b

add(5)
```

Missing one required argument.

------------------------------------------------------------------------

## Mistake 5: Positional argument after keyword argument

Wrong:

``` python
function(a=10, 20)
```

Correct:

``` python
function(10, 20)
```

or:

``` python
function(a=10, b=20)
```

------------------------------------------------------------------------

## Mistake 6: Expecting `print()` to return a value

``` python
def add(a, b):
    print(a + b)

result = add(2, 3)

print(result)
```

Output:

``` text
5
None
```

If you need the value:

``` python
def add(a, b):
    return a + b
```

------------------------------------------------------------------------

## Mistake 7: Trying to use a positional-only parameter as a keyword

Given:

``` python
def greet(name, /):
    print(name)
```

Wrong:

``` python
greet(name="Tahmid")
```

Correct:

``` python
greet("Tahmid")
```

------------------------------------------------------------------------

## Mistake 8: Passing a keyword-only parameter positionally

Given:

``` python
def greet(*, name):
    print(name)
```

Wrong:

``` python
greet("Tahmid")
```

Correct:

``` python
greet(name="Tahmid")
```

------------------------------------------------------------------------

## Mistake 9: Forgetting `return`

Wrong:

``` python
def square(n):
    n * n
```

Correct:

``` python
def square(n):
    return n * n
```

------------------------------------------------------------------------

# 21. Quick Revision Sheet

## Basic function

``` python
def function_name():
    ...
```

Call:

``` python
function_name()
```

------------------------------------------------------------------------

## Parameter

``` python
def greet(name):
    ...
```

`name` = parameter.

------------------------------------------------------------------------

## Argument

``` python
greet("Tahmid")
```

`"Tahmid"` = argument.

------------------------------------------------------------------------

## Return

``` python
def add(a, b):
    return a + b
```

Use:

``` python
result = add(5, 3)
```

------------------------------------------------------------------------

## No return

``` python
def greet():
    print("Hello")
```

Returns:

``` python
None
```

------------------------------------------------------------------------

## Default parameter

``` python
def greet(name="friend"):
    print(name)
```

Call:

``` python
greet()
greet("Tahmid")
```

------------------------------------------------------------------------

## Positional argument

``` python
greet("Tahmid")
```

------------------------------------------------------------------------

## Keyword argument

``` python
greet(name="Tahmid")
```

------------------------------------------------------------------------

## Positional + keyword

``` python
function(10, name="Tahmid")
```

Remember:

``` text
positional → before keyword
```

------------------------------------------------------------------------

## Positional-only

``` python
def function(name, /):
    ...
```

Call:

``` python
function("Tahmid")
```

------------------------------------------------------------------------

## Keyword-only

``` python
def function(*, name):
    ...
```

Call:

``` python
function(name="Tahmid")
```

------------------------------------------------------------------------

## Both

``` python
def function(a, b, /, *, c, d):
    ...
```

Call:

``` python
function(1, 2, c=3, d=4)
```

------------------------------------------------------------------------

# 22. Practice Files

  ------------------------------------------------------------------------
                            \# File                  Main Topics
  ---------------------------- --------------------- ---------------------
                            01 `01.functions.py`     Function definition,
                                                     calling functions,
                                                     naming rules,
                                                     `return`, `None`,
                                                     `pass`

                            02 `02.arguments.py`     Parameters,
                                                     arguments, argument
                                                     count, defaults,
                                                     positional/keyword
                                                     arguments, data
                                                     types, return values,
                                                     positional-only and
                                                     keyword-only
                                                     arguments
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# 🧠 Final Mental Model

Think of a function as a reusable machine:

``` text
             ARGUMENTS
                 ↓
        ┌─────────────────┐
        │    FUNCTION     │
        │                 │
        │    PROCESS      │
        │                 │
        └────────┬────────┘
                 ↓
              RETURN
                 ↓
              RESULT
```

For example:

``` python
def add(a, b):
    return a + b

result = add(10, 20)
```

Mental flow:

``` text
10 ──┐
     ├──→ add() ──→ 30
20 ──┘
```

And remember the four core ideas:

``` text
def       → define a function
call      → execute a function
parameter → variable in the definition
argument  → value passed during the call
return    → send a result back
```

------------------------------------------------------------------------

# 🎯 What You Should Be Able to Do After This Chapter

Before moving to the next Python topic, make sure you can:

-   [ ] Define a function using `def`
-   [ ] Call a function
-   [ ] Explain why functions are useful
-   [ ] Follow Python function naming rules
-   [ ] Distinguish parameters from arguments
-   [ ] Pass one or multiple arguments
-   [ ] Understand positional arguments
-   [ ] Understand keyword arguments
-   [ ] Mix positional and keyword arguments correctly
-   [ ] Use default parameter values
-   [ ] Pass strings, numbers, lists, dictionaries and other objects to
    functions
-   [ ] Return values using `return`
-   [ ] Explain the difference between `print()` and `return`
-   [ ] Understand that a function without an explicit return gives
    `None`
-   [ ] Use `pass` as a function placeholder
-   [ ] Use positional-only parameters with `/`
-   [ ] Use keyword-only parameters with `*`
-   [ ] Combine positional-only and keyword-only parameters
-   [ ] Build small reusable functions
-   [ ] Read a function call and identify which value goes to which
    parameter

------------------------------------------------------------------------

> **Revision tip:** Don't memorize function syntax only. Practice by
> taking a small problem and asking: **"What part can I turn into a
> reusable function?"** Start with simple functions such as `add()`,
> `is_even()`, `find_max()`, and `calculate_average()`, then gradually
> build functions that work with lists, strings and dictionaries.
