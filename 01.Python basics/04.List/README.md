# 🐍 Python Lists — Complete Revision Notes

> **A revision-friendly guide based on the code in this folder.**
>
> This README covers Python Lists from the basics to practical list operations, list comprehension, sorting, copying, joining, looping, and all major built-in list methods demonstrated in the examples.

---

## 📚 Table of Contents

1. [What is a List?](#1-what-is-a-list)
2. [Creating Lists](#2-creating-lists)
3. [List Properties](#3-list-properties)
4. [Accessing List Items](#4-accessing-list-items)
5. [Negative Indexing](#5-negative-indexing)
6. [List Slicing](#6-list-slicing)
7. [Checking Whether an Item Exists](#7-checking-whether-an-item-exists)
8. [Changing List Items](#8-changing-list-items)
9. [Changing a Range of Items](#9-changing-a-range-of-items)
10. [Inserting Items](#10-inserting-items)
11. [Adding Items](#11-adding-items)
12. [Removing Items](#12-removing-items)
13. [Looping Through a List](#13-looping-through-a-list)
14. [List Comprehension](#14-list-comprehension)
15. [Sorting Lists](#15-sorting-lists)
16. [Copying Lists](#16-copying-lists)
17. [Joining Lists](#17-joining-lists)
18. [All Important List Methods](#18-all-important-list-methods)
19. [Method Quick Reference](#19-method-quick-reference)
20. [Time Complexity Cheat Sheet](#20-time-complexity-cheat-sheet)
21. [Common Mistakes](#21-common-mistakes)
22. [Revision Checklist](#22-revision-checklist)

---

# 1. What is a List?

A **list** is one of Python's built-in collection data types.

A list is used when we want to store **multiple values inside one variable**.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits)
```

Output:

```text
['apple', 'banana', 'cherry']
```

Instead of:

```python
fruit1 = "apple"
fruit2 = "banana"
fruit3 = "cherry"
```

we can store everything in one list:

```python
fruits = ["apple", "banana", "cherry"]
```

---

# 2. Creating Lists

## 2.1 Basic list

```python
numbers = [10, 20, 30, 40]
```

## 2.2 List with strings

```python
names = ["Tahmid", "Dhrubo", "Taqi"]
```

## 2.3 Mixed data types

Python lists can contain different types of values.

```python
mylist = ["abc", 34, True, 40, "male"]
```

A single list can contain:

- `str`
- `int`
- `float`
- `bool`
- another `list`
- objects
- etc.

## 2.4 Creating a list with `list()`

The `list()` constructor can create a list from an iterable.

```python
marks = list((85, 87, 56))

print(marks)
```

Output:

```text
[85, 87, 56]
```

---

# 3. List Properties

Python lists have several important properties.

## 3.1 Ordered

Items maintain their order.

```python
x = ["a", "b", "c"]
```

The order is:

```text
a → b → c
```

## 3.2 Changeable / Mutable

We can change an existing element.

```python
marks = [90, 98, 87]

marks[0] = 82

print(marks)
```

Output:

```text
[82, 98, 87]
```

## 3.3 Allow Duplicates

A list can contain the same value multiple times.

```python
numbers = [10, 20, 10, 30, 10]
```

Here `10` appears three times.

## 3.4 Indexed

Every element has a position called an **index**.

```text
Value:  apple   banana   cherry
Index:    0        1         2
```

## 3.5 Dynamic Size

Lists can grow and shrink during program execution.

```python
numbers = [1, 2]

numbers.append(3)

print(numbers)
```

Output:

```text
[1, 2, 3]
```

---

# 4. Accessing List Items

List elements are accessed using indexes.

```python
names = ["Tahmid", "Dhrubo", "Taqi"]

print(names[1])
```

Output:

```text
Dhrubo
```

### Index diagram

```text
          0         1        2
        ┌────────┬────────┬────────┐
        │ Tahmid │ Dhrubo │  Taqi  │
        └────────┴────────┴────────┘
```

General syntax:

```python
list_name[index]
```

Example:

```python
print(names[0])  # Tahmid
print(names[2])  # Taqi
```

### Important

Python uses **zero-based indexing**.

The first item is at index `0`, not `1`.

---

# 5. Negative Indexing

Python also supports negative indexes.

```text
Positive:     0       1       2
             ┌───────┬───────┬───────┐
             │ apple │banana │cherry │
             └───────┴───────┴───────┘
Negative:    -3      -2      -1
```

So:

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[-1])
```

Output:

```text
cherry
```

### Negative index rules

- `-1` → last item
- `-2` → second-last item
- `-3` → third-last item

---

# 6. List Slicing

Slicing allows us to extract a part of a list.

Syntax:

```python
list[start:stop]
```

The `stop` index is **not included**.

Example:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[2:5])
```

Output:

```text
['cherry', 'orange', 'kiwi']
```

Indexes:

```text
0       1        2         3        4       5       6
apple banana   cherry    orange    kiwi    melon   mango
                  ↑                  ↑
                start               stop
```

`2:5` means:

```text
2, 3, 4
```

but not `5`.

## Negative slicing

```python
fruits[-4:-1]
```

This means:

```text
-4, -3, -2
```

The `-1` position is excluded.

## Useful slicing forms

```python
numbers[:]       # entire list
numbers[:3]      # first 3 items
numbers[2:]      # from index 2 to end
numbers[-3:]     # last 3 items
numbers[::2]     # every second item
numbers[::-1]    # reverse order
```

---

# 7. Checking Whether an Item Exists

Use the `in` operator.

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple exists")
```

Output:

```text
Apple exists
```

You can also use `not in`:

```python
if "mango" not in fruits:
    print("Mango does not exist")
```

This is very useful before operations such as `remove()`.

---

# 8. Changing List Items

Because lists are mutable, individual elements can be changed.

```python
marks = [90, 98, 87]

marks[0] = 82

print(marks)
```

Result:

```text
[82, 98, 87]
```

---

# 9. Changing a Range of Items

A slice can be replaced with another list.

```python
fruits = ["apple", "banana", "cherry", "orange"]

fruits[1:3] = ["blackcurrant", "watermelon"]

print(fruits)
```

Result:

```text
['apple', 'blackcurrant', 'watermelon', 'orange']
```

## Replacing one item with multiple items

```python
fruits = ["apple", "banana", "cherry"]

fruits[1:2] = ["blackcurrant", "watermelon"]
```

Result:

```text
['apple', 'blackcurrant', 'watermelon', 'cherry']
```

The list grows because one item was replaced by two.

## Replacing multiple items with one

```python
fruits = ["apple", "banana", "cherry"]

fruits[1:3] = ["watermelon"]
```

Result:

```text
['apple', 'watermelon']
```

The list becomes smaller.

---

# 10. Inserting Items

Use:

```python
insert(index, value)
```

Example:

```python
fruits = ["apple", "banana", "cherry"]

fruits.insert(2, "watermelon")

print(fruits)
```

Result:

```text
['apple', 'banana', 'watermelon', 'cherry']
```

The existing element at index `2` and the elements after it shift right.

### Important

`insert()` does **not replace** an existing item.

It adds a new item.

---

# 11. Adding Items

There are three important operations demonstrated in the code:

- `append()`
- `extend()`
- `insert()`

## 11.1 `append()`

Adds **one element** to the end.

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)
```

Result:

```text
['apple', 'banana', 'cherry', 'orange']
```

### Important distinction

```python
numbers.append([4, 5])
```

adds the entire list as **one element**:

```text
[1, 2, 3, [4, 5]]
```

---

## 11.2 `extend()`

Adds elements from another iterable.

```python
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

fruits.extend(tropical)
```

Result:

```text
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

### `append()` vs `extend()`

```python
a = [1, 2]
a.append([3, 4])
```

Result:

```text
[1, 2, [3, 4]]
```

But:

```python
a = [1, 2]
a.extend([3, 4])
```

Result:

```text
[1, 2, 3, 4]
```

### `extend()` accepts any iterable

```python
letters = ["a", "b"]

letters.extend(("c", "d"))
```

Result:

```text
['a', 'b', 'c', 'd']
```

With a string:

```python
letters.extend("ef")
```

Result:

```text
['a', 'b', 'c', 'd', 'e', 'f']
```

A string is iterable, so its characters are added individually.

---

# 12. Removing Items

Python provides several ways to remove elements.

## 12.1 `remove(value)`

Removes the **first occurrence** of a value.

```python
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")
```

Result:

```text
['apple', 'cherry']
```

If duplicates exist:

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
```

Only the first `"banana"` is removed.

### If value doesn't exist

```python
fruits.remove("mango")
```

raises:

```text
ValueError
```

Safer:

```python
if "mango" in fruits:
    fruits.remove("mango")
```

---

## 12.2 `pop(index)`

Removes an element by index and **returns the removed value**.

```python
fruits = ["apple", "banana", "cherry"]

removed = fruits.pop(1)

print(removed)
print(fruits)
```

Output:

```text
banana
['apple', 'cherry']
```

### `pop()` without an index

```python
fruits.pop()
```

removes the last element.

This is useful when implementing stack-like behavior.

---

## 12.3 `del`

Delete an item by index:

```python
fruits = ["apple", "banana", "cherry"]

del fruits[0]
```

Result:

```text
['banana', 'cherry']
```

It can also delete a range:

```python
del fruits[1:3]
```

It can even delete the entire list variable:

```python
del fruits
```

After this, the variable `fruits` no longer exists.

---

## 12.4 `clear()`

Removes all elements but keeps the list object.

```python
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
```

Output:

```text
[]
```

### `del` vs `clear()`

```python
del fruits
```

→ deletes the variable/list reference.

```python
fruits.clear()
```

→ keeps the list but makes it empty.

---

# 13. Looping Through a List

## 13.1 Simple `for` loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

This is the cleanest way when you only need the values.

---

## 13.2 Loop using indexes

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(fruits[i])
```

Here:

```python
len(fruits)
```

gives the number of elements.

Then:

```python
range(len(fruits))
```

generates the valid indexes.

---

## 13.3 `while` loop

```python
fruits = ["apple", "banana", "cherry"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

Useful when the loop needs more control over the index.

---

## 13.4 Loop with list comprehension

```python
fruits = ["apple", "banana", "cherry"]

[print(x) for x in fruits]
```

This works, but **list comprehension is primarily intended for creating lists**, not just printing values.

Prefer:

```python
for x in fruits:
    print(x)
```

for simple printing.

---

# 14. List Comprehension

List comprehension is a compact way to create a new list.

Instead of:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
```

we can write:

```python
newlist = [x for x in fruits if "a" in x]
```

---

## General Syntax

```python
newlist = [expression for item in iterable if condition]
```

Think of it as:

```text
            What to put in new list
                       ↓
        [ expression for item in iterable if condition ]
                       ↑                     ↑
                    variable              filter
```

---

## Example 1 — Filter values

```python
numbers = range(10)

newlist = [x for x in numbers if x < 5]
```

Result:

```text
[0, 1, 2, 3, 4]
```

---

## Example 2 — Exclude a value

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]
```

Result:

```text
['banana', 'cherry', 'kiwi', 'mango']
```

---

## Example 3 — Transform values

```python
newlist = [x.upper() for x in fruits]
```

Result:

```text
['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```

---

## Example 4 — Create a fixed-value list

```python
newlist = ["hello" for x in fruits]
```

If `fruits` has 5 elements:

```text
['hello', 'hello', 'hello', 'hello', 'hello']
```

---

## Example 5 — `if ... else`

```python
newlist = [
    x if x != "banana" else "orange"
    for x in fruits
]
```

This means:

```text
if item != "banana"
    keep item
else
    use "orange"
```

### Important difference

Filter:

```python
[x for x in numbers if x > 5]
```

Conditional transformation:

```python
[x if x > 5 else 0 for x in numbers]
```

---

# 15. Sorting Lists

Python provides `sort()` for in-place sorting.

## 15.1 Alphabetical / ascending order

```python
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

fruits.sort()

print(fruits)
```

Result:

```text
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

---

## 15.2 Descending order

```python
fruits.sort(reverse=True)
```

---

## 15.3 Numeric sorting

```python
numbers = [100, 50, 65, 82, 23]

numbers.sort()
```

Result:

```text
[23, 50, 65, 82, 100]
```

---

## 15.4 Custom sorting with `key`

Suppose we want numbers sorted by their distance from `50`.

```python
def myfunc(n):
    return abs(n - 50)

numbers = [100, 50, 65, 82, 23]

numbers.sort(key=myfunc)
```

The key values are:

```text
100 → 50
50  → 0
65  → 15
82  → 32
23  → 27
```

So the order becomes:

```text
[50, 65, 23, 82, 100]
```

The `key` function tells Python **what value to use for comparison**.

---

## 15.5 Case-insensitive sorting

Normal sorting can be affected by uppercase/lowercase characters.

```python
words = ["banana", "Orange", "Kiwi", "cherry"]

words.sort(key=str.lower)
```

This sorts using lowercase versions for comparison.

---

## 15.6 Sorting by a tuple field

```python
people = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 20),
    ("David", 35)
]

people.sort(key=lambda x: x[1])
```

This sorts by age.

To sort by name:

```python
people.sort(key=lambda x: x[0])
```

### Remember

```python
key=lambda x: x[1]
```

means:

> Use the second element of each tuple as the sorting key.

---

# 16. Copying Lists

There are multiple ways to copy a list.

## 16.1 `copy()`

```python
original = ["apple", "banana", "cherry"]

copied = original.copy()
```

The result is a new list.

```python
print(original is copied)
```

Output:

```text
False
```

---

## 16.2 Using `list()`

```python
copied = list(original)
```

---

## 16.3 Using slicing

```python
copied = original[:]
```

All three create a **shallow copy**.

---

## Why copying matters

Consider:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

Why?

Because:

```python
b = a
```

does not create a new list. Both names refer to the same list.

But:

```python
b = a.copy()
```

creates a separate list.

---

# 17. Joining Lists

## 17.1 Using `+`

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
```

Result:

```text
['a', 'b', 'c', 1, 2, 3]
```

This creates a new list.

---

## 17.2 Using `append()` in a loop

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
```

Result:

```text
['a', 'b', 'c', 1, 2, 3]
```

---

## 17.3 Using `extend()`

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
```

Usually this is the cleanest option when you want to add all elements of one list to another.

---

# 18. All Important List Methods

The code includes a comprehensive demonstration of these **11 core list methods**:

```text
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
```

---

## 18.1 `append()`

### Purpose

Adds one element to the end.

```python
numbers = [1, 2, 3]

numbers.append(4)
```

Result:

```text
[1, 2, 3, 4]
```

### Key point

`append()` changes the original list.

---

## 18.2 `clear()`

### Purpose

Removes everything.

```python
numbers = [1, 2, 3]

numbers.clear()
```

Result:

```text
[]
```

---

## 18.3 `copy()`

### Purpose

Creates a shallow copy.

```python
a = [1, 2, 3]

b = a.copy()
```

Now:

```text
a → [1, 2, 3]
b → [1, 2, 3]
```

but they are different list objects.

---

## 18.4 `count()`

### Purpose

Counts occurrences of a value.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Output:

```text
3
```

If the item does not exist:

```python
numbers.count(99)
```

returns:

```text
0
```

---

## 18.5 `extend()`

### Purpose

Adds every element from an iterable.

```python
a = [1, 2]
b = [3, 4]

a.extend(b)
```

Result:

```text
[1, 2, 3, 4]
```

---

## 18.6 `index()`

### Purpose

Finds the index of the first matching value.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits.index("cherry"))
```

Output:

```text
2
```

### With a starting position

```python
numbers = [10, 20, 30, 20, 40, 20, 50]

numbers.index(20, 3)
```

Search begins from index `3`.

### With start and end

```python
numbers.index(20, 2, 5)
```

Searches within the specified range.

### If not found

`index()` raises:

```text
ValueError
```

---

## 18.7 `insert()`

### Purpose

Adds an item at a specific index.

```python
colors = ["red", "green", "blue"]

colors.insert(1, "yellow")
```

Result:

```text
['red', 'yellow', 'green', 'blue']
```

---

## 18.8 `pop()`

### Purpose

Removes and returns an item.

```python
numbers = [10, 20, 30]

x = numbers.pop(1)

print(x)
```

Output:

```text
20
```

List becomes:

```text
[10, 30]
```

Without an index:

```python
numbers.pop()
```

removes the last element.

---

## 18.9 `remove()`

### Purpose

Removes the first matching value.

```python
numbers = [10, 20, 20, 30]

numbers.remove(20)
```

Result:

```text
[10, 20, 30]
```

Only the first `20` is removed.

---

## 18.10 `reverse()`

### Purpose

Reverses the list **in place**.

```python
letters = ["a", "b", "c", "d"]

letters.reverse()
```

Result:

```text
['d', 'c', 'b', 'a']
```

It modifies the original list.

### `reverse()` vs `reversed()`

```python
numbers.reverse()
```

changes the original list.

But:

```python
reversed_numbers = list(reversed(numbers))
```

creates a new list and leaves the original unchanged.

---

## 18.11 `sort()`

### Purpose

Sorts the list in place.

```python
numbers = [5, 2, 8, 1]

numbers.sort()
```

Result:

```text
[1, 2, 5, 8]
```

Descending:

```python
numbers.sort(reverse=True)
```

Custom:

```python
numbers.sort(key=len)
```

Lambda:

```python
people.sort(key=lambda x: x[1])
```

---

# 19. Method Quick Reference

| Method | Purpose | Changes Original? |
|---|---|---|
| `append(x)` | Add one item at end | ✅ |
| `clear()` | Remove all items | ✅ |
| `copy()` | Create shallow copy | ❌ |
| `count(x)` | Count occurrences | ❌ |
| `extend(iterable)` | Add multiple items | ✅ |
| `index(x)` | Find first index | ❌ |
| `insert(i, x)` | Insert at index | ✅ |
| `pop(i)` | Remove + return item | ✅ |
| `remove(x)` | Remove first matching value | ✅ |
| `reverse()` | Reverse in place | ✅ |
| `sort()` | Sort in place | ✅ |

---

# 20. Time Complexity Cheat Sheet

For a Python list, remember these approximate complexities:

| Operation | Typical Complexity |
|---|---:|
| Access `a[i]` | **O(1)** |
| Update `a[i]` | **O(1)** |
| `append()` | **O(1)** amortized |
| `pop()` from end | **O(1)** |
| `insert(0, x)` | **O(n)** |
| `pop(0)` | **O(n)** |
| `remove(x)` | **O(n)** |
| `x in list` | **O(n)** |
| `index(x)` | **O(n)** |
| `count(x)` | **O(n)** |
| `reverse()` | **O(n)** |
| `sort()` | **O(n log n)** |
| Copy entire list | **O(n)** |

### Why is `insert(0, x)` O(n)?

Because existing elements need to shift to the right.

Example:

```text
Before:
[10, 20, 30, 40]

insert(0, 5)

After:
[5, 10, 20, 30, 40]
```

Several elements had to move.

---

# 21. Common Mistakes

## Mistake 1 — Confusing `append()` and `extend()`

```python
a = [1, 2]

a.append([3, 4])
```

Result:

```text
[1, 2, [3, 4]]
```

Whereas:

```python
a.extend([3, 4])
```

Result:

```text
[1, 2, 3, 4]
```

---

## Mistake 2 — Forgetting that slicing excludes the stop index

```python
a[1:4]
```

includes:

```text
1, 2, 3
```

not `4`.

---

## Mistake 3 — Thinking assignment creates a copy

```python
a = [1, 2, 3]
b = a
```

`a` and `b` refer to the same list.

Use:

```python
b = a.copy()
```

if you need a separate shallow copy.

---

## Mistake 4 — `remove()` uses a value, not an index

Correct:

```python
a.remove(20)
```

Wrong if you mean "remove index 20":

```python
a.remove(20)
```

For an index use:

```python
a.pop(20)
```

or:

```python
del a[20]
```

---

## Mistake 5 — `pop()` returns the removed item

```python
x = a.pop()
```

`x` contains the removed value.

This makes `pop()` especially useful in stack implementations.

---

## Mistake 6 — `sort()` changes the original list

```python
numbers.sort()
```

does not create a new sorted list.

If you want a new sorted list:

```python
new_numbers = sorted(numbers)
```

---

## Mistake 7 — `index()` may raise an error

```python
numbers.index(100)
```

raises `ValueError` if `100` is absent.

Safer:

```python
if 100 in numbers:
    print(numbers.index(100))
```

---

# 22. Revision Checklist

Use this before an exam or coding session.

- [ ] I understand what a Python list is.
- [ ] I know that lists are ordered, mutable, and allow duplicates.
- [ ] I understand zero-based indexing.
- [ ] I can use positive and negative indexes.
- [ ] I can slice a list.
- [ ] I understand that the slicing stop index is excluded.
- [ ] I can check membership using `in` and `not in`.
- [ ] I can change individual list items.
- [ ] I can replace a range of items.
- [ ] I know how `insert()` works.
- [ ] I understand `append()` vs `extend()`.
- [ ] I know the difference between `remove()`, `pop()`, `del`, and `clear()`.
- [ ] I can loop through a list with `for`.
- [ ] I can loop using indexes.
- [ ] I can use a `while` loop with a list.
- [ ] I understand list comprehension syntax.
- [ ] I can filter values with list comprehension.
- [ ] I can transform values with list comprehension.
- [ ] I can use `if ... else` inside list comprehension.
- [ ] I can sort ascending and descending.
- [ ] I understand the `key` parameter of `sort()`.
- [ ] I can sort using a lambda function.
- [ ] I know three ways to copy a list.
- [ ] I understand why `b = a` is not a real copy.
- [ ] I know multiple ways to join lists.
- [ ] I know all 11 important list methods.
- [ ] I understand common list operation complexities.

---

# ⚡ Ultra-Quick Revision

```python
# Create
a = [1, 2, 3]

# Access
a[0]
a[-1]

# Slice
a[1:3]

# Change
a[0] = 100

# Insert
a.insert(1, 50)

# Add
a.append(4)
a.extend([5, 6])

# Remove
a.remove(50)
a.pop()
del a[0]
a.clear()

# Search
3 in a
a.index(3)
a.count(3)

# Loop
for x in a:
    print(x)

# Comprehension
squares = [x*x for x in a]

# Sort
a.sort()
a.sort(reverse=True)

# Reverse
a.reverse()

# Copy
b = a.copy()

# Join
c = a + b
a.extend(b)
```

---

## 🧠 The Most Important Differences

### `append()` vs `extend()`

```text
append([3,4])  → [1,2,[3,4]]
extend([3,4])  → [1,2,3,4]
```

### `remove()` vs `pop()`

```text
remove(value) → remove by VALUE
pop(index)    → remove by INDEX and return value
```

### `del` vs `clear()`

```text
del a      → delete the list variable
clear()    → empty the list
```

### `reverse()` vs `reversed()`

```text
reverse()   → modifies original list
reversed()  → returns an iterator
```

### `sort()` vs `sorted()`

```text
sort()      → sorts original list
sorted()    → returns a new sorted result
```

### `b = a` vs `a.copy()`

```text
b = a       → same list object
a.copy()    → new shallow list
```

---

# 🎯 Final Takeaway

A Python list is one of the most important data structures to master before moving deeper into Python, problem solving, data structures, and machine learning.

The core ideas to remember are:

```text
LIST
 │
 ├── Create
 ├── Access
 ├── Slice
 ├── Change
 ├── Insert
 ├── Append
 ├── Extend
 ├── Remove
 ├── Pop
 ├── Delete
 ├── Clear
 ├── Loop
 ├── Comprehension
 ├── Sort
 ├── Reverse
 ├── Copy
 └── Join
```

If these operations become natural, you will be able to use Python lists comfortably in **competitive programming, automation, data processing, AI/ML, and everyday Python development**.
