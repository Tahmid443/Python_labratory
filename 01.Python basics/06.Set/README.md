# 🐍 Python Sets — Complete Revision Notes

> **Revision-focused notes based on the code in this `06.Set` folder.**
>
> This README covers Python `set`, set operations, all important set methods, operator shortcuts, `frozenset`, and the important differences between methods that return a new set and methods that modify the original set.

---

## 📚 Table of Contents

1. [What is a Set?](#1-what-is-a-set)
2. [Creating Sets](#2-creating-sets)
3. [Important Properties of Sets](#3-important-properties-of-sets)
4. [Duplicate Values](#4-duplicate-values)
5. [True and 1, False and 0](#5-true-and-1-false-and-0)
6. [Set Length](#6-set-length)
7. [Set Constructor](#7-set-constructor)
8. [Accessing Set Items](#8-accessing-set-items)
9. [Checking Membership](#9-checking-membership)
10. [Adding Items](#10-adding-items)
11. [Removing Items](#11-removing-items)
12. [Joining Sets](#12-joining-sets)
13. [Union](#13-union)
14. [Intersection](#14-intersection)
15. [Difference](#15-difference)
16. [Symmetric Difference](#16-symmetric-difference)
17. [Update Operations](#17-update-operations)
18. [Subset and Superset](#18-subset-and-superset)
19. [Disjoint Sets](#19-disjoint-sets)
20. [All Important Set Methods](#20-all-important-set-methods)
21. [Set Operators Cheat Sheet](#21-set-operators-cheat-sheet)
22. [New Set vs Update Methods](#22-new-set-vs-update-methods)
23. [Frozenset](#23-frozenset)
24. [Frozenset Methods](#24-frozenset-methods)
25. [Set vs Tuple vs List](#25-set-vs-tuple-vs-list)
26. [Time Complexity Cheat Sheet](#26-time-complexity-cheat-sheet)
27. [Common Mistakes](#27-common-mistakes)
28. [Revision Checklist](#28-revision-checklist)
29. [Ultra-Quick Revision](#29-ultra-quick-revision)

---

# 1. What is a Set?

A **set** is a Python collection used to store **unique elements**.

Example:

```python
thisset = {"apple", "banana", "cherry"}

print(thisset)
```

A set is especially useful when you care about:

- uniqueness
- fast membership checking
- mathematical set operations
- removing duplicates

For example:

```python
numbers = {1, 2, 3, 2, 1}
```

The duplicate values are automatically removed.

The resulting set contains only:

```text
{1, 2, 3}
```

---

# 2. Creating Sets

## 2.1 Using `{}`

The most common syntax is:

```python
fruits = {"apple", "banana", "cherry"}
```

---

## 2.2 Mixed data types

A set can contain different hashable data types:

```python
data = {"apple", 10, True, 3.14}
```

---

## 2.3 Empty set

Be careful:

```python
x = {}
```

does **not** create an empty set.

It creates an empty dictionary.

To create an empty set:

```python
x = set()
```

This is an important Python rule.

---

## 2.4 Using `set()`

The `set()` constructor can convert an iterable into a set.

```python
thisset = set(("apple", "banana", "cherry"))

print(thisset)
```

Output contains:

```text
{'apple', 'banana', 'cherry'}
```

The double parentheses are because the tuple is being passed as the argument:

```python
set(
    ("apple", "banana", "cherry")
)
```

You can also convert a list:

```python
numbers = set([1, 2, 3, 2])
```

Result:

```text
{1, 2, 3}
```

---

# 3. Important Properties of Sets

Python sets have several important characteristics.

## 3.1 Unordered

Sets do not provide a positional order that you can rely on.

```python
fruits = {"apple", "banana", "cherry"}
```

You should not expect the elements to appear in a particular order when printed or iterated.

---

## 3.2 Unindexed

You cannot access a set using an index.

This is invalid:

```python
fruits[0]  # ❌
```

Unlike lists and tuples, sets do not support:

```python
set[index]
```

If you need to inspect every element, use a loop:

```python
for fruit in fruits:
    print(fruit)
```

---

## 3.3 No duplicate elements

A set stores each unique value only once.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Conceptually:

```text
{1, 2, 3}
```

---

## 3.4 Mutable

A set itself can be changed.

You can:

```python
add()
remove()
discard()
pop()
clear()
update()
```

But the individual elements must be **hashable**.

For example:

```python
A = {1, 2, 3}

A.add(4)
```

is valid.

A mutable list cannot normally be an element:

```python
A = {[1, 2]}  # ❌
```

because lists are unhashable.

---

# 4. Duplicate Values

Duplicates are automatically ignored.

Example:

```python
thisset = {
    "apple",
    "banana",
    "cherry",
    "apple"
}

print(thisset)
```

There is only one `"apple"` in the resulting set.

This makes sets extremely useful for removing duplicates from a sequence:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)
```

Result:

```text
{1, 2, 3, 4}
```

### Important

A set does not count how many times a value originally appeared.

It keeps only the unique value.

---

# 5. True and 1, False and 0

Python considers:

```python
True == 1
False == 0
```

Therefore, sets treat these as equivalent values for uniqueness.

Example:

```python
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
```

`True` and `1` cannot exist as two separate set elements because they compare equal.

Similarly:

```python
{False, 0}
```

contains only one of those equivalent values.

### Revision rule

```text
True  == 1
False == 0
```

This matters when working with set uniqueness and set operations.

---

# 6. Set Length

Use:

```python
len(set_name)
```

Example:

```python
thisset = {"apple", "banana", "cherry", "apple"}

print(len(thisset))
```

The result is the number of **unique elements**, not the number of values originally written.

For example:

```python
x = {1, 2, 2, 3, 3, 3}

len(x)
```

returns:

```text
3
```

---

# 7. Set Constructor

The `set()` constructor accepts an iterable.

Examples:

```python
set([1, 2, 3])
```

```python
set((1, 2, 3))
```

```python
set("hello")
```

The string example produces unique characters, conceptually:

```text
{'h', 'e', 'l', 'o'}
```

Repeated characters are removed.

### Important

The order of a normal set should not be relied upon.

---

# 8. Accessing Set Items

There is **no indexing** in a set.

This is invalid:

```python
myset = {"apple", "banana", "cherry"}

print(myset[0])  # ❌
```

Instead, iterate:

```python
for x in myset:
    print(x)
```

Because sets are unordered, the iteration order should not be treated as a meaningful sequence order.

---

# 9. Checking Membership

One of the most important uses of a set is membership checking.

Use:

```python
in
```

Example:

```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

Output:

```text
True
```

---

## Using `not in`

```python
print("banana" not in thisset)
```

Output:

```text
False
```

Example:

```python
if "mango" not in thisset:
    print("Mango is not present")
```

### Why sets are useful here

Set membership is typically **O(1) average-case**, making sets very useful when you repeatedly need to ask:

> "Does this value exist?"

---

# 10. Adding Items

There are two important ways demonstrated in the code:

```text
add()
update()
```

---

## 10.1 `add()`

Adds one element.

```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```

Result contains:

```text
orange
```

### Important

If the element already exists:

```python
thisset.add("apple")
```

the set remains unchanged.

No duplicate is created.

---

## 10.2 `update()`

Adds elements from another iterable.

```python
thisset = {"apple", "banana", "cherry"}

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
```

Now the set contains elements from both collections.

---

## `update()` does not require a set

The argument can be any iterable.

Example from the code:

```python
thisset = {"apple", "banana", "cherry"}

mylist = ["kiwi", "orange"]

thisset.update(mylist)
```

The list elements are added to the set.

You can also use:

```python
thisset.update((1, 2, 3))
```

---

## `add()` vs `update()`

```text
add(x)
    ↓
adds ONE element

update(iterable)
    ↓
adds ALL elements from the iterable
```

Example:

```python
A = {1, 2}

A.add((3, 4))
```

The tuple itself becomes one element:

```text
{1, 2, (3, 4)}
```

But:

```python
A = {1, 2}

A.update((3, 4))
```

adds the elements:

```text
{1, 2, 3, 4}
```

---

# 11. Removing Items

The code demonstrates four major removal operations:

```text
remove()
discard()
pop()
clear()
```

and also:

```text
del
```

---

# 11.1 `remove()`

Removes a specified element.

```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
```

Result:

```text
{'apple', 'cherry'}
```

### Important

If the item does not exist:

```python
thisset.remove("mango")
```

raises:

```text
KeyError
```

---

# 11.2 `discard()`

Also removes a specified element:

```python
thisset.discard("banana")
```

But there is an important difference.

If the element does not exist:

```python
thisset.discard("mango")
```

**no error occurs**.

### `remove()` vs `discard()`

```text
remove(x)
    ├── exists     → remove
    └── absent     → KeyError

discard(x)
    ├── exists     → remove
    └── absent     → nothing happens
```

### Easy memory trick

```text
remove()   → strict
discard()  → safe
```

---

# 11.3 `pop()`

`pop()` removes and returns an **arbitrary element**.

```python
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)
```

Because sets are unordered, you cannot reliably predict which element will be removed.

### Important

Do not think:

```python
set.pop()
```

means "remove the last item".

That is true for a list, but **not for a set**.

For a set:

```text
pop() → removes an arbitrary element
```

---

# 11.4 `clear()`

Removes every element.

```python
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
```

Output:

```text
set()
```

The set still exists; it is simply empty.

---

# 11.5 `del`

`del` can delete the set variable completely.

```python
thisset = {"apple", "banana", "cherry"}

del thisset
```

After this, `thisset` no longer exists.

Trying:

```python
print(thisset)
```

raises:

```text
NameError
```

### `clear()` vs `del`

```text
clear() → keep set, remove all elements
del     → delete the variable/set itself
```

---

# 12. Joining Sets

The code demonstrates several mathematical set operations:

```text
union
intersection
difference
symmetric difference
```

These operations are fundamental.

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Visualize them as:

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Common:
{3, 4}

Only A:
{1, 2}

Only B:
{5, 6}

Everything:
{1, 2, 3, 4, 5, 6}

Only one side:
{1, 2, 5, 6}
```

These four ideas correspond to:

```text
Union
Intersection
Difference
Symmetric Difference
```

---

# 13. Union

## Meaning

The **union** contains every unique element from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B)

print(C)
```

Result:

```text
{1, 2, 3, 4, 5}
```

Think:

```text
A ∪ B
```

---

## Operator form

Instead of:

```python
A.union(B)
```

you can use:

```python
A | B
```

Example:

```python
C = A | B
```

Both represent union.

---

## Union of multiple sets

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
```

You can also use:

```python
myset = set1 | set2 | set3 | set4
```

---

## `union()` with other iterables

The `union()` method can accept other iterable objects.

```python
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
```

This works.

However:

```python
x | y
```

requires set operands and does not provide the same general iterable flexibility as `union()`.

---

# 14. Intersection

## Meaning

The **intersection** contains only the elements common to both sets.

```python
A = {"apple", "banana", "cherry"}
B = {"google", "microsoft", "apple"}

C = A.intersection(B)

print(C)
```

Result:

```text
{'apple'}
```

Mathematically:

```text
A ∩ B
```

---

## Operator form

```python
C = A & B
```

is equivalent to:

```python
C = A.intersection(B)
```

---

## Visual idea

```text
A: {1, 2, 3, 4}
B: {3, 4, 5, 6}

A ∩ B = {3, 4}
```

Think:

> What exists in **both**?

---

# 15. Difference

## Meaning

`difference()` returns elements that are in the **first set but not the second**.

```python
A = {"apple", "banana", "cherry"}
B = {"google", "microsoft", "apple"}

C = A.difference(B)
```

Result:

```text
{'banana', 'cherry'}
```

Mathematically:

```text
A - B
```

---

## Operator form

```python
C = A - B
```

Important:

```python
A - B
```

is not necessarily the same as:

```python
B - A
```

Example:

```python
A = {1, 2, 3}
B = {3, 4, 5}

A - B
```

gives:

```text
{1, 2}
```

while:

```python
B - A
```

gives:

```text
{4, 5}
```

### Easy memory trick

```text
A - B
↓
What is in A but NOT in B?
```

---

# 16. Symmetric Difference

## Meaning

Symmetric difference contains elements that are in **either set, but not both**.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.symmetric_difference(B)
```

Result:

```text
{1, 2, 5, 6}
```

The common values:

```text
3, 4
```

are removed.

---

## Operator form

```python
C = A ^ B
```

Equivalent to:

```python
C = A.symmetric_difference(B)
```

---

## Visual idea

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Only A → {1, 2}
Only B → {5, 6}

Symmetric difference:
{1, 2, 5, 6}
```

### Easy memory trick

```text
Union             → everything
Intersection      → common
Difference        → first only
Symmetric diff.   → only one side
```

---

# 17. Update Operations

A very important distinction in the code is between methods that:

> return a new set

and methods that:

> modify the original set.

The major update methods are:

```text
update()
intersection_update()
difference_update()
symmetric_difference_update()
```

---

# 17.1 `update()`

Adds elements from another iterable to the original set.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
```

Result:

```text
{1, 2, 3, 4, 5}
```

`A` itself is changed.

---

## Operator form

```python
A |= B
```

Equivalent to:

```python
A.update(B)
```

---

# 17.2 `intersection_update()`

Keeps only common elements **inside the original set**.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)
```

Result:

```text
{3, 4}
```

Operator form:

```python
A &= B
```

---

# 17.3 `difference_update()`

Removes elements from the original set that are also present in another set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)
```

Result:

```text
{1, 2}
```

Operator form:

```python
A -= B
```

---

# 17.4 `symmetric_difference_update()`

Updates the original set with the symmetric difference.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.symmetric_difference_update(B)
```

Result:

```text
{1, 2, 5, 6}
```

Operator form:

```python
A ^= B
```

---

# 18. Subset and Superset

These operations answer containment questions.

Suppose:

```python
A = {1, 2}
B = {1, 2, 3}
```

Since every element of `A` exists in `B`:

```text
A is a subset of B
```

And because `B` contains all elements of `A`:

```text
B is a superset of A
```

---

# 18.1 `issubset()`

```python
A.issubset(B)
```

Example:

```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
```

Output:

```text
True
```

Meaning:

> Every element of `A` is present in `B`.

---

## Operator forms

Subset allowing equality:

```python
A <= B
```

Proper subset:

```python
A < B
```

---

## `<=` vs `<`

Suppose:

```python
A = {1, 2}
B = {1, 2}
```

Then:

```python
A <= B
```

is:

```text
True
```

because a set is considered a subset of itself.

But:

```python
A < B
```

is:

```text
False
```

because `A` is not a **proper** subset of `B`; they are equal.

### Remember

```text
<= → subset, equality allowed
<  → proper subset, must be smaller
```

---

# 18.2 `issuperset()`

Checks whether the first set contains every element of the second.

```python
A = {1, 2, 3}
B = {1, 2}

print(A.issuperset(B))
```

Output:

```text
True
```

---

## Operator forms

```python
A >= B
```

means superset, equality allowed.

```python
A > B
```

means proper superset.

### Remember

```text
>= → superset, equality allowed
>  → proper superset, must be larger
```

---

# 19. Disjoint Sets

Two sets are **disjoint** if they have no common elements.

Use:

```python
isdisjoint()
```

Example:

```python
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
```

Output:

```text
True
```

There are no common elements.

But:

```python
C = {3, 4, 5}

print(A.isdisjoint(C))
```

Output:

```text
False
```

because both contain `3`.

### Easy memory trick

```text
isdisjoint() → "Do these two sets have NOTHING in common?"
```

---

# 20. All Important Set Methods

The code demonstrates these important set methods:

```text
add()
clear()
copy()
difference()
difference_update()
discard()
intersection()
intersection_update()
isdisjoint()
issubset()
issuperset()
pop()
remove()
symmetric_difference()
symmetric_difference_update()
union()
update()
```

---

## 20.1 `add()`

Adds one element.

```python
A = {1, 2, 3}

A.add(4)
```

---

## 20.2 `clear()`

Removes everything.

```python
A.clear()
```

Result:

```text
set()
```

---

## 20.3 `copy()`

Creates a shallow copy.

```python
A = {1, 2, 3}

B = A.copy()
```

`B` is a separate set object.

---

## 20.4 `difference()`

Returns elements only in the first set.

```python
A.difference(B)
```

Operator:

```python
A - B
```

---

## 20.5 `difference_update()`

Modifies the original set by removing elements found in another set.

```python
A.difference_update(B)
```

Operator:

```python
A -= B
```

---

## 20.6 `discard()`

Safely removes an element.

```python
A.discard(10)
```

No error if `10` is absent.

---

## 20.7 `intersection()`

Returns common elements.

```python
A.intersection(B)
```

Operator:

```python
A & B
```

---

## 20.8 `intersection_update()`

Keeps only common elements in the original set.

```python
A.intersection_update(B)
```

Operator:

```python
A &= B
```

---

## 20.9 `isdisjoint()`

Checks whether there are no common elements.

```python
A.isdisjoint(B)
```

Returns:

```text
True / False
```

---

## 20.10 `issubset()`

Checks whether all elements of the first set exist in the second.

```python
A.issubset(B)
```

Operators:

```python
A <= B
A < B
```

---

## 20.11 `issuperset()`

Checks whether the first set contains all elements of the second.

```python
A.issuperset(B)
```

Operators:

```python
A >= B
A > B
```

---

## 20.12 `pop()`

Removes and returns an arbitrary element.

```python
x = A.pop()
```

Because sets are unordered, do not assume which element is removed.

---

## 20.13 `remove()`

Removes a specified element.

```python
A.remove(2)
```

Raises `KeyError` if the element is absent.

---

## 20.14 `symmetric_difference()`

Returns elements present in exactly one of the sets.

```python
A.symmetric_difference(B)
```

Operator:

```python
A ^ B
```

---

## 20.15 `symmetric_difference_update()`

Modifies the original set with the symmetric difference.

```python
A.symmetric_difference_update(B)
```

Operator:

```python
A ^= B
```

---

## 20.16 `union()`

Returns all unique elements from the sets.

```python
A.union(B)
```

Operator:

```python
A | B
```

---

## 20.17 `update()`

Adds elements from another iterable to the original set.

```python
A.update(B)
```

Operator:

```python
A |= B
```

---

# 21. Set Operators Cheat Sheet

Python provides convenient operators for mathematical set operations.

| Operation | Method | Operator | Meaning |
|---|---|---|---|
| Union | `union()` | `\|` | All unique elements |
| Intersection | `intersection()` | `&` | Common elements |
| Difference | `difference()` | `-` | Elements only in first |
| Symmetric Difference | `symmetric_difference()` | `^` | Elements in exactly one |
| Union update | `update()` | `\|=` | Add to original |
| Intersection update | `intersection_update()` | `&=` | Keep common in original |
| Difference update | `difference_update()` | `-=` | Remove common from original |
| Symmetric difference update | `symmetric_difference_update()` | `^=` | Replace with symmetric difference |
| Subset | `issubset()` | `<=`, `<` | Containment |
| Superset | `issuperset()` | `>=`, `>` | Reverse containment |

---

# 22. New Set vs Update Methods

This is probably the **most important thing to understand** from the set methods code.

## Normal methods return a new set

```python
C = A.union(B)
```

`A` remains unchanged.

Similarly:

```python
C = A.intersection(B)
C = A.difference(B)
C = A.symmetric_difference(B)
```

These create a result.

---

## Update methods modify the original set

```python
A.update(B)
```

Now `A` changes.

Likewise:

```python
A.intersection_update(B)
A.difference_update(B)
A.symmetric_difference_update(B)
```

modify `A`.

### Visual summary

```text
NORMAL
A.union(B)
      ↓
   NEW SET
      ↓
     C

A remains unchanged
```

versus:

```text
UPDATE
A.update(B)
      ↓
A itself changes
```

---

## Quick comparison

| New-result method | Modifies original |
|---|---|
| `union()` | `update()` |
| `intersection()` | `intersection_update()` |
| `difference()` | `difference_update()` |
| `symmetric_difference()` | `symmetric_difference_update()` |

---

# 23. Frozenset

A **frozenset** is an immutable version of a set.

Example:

```python
x = frozenset({"apple", "banana", "cherry"})

print(x)
print(type(x))
```

Conceptually:

```text
set       → mutable
frozenset → immutable
```

---

## Why use `frozenset`?

Use a frozenset when you need set-like behavior but the collection itself must not be modified.

A frozenset does not support operations such as:

```python
add()
remove()
discard()
pop()
clear()
update()
```

because it is immutable.

---

## Example

```python
fs = frozenset([1, 2, 3])
```

You cannot do:

```python
fs.add(4)  # ❌
```

---

## Frozensets can be useful as immutable set values

Because a frozenset is immutable and hashable, it can be used in situations where a normal mutable set cannot, such as as a dictionary key or as an element of another set.

Example:

```python
A = frozenset([1, 2])

data = {A}

print(data)
```

---

# 24. Frozenset Methods

The code demonstrates these frozenset methods:

```text
copy()
difference()
intersection()
isdisjoint()
issubset()
issuperset()
symmetric_difference()
union()
```

These are operations that do not require modifying the frozenset.

---

## 24.1 `copy()`

```python
A = frozenset([1, 2, 3])

B = A.copy()
```

Returns a frozenset copy.

---

## 24.2 `difference()`

```python
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

A.difference(B)
```

Result:

```text
frozenset({1, 2})
```

Operator:

```python
A - B
```

---

## 24.3 `intersection()`

```python
A.intersection(B)
```

returns common elements.

Operator:

```python
A & B
```

Example:

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ∩ B = {3, 4}
```

---

## 24.4 `isdisjoint()`

```python
A.isdisjoint(B)
```

returns `True` when the sets have no common elements.

---

## 24.5 `issubset()`

```python
A.issubset(B)
```

Operators:

```python
A <= B
A < B
```

---

## 24.6 `issuperset()`

```python
A.issuperset(B)
```

Operators:

```python
A >= B
A > B
```

---

## 24.7 `symmetric_difference()`

```python
A.symmetric_difference(B)
```

Operator:

```python
A ^ B
```

Returns elements that occur in exactly one of the two sets.

---

## 24.8 `union()`

```python
A.union(B)
```

Operator:

```python
A | B
```

Returns all unique elements.

---

## Frozenset method summary

| Method | Operator | Purpose |
|---|---|---|
| `copy()` | — | Copy |
| `difference()` | `-` | First-only elements |
| `intersection()` | `&` | Common elements |
| `isdisjoint()` | — | No common elements |
| `issubset()` | `<=`, `<` | Check subset |
| `issuperset()` | `>=`, `>` | Check superset |
| `symmetric_difference()` | `^` | Only-one-side elements |
| `union()` | `\|` | All unique elements |

---

# 25. Set vs Tuple vs List

This comparison is extremely important.

| Feature | List | Tuple | Set |
|---|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Ordered | ✅ | ✅ | ❌ |
| Indexed | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicates | ✅ | ✅ | ❌ |
| Slicing | ✅ | ✅ | ❌ |
| Fast membership | Usually O(n) | Usually O(n) | Average O(1) |
| Mathematical operations | ❌ | ❌ | ✅ |
| `append()` | ✅ | ❌ | ❌ |
| `add()` | ❌ | ❌ | ✅ |
| `count()` | ✅ | ✅ | ❌ |
| `index()` | ✅ | ✅ | ❌ |

### Easy memory model

```text
LIST
→ ordered
→ mutable
→ duplicates allowed

TUPLE
→ ordered
→ immutable
→ duplicates allowed

SET
→ unordered
→ mutable
→ unique elements only
```

---

# 26. Time Complexity Cheat Sheet

For a Python set, average-case complexity is generally:

| Operation | Average Complexity |
|---|---:|
| `x in s` | **O(1)** |
| `add(x)` | **O(1)** |
| `remove(x)` | **O(1)** |
| `discard(x)` | **O(1)** |
| `pop()` | **O(1)** average |
| `len(s)` | **O(1)** |
| `clear()` | **O(n)** |
| `copy()` | **O(n)** |
| `union()` | **O(n + m)** |
| `intersection()` | **O(min(n, m))** average |
| `difference()` | **O(n)** average |
| `symmetric_difference()` | **O(n + m)** |
| `issubset()` | **O(n)** average |
| `issuperset()` | **O(m)** average |
| `isdisjoint()` | **O(min(n, m))** average |

Here:

```text
n = size of first set
m = size of second set
```

### Why is membership usually O(1)?

Python sets are hash-table based.

Conceptually:

```text
value
  ↓
hash()
  ↓
location
  ↓
check
```

This makes:

```python
x in my_set
```

very fast on average.

---

# 27. Common Mistakes

## Mistake 1 — Using `{}` for an empty set

Wrong:

```python
x = {}
```

This creates a dictionary.

Correct:

```python
x = set()
```

---

## Mistake 2 — Trying to index a set

Wrong:

```python
myset[0]
```

Sets are not indexed.

Use:

```python
for x in myset:
    print(x)
```

---

## Mistake 3 — Assuming set order

Do not rely on:

```python
print(myset)
```

to display elements in a meaningful sequence.

Sets are unordered collections.

---

## Mistake 4 — Thinking `pop()` removes the last element

For a list:

```python
list.pop()
```

removes the last item.

For a set:

```python
set.pop()
```

removes an arbitrary element.

---

## Mistake 5 — Confusing `remove()` and `discard()`

```python
remove(x)
```

raises `KeyError` if `x` is missing.

```python
discard(x)
```

does not.

---

## Mistake 6 — Confusing `add()` and `update()`

```python
A.add([1, 2])      # ❌ list is unhashable
```

But:

```python
A.update([1, 2])
```

adds the two elements.

If you want to add the list itself as one element, that is not possible because lists are mutable and unhashable.

---

## Mistake 7 — Confusing difference direction

```python
A - B
```

means:

> elements in A that are not in B.

It does not mean all elements that are different between the two sets.

For that, use:

```python
A ^ B
```

---

## Mistake 8 — Confusing intersection and union

```text
A | B → everything unique
A & B → common only
```

---

## Mistake 9 — Forgetting update methods mutate

```python
A.intersection_update(B)
```

changes `A`.

Whereas:

```python
C = A.intersection(B)
```

creates a result and leaves `A` unchanged.

---

# 28. Revision Checklist

Before moving to the next topic, make sure you can explain and implement:

- [ ] What is a set?
- [ ] Why are duplicate values removed?
- [ ] Why are sets unordered?
- [ ] Why can't sets be indexed?
- [ ] How do you create a set?
- [ ] How do you create an empty set?
- [ ] What does `set()` do?
- [ ] How does `len()` work with sets?
- [ ] What happens with `True` and `1`?
- [ ] What happens with `False` and `0`?
- [ ] How do you loop through a set?
- [ ] How do you check membership?
- [ ] How does `add()` work?
- [ ] How does `update()` work?
- [ ] What is the difference between `add()` and `update()`?
- [ ] How does `remove()` work?
- [ ] How does `discard()` work?
- [ ] What is the difference between `remove()` and `discard()`?
- [ ] What does set `pop()` do?
- [ ] What does `clear()` do?
- [ ] What does `del` do?
- [ ] What is union?
- [ ] What is intersection?
- [ ] What is difference?
- [ ] What is symmetric difference?
- [ ] What are the operator shortcuts for these operations?
- [ ] What is the difference between `difference()` and `difference_update()`?
- [ ] What is the difference between `intersection()` and `intersection_update()`?
- [ ] What is the difference between `union()` and `update()`?
- [ ] What is a subset?
- [ ] What is a proper subset?
- [ ] What is a superset?
- [ ] What is a proper superset?
- [ ] What does `isdisjoint()` mean?
- [ ] What is a frozenset?
- [ ] Why is a frozenset immutable?
- [ ] Which methods are available on frozenset?
- [ ] When should you use a set instead of a list or tuple?
- [ ] What is the average complexity of set membership?

---

# 29. Ultra-Quick Revision

```python
# Create
A = {1, 2, 3}

# Empty set
A = set()

# Length
len(A)

# Membership
2 in A
5 not in A

# Loop
for x in A:
    print(x)

# Add one
A.add(4)

# Add many
A.update([5, 6])

# Remove
A.remove(2)

# Safe remove
A.discard(10)

# Remove arbitrary element
x = A.pop()

# Empty
A.clear()

# Copy
B = A.copy()

# Union
C = A.union(B)
C = A | B

# Intersection
C = A.intersection(B)
C = A & B

# Difference
C = A.difference(B)
C = A - B

# Symmetric difference
C = A.symmetric_difference(B)
C = A ^ B

# Update operations
A.update(B)
A.intersection_update(B)
A.difference_update(B)
A.symmetric_difference_update(B)

# Operators
A |= B
A &= B
A -= B
A ^= B

# Subset
A.issubset(B)
A <= B
A < B

# Superset
A.issuperset(B)
A >= B
A > B

# Disjoint
A.isdisjoint(B)

# Frozenset
F = frozenset([1, 2, 3])
```

---

# 🧠 The Most Important Set Concepts

## 1. Set = Unique Collection

```text
{1, 2, 2, 3, 3}
        ↓
   {1, 2, 3}
```

---

## 2. Set has no indexing

```python
A[0]  # ❌
```

Use:

```python
for x in A:
    print(x)
```

---

## 3. Membership is fast

```python
x in A
```

Average:

```text
O(1)
```

---

## 4. Four core mathematical operations

```text
UNION
A | B
→ everything unique

INTERSECTION
A & B
→ common elements

DIFFERENCE
A - B
→ only A

SYMMETRIC DIFFERENCE
A ^ B
→ only one side
```

---

## 5. The update versions modify the original

```text
union()                    → new set
update()                   → modify original

intersection()             → new set
intersection_update()     → modify original

difference()               → new set
difference_update()       → modify original

symmetric_difference()     → new set
symmetric_difference_update() → modify original
```

---

## 6. `remove()` vs `discard()`

```text
remove()  → KeyError if absent
discard() → no error if absent
```

---

## 7. `set` vs `frozenset`

```text
set
→ mutable
→ can add/remove/update

frozenset
→ immutable
→ cannot add/remove/update
```

---

# 🎯 Final Takeaway

Python sets are designed primarily for **uniqueness, membership testing, and mathematical set operations**.

The complete mental model is:

```text
SET
 │
 ├── Unique elements
 ├── Unordered
 ├── Unindexed
 ├── Mutable
 │
 ├── Add
 │    ├── add()
 │    └── update()
 │
 ├── Remove
 │    ├── remove()
 │    ├── discard()
 │    ├── pop()
 │    ├── clear()
 │    └── del
 │
 ├── Mathematical operations
 │    ├── union()
 │    ├── intersection()
 │    ├── difference()
 │    └── symmetric_difference()
 │
 ├── Update operations
 │    ├── update()
 │    ├── intersection_update()
 │    ├── difference_update()
 │    └── symmetric_difference_update()
 │
 ├── Relationship checks
 │    ├── issubset()
 │    ├── issuperset()
 │    └── isdisjoint()
 │
 └── Immutable version
      └── frozenset
```

If you remember only one section before an exam or coding session, remember:

```text
A | B  → UNION              → everything
A & B  → INTERSECTION       → common
A - B  → DIFFERENCE         → A only
A ^ B  → SYMMETRIC DIFF.    → only one side

A <= B → subset
A >= B → superset

remove(x)  → error if missing
discard(x) → safe if missing

set      → mutable
frozenset → immutable
```

These concepts form the complete foundation for using Python sets in **problem solving, competitive programming, data processing, algorithms, and real-world Python applications**.
