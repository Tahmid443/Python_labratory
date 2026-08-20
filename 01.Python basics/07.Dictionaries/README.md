# 🐍 Python Dictionaries — Complete Revision Notes

> A detailed revision guide based on the code files in this folder.

## 📚 Table of Contents

1. [What is a Dictionary?](#1-what-is-a-dictionary)
2. [Creating a Dictionary](#2-creating-a-dictionary)
3. [Dictionary Properties](#3-dictionary-properties)
4. [Key-Value Pairs](#4-key-value-pairs)
5. [Duplicate Keys](#5-duplicate-keys)
6. [Dictionary Length](#6-dictionary-length)
7. [Different Data Types](#7-different-data-types)
8. [dict() Constructor](#8-dict-constructor)
9. [Accessing Dictionary Items](#9-accessing-dictionary-items)
10. [get() Method](#10-get-method)
11. [keys(), values(), and items()](#11-keys-values-and-items)
12. [Checking if a Key Exists](#12-checking-if-a-key-exists)
13. [Changing Dictionary Items](#13-changing-dictionary-items)
14. [Adding Dictionary Items](#14-adding-dictionary-items)
15. [Removing Dictionary Items](#15-removing-dictionary-items)
16. [Looping Through Dictionaries](#16-looping-through-dictionaries)
17. [Copying Dictionaries](#17-copying-dictionaries)
18. [Nested Dictionaries](#18-nested-dictionaries)
19. [Complete Dictionary Methods](#19-complete-dictionary-methods)
20. [Important Differences](#20-important-differences)
21. [Common Mistakes](#21-common-mistakes)
22. [Quick Revision Sheet](#22-quick-revision-sheet)
23. [Practice Files](#23-practice-files)

---

# 1. What is a Dictionary?

A **dictionary** is a Python data structure used to store data in **key-value pairs**.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}
```

Here:

```text
"name"       → key
"Tahmid"     → value
"age"        → key
21            → value
"department" → key
"CSE"        → value
```

A dictionary is useful when you want to associate one piece of information with another.

Examples:

```python
student = {"name": "Tahmid", "age": 21}
```

```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
```

```python
marks = {"math": 90, "physics": 85, "chemistry": 88}
```

Think of a dictionary like a real dictionary:

```text
word → meaning
```

In Python:

```text
key → value
```

---

# 2. Creating a Dictionary

The simplest way is to use curly braces `{}`.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}
```

An empty dictionary can be created with:

```python
data = {}
```

You can also use `dict()`:

```python
student = dict(name="Tahmid", age=21, department="CSE")
```

Both create dictionaries.

---

# 3. Dictionary Properties

Python dictionaries have several important properties.

## 3.1 Ordered

Modern Python dictionaries preserve **insertion order**. This means items are remembered in the order they were inserted.

```python
student = {}
student["name"] = "Tahmid"
student["age"] = 21
student["department"] = "CSE"
```

Iteration follows that insertion order.

> Note: The old statement that dictionaries are "unordered" applies to older Python versions. In current Python, dictionary insertion order is guaranteed.

## 3.2 Changeable / Mutable

You can add, remove, or change items after creating a dictionary.

```python
student["age"] = 22
```

## 3.3 Keys are unique

A dictionary cannot contain two separate entries with the same key.

```python
student = {"name": "Tahmid", "age": 21, "age": 22}
```

The later value replaces the earlier one.

Result:

```python
{'name': 'Tahmid', 'age': 22}
```

## 3.4 Values can be duplicated

Different keys can have the same value.

```python
data = {
    "a": 10,
    "b": 10,
    "c": 20
}
```

That is completely valid.

---

# 4. Key-Value Pairs

Each dictionary item consists of:

```text
key : value
```

Example:

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
```

The pairs are:

| Key | Value |
|---|---|
| `brand` | `Ford` |
| `model` | `Mustang` |
| `year` | `1964` |

The key is used to access its value.

```python
print(car["model"])
```

Output:

```text
Mustang
```

---

# 5. Duplicate Keys

Keys must be unique.

```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
```

Python keeps the **last value** assigned to `year`.

```python
print(thisdict)
```

Result:

```python
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

### Remember

```text
Duplicate key → later value overwrites earlier value
```

---

# 6. Dictionary Length

Use `len()` to find the number of key-value pairs.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}

print(len(student))
```

Output:

```text
3
```

`len()` counts **items/pairs**, not individual keys and values separately.

---

# 7. Different Data Types

Dictionary values can have different data types.

```python
student = {
    "name": "Tahmid",        # str
    "age": 21,                # int
    "cgpa": 3.75,             # float
    "active": True,            # bool
    "skills": ["Python", "C++"] # list
}
```

A dictionary can contain:

- strings
- integers
- floats
- booleans
- lists
- tuples
- sets
- other dictionaries
- and other Python objects

Keys have restrictions: dictionary keys must be **hashable**. Common key types include strings, integers, and tuples containing hashable values.

A list cannot be used as a dictionary key because lists are mutable and unhashable.

---

# 8. `dict()` Constructor

A dictionary can also be created using the `dict()` constructor.

```python
thisdict = dict(
    name="John",
    age=36,
    country="Norway"
)
```

Result:

```python
{
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

This form is convenient when the keys are valid Python identifiers.

For arbitrary keys, use normal dictionary syntax:

```python
data = {
    "first-name": "John",
    "age": 36
}
```

---

# 9. Accessing Dictionary Items

The most common way to access a value is with its key.

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car["model"])
```

Output:

```text
Mustang
```

## Important

If the key does not exist:

```python
print(car["color"])
```

Python raises:

```text
KeyError
```

When you are unsure whether a key exists, `get()` is often safer.

---

# 10. `get()` Method

`get()` retrieves a value without raising `KeyError` when the key is missing.

```python
student = {
    "name": "Tahmid",
    "age": 21
}

print(student.get("name"))
```

Output:

```text
Tahmid
```

For a missing key:

```python
print(student.get("email"))
```

Output:

```text
None
```

You can provide your own default value:

```python
print(student.get("email", "Not Found"))
```

Output:

```text
Not Found
```

### `[]` vs `get()`

```python
student["email"]
```

→ raises `KeyError` if missing.

```python
student.get("email")
```

→ returns `None` if missing.

```python
student.get("email", "N/A")
```

→ returns `"N/A"` if missing.

---

# 11. `keys()`, `values()`, and `items()`

These are among the most important dictionary methods.

## 11.1 `keys()`

Returns a dynamic view containing all keys.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}

print(student.keys())
```

Typical output:

```text
dict_keys(['name', 'age', 'department'])
```

Loop through keys:

```python
for key in student.keys():
    print(key)
```

You can also simply write:

```python
for key in student:
    print(key)
```

because iterating over a dictionary directly iterates over its keys.

---

## 11.2 `values()`

Returns a dynamic view containing all values.

```python
print(student.values())
```

Example:

```text
dict_values(['Tahmid', 21, 'CSE'])
```

Loop:

```python
for value in student.values():
    print(value)
```

---

## 11.3 `items()`

Returns a dynamic view containing key-value pairs.

```python
print(student.items())
```

Typical output:

```text
dict_items([('name', 'Tahmid'), ('age', 21), ('department', 'CSE')])
```

Each item behaves like a two-element tuple:

```python
('name', 'Tahmid')
```

The most useful pattern is:

```python
for key, value in student.items():
    print(key, value)
```

---

## Dynamic dictionary views

Your code demonstrates that `keys()`, `values()`, and `items()` return **view objects** that reflect later changes to the dictionary.

```python
car = {
    "brand": "Ford",
    "model": "Mustang"
}

x = car.keys()

car["color"] = "white"

print(x)
```

The view reflects the new key.

The same idea applies to `values()` and `items()`.

> They are views, not ordinary lists. If you specifically need a list, convert them with `list()`.

```python
keys = list(car.keys())
```

---

# 12. Checking if a Key Exists

Use the `in` operator.

```python
student = {
    "name": "Tahmid",
    "age": 21
}

if "name" in student:
    print("Name exists")
```

Output:

```text
Name exists
```

By default, `in` checks dictionary **keys**.

```python
"name" in student
```

checks for a key.

To check values:

```python
"Tahmid" in student.values()
```

---

# 13. Changing Dictionary Items

Because dictionaries are mutable, values can be changed.

## Direct assignment

```python
student = {
    "name": "Tahmid",
    "age": 21
}

student["age"] = 22
```

Now:

```python
{'name': 'Tahmid', 'age': 22}
```

The key already exists, so its value is changed.

## Using `update()`

```python
student.update({"age": 22})
```

Multiple items can be updated at once:

```python
student.update({
    "age": 22,
    "department": "CSE"
})
```

`update()` can both **modify existing keys** and **add new keys**.

---

# 14. Adding Dictionary Items

There are two important ways shown in your code.

## 14.1 Direct assignment

```python
student = {
    "name": "Tahmid",
    "age": 21
}

student["department"] = "CSE"
```

Because `department` did not exist, it is added.

## 14.2 `update()`

```python
student.update({"department": "CSE"})
```

If the key does not exist, `update()` adds it.

If it already exists, `update()` changes its value.

### Easy rule

```text
existing key + assignment/update → change
new key + assignment/update      → add
```

---

# 15. Removing Dictionary Items

Your code demonstrates four important removal techniques.

## 15.1 `pop()`

Removes a specific key and **returns its value**.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}

removed = student.pop("age")

print(removed)
```

Output:

```text
21
```

The dictionary becomes:

```python
{
    "name": "Tahmid",
    "department": "CSE"
}
```

If the key does not exist, `pop()` raises `KeyError` unless a default value is supplied.

```python
student.pop("email", "Not Found")
```

---

## 15.2 `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}

removed = student.popitem()
print(removed)
```

Output:

```text
('department', 'CSE')
```

Remember:

```text
pop()      → remove a specified key
popitem()  → remove the last inserted pair
```

---

## 15.3 `del`

Removes a specified item.

```python
student = {
    "name": "Tahmid",
    "age": 21
}

del student["age"]
```

You can also delete the entire dictionary variable:

```python
del student
```

After that, using `student` causes a `NameError` because the variable itself no longer exists.

---

## 15.4 `clear()`

Removes all items but keeps the dictionary object.

```python
student = {
    "name": "Tahmid",
    "age": 21
}

student.clear()

print(student)
```

Output:

```text
{}
```

### `clear()` vs `del`

```python
student.clear()
```

→ dictionary becomes empty.

```python
del student
```

→ variable is deleted.

---

# 16. Looping Through Dictionaries

Dictionaries are commonly processed using `for` loops.

## 16.1 Loop through keys

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}

for key in student:
    print(key)
```

Equivalent explicit form:

```python
for key in student.keys():
    print(key)
```

---

## 16.2 Loop through values

Using indexing by key:

```python
for key in student:
    print(student[key])
```

Or, more directly:

```python
for value in student.values():
    print(value)
```

The second form is usually clearer when you only need values.

---

## 16.3 Loop through key-value pairs

Use `items()`:

```python
for key, value in student.items():
    print(key, value)
```

Example output:

```text
name Tahmid
age 21
department CSE
```

This is one of the most important dictionary loop patterns to remember.

---

# 17. Copying Dictionaries

Your code demonstrates two ways to create a copy.

## 17.1 `copy()`

```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()
```

This creates a new dictionary object.

## 17.2 `dict()`

```python
mydict = dict(thisdict)
```

This also creates a new dictionary.

---

## Why not simply use `=`?

Consider:

```python
thisdict = {
    "name": "Tahmid"
}

mydict = thisdict
```

This does **not** create an independent dictionary. Both names refer to the same dictionary object.

```python
mydict["age"] = 21

print(thisdict)
```

The original dictionary also changes.

With:

```python
mydict = thisdict.copy()
```

`mydict` is a separate top-level dictionary.

### Important advanced note

`copy()` makes a **shallow copy**. If the dictionary contains nested mutable objects such as lists or dictionaries, those nested objects can still be shared.

For example:

```python
original = {"skills": ["Python"]}
copy_dict = original.copy()

copy_dict["skills"].append("C++")
```

The nested list is shared, so both dictionaries see the new item.

For a fully independent nested copy, Python provides `copy.deepcopy()`.

---

# 18. Nested Dictionaries

A dictionary can contain another dictionary as a value.

This is called a **nested dictionary**.

Your code uses:

```python
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
```

Think of the structure as:

```text
myfamily
├── child1
│   ├── name
│   └── year
├── child2
│   ├── name
│   └── year
└── child3
    ├── name
    └── year
```

## Access nested data

```python
print(myfamily["child2"]["name"])
```

Output:

```text
Tobias
```

The access happens in two steps:

```text
myfamily["child2"]
        ↓
child2 dictionary
        ↓
["name"]
        ↓
Tobias
```

---

## Creating nested dictionaries separately

You can also create the child dictionaries first:

```python
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
```

This can be useful when the nested dictionaries are complex or reused.

---

## Loop through nested dictionaries

```python
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])
```

The outer loop processes each child dictionary.

The inner loop processes the keys inside that child dictionary.

A cleaner alternative is:

```python
for child, details in myfamily.items():
    print(child)
    for key, value in details.items():
        print(key, ":", value)
```

---

# 19. Complete Dictionary Methods

Your `09.methods.py` file demonstrates the major built-in dictionary methods.

| Method | Purpose | Example |
|---|---|---|
| `clear()` | Removes all items | `d.clear()` |
| `copy()` | Creates a shallow copy | `d.copy()` |
| `fromkeys()` | Creates a dictionary from keys | `dict.fromkeys(keys)` |
| `get()` | Gets a value safely | `d.get("name")` |
| `items()` | Returns key-value pairs | `d.items()` |
| `keys()` | Returns keys | `d.keys()` |
| `pop()` | Removes a specified key and returns its value | `d.pop("age")` |
| `popitem()` | Removes and returns last inserted pair | `d.popitem()` |
| `setdefault()` | Gets value; inserts key if missing | `d.setdefault("city", "Dhaka")` |
| `update()` | Adds/updates pairs | `d.update({...})` |
| `values()` | Returns values | `d.values()` |

---

## 19.1 `clear()`

```python
d = {"a": 1, "b": 2}
d.clear()

print(d)
```

Output:

```python
{}
```

**Use when:** you want to empty the dictionary.

---

## 19.2 `copy()`

```python
d = {"a": 1, "b": 2}
new_d = d.copy()
```

**Use when:** you need a separate shallow copy.

---

## 19.3 `fromkeys()`

Creates a new dictionary from a collection of keys.

```python
keys = ("name", "age", "department")

student = dict.fromkeys(keys, "Unknown")
```

Result:

```python
{
    "name": "Unknown",
    "age": "Unknown",
    "department": "Unknown"
}
```

Without a value:

```python
data = dict.fromkeys(["a", "b", "c"])
```

Result:

```python
{'a': None, 'b': None, 'c': None}
```

### Important

`fromkeys()` uses the same value object for every key when a value is supplied. Be careful when that value is mutable.

---

## 19.4 `get()`

```python
student.get("name")
```

Returns the associated value.

```python
student.get("email", "Not Found")
```

Returns the default if the key is missing.

---

## 19.5 `items()`

```python
student.items()
```

Used heavily in loops:

```python
for key, value in student.items():
    print(key, value)
```

---

## 19.6 `keys()`

```python
student.keys()
```

Gets all dictionary keys.

---

## 19.7 `pop()`

```python
removed = student.pop("age")
```

Removes `age` and returns its value.

Optional default:

```python
student.pop("email", "Not Found")
```

---

## 19.8 `popitem()`

```python
removed = student.popitem()
```

Removes and returns the last inserted pair.

---

## 19.9 `setdefault()`

`setdefault()` is especially useful when you want to get a value while also providing a value to insert if the key does not exist.

```python
student = {
    "name": "Tahmid",
    "age": 21
}

student.setdefault("department", "CSE")
```

Because `department` does not exist, Python adds it:

```python
{
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}
```

If the key already exists:

```python
student.setdefault("name", "Unknown")
```

Python returns the existing value and does not replace it.

### Important difference

```python
d.get("name", "Unknown")
```

only retrieves a value.

```python
d.setdefault("name", "Unknown")
```

retrieves it, and if missing, inserts the key.

---

## 19.10 `update()`

Add or modify one or more items:

```python
student.update({
    "department": "CSE",
    "cgpa": 3.75
})
```

Existing keys are overwritten:

```python
student.update({"age": 22})
```

---

## 19.11 `values()`

```python
student.values()
```

Returns a dynamic view of all values.

---

# 20. Important Differences

## `get()` vs `[]`

| Expression | Missing key behavior |
|---|---|
| `d["key"]` | Raises `KeyError` |
| `d.get("key")` | Returns `None` |
| `d.get("key", default)` | Returns `default` |

### Example

```python
student = {"name": "Tahmid"}

student["age"]
```

→ `KeyError`

```python
student.get("age")
```

→ `None`

```python
student.get("age", 0)
```

→ `0`

---

## `pop()` vs `popitem()`

```python
d.pop("age")
```

→ removes a **specific key**.

```python
d.popitem()
```

→ removes the **last inserted pair**.

---

## `clear()` vs `del`

```python
d.clear()
```

→ dictionary becomes `{}`.

```python
del d
```

→ variable `d` is deleted.

---

## `copy()` vs assignment

```python
b = a.copy()
```

→ separate top-level dictionary.

```python
b = a
```

→ both names refer to the same dictionary.

---

## `items()` vs `keys()` vs `values()`

```text
items()  → key + value
keys()   → key only
values() → value only
```

Example:

```python
d = {"a": 10, "b": 20}
```

```python
d.keys()
```

→ `a, b`

```python
d.values()
```

→ `10, 20`

```python
d.items()
```

→ `('a', 10), ('b', 20)`

---

# 21. Common Mistakes

## Mistake 1: Using a missing key directly

```python
student["email"]
```

If `email` does not exist, this raises `KeyError`.

Safer:

```python
student.get("email")
```

---

## Mistake 2: Thinking `keys()` returns a normal list

```python
student.keys()
```

returns a dictionary view object, not a list.

If you need a list:

```python
list(student.keys())
```

---

## Mistake 3: Forgetting that keys must be unique

```python
d = {"a": 1, "a": 2}
```

The final value is `2`.

---

## Mistake 4: Confusing `pop()` with `popitem()`

```python
d.pop("age")
```

removes a named key.

```python
d.popitem()
```

removes the last inserted pair.

---

## Mistake 5: Assuming `copy()` is a deep copy

```python
b = a.copy()
```

is a shallow copy. Nested mutable objects may still be shared.

---

## Mistake 6: Using `del` when you only want an empty dictionary

If you want to keep the variable but remove its contents:

```python
d.clear()
```

If you want to delete the variable itself:

```python
del d
```

---

## Mistake 7: Forgetting that direct dictionary iteration gives keys

```python
for x in student:
    print(x)
```

prints keys, not values.

For values:

```python
for x in student.values():
    print(x)
```

For both:

```python
for key, value in student.items():
    print(key, value)
```

---

# 22. Quick Revision Sheet

## Create

```python
student = {
    "name": "Tahmid",
    "age": 21
}
```

```python
student = dict(name="Tahmid", age=21)
```

## Access

```python
student["name"]
```

```python
student.get("name")
```

## Check key

```python
if "name" in student:
    print("Found")
```

## Add

```python
student["department"] = "CSE"
```

## Change

```python
student["age"] = 22
```

## Add/change multiple

```python
student.update({"age": 22, "cgpa": 3.75})
```

## Remove specific key

```python
student.pop("age")
```

## Remove last inserted item

```python
student.popitem()
```

## Delete specific item

```python
del student["age"]
```

## Empty dictionary

```python
student.clear()
```

## Copy

```python
new_student = student.copy()
```

## Keys

```python
student.keys()
```

## Values

```python
student.values()
```

## Key-value pairs

```python
student.items()
```

## Loop keys

```python
for key in student:
    print(key)
```

## Loop values

```python
for value in student.values():
    print(value)
```

## Loop both

```python
for key, value in student.items():
    print(key, value)
```

## Nested dictionary

```python
family["child1"]["name"]
```

---

# 🧠 Dictionary Mental Model

Think of a dictionary as a labeled storage system:

```text
              DICTIONARY
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
      key       key       key
        │         │         │
        ↓         ↓         ↓
     value      value      value
```

For example:

```python
student = {
    "name": "Tahmid",
    "age": 21,
    "department": "CSE"
}
```

Think:

```text
"name"       ──→ "Tahmid"
"age"        ──→ 21
"department" ──→ "CSE"
```

The key is the label you use to find the value.

---

# ⚡ Most Important Patterns to Memorize

### 1. Access

```python
d["key"]
```

### 2. Safe access

```python
d.get("key")
```

### 3. Add/change

```python
d["key"] = value
```

### 4. Multiple add/change

```python
d.update({"key": value})
```

### 5. Remove specific item

```python
d.pop("key")
```

### 6. Loop keys

```python
for key in d:
    print(key)
```

### 7. Loop values

```python
for value in d.values():
    print(value)
```

### 8. Loop key + value

```python
for key, value in d.items():
    print(key, value)
```

### 9. Check existence

```python
if "key" in d:
    ...
```

### 10. Nested access

```python
d["outer"]["inner"]
```

---

# 🎯 Dictionary Methods at a Glance

```text
clear()       → remove everything
copy()        → shallow copy
fromkeys()    → create dictionary from keys
get()         → safely get a value
items()       → get key-value pairs
keys()        → get keys
pop()         → remove a specified key
popitem()     → remove last inserted pair
setdefault()  → get value / insert if missing
update()      → add or modify items
values()      → get values
```

### Easy memory grouping

```text
READ
├── get()
├── keys()
├── values()
└── items()

WRITE
├── d[key] = value
├── update()
└── setdefault()

REMOVE
├── pop()
├── popitem()
├── del
└── clear()

COPY / CREATE
├── copy()
└── fromkeys()
```

---

# 📁 Practice Files

| File | Main Topics |
|---|---|
| `01.dict.py` | Dictionary basics, properties, duplicate keys, `len()`, data types, `dict()` |
| `02.access_item.py` | Accessing items, `get()`, `keys()`, `values()`, `items()`, `in` |
| `03.change_item.py` | Changing values, `update()` |
| `04.add_items.py` | Adding items, `update()` |
| `05.remove_items.py` | `pop()`, `popitem()`, `del`, `clear()` |
| `06.loop_dict.py` | Dictionary iteration, keys, values, items |
| `07.copy_dict.py` | `copy()` and `dict()` copying |
| `08.nested_dict.py` | Nested dictionaries and nested loops |
| `09.methods.py` | Complete dictionary method revision |

---

# 📝 Mini Practice Problems

Try solving these without looking at the notes.

### Problem 1
Create a dictionary containing:

```text
name
age
department
cgpa
```

Then print each value.

### Problem 2
Add a new key called `university`.

### Problem 3
Change the student's `cgpa`.

### Problem 4
Safely retrieve an `email` key that may not exist.

### Problem 5
Loop through the dictionary and print:

```text
key : value
```

### Problem 6
Remove the `age` key.

### Problem 7
Create a nested dictionary containing information about three students.

### Problem 8
Find whether a particular key exists using `in`.

### Problem 9
Create a dictionary from a list of keys using `fromkeys()`.

### Problem 10
Use `setdefault()` to create a missing `country` key with a default value.

---

# ✅ Final Checklist

Before moving to the next Python topic, make sure you can:

- [ ] Explain what a dictionary is
- [ ] Create an empty dictionary
- [ ] Create a dictionary with key-value pairs
- [ ] Use the `dict()` constructor
- [ ] Explain dictionary insertion order
- [ ] Explain why keys must be unique
- [ ] Access a value using `[]`
- [ ] Safely access a value using `get()`
- [ ] Check whether a key exists with `in`
- [ ] Add a new item
- [ ] Change an existing item
- [ ] Use `update()`
- [ ] Remove an item with `pop()`
- [ ] Understand `popitem()`
- [ ] Use `del`
- [ ] Empty a dictionary with `clear()`
- [ ] Loop through keys
- [ ] Loop through values
- [ ] Loop through key-value pairs
- [ ] Understand dictionary views
- [ ] Copy a dictionary
- [ ] Understand shallow copying
- [ ] Create nested dictionaries
- [ ] Access nested values
- [ ] Loop through nested dictionaries
- [ ] Use all major dictionary methods
- [ ] Explain `get()` vs `[]`
- [ ] Explain `pop()` vs `popitem()`
- [ ] Explain `clear()` vs `del`
- [ ] Explain `copy()` vs `=`

---

# 🚀 Final Takeaway

A Python dictionary is one of the most useful data structures for real-world programming because it lets you organize information using meaningful keys.

The core pattern is:

```python
dictionary = {
    "key": "value"
}
```

Then learn these operations first:

```python
# Access
d["key"]

# Safe access
d.get("key")

# Add / change
d["key"] = value

# Update multiple
d.update({...})

# Remove
d.pop("key")

# Loop
for key, value in d.items():
    print(key, value)
```

If you understand these patterns well, you already have the foundation needed to use dictionaries in **projects, APIs, JSON data, databases, automation, backend development, and Data Structures & Algorithms**.

> **Revision rule:** When revising dictionaries, don't just memorize the methods. Write a small dictionary and practice **create → access → add → update → search → loop → remove → copy → nest**. That sequence covers almost everything in this chapter.
