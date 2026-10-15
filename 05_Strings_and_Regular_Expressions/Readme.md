# 05. Python Strings and Regular Expressions

Strings are one of the most important data types in Python. They are used to represent text, process input, format output, search for patterns, and manipulate textual data.

Regular expressions (regex) provide a powerful way to search, match, extract, validate, and replace text using patterns.

These concepts are useful in everyday Python programming, data processing, and competitive programming.

## Table of Contents

1. [String Formatting](#1-string-formatting)
2. [F-Strings](#2-f-strings)
3. [String Slicing](#3-string-slicing)
4. [String Methods](#4-string-methods)
5. [Regular Expression Basics](#5-regular-expression-basics)
6. [Regex Groups](#6-regex-groups)
7. [Regex Practice](#7-regex-practice)
8. [Regex Quick Reference](#8-regex-quick-reference)
9. [Common Mistakes](#9-common-mistakes)
10. [Time Complexity](#10-time-complexity)
11. [Practice Problems](#11-practice-problems)

---

## 1. String Formatting

**File:** `01_string_formatting.py`

String formatting inserts values into strings and controls how those values appear.

### 1.1 Old-Style Formatting (`%`)

```python
name = "Alice"
age = 30

print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % 3.14159)
```

Output:

```text
Name: Alice, Age: 30
Pi: 3.14
```

Common format specifiers:

| Specifier | Meaning |
|---|---|
| `%s` | String representation |
| `%d` | Integer |
| `%f` | Floating-point number |
| `%.2f` | Float with two digits after the decimal point |

This style is still supported, but modern Python code usually prefers f-strings.

### 1.2 The `str.format()` Method

```python
name = "Alice"
age = 30

print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))
```

Output:

```text
Name: Alice, Age: 30
Name: Alice, Age: 30
Name: Alice, Age: 30
```

You can use automatic positions, explicit positions, or named placeholders.

### 1.3 Text Alignment

```python
print("{:<10}|".format("left"))
print("{:>10}|".format("right"))
print("{:^10}|".format("center"))
```

Output:

```text
left      |
     right|
  center  |
```

- `<` aligns text to the left.
- `>` aligns text to the right.
- `^` centers text.
- `10` specifies the minimum field width.

### 1.4 Formatting Numbers

```python
print("{:.2f}".format(3.14159))
print("{:,}".format(1000000))
print("{:%}".format(0.25))
print("{:b}".format(255))
print("{:o}".format(255))
print("{:x}".format(255))
```

Output:

```text
3.14
1,000,000
25.000000%
11111111
377
ff
```

Useful format specifiers:

| Specifier | Result or meaning |
|---|---|
| `:.2f` | Two decimal places |
| `:,` | Thousands separators |
| `:%` | Percentage representation |
| `:b` | Binary |
| `:o` | Octal |
| `:x` | Lowercase hexadecimal |
| `:05d` | Integer padded to width five with zeros |

### 1.5 F-Strings: The Recommended Approach

```python
name = "Alice"
age = 30

print(f"Name: {name}, Age: {age}")
print(f"Next year: {age + 1}")
print(f"Pi: {3.14159:.2f}")
```

Output:

```text
Name: Alice, Age: 30
Next year: 31
Pi: 3.14
```

F-strings allow expressions inside `{}`.

```python
print(f"Upper: {name.upper()}")
print(f"Sum: {1 + 2 + 3}")
```

Python evaluates the expressions and inserts their results into the string.

### 1.6 Debug Formatting

Python 3.8 and later supports the `=` debug specifier.

```python
name = "Alice"
age = 30

print(f"{name=}, {age=}")
print(f"{age + 1 = }")
```

Output:

```text
name='Alice', age=30
age + 1 = 31
```

This is useful when debugging algorithms and checking intermediate values.

**Key takeaway:** Prefer f-strings for modern Python code. Use `str.format()` when appropriate for templates and older codebases.

---

## 2. F-Strings

**File:** `02_f_strings.py`

F-strings are formatted string literals prefixed with `f` or `F`.

### 2.1 Basic Expressions

```python
name = "Alice"
age = 30

print(f"Hello, {name}!")
print(f"{age + 1} years old next year")
print(f"{name.upper()}")
```

Output:

```text
Hello, Alice!
31 years old next year
ALICE
```

### 2.2 Conditional Expressions

```python
age = 30

print(f"{'even' if age % 2 == 0 else 'odd'}")
```

Output:

```text
even
```

The expression inside the braces is evaluated before the final string is produced.

### 2.3 Format Specifications

```python
pi = 3.14159
age = 30

print(f"{pi:.3f}")
print(f"{age:05d}")
print(f"{1000000:,}")
```

Output:

```text
3.142
00030
1,000,000
```

The format specification appears after a colon.

General form:

```python
f"{expression:format_spec}"
```

Examples:

- `f"{x:.2f}"` — two decimal places.
- `f"{n:05d}"` — zero-padded integer.
- `f"{n:,}"` — thousands separators.
- `f"{text:>10}"` — right-aligned text.

### 2.4 Dictionary and Attribute Access

```python
person = {"name": "Bob", "age": 25}

print(f"{person['name']} is {person['age']}")
```

Output:

```text
Bob is 25
```

F-strings can also access object attributes:

```python
class Person:
    def __init__(self):
        self.name = "Alice"

p = Person()
print(f"{p.name}")
```

Output:

```text
Alice
```

### 2.5 Multiline F-Strings

```python
name = "Alice"
age = 30
pi = 3.14159

msg = (
    f"Name: {name}\n"
    f"Age:  {age}\n"
    f"Pi:   {pi:.2f}"
)

print(msg)
```

Output:

```text
Name: Alice
Age:  30
Pi:   3.14
```

Adjacent string literals are combined, making this approach useful for readable multiline output.

### 2.6 Escaping Braces

To display literal curly braces, double them.

```python
print(f"{{literal braces}}")
```

Output:

```text
{literal braces}
```

**Important:** F-strings evaluate expressions. Avoid evaluating untrusted text as code, and do not use f-strings as a substitute for parameterized SQL queries.

---

## 3. String Slicing

**File:** `03_slicing.py`

Slicing extracts a portion of a sequence, such as a string, list, or tuple.

### 3.1 Basic Slicing

General syntax:

```python
sequence[start:stop:step]
```

- `start`: Index where slicing begins, inclusive.
- `stop`: Index where slicing ends, exclusive.
- `step`: Distance between selected elements.

Example:

```python
s = "Python Programming"

print(s[0:6])
print(s[7:])
print(s[:6])
print(s[:])
```

Output:

```text
Python
Programming
Python
Python Programming
```

If omitted, `start` and `stop` use the sequence boundaries, depending on the step direction.

### 3.2 Negative Indexing

Negative indices count from the end of the sequence.

```python
s = "Python Programming"

print(s[-11:])
print(s[:-12])
```

Output:

```text
Programming
Python
```

For `"Python Programming"`:

- `s[-1]` is the final character, `"g"`.
- `s[-11:]` extracts `"Programming"`.
- `s[:-12]` extracts `"Python"`.

### 3.3 Slicing with a Step

```python
s = "Python Programming"

print(s[::2])
print(s[::-1])
```

The first expression selects every second character. The second reverses the string.

```python
word = "Python"
print(word[::-1])
```

Output:

```text
nohtyP
```

Reverse a list similarly:

```python
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
```

### 3.4 Reverse Words Instead of Characters

```python
s = "Python Programming"

words = s.split()
print(" ".join(words[::-1]))
```

Output:

```text
Programming Python
```

This reverses the order of words, not the characters inside each word.

### 3.5 Slice Assignment

Strings are immutable, so their characters cannot be replaced through slice assignment. Lists are mutable and support it.

```python
lst = [1, 2, 3, 4, 5]

lst[1:4] = [10, 20, 30]
print(lst)
```

Output:

```text
[1, 10, 20, 30, 5]
```

Slice assignment with a step other than `1` requires the replacement iterable to have the same number of elements as the selected slice.

```python
lst[::2] = [0, 0, 0]
print(lst)
```

Output:

```text
[0, 10, 0, 30, 0]
```

### 3.6 Deleting a Slice

```python
lst = [1, 2, 3, 4, 5]

del lst[1:3]
print(lst)
```

Output:

```text
[1, 4, 5]
```

The selected elements are removed from the list.

### 3.7 Copying a List with Slicing

```python
original = [1, 2, 3]
copy = original[:]

copy.append(4)

print(original)
print(copy)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

`original[:]` creates a shallow copy of the list. It does not recursively copy nested objects.

### 3.8 Out-of-Range Slices

```python
s = "Python"

print(s[100:200])
```

Output:

```text

```

A slice with an out-of-range boundary generally returns an empty sequence rather than raising `IndexError`. Direct indexing, such as `s[100]`, does raise `IndexError`.

**Competitive programming tip:** Become comfortable with `s[::-1]`, `arr[:]`, `arr[left:right]`, and negative indices. They are common Python idioms.

---

## 4. String Methods

**File:** `04_string_methods.py`

Strings are immutable in Python. String methods generally return a new string instead of modifying the original string.

### 4.1 Removing Whitespace

```python
s = "  Hello, World!  "

print(s.strip())
print(s.lstrip())
print(s.rstrip())
```

- `strip()` removes leading and trailing whitespace.
- `lstrip()` removes leading whitespace.
- `rstrip()` removes trailing whitespace.

You can provide a set of characters to remove:

```python
print(s.strip(" !"))
```

The argument specifies a set of removable characters, not a complete substring.

### 4.2 Changing Letter Case

```python
s = "  Hello, World!  "

print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.capitalize())
```

| Method | Purpose |
|---|---|
| `upper()` | Convert letters to uppercase |
| `lower()` | Convert letters to lowercase |
| `title()` | Capitalize words according to Python's title-casing rules |
| `swapcase()` | Reverse the case of letters |
| `capitalize()` | Capitalize the first character and lowercase the rest |

### 4.3 Searching Strings

```python
s = "Hello, World!"

print(s.find("World"))
print(s.find("xyz"))
print(s.index("World"))
print(s.count("l"))
print(s.startswith("Hello"))
print(s.endswith("!"))
```

Important differences:

- `find(substring)` returns the first matching index or `-1`.
- `index(substring)` returns the first matching index or raises `ValueError`.
- `count(substring)` counts non-overlapping occurrences.
- `startswith()` and `endswith()` return Boolean values.

Use `find()` when absence is expected and you want to handle it without an exception.

### 4.4 Replacing Text

```python
s = "Hello, World!"

print(s.replace("World", "Python"))
print(s.replace("l", "L", 2))
```

`replace(old, new, count)` returns a new string. The optional `count` limits the number of replacements.

### 4.5 Splitting and Joining

```python
csv = "a,b,c"

print(csv.split(","))
print(" ".join(["a", "b", "c"]))
```

Output:

```text
['a', 'b', 'c']
a b c
```

- `split(separator)` divides a string into a list.
- `join(iterable)` joins strings using the separator.

A particularly useful distinction:

```python
print("  a   b  ".split())
print("  a   b  ".split(" "))
```

Calling `split()` without an argument treats runs of whitespace as separators and ignores leading and trailing whitespace. Passing `" "` explicitly splits on individual space characters, so empty strings may appear.

### 4.6 Splitting Lines

```python
text = "line1\nline2"
print(text.splitlines())
```

Output:

```text
['line1', 'line2']
```

This is useful for processing multiline input and file contents.

### 4.7 Checking String Contents

```python
print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("   ".isspace())
print("Hello".istitle())
print("HELLO".isupper())
print("hello".islower())
```

| Method | Returns `True` when |
|---|---|
| `isalpha()` | All characters are alphabetic and the string is non-empty |
| `isdigit()` | All characters are digits according to the method's Unicode rules and the string is non-empty |
| `isalnum()` | All characters are alphabetic or numeric and the string is non-empty |
| `isspace()` | All characters are whitespace and the string is non-empty |
| `istitle()` | The string follows title-case rules |
| `isupper()` | There is at least one cased character and all cased characters are uppercase |
| `islower()` | There is at least one cased character and all cased characters are lowercase |

For ASCII-only competitive programming problems, these methods are often sufficient for simple input validation. Remember that Python's string classification methods support Unicode, so their behavior is broader than ASCII checks.

### 4.8 Padding Strings

```python
print("5".zfill(3))
print("hi".center(10, "*"))
print("hi".ljust(10, "."))
print("hi".rjust(10, "."))
```

Output:

```text
005
****hi****
hi........
........hi
```

These methods are useful for formatting output.

### 4.9 `casefold()` vs. `lower()`

`casefold()` is designed for caseless text comparison.

```python
print("STRASSE".casefold() == "straße".casefold())
```

Output:

```text
True
```

For ASCII-only data, `lower()` is often sufficient. For Unicode text comparisons, `casefold()` can handle additional case-equivalence rules.

### 4.10 Encoding and Decoding

Strings are Unicode text. Encoding converts text into bytes, and decoding converts bytes back into text.

```python
b = "hello".encode("utf-8")
print(b)

print(b.decode("utf-8"))
```

Output:

```text
b'hello'
hello
```

Encoding is important when working with files, network protocols, and binary data.

---

## 5. Regular Expression Basics

**File:** `05_regex_basics.py`

A regular expression, or regex, is a pattern used to match text.

Python provides the built-in `re` module.

```python
import re
```

Use raw strings, such as `r"\d+"`, for most regex patterns. They make backslashes easier to read because Python does not process them as ordinary string escape sequences first.

### 5.1 `re.search()`

Finds the first match anywhere in the string.

```python
import re

text = "The year is 2024 and the month is 10."

m = re.search(r"\d+", text)

if m:
    print(m.group())
    print(m.start())
    print(m.end())
```

Output:

```text
2024
12
16
```

Match objects provide useful methods:

- `group()` returns the matched text.
- `start()` returns the starting index.
- `end()` returns the exclusive ending index.
- `span()` returns both indices.

Always check whether `search()` returned a match before accessing its methods.

### 5.2 `re.findall()`

Returns all non-overlapping matches.

```python
print(re.findall(r"\d+", "2024, 10, 25"))
```

Output:

```text
['2024', '10', '25']
```

With capturing groups, `findall()` returns captured text rather than the complete match. If a pattern has multiple capturing groups, it returns tuples of the captured values.

### 5.3 `re.finditer()`

Returns an iterator of match objects.

```python
text = "Numbers: 12, 345"

for m in re.finditer(r"\d+", text):
    print(m.group(), m.span())
```

Use `finditer()` when you need the matched text together with its positions.

### 5.4 `re.match()`

Checks for a match only at the beginning of the string.

```python
print(re.match(r"The", "The year is 2024"))
print(re.match(r"year", "The year is 2024"))
```

The first call returns a match object; the second returns `None`.

### 5.5 `re.fullmatch()`

Requires the entire string to match the pattern.

```python
print(re.fullmatch(r"\d+", "12345"))
print(re.fullmatch(r"\d+", "12a45"))
```

The first matches, and the second returns `None`.

For validating a whole input field, `fullmatch()` is often clearer than relying on anchors.

### 5.6 `re.sub()`

Replaces matching text.

```python
text = "Year 2024, month 10"

print(re.sub(r"\d+", "X", text))
```

Output:

```text
Year X, month X
```

### 5.7 `re.split()`

Splits text wherever the regex matches.

```python
print(re.split(r"\s+", "a  b   c"))
```

Output:

```text
['a', 'b', 'c']
```

Here, `\s+` matches one or more whitespace characters.

### 5.8 Compiling a Pattern

```python
pattern = re.compile(r"\d+")

print(pattern.findall("2024 and 10"))
print(pattern.search("Year 2024").group())
```

Compiled patterns are convenient when the same pattern is reused. They avoid repeatedly expressing the pattern in each operation; Python also caches some recent regex patterns internally.

### 5.9 Character Classes

| Pattern | Meaning |
|---|---|
| `[abc]` | Any one of `a`, `b`, or `c` |
| `[a-z]` | A lowercase ASCII letter |
| `[A-Z]` | An uppercase ASCII letter |
| `[0-9]` | An ASCII digit |
| `[^abc]` | Any character except `a`, `b`, or `c` |
| `\d` | A Unicode decimal digit by default |
| `\w` | A Unicode word character by default |
| `\s` | A whitespace character |

Examples:

```python
print(re.findall(r"[aeiou]", "hello world"))
print(re.findall(r"[^aeiou]", "hello"))
print(re.findall(r"\w+", "hi there_42!"))
print(re.findall(r"\s", "a b\tc"))
```

In Unicode mode, `\w`, `\d`, and related shorthand classes are not restricted to ASCII. Use `re.ASCII` or explicit character ranges if an ASCII-only definition is required.

### 5.10 Anchors

| Pattern | Meaning |
|---|---|
| `^` | Start of string, or start of line with multiline mode |
| `$` | End of string, or end of line with multiline mode |
| `\b` | Word boundary |
| `\B` | Position that is not a word boundary |

```python
print(re.findall(r"^\w+", "hello world"))
print(re.findall(r"\w+$", "hello world"))
```

Output:

```text
['hello']
['world']
```

By default, `^` and `$` refer to the string boundaries, subject to the special end-of-string behavior of `$`. With `re.MULTILINE`, they can match line boundaries.

For exact whole-string validation, prefer `re.fullmatch()`.

### 5.11 Quantifiers

| Pattern | Meaning |
|---|---|
| `*` | Zero or more |
| `+` | One or more |
| `?` | Zero or one |
| `{n}` | Exactly `n` repetitions |
| `{n,m}` | Between `n` and `m` repetitions |
| `{n,}` | At least `n` repetitions |

Examples:

```python
print(re.findall(r"a+", "aaa b aa c a"))
print(re.findall(r"a{2,3}", "a aa aaa aaaa"))
```

Output:

```text
['aaa', 'aa', 'a']
['aa', 'aaa', 'aaa', 'aa']
```

Quantifiers are greedy by default: they try to match as much as possible while still allowing the overall pattern to match.

The `*` and `?` quantifiers can also match zero characters. Consequently, patterns such as `a*` and `a?` may produce empty matches.

### 5.12 Regex Flags

```python
print(re.findall(r"hello", "Hello World", re.I))
print(re.findall(r"^world", "hello\nworld", re.M))
```

Common flags:

| Flag | Purpose |
|---|---|
| `re.I` or `re.IGNORECASE` | Case-insensitive matching |
| `re.M` or `re.MULTILINE` | `^` and `$` match line boundaries |
| `re.S` or `re.DOTALL` | `.` also matches newline characters |
| `re.A` or `re.ASCII` | Make shorthand character classes use ASCII rules |

---

## 6. Regex Groups

**File:** `06_regex_groups.py`

Groups let you capture portions of a match, apply alternatives, and express more complex matching rules.

### 6.1 Capturing Groups

Parentheses create capturing groups.

```python
import re

text = "John: 30, Jane: 25, Bob: 45"
pattern = r"(\w+): (\d+)"

for m in re.finditer(pattern, text):
    print(m.group(1), m.group(2))
    print(m.groups())
```

Output:

```text
John 30
('John', '30')
Jane 25
('Jane', '25')
Bob 45
('Bob', '45')
```

- `group(0)` or `group()` returns the entire match.
- `group(1)` returns the first captured group.
- `group(2)` returns the second captured group.
- `groups()` returns all captured groups as a tuple.

### 6.2 Named Groups

Named groups make patterns easier to read.

```python
pattern = r"(?P<name>\w+): (?P<age>\d+)"

for m in re.finditer(pattern, "John: 30, Jane: 25"):
    print(m.group("name"), m.group("age"))
    print(m.groupdict())
```

Output:

```text
John 30
{'name': 'John', 'age': '30'}
Jane 25
{'name': 'Jane', 'age': '25'}
```

Named groups are especially helpful when extracting multiple fields from structured text.

### 6.3 Non-Capturing Groups

`(?:...)` groups a pattern without capturing the matched text separately.

```python
pattern = r"(?:Mr|Ms|Dr)\. (\w+)"

print(re.findall(pattern, "Mr. Smith and Ms. Jones"))
```

Output:

```text
['Smith', 'Jones']
```

Use non-capturing groups when grouping is necessary for alternation or quantification but the group's text is not needed as a separate result.

### 6.4 Backreferences

A backreference matches the same text captured by an earlier group.

```python
pattern = r"\b(\w+)\s+\1\b"

print(re.findall(pattern, "hello hello world"))
```

Output:

```text
['hello']
```

`\1` refers to the text matched by the first capturing group.

This pattern finds adjacent repeated words.

### 6.5 Alternation

The `|` symbol means OR.

```python
print(re.findall(r"cat|dog", "cat dog bird"))
```

Output:

```text
['cat', 'dog']
```

For whole-word matching:

```python
print(re.findall(r"\b(?:cat|dog)\b", "cat dog catalog"))
```

Output:

```text
['cat', 'dog']
```

The word boundaries prevent `cat` from matching as part of `catalog`.

### 6.6 Lookahead Assertions

A lookahead checks what comes next without consuming those characters as part of the match.

Positive lookahead `(?=...)`:

```python
print(re.findall(r"\d+(?= dollars)", "100 dollars, 200 euros"))
```

Output:

```text
['100']
```

Negative lookahead `(?!...)`:

```python
print(re.findall(r"\d+(?! dollars)", "100 dollars, 200 euros"))
```

This pattern is more subtle than it looks. It may match a prefix of `100` because the engine can backtrack and match fewer digits before the negative lookahead. It is not a reliable way to extract all numbers that are not followed by `" dollars"`.

To test a complete number token, use a pattern with explicit boundaries and a clearly defined token format.

### 6.7 Lookbehind Assertions

Lookbehind checks what appears before the current position.

Positive lookbehind `(?<=...)`:

```python
print(re.findall(r"(?<=\$)\d+", "$100 $200"))
```

Output:

```text
['100', '200']
```

Negative lookbehind `(?<!...)`:

```python
print(re.findall(r"(?<!\$)\b\d+", "$100 200"))
```

Output:

```text
['200']
```

Python's standard `re` module requires lookbehind patterns to have fixed width.

### 6.8 Greedy vs. Non-Greedy Matching

```python
html = "<b>bold</b> and <i>italic</i>"

print(re.findall(r"<.+>", html))
print(re.findall(r"<.+?>", html))
```

The greedy pattern `.+` attempts to consume as much text as possible. The non-greedy pattern `.+?` attempts to consume as little as possible while still allowing the match.

For this example, the greedy pattern can match from the first `<` to the last `>`, while the non-greedy pattern finds individual tag-like substrings.

**Important:** Regex is not a complete HTML parser. Use an HTML parser when you need to process real HTML documents.

---

## 7. Regex Practice

**File:** `07_regex_practice.py`

This file applies regular expressions to common text-processing tasks.

### 7.1 Email Pattern

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))
```

The pattern checks for a simple email-like structure:

- A local part containing permitted characters.
- An `@` symbol.
- A domain-like section.
- A dot followed by at least two ASCII letters.

This is a practical screening pattern, not a complete implementation of every valid email address rule. For production systems, use a suitable validation library and verify addresses when necessary.

### 7.2 Phone Number Pattern

```python
import re

def is_valid_phone(phone):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return bool(re.fullmatch(pattern, phone))
```

This pattern supports examples such as:

```text
1234567890
123-456-7890
123.456.7890
(123) 456-7890
```

It checks a simple 10-digit phone-number format. It does not establish whether a phone number is assigned, reachable, or valid under every country's numbering rules.

### 7.3 URL Pattern

```python
import re

def is_valid_url(url):
    pattern = (
        r"https?://[\w.-]+(?:\.[\w.-]+)+"
        r"[\w\-._~:/?#\[\]@!$&'()*+,;=]*"
    )
    return bool(re.fullmatch(pattern, url))
```

The pattern accepts many common HTTP and HTTPS URL forms, but it is not a complete standards-compliant URL validator. For production use, parse URLs with a URL-parsing library and validate the parts required by your application.

### 7.4 Checking Password Characteristics

```python
import re

def password_strength(password):
    return {
        "length": len(password) >= 8,
        "upper": bool(re.search(r"[A-Z]", password)),
        "lower": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*]", password)),
    }

print(password_strength("Abc123!@#"))
```

This returns a dictionary of Boolean checks.

It is a basic educational example, not a comprehensive password-security assessment. Real password policies should consider the application's threat model, breached-password checks, and secure password storage.

### 7.5 Extracting Dates

```python
import re

def extract_dates(text):
    return re.findall(r"\d{4}-\d{2}-\d{2}", text)

print(extract_dates("2024-01-01 and 2025-12-31"))
```

Output:

```text
['2024-01-01', '2025-12-31']
```

This pattern extracts strings in a `YYYY-MM-DD`-like shape. It does not verify whether a date actually exists. For example, it can match `2024-99-99`.

For real date validation, parse the extracted values with `datetime.strptime()` or an appropriate date library.

### 7.6 Extracting Hashtags

```python
import re

def extract_hashtags(text):
    return re.findall(r"#(\w+)", text)

print(extract_hashtags("#python #dsa"))
```

Output:

```text
['python', 'dsa']
```

The capturing group excludes the `#` symbol from the returned values.

### 7.7 Extracting URLs from Text

```python
import re

def extract_urls(text):
    return re.findall(r"https?://\S+", text)

print(extract_urls("Visit https://a.com and http://b.org"))
```

Output:

```text
['https://a.com', 'http://b.org']
```

This simple pattern extracts non-whitespace sequences beginning with HTTP or HTTPS. It may include trailing punctuation, so real-world extraction often requires additional cleanup or a dedicated parser.

### 7.8 Normalizing Whitespace

```python
import re

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()

print(normalize_whitespace("  too   much   space  "))
```

Output:

```text
too much space
```

`\s+` matches one or more consecutive whitespace characters. Replacing each match with one space and trimming the result produces normalized spacing.

### 7.9 Running a Python File Safely

```python
if __name__ == "__main__":
    print(is_valid_email("alice@example.com"))
    print(extract_dates("2024-01-01 and 2025-12-31"))
```

The `if __name__ == "__main__":` guard runs the demonstration code when the file is executed directly. It prevents that demonstration block from running automatically when the file is imported as a module.

---

## 8. Regex Quick Reference

| Pattern | Meaning | Example |
|---|---|---|
| `.` | Any character except newline by default | `a.c` |
| `\d` | Unicode decimal digit | `\d+` |
| `\w` | Unicode word character | `\w+` |
| `\s` | Whitespace | `\s+` |
| `[abc]` | One character from a set | `[aeiou]` |
| `[^abc]` | One character outside a set | `[^0-9]` |
| `^` | Start boundary | `^Hello` |
| `$` | End boundary | `world$` |
| `\b` | Word boundary | `\bcat\b` |
| `*` | Zero or more | `a*` |
| `+` | One or more | `a+` |
| `?` | Zero or one | `colou?r` |
| `{n}` | Exactly `n` repetitions | `\d{4}` |
| `{n,m}` | Between `n` and `m` repetitions | `\d{2,4}` |
| `(abc)` | Capturing group | `(\d+)` |
| `(?:abc)` | Non-capturing group | `(?:Mr|Ms)` |
| `(?P<name>...)` | Named capturing group | `(?P<age>\d+)` |
| `\1` | Backreference to group 1 | `(\w+)\s+\1` |
| `a\|b` | Match `a` or `b` | `cat\|dog` |
| `(?=...)` | Positive lookahead | `\d+(?= dollars)` |
| `(?!...)` | Negative lookahead | `\d+(?! dollars)` |
| `(?<=...)` | Positive lookbehind | `(?<=\$)\d+` |
| `(?<!...)` | Negative lookbehind | `(?<!\$)\d+` |

Remember that regex shorthand classes are Unicode-aware by default in Python. Use explicit ranges or `re.ASCII` when an ASCII-only pattern is required.

---

## 9. Common Mistakes

### Mistake 1: Forgetting That the Stop Index Is Exclusive

```python
s = "Python"
print(s[0:3])
```

Output:

```text
Pyt
```

The character at index `3` is not included.

### Mistake 2: Trying to Modify a String in Place

Incorrect:

```python
# s[0] = "J"
```

Strings are immutable. Create a new string instead:

```python
s = "Python"
s = "J" + s[1:]
print(s)
```

### Mistake 3: Forgetting to Store the Result of a String Method

Incorrect:

```python
s = "hello"
s.upper()
print(s)
```

Output:

```text
hello
```

Correct:

```python
s = s.upper()
print(s)
```

Output:

```text
HELLO
```

### Mistake 4: Confusing `match()`, `search()`, and `fullmatch()`

- `match()` checks at the beginning.
- `search()` looks anywhere.
- `fullmatch()` requires the entire string to match.

Choose the function based on the actual requirement.

### Mistake 5: Forgetting Raw Strings

Prefer:

```python
pattern = r"\d+"
```

This makes regex backslashes easier to manage.

### Mistake 6: Assuming `findall()` Always Returns Strings

With no capturing groups, `findall()` usually returns matched strings. With one capturing group, it returns the captured text; with multiple groups, it returns tuples.

Use `finditer()` when you need match objects and their positions.

### Mistake 7: Assuming a Regex Validates Everything

A pattern matching the shape of an email, URL, phone number, or date does not necessarily prove the value is valid. Define the validation requirements carefully.

### Mistake 8: Using Regex for Every Text Task

For simple tasks, ordinary string methods are often better:

```python
text = "hello world"

print(text.startswith("hello"))
print("world" in text)
print(text.split())
```

Use regex when the pattern genuinely needs pattern matching.

---

## 10. Time Complexity

Let \(n\) be the length of the input string.

| Operation | Typical complexity |
|---|---:|
| Indexing a string | \(O(1)\) |
| Slicing a string of length \(k\) | \(O(k)\) |
| Reversing a string | \(O(n)\) |
| `strip()`, `lower()`, `upper()` | \(O(n)\) |
| `replace()` | Typically \(O(n)\), depending on the replacement and implementation |
| `split()` | \(O(n)\), excluding additional representation details |
| `join()` | \(O(n)\) in total output length |
| Simple regex search | Pattern-dependent; often linear for straightforward patterns |
| Regex with ambiguous nested repetition | Can take exponential time in pathological cases |

Regex performance depends on the pattern and input. Some patterns with nested, overlapping repetition can cause catastrophic backtracking. Avoid ambiguous patterns on untrusted input when possible, and consider timeouts or a safer regex engine for applications that require strict performance guarantees.

For competitive programming, prefer the simplest operation that satisfies the requirements.

---

## 11. Practice Problems

### Beginner: Strings and Slicing

- [ ] Reverse a string without using a loop.
- [ ] Check whether a string is a palindrome.
- [ ] Count vowels and consonants.
- [ ] Count uppercase and lowercase letters.
- [ ] Remove leading and trailing whitespace.
- [ ] Reverse the order of words in a sentence.
- [ ] Find the frequency of each character.
- [ ] Remove duplicate characters while preserving order.
- [ ] Check whether two strings are anagrams.
- [ ] Find the longest word in a sentence.

### Intermediate: String Processing

- [ ] Compress consecutive repeated characters.
- [ ] Find the first non-repeating character.
- [ ] Check whether one string is a rotation of another.
- [ ] Find all occurrences of a substring.
- [ ] Normalize whitespace in a paragraph.
- [ ] Extract all integers from a string.
- [ ] Validate a simple date format.
- [ ] Sort a list of words by length using a key function.
- [ ] Format a table of names and scores using f-strings.
- [ ] Parse comma-separated values while accounting for quoted fields using the `csv` module.

### Regular Expression Practice

- [ ] Extract all numbers from a paragraph.
- [ ] Find all words beginning with a capital letter.
- [ ] Find repeated adjacent words.
- [ ] Extract hashtags from text.
- [ ] Extract dates in `YYYY-MM-DD` format.
- [ ] Match strings containing only ASCII digits.
- [ ] Extract usernames and values from `username: value` lines.
- [ ] Find words that end with `ing`.
- [ ] Replace multiple whitespace characters with one space.
- [ ] Extract HTTP and HTTPS URL candidates from a text.
- [ ] Validate a simplified email-address format.
- [ ] Compare regex extraction with ordinary string methods.

### Competitive Programming Challenges

- [ ] Implement a basic substring search.
- [ ] Check whether two strings are anagrams.
- [ ] Solve the longest common prefix problem.
- [ ] Find the longest palindromic substring.
- [ ] Implement run-length encoding.
- [ ] Count distinct substrings for a short input.
- [ ] Learn the prefix-function or KMP algorithm for efficient pattern matching.
- [ ] Study the Z-function for string matching.
- [ ] Learn rolling hash for substring comparison.

---

## Final Revision Checklist

Before moving to the next chapter, make sure you can:

- [ ] Format strings using f-strings and `str.format()`.
- [ ] Use format specifications for alignment, padding, and numbers.
- [ ] Read and write string slices.
- [ ] Reverse strings and lists using slicing.
- [ ] Explain why strings are immutable.
- [ ] Use common string methods for searching, cleaning, splitting, and joining.
- [ ] Understand the difference between `find()` and `index()`.
- [ ] Use `re.search()`, `re.findall()`, `re.finditer()`, and `re.sub()`.
- [ ] Distinguish `match()`, `search()`, and `fullmatch()`.
- [ ] Understand character classes, anchors, and quantifiers.
- [ ] Use capturing groups, named groups, and backreferences.
- [ ] Understand lookahead, lookbehind, and greedy matching.
- [ ] Recognize the limitations of regex-based validation.
- [ ] Analyze the time complexity of common string operations.

**Next topic:** Python modules, packages, exception handling, or file handling.

**Study strategy:** First master slicing and string methods. Then practice regex matching and extraction. For competitive programming, focus particularly on string manipulation, character frequencies, anagrams, palindrome checks, substring search, and efficient pattern-matching algorithms.