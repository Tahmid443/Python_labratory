# 🐍 Python Modules & Packages — Complete Revision Notes

> **Revision-focused notes based on the code in this `10.Module and Packages` folder.**
>
> This chapter covers Python modules, imports, the standard library, `random`, `requests`, `statistics`, `math`, and `cmath`. It is written as a quick-reference README so you can return here whenever you need to revise.

---

## 📚 Table of Contents

1. [What is a Module?](#1-what-is-a-module)
2. [What is a Package?](#2-what-is-a-package)
3. [Why Modules and Packages?](#3-why-modules-and-packages)
4. [Importing Modules](#4-importing-modules)
5. [Different Import Styles](#5-different-import-styles)
6. [Python Standard Library](#6-python-standard-library)
7. [Important Built-in Modules](#7-important-built-in-modules)
8. [Random Module](#8-random-module)
9. [Random Module — Methods](#9-random-module--methods)
10. [Requests Module](#10-requests-module)
11. [HTTP Methods with Requests](#11-http-methods-with-requests)
12. [Requests Parameters](#12-requests-parameters)
13. [Requests Response Object](#13-requests-response-object)
14. [Requests Error Handling](#14-requests-error-handling)
15. [Statistics Module](#15-statistics-module)
16. [Mean, Median and Mode](#16-mean-median-and-mode)
17. [Population vs Sample](#17-population-vs-sample)
18. [Math Module](#18-math-module)
19. [Math — Trigonometry](#19-math--trigonometry)
20. [Math — Logs, Powers and Roots](#20-math--logs-powers-and-roots)
21. [Math — Rounding and Remainders](#21-math--rounding-and-remainders)
22. [Math — Combinatorics](#22-math--combinatorics)
23. [Math — Numeric Utilities](#23-math--numeric-utilities)
24. [Math — Checking Functions](#24-math--checking-functions)
25. [Math Constants](#25-math-constants)
26. [cmath Module](#26-cmath-module)
27. [Complex Numbers](#27-complex-numbers)
28. [Complex Number Operations](#28-complex-number-operations)
29. [Polar and Rectangular Forms](#29-polar-and-rectangular-forms)
30. [Math vs cmath](#30-math-vs-cmath)
31. [Common Errors](#31-common-errors)
32. [Quick Comparison Tables](#32-quick-comparison-tables)
33. [Revision Checklist](#33-revision-checklist)
34. [Ultra-Quick Revision](#34-ultra-quick-revision)

---

# 1. What is a Module?

A **module** is a Python file containing reusable code.

A module can contain:

- variables
- functions
- classes
- constants
- executable statements

Example:

```python
# calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Another file can reuse it:

```python
import calculator

print(calculator.add(10, 20))
```

### Mental model

```text
calculator.py
      ↓
 reusable code
      ↓
 import into another program
```

---

# 2. What is a Package?

A **package** is a way to organize related Python modules into a directory structure.

Conceptually:

```text
my_project/
│
├── main.py
│
└── utilities/
    ├── module_a.py
    ├── module_b.py
    └── module_c.py
```

The package groups related functionality.

Modern Python packages can be regular packages or namespace packages. A traditional package commonly contains an `__init__.py` file.

Example:

```python
from utilities import module_a
```

---

# 3. Why Modules and Packages?

Without modules:

```text
one huge Python file
        ↓
hard to read
hard to maintain
hard to reuse
hard to test
```

With modules/packages:

```text
project
├── authentication.py
├── database.py
├── api.py
├── models.py
└── main.py
```

### Main benefits

- Code reuse
- Better organization
- Easier debugging
- Easier testing
- Separation of responsibilities
- Namespace management
- Easier collaboration

---

# 4. Importing Modules

The basic form is:

```python
import math
```

Then access members through the module name:

```python
math.sqrt(25)
math.pi
```

Output:

```text
5.0
3.141592653589793
```

---

# 5. Different Import Styles

## 5.1 Import the whole module

```python
import math

print(math.sqrt(16))
```

### Advantage

The namespace is clear:

```python
math.sqrt()
math.sin()
math.pi
```

---

## 5.2 Import selected functions

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))
```

Now you don't need:

```python
math.sqrt()
```

---

## 5.3 Import with an alias

```python
import math as m

print(m.sqrt(25))
```

Common example:

```python
import numpy as np
```

---

## 5.4 Import everything

```python
from math import *
```

This is generally discouraged because it can:

- pollute the namespace
- create naming conflicts
- make code harder to understand

Prefer:

```python
from math import sqrt
```

or:

```python
import math
```

---

# 6. Python Standard Library

Python comes with a very large collection of modules called the **Python Standard Library**.

The `01.built_in_modules.py` file provides an A-to-Z reference of standard-library modules.

You do **not** normally install these separately.

Examples:

```python
import math
import random
import statistics
import os
import json
import re
import datetime
```

---

# 7. Important Built-in Modules

The code lists many standard-library modules. You don't need to memorize every module, but you should recognize the important ones.

| Module | Main Purpose |
|---|---|
| `abc` | Abstract Base Classes |
| `argparse` | Command-line arguments |
| `array` | Typed numeric arrays |
| `asyncio` | Asynchronous programming |
| `atexit` | Run functions at program exit |
| `base64` | Base16/32/64 encoding |
| `bisect` | Binary search in sorted lists |
| `calendar` | Calendar operations |
| `collections` | Specialized containers |
| `configparser` | INI configuration files |
| `contextlib` | Context-manager utilities |
| `copy` | Shallow/deep copying |
| `csv` | CSV files |
| `dataclasses` | Data-focused classes |
| `datetime` | Dates and times |
| `decimal` | Decimal arithmetic |
| `difflib` | Compare sequences |
| `enum` | Enumerations |
| `functools` | Higher-order functions |
| `glob` | File pattern matching |
| `gzip` | GZIP compression |
| `hashlib` | Hashing |
| `heapq` | Heap/priority queue |
| `json` | JSON encoding/decoding |
| `logging` | Application logging |
| `math` | Real-number mathematics |
| `os` | Operating-system interface |
| `pathlib` | Filesystem paths |
| `pickle` | Object serialization |
| `pprint` | Pretty-print data |
| `queue` | Thread-safe queues |
| `random` | Pseudo-random numbers |
| `re` | Regular expressions |
| `statistics` | Statistical calculations |
| `time` | Time-related operations |
| `typing` | Type hints |
| `urllib` | URL handling |
| `uuid` | UUID generation |
| `xml` | XML processing |
| `zipfile` | ZIP archives |

### High-priority modules for a beginner

Focus first on:

```text
math
random
statistics
datetime
os
pathlib
json
re
collections
itertools
functools
```

---

# 8. Random Module

The `random` module generates **pseudo-random** values.

```python
import random
```

Important:

> `random` is designed for simulations, games, sampling and general-purpose randomness. It is **not** appropriate for security-sensitive secrets. For security-sensitive randomness, use Python's `secrets` module.

---

# 9. Random Module — Methods

## 9.1 `random()`

Returns a floating-point number in:

```text
0.0 <= x < 1.0
```

Example:

```python
import random

print(random.random())
```

Possible output:

```text
0.374829
```

---

## 9.2 `randint(a, b)`

Returns an integer between `a` and `b`, **including both endpoints**.

```python
random.randint(1, 10)
```

Possible results:

```text
1, 2, 3, ..., 10
```

---

## 9.3 `randrange()`

Works like choosing from a `range()`.

```python
random.randrange(1, 10)
```

Possible values:

```text
1 through 9
```

The stop value is excluded.

You can also use a step:

```python
random.randrange(0, 20, 2)
```

Possible values:

```text
0, 2, 4, ..., 18
```

### Remember

```text
randint(1, 10)   → 1 ... 10
randrange(1, 10) → 1 ... 9
```

---

## 9.4 `choice()`

Selects one random element:

```python
items = ["red", "green", "blue"]

print(random.choice(items))
```

---

## 9.5 `choices()`

Selects multiple elements **with replacement**.

```python
random.choices(items, k=3)
```

The same element can appear more than once.

Weights can also be used:

```python
random.choices(items, weights=[1, 5, 1], k=5)
```

---

## 9.6 `sample()`

Selects unique elements **without replacement**.

```python
random.sample(items, k=2)
```

If the population does not contain enough distinct elements for the requested sample size, an exception is raised.

### Remember

```text
choice()   → one item
choices()  → multiple, replacement allowed
sample()   → multiple, no replacement
```

---

## 9.7 `shuffle()`

Randomly rearranges a mutable sequence **in place**.

```python
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

Important:

```python
result = random.shuffle(numbers)
```

does not give you the shuffled list.

`shuffle()` modifies the list and returns `None`.

---

## 9.8 `uniform(a, b)`

Returns a random floating-point value around the interval between `a` and `b`.

```python
random.uniform(1, 10)
```

---

## 9.9 `getrandbits(k)`

Returns a non-negative integer generated from `k` random bits.

```python
random.getrandbits(8)
```

The result ranges from:

```text
0 to 255
```

for 8 bits.

---

## 9.10 `seed()`

Initializes the pseudo-random generator.

```python
random.seed(10)
```

Using the same seed makes the sequence reproducible:

```python
random.seed(42)
print(random.randint(1, 100))
```

This is useful for:

- testing
- debugging
- simulations
- reproducible experiments

---

## 9.11 `getstate()` and `setstate()`

Save and restore the generator's internal state.

```python
state = random.getstate()

# generate values...

random.setstate(state)
```

Useful when you need reproducible continuation of a pseudo-random sequence.

---

## 9.12 Distribution functions

The file also lists:

```python
random.triangular()
random.betavariate()
random.expovariate()
random.gammavariate()
random.gauss()
random.lognormvariate()
random.normalvariate()
random.vonmisesvariate()
random.paretovariate()
random.weibullvariate()
```

These generate values from different probability distributions.

For most beginner programs, focus first on:

```text
random()
randint()
randrange()
choice()
choices()
sample()
shuffle()
uniform()
seed()
```

---

# 10. Requests Module

`requests` is a popular **third-party Python library** for making HTTP requests.

Unlike `math`, `random`, and `statistics`, it is not part of the Python standard library.

Install it with:

```bash
pip install requests
```

Then:

```python
import requests
```

---

## What is HTTP?

HTTP is the protocol commonly used for communication between clients and web servers.

Typical flow:

```text
Python program
      ↓
HTTP request
      ↓
Web/API server
      ↓
HTTP response
      ↓
Python program
```

---

# 11. HTTP Methods with Requests

The code demonstrates:

```text
GET
HEAD
PATCH
POST
PUT
DELETE
REQUEST
```

---

## 11.1 GET

Used to retrieve data.

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code)
print(response.json())
```

Typical use:

```text
Read/fetch data
```

---

## 11.2 HEAD

Requests headers without normally retrieving the response body.

```python
response = requests.head(url)

print(response.status_code)
print(response.headers)
```

Useful for checking information about a resource without downloading the full body.

---

## 11.3 POST

Usually used to create a new resource or submit data.

```python
data = {
    "title": "New Post",
    "body": "Content",
    "userId": 1
}

response = requests.post(url, data=data)
```

For JSON APIs:

```python
response = requests.post(
    url,
    json={"name": "John", "age": 30}
)
```

---

## 11.4 PUT

Usually used to replace/update a resource.

```python
response = requests.put(
    url,
    json={
        "name": "Updated Name"
    }
)
```

### Mental model

```text
POST → create
PUT  → replace/update entire resource
PATCH → partially update
```

The exact semantics ultimately depend on the API.

---

## 11.5 PATCH

Used for a partial update.

```python
response = requests.patch(
    url,
    json={"status": "active"}
)
```

Only the specified fields need to change.

---

## 11.6 DELETE

Used to request deletion of a resource.

```python
response = requests.delete(url)
```

---

## 11.7 Generic `request()`

You can use one generic function for any HTTP method:

```python
response = requests.request(
    "GET",
    url
)
```

Example:

```python
response = requests.request(
    method="POST",
    url=url,
    json={"data": "value"},
    timeout=5
)
```

---

# 12. Requests Parameters

The code demonstrates the most important arguments.

## `params`

Adds query parameters to the URL.

```python
params = {
    "userId": 1,
    "id": 2
}

response = requests.get(url, params=params)
```

Conceptually:

```text
/api/posts?userId=1&id=2
```

---

## `data`

Sends form data or a request body.

```python
requests.post(
    url,
    data={"name": "Tahmid"}
)
```

---

## `json`

Sends a JSON request body.

```python
requests.post(
    url,
    json={
        "name": "Tahmid",
        "age": 20
    }
)
```

For JSON APIs, this is usually more convenient than manually encoding JSON.

---

## `headers`

Adds HTTP headers.

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

requests.get(url, headers=headers)
```

---

## `cookies`

Send cookies:

```python
requests.get(
    url,
    cookies={"session": "abc"}
)
```

---

## `auth`

Basic authentication can be supplied as:

```python
requests.get(
    url,
    auth=("username", "password")
)
```

Use the authentication method required by the actual API.

---

## `timeout`

Prevents a request from waiting indefinitely.

```python
requests.get(
    url,
    timeout=5
)
```

This is a very important production habit.

---

## `verify`

Controls SSL certificate verification.

```python
requests.get(
    url,
    verify=True
)
```

Normally, keep certificate verification enabled.

---

## `files`

Used for file uploads.

```python
files = {
    "file": ("filename.txt", b"File content")
}

requests.post(url, files=files)
```

---

# 13. Requests Response Object

After:

```python
response = requests.get(url)
```

the response object contains useful information.

## `status_code`

HTTP status:

```python
response.status_code
```

Common examples:

```text
200 → OK
201 → Created
204 → No Content
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

---

## `headers`

```python
response.headers
```

Contains response metadata.

---

## `text`

```python
response.text
```

Returns response body as text.

---

## `content`

```python
response.content
```

Returns response body as bytes.

Useful for binary content such as files/images.

---

## `json()`

```python
response.json()
```

Parses a JSON response into Python objects such as:

```text
dict
list
str
int
float
bool
None
```

If the response is not valid JSON, parsing can fail.

---

## `url`

```python
response.url
```

Shows the final URL.

---

## `elapsed`

```python
response.elapsed
```

Shows the approximate elapsed request time.

---

## `encoding`

```python
response.encoding
```

Shows/controls the character encoding used to decode response text.

---

## `cookies`

```python
response.cookies
```

Contains cookies returned by the server.

---

## `history`

```python
response.history
```

Contains redirect responses when redirects occurred.

---

# 14. Requests Error Handling

A good pattern from the code is:

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")

except requests.exceptions.ConnectionError as err:
    print(f"Connection error: {err}")

except requests.exceptions.Timeout as err:
    print(f"Timeout error: {err}")

except requests.exceptions.RequestException as err:
    print(f"General error: {err}")
```

---

## `raise_for_status()`

This is important:

```python
response.raise_for_status()
```

It raises an HTTP-related exception for unsuccessful HTTP status codes.

Instead of manually checking every status code:

```python
if response.status_code >= 400:
    ...
```

you can use:

```python
response.raise_for_status()
```

when appropriate.

---

## Requests exception hierarchy — useful idea

```text
requests.exceptions.RequestException
├── HTTPError
├── ConnectionError
│   ├── ...
├── Timeout
│   ├── ConnectTimeout
│   └── ReadTimeout
└── ...
```

A broad:

```python
except requests.exceptions.RequestException:
```

can be used as a final requests-specific fallback after more specific handlers.

---

# 15. Statistics Module

Python's `statistics` module provides functions for common statistical calculations.

```python
import statistics
```

The code covers:

```text
harmonic_mean()
mean()
median()
median_grouped()
median_high()
median_low()
mode()
pstdev()
stdev()
pvariance()
variance()
```

---

# 16. Mean, Median and Mode

## 16.1 Arithmetic Mean

Formula:

\[
\bar{x} = \frac{x_1+x_2+\cdots+x_n}{n}
\]

Python:

```python
statistics.mean([10, 20, 30, 40, 50])
```

Result:

```text
30
```

Use it for the ordinary average.

---

## 16.2 Median

The median is the middle value after sorting.

Example:

```text
1, 3, 5, 7, 9
```

Median:

```text
5
```

For an even number of values:

```text
1, 3, 5, 7
```

Middle values:

```text
3 and 5
```

Median:

```text
(3 + 5) / 2 = 4
```

Python:

```python
statistics.median(data)
```

---

## 16.3 `median_low()`

For an even-sized dataset, returns the lower middle value.

```python
statistics.median_low([1, 3, 5, 7])
```

Result:

```text
3
```

---

## 16.4 `median_high()`

For an even-sized dataset, returns the higher middle value.

```python
statistics.median_high([1, 3, 5, 7])
```

Result:

```text
5
```

---

## 16.5 `median_grouped()`

Used for grouped continuous data.

```python
statistics.median_grouped(data)
```

It supports an `interval` parameter.

---

## 16.6 Mode

The mode is the most frequently occurring value.

```python
data = [1, 2, 2, 3, 4, 4, 4, 5]

statistics.mode(data)
```

Result:

```text
4
```

It can also work with nominal data:

```python
statistics.mode(
    ["red", "blue", "red", "green", "red"]
)
```

Result:

```text
red
```

---

## 16.7 Harmonic Mean

Formula:

\[
H = \frac{n}{\frac{1}{x_1}+\frac{1}{x_2}+\cdots+\frac{1}{x_n}}
\]

Python:

```python
statistics.harmonic_mean([40, 60, 80])
```

It is especially useful for certain:

- rates
- speeds
- ratios

when the mathematical conditions for harmonic averaging apply.

---

# 17. Population vs Sample

This is one of the most important parts of the statistics module.

## Population

The dataset contains the **entire population**.

Use:

```python
statistics.pstdev()
statistics.pvariance()
```

---

## Sample

The dataset is only a **sample** from a larger population.

Use:

```python
statistics.stdev()
statistics.variance()
```

---

## Standard deviation

Population:

```python
statistics.pstdev(data)
```

Sample:

```python
statistics.stdev(data)
```

---

## Variance

Population:

```python
statistics.pvariance(data)
```

Sample:

```python
statistics.variance(data)
```

---

## Why are they different?

Population variance uses:

\[
\sigma^2 =
\frac{\sum (x_i-\mu)^2}{N}
\]

Sample variance uses Bessel's correction:

\[
s^2 =
\frac{\sum (x_i-\bar{x})^2}{n-1}
\]

### Memory trick

```text
pvariance → population
variance  → sample

pstdev → population
stdev  → sample
```

---

# 18. Math Module

The `math` module provides mathematical functions for **real numbers**.

```python
import math
```

It contains functions for:

- trigonometry
- logarithms
- exponentials
- powers
- roots
- rounding
- combinatorics
- number utilities
- special functions
- floating-point checks

---

# 19. Math — Trigonometry

Python's trigonometric functions use **radians**.

```python
math.sin(math.pi / 2)
```

Result:

```text
1.0
```

---

## Basic functions

```python
math.sin(x)
math.cos(x)
math.tan(x)
```

Example:

```python
math.cos(math.pi)
```

→ `-1.0`

---

## Inverse trigonometric functions

```python
math.asin(x)
math.acos(x)
math.atan(x)
```

They return angles in radians.

Example:

```python
math.atan(1)
```

→ approximately:

```text
π / 4
```

---

## `atan2(y, x)`

```python
math.atan2(y, x)
```

Computes an angle from the coordinates `(x, y)` and handles the quadrant correctly.

This is usually preferable to manually computing:

```python
math.atan(y / x)
```

when you have coordinate components.

---

## Hyperbolic functions

```python
math.sinh(x)
math.cosh(x)
math.tanh(x)
```

Inverse hyperbolic functions:

```python
math.asinh(x)
math.acosh(x)
math.atanh(x)
```

---

# 20. Math — Logs, Powers and Roots

## `exp(x)`

Calculates:

\[
e^x
\]

```python
math.exp(1)
```

---

## `expm1(x)`

Calculates:

\[
e^x-1
\]

and is designed to be accurate for small values of `x`.

```python
math.expm1(0.001)
```

---

## `log(x)`

Natural logarithm:

\[
\ln(x)
\]

```python
math.log(math.e)
```

→ `1.0`

With a base:

```python
math.log(100, 10)
```

→ `2.0`

---

## `log10(x)`

Base-10 logarithm:

```python
math.log10(1000)
```

→ `3.0`

---

## `log2(x)`

Base-2 logarithm:

```python
math.log2(8)
```

→ `3.0`

---

## `log1p(x)`

Calculates:

\[
\ln(1+x)
\]

and is useful for numerical accuracy when `x` is very small.

---

## `pow(x, y)`

Calculates:

\[
x^y
\]

```python
math.pow(2, 3)
```

→ `8.0`

---

## `sqrt(x)`

Square root:

```python
math.sqrt(16)
```

→ `4.0`

---

## `isqrt(x)`

Integer square root, rounded down.

```python
math.isqrt(17)
```

→ `4`

Because:

```text
sqrt(17) ≈ 4.123
floor → 4
```

---

## `hypot()`

Calculates Euclidean norm.

For 2D:

\[
\sqrt{x^2+y^2}
\]

```python
math.hypot(3, 4)
```

→ `5.0`

It also accepts more coordinates.

---

# 21. Math — Rounding and Remainders

## `ceil()`

Rounds toward positive infinity.

```python
math.ceil(4.2)   # 5
math.ceil(-4.2)  # -4
```

---

## `floor()`

Rounds toward negative infinity.

```python
math.floor(4.8)   # 4
math.floor(-4.8)  # -5
```

---

## `trunc()`

Removes the fractional part, toward zero.

```python
math.trunc(4.8)   # 4
math.trunc(-4.8)  # -4
```

### Important difference

```text
ceil(-4.8)  → -4
floor(-4.8) → -5
trunc(-4.8) → -4
```

---

## `fmod(x, y)`

Returns a floating-point remainder.

```python
math.fmod(10, 3)
```

→ `1.0`

---

## `remainder(x, y)`

Returns the IEEE-style remainder based on the closest multiple of `y`.

It is **not simply the same operation as `%`**.

---

# 22. Math — Combinatorics

## Factorial

\[
n! = n(n-1)(n-2)\cdots1
\]

```python
math.factorial(5)
```

→ `120`

---

## Combination

\[
^nC_k = \frac{n!}{k!(n-k)!}
\]

Python:

```python
math.comb(5, 2)
```

→ `10`

### Important

Combination does **not** care about order.

---

## Permutation

\[
^nP_k = \frac{n!}{(n-k)!}
\]

Python:

```python
math.perm(5, 2)
```

→ `20`

### Important

Permutation **does** care about order.

---

## Memory trick

```text
Combination → order doesn't matter
Permutation  → order matters
```

Example choosing 2 people:

```text
AB and BA
```

are the same combination but different permutations.

---

# 23. Math — Numeric Utilities

## `fabs(x)`

Floating-point absolute value:

```python
math.fabs(-5)
```

→ `5.0`

---

## `copysign(x, y)`

Returns the magnitude of `x` with the sign of `y`.

```python
math.copysign(5, -1)
```

→ `-5.0`

---

## `gcd(a, b)`

Greatest common divisor.

```python
math.gcd(12, 18)
```

→ `6`

---

## `fsum(iterable)`

Accurate floating-point sum.

```python
math.fsum([0.1, 0.2, 0.3])
```

This is useful when floating-point summation accuracy matters.

---

## `prod(iterable)`

Product of all elements:

```python
math.prod([1, 2, 3, 4])
```

→ `24`

---

## `dist(p, q)`

Euclidean distance between points.

```python
math.dist([0, 0], [3, 4])
```

→ `5.0`

---

## `frexp(x)`

Splits a number into mantissa and exponent:

```python
m, e = math.frexp(10)
```

Such that:

\[
10 = m \times 2^e
\]

---

## `ldexp(x, i)`

Performs:

\[
x \times 2^i
\]

It is essentially the inverse operation of `frexp()`.

---

## `gamma(x)`

Gamma function.

For positive integers:

\[
\Gamma(n) = (n-1)!
\]

Therefore:

```python
math.gamma(5)
```

→ `24.0`

---

## `lgamma(x)`

Returns:

\[
\ln(|\Gamma(x)|)
\]

---

## `erf()` and `erfc()`

Used in mathematical/statistical applications involving the error function.

```python
math.erf(x)
math.erfc(x)
```

with:

\[
erfc(x)=1-erf(x)
\]

---

# 24. Math — Checking Functions

## `isclose(a, b)`

Checks whether two floating-point values are sufficiently close.

```python
math.isclose(0.1 + 0.2, 0.3)
```

→ `True`

This is important because floating-point calculations can contain small representation errors.

---

## `isfinite(x)`

Checks that a number is neither infinity nor NaN.

```python
math.isfinite(5)          # True
math.isfinite(float("inf"))  # False
math.isfinite(float("nan"))  # False
```

---

## `isinf(x)`

Checks for positive or negative infinity.

```python
math.isinf(float("inf"))
```

→ `True`

---

## `isnan(x)`

Checks for NaN:

```python
math.isnan(float("nan"))
```

→ `True`

---

# 25. Math Constants

Important constants:

```python
math.pi
math.e
math.tau
math.inf
math.nan
```

### `pi`

\[
\pi \approx 3.141592653589793
\]

### `e`

\[
e \approx 2.718281828459045
\]

### `tau`

\[
\tau = 2\pi
\]

### `inf`

Positive infinity.

### `nan`

Not-a-Number.

---

# 26. cmath Module

`cmath` provides mathematical operations for **complex numbers**.

```python
import cmath
```

Many functions look similar to `math`:

```python
cmath.sin()
cmath.cos()
cmath.sqrt()
cmath.log()
```

But they are designed for complex-number calculations.

---

# 27. Complex Numbers

A complex number has the form:

\[
z=a+bj
\]

where:

- `a` = real part
- `b` = imaginary part
- `j` = imaginary unit

Python:

```python
z = 3 + 4j
```

---

## Creating complex numbers

Directly:

```python
z1 = 3 + 4j
```

Using `complex()`:

```python
z2 = complex(3, 4)
```

Both represent:

```text
3 + 4j
```

---

# 28. Complex Number Operations

Given:

```python
a = 1 + 2j
b = 3 + 4j
```

Python supports:

```python
a + b
a - b
a * b
a / b
a ** 2
```

Complex arithmetic follows the usual mathematical rules.

---

## Real and imaginary components

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

Results:

```text
3.0
4.0
```

---

## Conjugate

```python
z.conjugate()
```

For:

\[
3+4j
\]

the conjugate is:

\[
3-4j
\]

---

# 29. Polar and Rectangular Forms

A complex number can be represented in two major ways.

## Rectangular form

\[
z=x+yj
\]

Example:

```text
3 + 4j
```

---

## Polar form

\[
z = r(\cos\theta+j\sin\theta)
\]

where:

- `r` = magnitude
- `θ` = phase/argument

---

## `phase()`

```python
z = 1 + 1j

angle = cmath.phase(z)
```

Returns the angle in radians.

For `1 + 1j`:

\[
\theta=\frac{\pi}{4}
\]

---

## `polar()`

Converts rectangular form to:

```text
(r, theta)
```

Example:

```python
r, theta = cmath.polar(3 + 4j)
```

For `3 + 4j`:

```text
r = 5
theta ≈ 0.9273 radians
```

---

## `rect()`

Converts polar coordinates back to rectangular form:

```python
z = cmath.rect(r, theta)
```

### Conversion cycle

```text
3 + 4j
   ↓
cmath.polar()
   ↓
(r, θ)
   ↓
cmath.rect()
   ↓
3 + 4j
```

---

# 30. Math vs cmath

This is a very important comparison.

| `math` | `cmath` |
|---|---|
| Real-number mathematics | Complex-number mathematics |
| `sqrt(-1)` raises `ValueError` | `sqrt(-1+0j)` returns `1j` |
| Real-valued results for supported real inputs | Generally complex-valued results |
| No complex phase/polar helpers | Has `phase()`, `polar()`, `rect()` |

Example:

```python
import math
import cmath

math.sqrt(4)
```

→ `2.0`

But:

```python
cmath.sqrt(-1 + 0j)
```

→ `1j`

---

## cmath functions in the code

### Trigonometric

```python
cmath.acos()
cmath.asin()
cmath.atan()
cmath.cos()
cmath.sin()
cmath.tan()
```

### Hyperbolic

```python
cmath.acosh()
cmath.asinh()
cmath.atanh()
cmath.cosh()
cmath.sinh()
cmath.tanh()
```

### Exponential/logarithmic

```python
cmath.exp()
cmath.log()
cmath.log10()
```

### Checking

```python
cmath.isclose()
cmath.isfinite()
cmath.isinf()
cmath.isnan()
```

### Complex-coordinate helpers

```python
cmath.phase()
cmath.polar()
cmath.rect()
```

### Root

```python
cmath.sqrt()
```

---

# 31. Common Errors

## `StatisticsError`

Can occur when statistical functions receive invalid/insufficient data, such as:

```python
statistics.mean([])
```

or when a function requires more observations than provided.

---

## `ValueError`

Example:

```python
cmath.log(0 + 0j)
```

can raise `ValueError`.

---

## `ZeroDivisionError`

Example:

```python
(1 + 2j) / (0 + 0j)
```

raises:

```text
ZeroDivisionError
```

---

## `OverflowError`

Very large exponential calculations can overflow.

Example from the code:

```python
cmath.exp(1000 + 1000j)
```

may raise:

```text
OverflowError
```

---

## Requests exceptions

Remember the main ones:

```python
requests.exceptions.HTTPError
requests.exceptions.ConnectionError
requests.exceptions.Timeout
requests.exceptions.RequestException
```

---

# 32. Quick Comparison Tables

## Module types

| Type | Example | Install? |
|---|---|---|
| User-defined module | `calculator.py` | No |
| Standard-library module | `math` | No |
| Third-party package/library | `requests` | Usually yes |

---

## Random selection

| Function | Meaning |
|---|---|
| `random()` | Random float `[0, 1)` |
| `randint(a,b)` | Integer including both endpoints |
| `randrange()` | Random value from a range |
| `choice()` | One random item |
| `choices()` | Multiple items, replacement allowed |
| `sample()` | Multiple items, no replacement |
| `shuffle()` | Shuffle a mutable sequence in place |
| `uniform()` | Random float in an interval |
| `seed()` | Initialize/reproduce pseudo-random sequence |

---

## HTTP methods

| Method | Typical purpose |
|---|---|
| `GET` | Retrieve |
| `POST` | Create/submit |
| `PUT` | Replace/update |
| `PATCH` | Partial update |
| `DELETE` | Delete |
| `HEAD` | Headers only |

---

## Statistics

| Function | Meaning |
|---|---|
| `mean()` | Arithmetic average |
| `median()` | Middle value |
| `median_low()` | Lower middle |
| `median_high()` | Higher middle |
| `median_grouped()` | Grouped continuous median |
| `mode()` | Most frequent value |
| `harmonic_mean()` | Harmonic average |
| `pstdev()` | Population standard deviation |
| `stdev()` | Sample standard deviation |
| `pvariance()` | Population variance |
| `variance()` | Sample variance |

---

## Math

| Function | Meaning |
|---|---|
| `sqrt()` | Square root |
| `isqrt()` | Integer square root |
| `pow()` | Power |
| `exp()` | `e^x` |
| `log()` | Natural/base logarithm |
| `log10()` | Base-10 logarithm |
| `log2()` | Base-2 logarithm |
| `ceil()` | Round toward +∞ |
| `floor()` | Round toward -∞ |
| `trunc()` | Remove fractional part |
| `factorial()` | Factorial |
| `comb()` | Combination |
| `perm()` | Permutation |
| `gcd()` | Greatest common divisor |
| `dist()` | Euclidean distance |
| `isclose()` | Approximate equality |

---

# 33. Revision Checklist

Before moving on, make sure you can explain:

### Modules & Packages

- [ ] What is a module?
- [ ] What is a package?
- [ ] Why use modules?
- [ ] Why use packages?
- [ ] `import module`
- [ ] `from module import function`
- [ ] `import module as alias`
- [ ] Why `from module import *` is usually discouraged
- [ ] Difference between standard-library and third-party packages

### Random

- [ ] `random()`
- [ ] `randint()`
- [ ] `randrange()`
- [ ] `choice()`
- [ ] `choices()`
- [ ] `sample()`
- [ ] `shuffle()`
- [ ] `uniform()`
- [ ] `seed()`
- [ ] Why `random` is not for security-sensitive secrets

### Requests

- [ ] What HTTP is
- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] PATCH
- [ ] DELETE
- [ ] HEAD
- [ ] `requests.request()`
- [ ] `params`
- [ ] `data`
- [ ] `json`
- [ ] `headers`
- [ ] `auth`
- [ ] `timeout`
- [ ] `verify`
- [ ] `files`
- [ ] `status_code`
- [ ] `text`
- [ ] `content`
- [ ] `json()`
- [ ] `raise_for_status()`
- [ ] Request exception handling

### Statistics

- [ ] Mean
- [ ] Median
- [ ] Mode
- [ ] Harmonic mean
- [ ] Low/high median
- [ ] Grouped median
- [ ] Population standard deviation
- [ ] Sample standard deviation
- [ ] Population variance
- [ ] Sample variance
- [ ] Difference between `N` and `N-1`

### Math

- [ ] Trigonometric functions
- [ ] Radians vs degrees
- [ ] `atan2()`
- [ ] Logarithms
- [ ] Powers
- [ ] Roots
- [ ] `ceil`, `floor`, `trunc`
- [ ] Factorial
- [ ] Combination
- [ ] Permutation
- [ ] GCD
- [ ] Distance
- [ ] `isclose`
- [ ] `isfinite`
- [ ] `isinf`
- [ ] `isnan`
- [ ] Math constants

### Complex Numbers

- [ ] Complex number form `a+bj`
- [ ] `complex()`
- [ ] `.real`
- [ ] `.imag`
- [ ] `.conjugate()`
- [ ] `cmath.sqrt()`
- [ ] `cmath.phase()`
- [ ] `cmath.polar()`
- [ ] `cmath.rect()`
- [ ] Math vs cmath

---

# 34. Ultra-Quick Revision

## Import

```python
import math
```

```python
from math import sqrt
```

```python
import math as m
```

---

## Random

```python
import random

random.random()
random.randint(1, 10)
random.randrange(1, 10)
random.choice([1, 2, 3])
random.choices([1, 2, 3], k=2)
random.sample([1, 2, 3], k=2)
random.shuffle(my_list)
random.uniform(1, 10)
random.seed(42)
```

---

## Requests

```python
import requests

response = requests.get(url)

response.status_code
response.headers
response.text
response.content
response.json()
response.url
```

Common:

```python
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()
requests.head()
requests.request()
```

Best-practice pattern:

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(e)
```

---

## Statistics

```python
import statistics

statistics.mean(data)
statistics.median(data)
statistics.mode(data)
statistics.harmonic_mean(data)

statistics.pstdev(data)
statistics.stdev(data)

statistics.pvariance(data)
statistics.variance(data)
```

Remember:

```text
p = population
no p = sample
```

---

## Math

```python
import math

math.pi
math.e
math.tau

math.sqrt(16)
math.isqrt(17)

math.pow(2, 3)
math.exp(1)

math.log(100, 10)
math.log10(100)
math.log2(8)

math.sin(math.pi / 2)
math.cos(math.pi)
math.tan(math.pi / 4)

math.ceil(4.2)
math.floor(4.8)
math.trunc(-4.8)

math.factorial(5)
math.comb(5, 2)
math.perm(5, 2)

math.gcd(12, 18)
math.dist([0, 0], [3, 4])

math.isclose(a, b)
math.isfinite(x)
math.isinf(x)
math.isnan(x)
```

---

## Complex numbers

```python
import cmath

z = 3 + 4j

z.real
z.imag
z.conjugate()

cmath.sqrt(-1 + 0j)
cmath.phase(z)
cmath.polar(z)
cmath.rect(r, theta)
```

---

# 🎯 Final Mental Model

Think about the entire chapter like this:

```text
                    MODULES & PACKAGES
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       Standard         Third-party      User-defined
       Library           Library           Modules
          │                │                │
    ┌─────┼─────┐       requests       my_file.py
    │     │     │
   math random statistics
    │
   cmath
```

### What to remember most

```text
MODULE
→ reusable Python file

PACKAGE
→ organized collection of modules

IMPORT
→ bring reusable code into your program

random
→ pseudo-random values and sampling

requests
→ communicate with HTTP APIs/web servers

statistics
→ mean, median, mode, variance, standard deviation

math
→ real-number mathematical functions

cmath
→ complex-number mathematical functions
```

> **The goal is not to memorize every function. Understand what each module is for, know the most common functions, and be able to quickly look up the exact parameters when needed.**
