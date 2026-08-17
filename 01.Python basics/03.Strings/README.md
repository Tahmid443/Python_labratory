# 🐍 Python Strings --- Complete Revision Notes

This folder contains my **Python String** practice programs. This README
is designed as a **revision notebook**: I can revise the complete String
chapter here without opening every `.py` file.

> **Practice files:** `01.strings.py` → `06.methods.py`

------------------------------------------------------------------------

## 📚 Table of Contents

1.  [What is a String?](#1-what-is-a-string)
2.  [Creating Strings](#2-creating-strings)
3.  [Multiline Strings](#3-multiline-strings)
4.  [String Concatenation](#4-string-concatenation)
5.  [String Indexing](#5-string-indexing)
6.  [Looping Through Strings](#6-looping-through-strings)
7.  [String Length](#7-string-length)
8.  [Checking Strings](#8-checking-strings)
9.  [String Slicing](#9-string-slicing)
10. [Modifying Strings](#10-modifying-strings)
11. [String Formatting](#11-string-formatting)
12. [Escape Sequences](#12-escape-sequences)
13. [String Methods --- Complete
    Reference](#13-string-methods--complete-reference)
14. [Important Differences](#14-important-differences)
15. [Common Mistakes](#15-common-mistakes)
16. [Quick Revision Sheet](#16-quick-revision-sheet)
17. [Practice Files](#17-practice-files)

------------------------------------------------------------------------

# 1. What is a String?

📄 **File:** `01.strings.py`

A **string** is a sequence of characters enclosed inside quotes.

``` python
name = "Taqi Tahmid"
```

Python supports:

``` python
"Hello"
'Hello'
```

Both represent strings.

``` python
a = "Python"
b = 'Python'

print(a == b)
```

Output:

``` text
True
```

## 1.1 Strings are sequences

A string is an ordered sequence of characters.

``` python
fruit = "Apple"
```

Its indexes are:

``` text
 A   p   p   l   e
 0   1   2   3   4
```

So:

``` python
print(fruit[0])   # A
print(fruit[2])   # p
print(fruit[4])   # e
```

Python uses **zero-based indexing**, meaning the first character has
index `0`.

## 1.2 Strings are immutable

Strings cannot be changed in place.

This is important:

``` python
name = "Python"
```

You cannot do:

``` python
name[0] = "J"
```

This raises `TypeError`.

Instead, create a new string:

``` python
name = "Python"
name = "J" + name[1:]
print(name)
```

Output:

``` text
Jython
```

Most string methods therefore return a **new string** instead of
modifying the original string.

------------------------------------------------------------------------

# 2. Creating Strings

Strings can be created using single or double quotes.

``` python
name = "Tahmid"
country = 'Bangladesh'
```

You can also use quotes inside a string by choosing the other quote
type.

``` python
text = "I don't like Python."
```

or:

``` python
text = 'He said "Hello".'
```

If you need the same quote character inside the string, use an escape
sequence:

``` python
text = 'I don\'t like Python.'
```

------------------------------------------------------------------------

# 3. Multiline Strings

Triple quotes can be used to create strings containing multiple lines.

``` python
multiLineString = """
Hello this is a multiline
string. It helps to store multiple
lines in a variable.
"""

print(multiLineString)
```

You can use either triple double quotes or triple single quotes.

``` python
"""
multiple lines
"""
```

### Important

Triple-quoted text is still a **string**. It is commonly used for
multiline text and docstrings; it is not technically a special
multi-line comment syntax.

------------------------------------------------------------------------

# 4. String Concatenation

**Concatenation** means joining strings together.

Use the `+` operator:

``` python
a = "apple"
b = "is a fruit"
c = a + " " + b
print(c)
```

Output:

``` text
apple is a fruit
```

## 4.1 String + Number

This is invalid:

``` python
age = 20
print("Age: " + age)
```

It raises a `TypeError`.

Convert the number first:

``` python
print("Age: " + str(age))
```

Or use an f-string:

``` python
print(f"Age: {age}")
```

------------------------------------------------------------------------

# 5. String Indexing

Characters can be accessed using their index.

``` python
fruit = "Apple"
print(fruit[0])
print(fruit[2])
```

Output:

``` text
A
p
```

## 5.1 Positive indexing

``` text
String:   A   p   p   l   e
Index:    0   1   2   3   4
```

## 5.2 Negative indexing

``` text
String:       P   y   t   h   o   n
Positive:     0   1   2   3   4   5
Negative:    -6  -5  -4  -3  -2  -1
```

Example:

``` python
text = "Python"
print(text[-1])   # n
print(text[-2])   # o
```

Easy trick:

``` text
-1 → last
-2 → second last
-3 → third last
```

------------------------------------------------------------------------

# 6. Looping Through Strings

Strings are iterable.

``` python
for x in "Tahmid":
    print(x)
```

Output:

``` text
T
a
h
m
i
d
```

This is useful for character processing, counting, searching and
validation.

------------------------------------------------------------------------

# 7. String Length

Use `len()` to find the number of characters.

``` python
name = "Taqi Tahmid Dhrubo"
print(len(name))
```

Spaces are also characters, so they are counted.

------------------------------------------------------------------------

# 8. Checking Strings

Python provides `in` and `not in` for membership testing.

``` python
txt = "My college name is Sylhet Engineering College"
print("college" in txt)
```

Output:

``` text
True
```

You can use it with `if`:

``` python
if "Sylhet" in txt:
    print("Yes, it is present")
```

And:

``` python
if "Dhaka" not in txt:
    print("Dhaka is absent in txt")
```

### Important

String membership is case-sensitive:

``` python
"python" in "Python"   # False
```

For case-insensitive matching:

``` python
"python" in "Python".casefold()
```

------------------------------------------------------------------------

# 9. String Slicing

📄 **File:** `02.slicing_string.py`

Slicing extracts a portion of a string.

General syntax:

``` python
string[start:stop]
```

The `start` index is included, but the `stop` index is excluded.

### 9.1 Basic slicing

``` python
a = "ThisIsSampleText"
print(a[2:5])
```

The selected indexes are `2, 3, 4`.

### 9.2 From beginning

``` python
print(a[:5])
```

Equivalent to:

``` python
print(a[0:5])
```

### 9.3 To the end

``` python
print(a[3:])
```

### 9.4 Negative slicing

``` python
print(a[-10:-5])
```

Negative indexes count from the end. Negative slicing does **not**
automatically reverse the string.

### 9.5 Step

General syntax:

``` python
string[start:stop:step]
```

Example:

``` python
text = "Python"
print(text[0:6:2])
```

Output:

``` text
Pto
```

### 9.6 Reverse

``` python
print(text[::-1])
```

Output:

``` text
nohtyP
```

### Useful slicing patterns

  Expression   Meaning
  ------------ ------------------------
  `s[:]`       Entire string
  `s[:n]`      First `n` characters
  `s[n:]`      From `n` to end
  `s[a:b]`     From `a` to `b-1`
  `s[::2]`     Every second character
  `s[::-1]`    Reverse

------------------------------------------------------------------------

# 10. Modifying Strings

📄 **File:** `03.modify_string.py`

Because strings are immutable, methods do not modify the original
string. They return a new string.

## `upper()`

``` python
name = "taqi tahmid"
print(name.upper())
```

## `lower()`

``` python
name = "TAqi TahMID"
print(name.lower())
```

## `strip()`

Removes leading and trailing whitespace, not spaces in the middle.

``` python
country = "      Bangladesh is my favourite country      "
print(country.strip())
```

## `replace()`

``` python
fruit = "Banana"
print(fruit.replace("an", "em"))
```

You can limit replacements:

``` python
text = "one one one"
print(text.replace("one", "two", 2))
```

## `split()`

``` python
a = "Taqi Tahmid Dhrubo"
print(a.split(" "))

b = "Chips,Juice,Biscuit"
print(b.split(","))
```

`split()` returns a list.

When no separator is provided, `split()` splits on whitespace.

------------------------------------------------------------------------

# 11. String Formatting

📄 **File:** `04.format_string.py`

## 11.1 f-strings

``` python
age = 23
name = "Tahmid"
print(f"My name is {name} and I am {age} years old")
```

The `{}` parts are replacement fields.

## 11.2 Expressions inside f-strings

``` python
print(f"The sum of 5 and 7 is {5 + 7}")
```

## 11.3 Format specifiers

A colon introduces a format specification:

``` python
price = 35.43223
print(f"The price is {price:.2f} dollars")
```

`.2f` means two digits after the decimal in fixed-point notation.

More examples:

``` python
price = 35.43223
print(f"{price:.2f}")
print(f"{price:.1f}")
print(f"{price:.0f}")
```

Percentage formatting:

``` python
rate = 0.856
print(f"{rate:.2%}")
```

------------------------------------------------------------------------

# 12. Escape Sequences

📄 **File:** `05.escape_notation.py`

Escape sequences begin with a backslash `\\` and represent special
characters.

  Escape    Meaning
  --------- -----------------------
  `\\'`     Single quote
  `\\"`     Double quote
  `\\\\`    Backslash
  `\\n`     New line
  `\\r`     Carriage return
  `\\t`     Horizontal tab
  `\\b`     Backspace
  `\\f`     Form feed
  `\\ooo`   Octal character
  `\\xhh`   Hexadecimal character

## Single quote

``` python
print('I don\'t like Python.')
```

## Double quote

``` python
print("He said \"Hello\"")
```

## Backslash

``` python
print("This is a backslash: \\")
```

## New line

``` python
print("Hello\nWorld")
```

## Carriage return

``` python
print("Hello\rWorld")
```

The exact visible result depends on the terminal because the carriage
return moves the cursor to the beginning of the current line.

## Tab

``` python
print("Name:\tTahmid")
print("Age:\t20")
```

## Backspace

``` python
print("Helloo\b")
```

The visible result can depend on the output environment.

## Form feed

``` python
print("Hello\fWorld")
```

Its appearance can vary between environments.

## Octal

``` python
print("\101")
```

Output:

``` text
A
```

## Hexadecimal

``` python
print("\x41")
```

Output:

``` text
A
```

## Raw strings

``` python
print(r"Hello\nWorld")
```

Output:

``` text
Hello\nWorld
```

Raw strings are useful for Windows paths and regular expressions:

``` python
path = r"C:\Users\Tahmid\Documents"
```

------------------------------------------------------------------------

# 13. String Methods --- Complete Reference

📄 **File:** `06.methods.py`

The methods file demonstrates **45 string methods**. The original file's
heading says 47, but the actual numbered examples run from 1 through 45.

## Method reference

  --------------------------------------------------------------------------
                            \# Method                Purpose
  ---------------------------- --------------------- -----------------------
                             1 `capitalize()`        First character
                                                     uppercase; remaining
                                                     cased characters
                                                     lowercase

                             2 `casefold()`          Strong Unicode-aware
                                                     case folding

                             3 `center()`            Center string within a
                                                     width

                             4 `count()`             Count non-overlapping
                                                     occurrences

                             5 `encode()`            Convert string to bytes
                                                     using an encoding

                             6 `endswith()`          Check suffix

                             7 `expandtabs()`        Replace tabs with
                                                     spaces

                             8 `find()`              First occurrence or
                                                     `-1`

                             9 `format()`            Format replacement
                                                     fields

                            10 `format_map()`        Format using a
                                                     mapping/dictionary

                            11 `index()`             First occurrence;
                                                     raises `ValueError` if
                                                     absent

                            12 `isalnum()`           All characters
                                                     alphanumeric

                            13 `isalpha()`           All characters
                                                     alphabetic

                            14 `isascii()`           All characters ASCII

                            15 `isdecimal()`         All characters decimal
                                                     characters

                            16 `isdigit()`           All characters Unicode
                                                     digits

                            17 `isidentifier()`      Valid Python identifier
                                                     syntax

                            18 `islower()`           Cased characters are
                                                     lowercase

                            19 `isnumeric()`         All characters Unicode
                                                     numeric characters

                            20 `isprintable()`       All characters
                                                     printable

                            21 `isspace()`           All characters
                                                     whitespace

                            22 `istitle()`           Title-case check

                            23 `isupper()`           Cased characters are
                                                     uppercase

                            24 `join()`              Join iterable using
                                                     string as separator

                            25 `ljust()`             Left-align within width

                            26 `lower()`             Convert to lowercase

                            27 `lstrip()`            Remove leading
                                                     characters/whitespace

                            28 `maketrans()`         Create translation
                                                     table

                            29 `partition()`         Split at first
                                                     separator into 3 parts

                            30 `replace()`           Replace substring
                                                     occurrences

                            31 `rfind()`             Last occurrence or `-1`

                            32 `rindex()`            Last occurrence; raises
                                                     `ValueError` if absent

                            33 `rjust()`             Right-align within
                                                     width

                            34 `rpartition()`        Split at last separator
                                                     into 3 parts

                            35 `rsplit()`            Split from right

                            36 `rstrip()`            Remove trailing
                                                     characters/whitespace

                            37 `split()`             Split into a list

                            38 `splitlines()`        Split at line
                                                     boundaries

                            39 `startswith()`        Check prefix

                            40 `strip()`             Remove leading and
                                                     trailing
                                                     characters/whitespace

                            41 `swapcase()`          Swap
                                                     uppercase/lowercase

                            42 `title()`             Convert to title case

                            43 `translate()`         Translate characters
                                                     using a table

                            44 `upper()`             Convert to uppercase

                            45 `zfill()`             Pad on the left with
                                                     zeros
  --------------------------------------------------------------------------

------------------------------------------------------------------------

## 13.1 `capitalize()`

``` python
"hello WORLD".capitalize()
# 'Hello world'
```

## 13.2 `casefold()`

Useful for case-insensitive Unicode comparison.

``` python
"Straße".casefold()
# 'strasse'
```

It is more aggressive than `lower()`.

## 13.3 `center()`

``` python
"Python".center(20, "*")
```

Centers the string inside the requested width.

## 13.4 `count()`

``` python
"banana".count("a")
# 3
```

Counts non-overlapping occurrences and can accept `start` and `end`
positions.

## 13.5 `encode()`

``` python
"Python".encode("utf-8")
# b'Python'
```

Converts text to bytes.

## 13.6 `endswith()`

``` python
"Python Programming 2024".endswith("2024")
# True
```

Can accept a tuple of suffixes.

## 13.7 `expandtabs()`

``` python
"Hello\tWorld".expandtabs(10)
```

Replaces tab characters according to tab-stop spacing.

## 13.8 `find()`

``` python
"Python Programming".find("gram")
```

Returns the first index, or `-1` if absent.

## 13.9 `format()`

``` python
"Hello {}, you are {} years old".format("John", 25)
```

Supports positional and named fields and many formatting options.

## 13.10 `format_map()`

``` python
data = {"name": "Alice", "age": 30}
text = "My name is {name} and I am {age} years old"
print(text.format_map(data))
```

Uses a mapping such as a dictionary.

## 13.11 `index()`

``` python
"Python Programming".index("gram")
```

Returns the first occurrence. Raises `ValueError` if absent.

## 13.12 `isalnum()`

``` python
"Python3".isalnum()       # True
"Python 3".isalnum()      # False
```

A non-empty string must contain only letters and/or digits.

## 13.13 `isalpha()`

``` python
"HelloWorld".isalpha()    # True
"Python3".isalpha()       # False
```

## 13.14 `isascii()`

``` python
"Hello123".isascii()      # True
"Hellö".isascii()         # False
```

## 13.15 `isdecimal()`

``` python
"12345".isdecimal()       # True
```

A relatively narrow numeric test.

## 13.16 `isdigit()`

``` python
"123".isdigit()           # True
"²".isdigit()             # True
```

Broader than `isdecimal()`.

## 13.17 `isidentifier()`

``` python
"variable_name".isidentifier()   # True
"123abc".isidentifier()          # False
```

Checks identifier syntax. A keyword can still pass this syntax test, so
use `keyword.iskeyword()` when necessary.

## 13.18 `islower()`

``` python
"hello".islower()         # True
```

Non-cased characters do not prevent the test from being true.

## 13.19 `isnumeric()`

``` python
"123".isnumeric()         # True
"½".isnumeric()           # True
```

Accepts a broad range of Unicode numeric characters.

## 13.20 `isprintable()`

``` python
"Hello World!".isprintable()       # True
"Hello\nWorld".isprintable()       # False
```

## 13.21 `isspace()`

``` python
"   \t\n".isspace()          # True
"Hello".isspace()        # False
```

## 13.22 `istitle()`

``` python
"The Quick Brown Fox".istitle()    # True
```

Checks title-case formatting.

## 13.23 `isupper()`

``` python
"HELLO".isupper()        # True
```

## 13.24 `join()`

The separator calls `join()` on the iterable:

``` python
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))
```

Output:

``` text
apple, banana, cherry
```

## 13.25 `ljust()`

``` python
"Python".ljust(15, ".")
```

Left-aligns the string.

## 13.26 `lower()`

``` python
"Hello WORLD".lower()
# 'hello world'
```

## 13.27 `lstrip()`

``` python
"   Hello".lstrip()
# 'Hello'
```

With an argument, it removes any of the specified characters from the
left rather than treating the argument as one exact substring.

## 13.28 `maketrans()`

``` python
trans = str.maketrans("aeiou", "12345")
```

Creates a character mapping for `translate()`.

## 13.29 `partition()`

``` python
"apple,banana,cherry".partition(",")
```

Returns:

``` python
('apple', ',', 'banana,cherry')
```

The result is always a 3-tuple:

``` text
(before, separator, after)
```

## 13.30 `replace()`

``` python
"Python Programming".replace("Python", "Java")
```

Can limit the number of replacements with a third argument.

## 13.31 `rfind()`

``` python
"hello world wow".rfind("o")
```

Returns the last occurrence, or `-1`.

## 13.32 `rindex()`

Like `rfind()`, but raises `ValueError` if absent.

## 13.33 `rjust()`

``` python
"Python".rjust(15, ".")
```

Right-aligns the string.

## 13.34 `rpartition()`

``` python
"apple,banana,cherry".rpartition(",")
```

Returns:

``` python
('apple,banana', ',', 'cherry')
```

It partitions at the last occurrence.

## 13.35 `rsplit()`

``` python
"apple,banana,cherry,date".rsplit(",", 2)
```

Returns:

``` python
['apple,banana', 'cherry', 'date']
```

## 13.36 `rstrip()`

``` python
"Hello   ".rstrip()
# 'Hello'
```

Removes trailing whitespace by default.

## 13.37 `split()`

``` python
"apple,banana,cherry".split(",")
```

Returns a list.

## 13.38 `splitlines()`

``` python
"Line1\nLine2\nLine3".splitlines()
```

Returns:

``` python
['Line1', 'Line2', 'Line3']
```

## 13.39 `startswith()`

``` python
"Python Programming".startswith("Python")
# True
```

## 13.40 `strip()`

``` python
"   Hello World   ".strip()
# 'Hello World'
```

It removes leading and trailing whitespace by default.

## 13.41 `swapcase()`

``` python
"Hello WORLD".swapcase()
# 'hELLO world'
```

## 13.42 `title()`

``` python
"hello world".title()
# 'Hello World'
```

## 13.43 `translate()`

``` python
trans = str.maketrans("aeiou", "12345")
print("hello world".translate(trans))
```

Output:

``` text
h2ll4 w4rld
```

## 13.44 `upper()`

``` python
"hello world".upper()
# 'HELLO WORLD'
```

## 13.45 `zfill()`

``` python
"42".zfill(5)
# '00042'
```

It pads on the left with zeros. It also handles a leading sign
specially:

``` python
"-42".zfill(5)
# '-0042'
```

------------------------------------------------------------------------

# 14. Important Differences

## `find()` vs `index()`

  Method      If found   If not found
  ----------- ---------- --------------
  `find()`    Index      `-1`
  `index()`   Index      `ValueError`

## `rfind()` vs `rindex()`

Same difference, but they search for the last occurrence.

## `partition()` vs `split()`

``` python
"a-b-c".partition("-")
# ('a', '-', 'b-c')

"a-b-c".split("-")
# ['a', 'b', 'c']
```

`partition()` returns exactly three parts and preserves the separator.
`split()` returns a list and normally removes the separator.

## `partition()` vs `rpartition()`

``` text
partition()  → first separator
rpartition() → last separator
```

## `split()` vs `rsplit()`

``` text
split()  → splits from the left
rsplit() → splits from the right
```

This matters especially when `maxsplit` is used.

## `strip()` vs `replace()`

``` text
strip()   → removes characters from the ends
replace() → replaces substrings wherever they occur
```

## `lstrip()` vs `rstrip()`

``` text
lstrip() → left/start
rstrip() → right/end
```

## `lower()` vs `casefold()`

``` text
lower()   → ordinary lowercase conversion
casefold() → stronger Unicode-aware case folding
```

## `isdecimal()` vs `isdigit()` vs `isnumeric()`

A useful mental model is:

``` text
isdecimal() ⊂ isdigit() ⊂ isnumeric()
```

They are not interchangeable; `isnumeric()` accepts the broadest range
of Unicode numeric characters.

------------------------------------------------------------------------

# 15. Common Mistakes

## 1. Trying to modify a string by index

Wrong:

``` python
text = "Python"
text[0] = "J"
```

Strings are immutable.

Correct:

``` python
text = "J" + text[1:]
```

## 2. Forgetting that slicing excludes the stop index

``` python
text[1:5]
```

means indexes `1, 2, 3, 4`.

## 3. Thinking `strip()` removes spaces everywhere

``` python
"Hello   World".strip()
```

still contains the spaces in the middle.

## 4. Confusing `replace()` and `strip()`

Use `replace()` for substring replacement and `strip()` for the
beginning/end.

## 5. Using `is` for string equality

Usually use:

``` python
a == b
```

not:

``` python
a is b
```

## 6. Forgetting case sensitivity

``` python
"Python" == "python"   # False
```

For robust case-insensitive comparison:

``` python
a.casefold() == b.casefold()
```

## 7. Expecting `split()` to return a string

`split()` returns a list.

## 8. Forgetting that string methods usually return new strings

This does not change `name`:

``` python
name = "tahmid"
name.upper()
print(name)
```

Use:

``` python
name = name.upper()
```

or print the returned value directly.

------------------------------------------------------------------------

# 16. Quick Revision Sheet

## Basic operations

``` python
text = "Python"

len(text)
text[0]
text[-1]
text[1:4]
text[::-1]
"Py" in text
"Java" not in text
```

## Case

``` python
text.upper()
text.lower()
text.capitalize()
text.casefold()
text.swapcase()
text.title()
```

## Whitespace

``` python
text.strip()
text.lstrip()
text.rstrip()
```

## Search

``` python
text.find("x")
text.index("x")
text.rfind("x")
text.rindex("x")
text.startswith("Py")
text.endswith("on")
```

## Split / Join

``` python
text.split()
text.rsplit()
text.splitlines()
" ".join(words)
```

## Validation

``` python
text.isalnum()
text.isalpha()
text.isascii()
text.isdecimal()
text.isdigit()
text.isidentifier()
text.islower()
text.isnumeric()
text.isprintable()
text.isspace()
text.istitle()
text.isupper()
```

## Formatting

``` python
f"Hello {name}"
f"{price:.2f}"
"Hello {}".format(name)
```

## Escape sequences

``` text
\n  newline
\t  tab
\\  backslash
\'  single quote
\"  double quote
\r  carriage return
\b  backspace
\f  form feed
\ooo octal
\xhh hexadecimal
```

## Translation

``` python
table = str.maketrans("abc", "123")
text.translate(table)
```

------------------------------------------------------------------------

# 17. Practice Files

  ----------------------------------------------------------------------------
                            \# File                      Main Topics
  ---------------------------- ------------------------- ---------------------
                            01 `01.strings.py`           Strings, multiline
                                                         strings,
                                                         concatenation,
                                                         indexing, iteration,
                                                         `len()`, `in`,
                                                         `not in`

                            02 `02.slicing_string.py`    Positive/negative
                                                         slicing, omitted
                                                         indexes, step,
                                                         reverse

                            03 `03.modify_string.py`     `upper()`, `lower()`,
                                                         `strip()`,
                                                         `replace()`,
                                                         `split()`

                            04 `04.format_string.py`     f-strings,
                                                         placeholders,
                                                         expressions, format
                                                         specifiers

                            05 `05.escape_notation.py`   Escape sequences, raw
                                                         strings,
                                                         octal/hexadecimal
                                                         escapes

                            06 `06.methods.py`           Comprehensive
                                                         string-method
                                                         reference and
                                                         examples
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

# 🧠 Final Mental Model

Think of a Python string as:

``` text
String
  │
  ├── Sequence of characters
  │       ├── Indexing
  │       └── Slicing
  │
  ├── Immutable
  │
  ├── Iterable
  │       └── for loop
  │
  ├── Search
  │       ├── in
  │       ├── find()
  │       ├── index()
  │       └── startswith()/endswith()
  │
  ├── Transform
  │       ├── upper()
  │       ├── lower()
  │       ├── replace()
  │       └── strip()
  │
  ├── Split / Join
  │       ├── split()
  │       ├── rsplit()
  │       └── join()
  │
  ├── Validate
  │       ├── isalpha()
  │       ├── isdigit()
  │       ├── isalnum()
  │       └── ...
  │
  └── Format
          ├── f-string
          └── format()
```

------------------------------------------------------------------------

# 🎯 What You Should Be Able to Do After This Chapter

-   [ ] Create strings using single and double quotes
-   [ ] Create multiline strings
-   [ ] Concatenate strings
-   [ ] Explain string immutability
-   [ ] Access characters using positive and negative indexes
-   [ ] Slice and reverse strings
-   [ ] Loop through strings
-   [ ] Find string length
-   [ ] Search using `in` and `not in`
-   [ ] Use `upper()`, `lower()`, `strip()`, `replace()`, and `split()`
-   [ ] Use f-strings and format specifiers
-   [ ] Understand escape sequences and raw strings
-   [ ] Use searching and validation methods
-   [ ] Split and join strings
-   [ ] Use `partition()` and `rpartition()`
-   [ ] Use `maketrans()` and `translate()`
-   [ ] Explain `find()` vs `index()`
-   [ ] Explain `split()` vs `rsplit()`
-   [ ] Explain `==` vs `is`

------------------------------------------------------------------------

> **Revision tip:** For Strings, master **indexing → slicing →
> immutability → searching → modification → splitting/joining →
> formatting** first. Then use the method reference as a lookup sheet
> while solving problems.
