# NumPy Notes — From Fundamentals to ML

> **Purpose:** A structured revision guide for the NumPy code in this folder, with explanations, examples, important concepts, common mistakes, and Machine Learning relevance.

---

## 📌 What is NumPy?

**NumPy** stands for **Numerical Python**. It is one of the most important Python libraries for numerical computing and is a foundation for:

- Machine Learning
- Data Science
- Scientific Computing
- Statistics
- Linear Algebra
- Deep Learning

The central object in NumPy is the **`ndarray` (N-dimensional array)**.

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)
```

Output:

```text
[1 2 3 4 5]
```

---

# 📚 Contents

1. [NumPy Array Basics](#1-numpy-array-basics)
2. [Array Creation](#2-array-creation)
3. [Shape and Dimensions](#3-shape-and-dimensions)
4. [Indexing and Slicing](#4-indexing-and-slicing)
5. [Universal Functions (ufuncs)](#5-universal-functions-ufuncs)
6. [Copy vs View](#6-copy-vs-view)
7. [Reshaping Arrays](#7-reshaping-arrays)
8. [Iterating Through Arrays](#8-iterating-through-arrays)
9. [Sorting Arrays](#9-sorting-arrays)
10. [Searching with `np.where()`](#10-searching-with-npwhere)
11. [Filtering Arrays](#11-filtering-arrays)
12. [Important NumPy Concepts for ML](#12-important-numpy-concepts-for-machine-learning)
13. [Common Mistakes](#13-common-mistakes)
14. [Practice Tasks](#14-practice-tasks)
15. [Next Topics to Learn](#15-next-topics-to-learn)

---

# 1. NumPy Array Basics

## Python List vs NumPy Array

Python list:

```python
my_list = [1, 2, 3, 4, 5]
```

NumPy array:

```python
np1 = np.array([1, 2, 3, 4, 5])
```

NumPy arrays are designed for efficient numerical operations.

### Why NumPy?

With a NumPy array, mathematical operations can be performed element-by-element without writing explicit Python loops.

```python
x = np.array([1, 2, 3])
print(x * 2)
```

Output:

```text
[2 4 6]
```

This idea is called **vectorization** and is extremely important in Machine Learning.

---

# 2. Array Creation

## 2.1 `np.array()`

Creates a NumPy array from a Python sequence.

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
```

You can also create multidimensional arrays:

```python
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

---

## 2.2 `np.arange()`

Creates values within a range.

```python
np.arange(10)
```

Output:

```text
[0 1 2 3 4 5 6 7 8 9]
```

Syntax:

```python
np.arange(start, stop, step)
```

Example:

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

### Important

The `stop` value is **not included**.

---

## 2.3 `np.zeros()`

Creates an array filled with zeros.

```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

2D:

```python
np.zeros((2, 5))
```

Output:

```text
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
```

Notice:

```python
np.zeros((rows, columns))
```

---

## 2.4 `np.full()`

Creates an array filled with a specified value.

```python
np.full(5, 6)
```

Output:

```text
[6 6 6 6 6]
```

2D:

```python
np.full((2, 5), 6)
```

---

## 2.5 Converting a List to NumPy

```python
my_list = [1, 2, 3, 4, 5]

x = np.array(my_list)
```

Now `x` is a NumPy `ndarray`.

---

# 3. Shape and Dimensions

Understanding **shape** is one of the most important NumPy skills for Machine Learning.

## 3.1 `shape`

```python
x = np.array([1, 2, 3, 4, 5])

print(x.shape)
```

Output:

```text
(5,)
```

This is a **1-dimensional array containing 5 elements**.

---

## 3.2 2D Shape

```python
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x.shape)
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

## 3.3 Shape in Machine Learning

Suppose:

```python
X.shape
```

returns:

```text
(1000, 20)
```

Usually this means:

```text
1000 → samples
20   → features
```

This interpretation is extremely important when working with ML datasets.

---

## 3.4 `ndim`

`ndim` tells you how many dimensions an array has.

```python
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x.ndim)
```

Output:

```text
2
```

---

# 4. Indexing and Slicing

File: `02.slice.py`

Suppose:

```python
x = np.array([1,2,3,4,5,6,7,8,9])
```

## 4.1 Single Element

```python
x[0]
```

Output:

```text
1
```

Python/NumPy uses **zero-based indexing**.

```text
index:  0 1 2 3 4
value:  1 2 3 4 5
```

---

## 4.2 Basic Slicing

```python
x[1:5]
```

Output:

```text
[2 3 4 5]
```

General syntax:

```python
array[start:stop]
```

`stop` is excluded.

---

## 4.3 From an Index to the End

```python
x[3:]
```

Output:

```text
[4 5 6 7 8 9]
```

---

## 4.4 Negative Slicing

```python
x[-3:-1]
```

Output:

```text
[7 8]
```

Negative indexes count from the end.

---

## 4.5 Step

```python
x[1:5:2]
```

Output:

```text
[2 4]
```

Syntax:

```python
[start:stop:step]
```

---

## 4.6 Every Second Element

```python
x[::2]
```

Output:

```text
[1 3 5 7 9]
```

---

## 4.7 2D Indexing

Given:

```python
x = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
```

Get row 2, column 3:

```python
x[1,2]
```

Output:

```text
8
```

Remember:

```python
array[row, column]
```

---

## 4.8 2D Slicing

```python
x[0:2, 1:3]
```

Meaning:

```text
rows    → 0 through 1
columns → 1 through 2
```

---

# 5. Universal Functions (ufuncs)

File: `03.universal.py`

A **ufunc** is a NumPy function that operates efficiently on array elements.

Example:

```python
x = np.array([1, 4, 9])

print(np.sqrt(x))
```

Output:

```text
[1. 2. 3.]
```

Instead of manually looping:

```python
result = []

for value in x:
    result.append(np.sqrt(value))
```

NumPy performs the operation in a vectorized way.

---

## 5.1 Important Mathematical Functions

### Square Root

```python
np.sqrt(x)
```

### Absolute Value

```python
np.absolute(x)
```

or:

```python
np.abs(x)
```

### Exponential

```python
np.exp(x)
```

Computes:

```text
e^x
```

### Minimum / Maximum

```python
np.min(x)
np.max(x)
```

### Sign

```python
np.sign(x)
```

Returns:

```text
-1 → negative
 0 → zero
+1 → positive
```

### Logarithm

```python
np.log(x)
```

Natural logarithm.

Also learn:

```python
np.log2(x)
np.log10(x)
```

### Trigonometric

```python
np.sin(x)
np.cos(x)
np.tan(x)
```

---

# 5.2 Important ufunc Categories

Your code contains a reference list of many NumPy operations. For ML, prioritize these groups.

## Arithmetic

```python
np.add()
np.subtract()
np.multiply()
np.divide()
np.power()
np.mod()
```

## Power / Root

```python
np.sqrt()
np.cbrt()
np.square()
np.reciprocal()
```

## Exponential / Log

```python
np.exp()
np.log()
np.log2()
np.log10()
np.expm1()
np.log1p()
```

## Rounding

```python
np.round()
np.floor()
np.ceil()
np.trunc()
```

## Comparison

```python
np.greater()
np.less()
np.equal()
np.not_equal()
```

## Logical Operations

```python
np.logical_and()
np.logical_or()
np.logical_not()
```

## Missing / Infinite Values

```python
np.isnan()
np.isinf()
np.isfinite()
```

## Maximum / Minimum

```python
np.maximum()
np.minimum()
np.clip()
```

---

## ⚠️ Important Note About the ufunc List

Not every item in the large reference section of `03.universal.py` is technically a NumPy **ufunc**.

For example, some functions belong to:

- `numpy.linalg`
- `numpy.char`
- datetime functionality
- helper functions

So use that list as a **NumPy numerical-function reference**, not as a strict list of only ufunc objects.

For ML, you do **not** need to memorize every function.

---

# 6. Copy vs View

File: `04.copyview.py`

This is an important NumPy concept because it affects memory and data modification.

---

## 6.1 View

```python
x = np.array([0,1,2,3,4,5])

y = x.view()
```

A view shares the same underlying data.

If:

```python
x[0] = 41
```

then `y` can also reflect that change.

Conceptually:

```text
x ─────┐
       ↓
   same data
       ↑
y ─────┘
```

---

## 6.2 Copy

```python
x = np.array([0,1,2,3,4,5])

y = x.copy()
```

Now `y` has its own independent data.

```python
x[0] = 41
```

does not change `y`.

Conceptually:

```text
x → [0 1 2 3 4 5]

y → [0 1 2 3 4 5]
```

Different memory.

---

## Copy vs View

| Feature | View | Copy |
|---|---|---|
| Shares underlying data | Yes | No |
| Independent data | No | Yes |
| Changes can affect original | Yes | No |
| Memory efficient | Usually | Uses more memory |

### ML relevance

This becomes important when:

- working with large datasets
- manipulating training data
- optimizing memory
- avoiding accidental modifications

---

# 7. Reshaping Arrays

File: `05.shape.py`

Reshaping changes the structure of an array without changing the values.

Suppose:

```python
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
```

Shape:

```text
(12,)
```

---

## 7.1 Reshape to 2D

```python
x.reshape(3,4)
```

Result:

```text
[
 [ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
]
```

Shape:

```text
(3,4)
```

---

## 7.2 Reshape to 3D

```python
x.reshape(2,3,2)
```

Shape:

```text
(2,3,2)
```

Total number of elements must remain the same:

```text
2 × 3 × 2 = 12
```

---

## 7.3 Flattening

You can turn a multidimensional array into 1D.

```python
x.reshape(-1)
```

The `-1` tells NumPy to calculate that dimension automatically.

---

## ⚠️ Correction in `05.shape.py`

The original code contains:

```python
np3 = np.reshape(3,4)
```

This is incorrect because `np.reshape()` requires an array to reshape.

The intended code is:

```python
np3 = np1.reshape(3,4)
```

or:

```python
np3 = np.reshape(np1, (3,4))
```

This is an important distinction.

---

# 8. Iterating Through Arrays

File: `06.iterating.py`

## 8.1 1D Array

```python
x = np.array([1,2,3,4,5])

for value in x:
    print(value)
```

---

## 8.2 2D Array

```python
x = np.array([
    [1,2,3],
    [4,5,6]
])

for row in x:
    print(row)
```

Each iteration returns a row.

To access individual values:

```python
for row in x:
    for value in row:
        print(value)
```

---

## 8.3 3D Array

A 3D array contains nested arrays.

Example:

```python
x = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
```

Manual nested loops can become cumbersome.

---

## 8.4 `np.nditer()`

NumPy provides:

```python
for value in np.nditer(x):
    print(value)
```

This iterates over every element regardless of dimensionality.

### Important ML Note

In real ML code, you should generally prefer **vectorized NumPy operations** over manually iterating through arrays whenever possible.

---

# 9. Sorting Arrays

File: `07.sorting.py`

## 9.1 Numeric Sorting

```python
x = np.array([6,7,4,9,0,2])

print(np.sort(x))
```

Output:

```text
[0 2 4 6 7 9]
```

---

## 9.2 String Sorting

```python
x = np.array(["Tahmid", "Dhrubo", "Taqi"])

print(np.sort(x))
```

Strings are sorted alphabetically/lexicographically.

---

## 9.3 Boolean Sorting

```python
x = np.array([True, False, False, True])

print(np.sort(x))
```

---

## 9.4 Important: `np.sort()` Returns a New Array

```python
x = np.array([6,7,4,9])

y = np.sort(x)
```

`x` remains unchanged.

This is called a **non-mutating operation** in this context.

---

## 9.5 Sorting 2D Arrays

```python
x = np.array([
    [6,7,1,9],
    [8,3,5,2]
])

np.sort(x)
```

By default, sorting occurs along the last axis, so each row is sorted.

---

# 10. Searching with `np.where()`

File: `08.searching.py`

`np.where()` is extremely useful.

Example:

```python
x = np.array([1,2,3,4,5,6,7,8,9,10,3])

result = np.where(x == 3)
```

It returns the indexes where the condition is true.

Conceptually:

```text
value:  1 2 3 4 5 6 7 8 9 10 3
index:  0 1 2 3 4 5 6 7 8  9 10

3 occurs at index 2 and 10
```

---

## Get the indexes

```python
result[0]
```

---

## Get the actual values

```python
x[result[0]]
```

---

## Find Even Values

```python
x % 2 == 0
```

Then:

```python
np.where(x % 2 == 0)
```

---

## Find Odd Values

```python
np.where(x % 2 == 1)
```

---

# 11. Filtering Arrays

File: `09.filter.py`

NumPy allows filtering using a **Boolean mask**.

```python
x = np.array([1,2,3,4,5,6,7,8,9,10])

filtered = x % 2 == 0

print(filtered)
```

This produces a Boolean array:

```text
[False  True False  True False  True False  True False  True]
```

Then:

```python
print(x[filtered])
```

Output:

```text
[2 4 6 8 10]
```

---

## Shortcut

You can write it directly:

```python
x[x % 2 == 0]
```

This is called **Boolean indexing / Boolean masking**.

---

# 12. Important NumPy Concepts for Machine Learning

The current code covers the fundamentals. For ML, the next concepts you should master are:

## 🔥 Tier 1 — Must Master

```text
ndarray
shape
ndim
indexing
slicing
reshape
axis
Boolean masking
np.where()
vectorization
broadcasting
```

## 🔥 Tier 2 — Essential for ML Mathematics

```text
np.mean()
np.std()
np.var()
np.sum()
np.min()
np.max()
np.dot()
@
transpose
np.linalg
random numbers
```

## 🔥 Tier 3 — Advanced ML

```text
matrix multiplication
norms
eigenvalues
eigenvectors
SVD
solve()
einsum()
numerical stability
views/copies
float32 vs float64
memory layout
```

---

# 13. Common Mistakes

## Mistake 1 — Confusing `*` and `@`

```python
A * B
```

means element-wise multiplication.

```python
A @ B
```

means matrix multiplication.

For ML, understanding this difference is critical.

---

## Mistake 2 — Ignoring Shape

Before performing an operation, check:

```python
print(X.shape)
```

A large percentage of NumPy/ML errors are shape-related.

---

## Mistake 3 — Forgetting that slicing excludes the stop

```python
x[1:5]
```

returns indexes:

```text
1, 2, 3, 4
```

not 5.

---

## Mistake 4 — Incorrect reshape

This is invalid:

```python
x.reshape(3,4)
```

if the array does not contain exactly:

```text
3 × 4 = 12
```

elements.

---

## Mistake 5 — Using Python `and` / `or`

Do not write:

```python
x[(x > 2) and (x < 8)]
```

Use:

```python
x[(x > 2) & (x < 8)]
```

For NumPy Boolean arrays:

```text
& → AND
| → OR
~ → NOT
```

---

## Mistake 6 — Accidentally modifying shared data

Be careful with views:

```python
y = x.view()
```

If you need independent data:

```python
y = x.copy()
```

---

# 14. Practice Tasks

After completing these files, solve these without looking at the answer.

## Beginner

### Task 1
Create:

```text
[10,20,30,40,50]
```

using NumPy.

### Task 2
Create an array from 0 to 100 with a step of 5.

### Task 3
Create a 3×4 array containing zeros.

### Task 4
Create a 4×4 array containing 7.

---

## Indexing / Slicing

### Task 5
Given:

```python
x = np.arange(1, 21)
```

Get:

- first 5 values
- last 5 values
- every second value
- values from index 5 to 14

---

## Reshaping

### Task 6

Create:

```text
1 → 12
```

and reshape it into:

```text
3 × 4
```

Then reshape it into:

```text
2 × 2 × 3
```

---

## Filtering

### Task 7

Given:

```python
x = np.arange(1, 101)
```

find:

- even numbers
- odd numbers
- numbers greater than 50
- numbers divisible by 3
- numbers between 30 and 70

---

## Mathematical Operations

### Task 8

Given:

```python
x = np.array([-4,-2,0,2,4])
```

calculate:

- absolute values
- squares
- square roots
- sign
- exponential

---

## ML-Oriented Challenge

### Task 9 — Standardization

Given:

```python
x = np.array([10,20,30,40,50])
```

calculate:

```text
mean
standard deviation
standardized values
```

using:

\[
z = \frac{x-\mu}{\sigma}
\]

---

### Task 10 — Feature Matrix

Create:

```python
X = np.array([
    [20, 50000],
    [25, 60000],
    [30, 75000],
    [35, 90000]
])
```

Interpret:

```text
rows    → samples
columns → features
```

Find:

- number of samples
- number of features
- mean of each feature
- standard deviation of each feature

This is the beginning of real ML data manipulation.

---

# 15. Next Topics to Learn

Your current code gives you a solid **NumPy fundamentals foundation**, but it does not yet cover everything required for advanced ML.

Follow this sequence:

```text
                    NUMPY
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
    Core Arrays              Mathematics
          │                       │
          ↓                       ↓
 Indexing / Slicing        Linear Algebra
          │                       │
          ↓                       ↓
 Reshape / Axis             Statistics
          │                       │
          ↓                       ↓
 Broadcasting              Probability
          │                       │
          └───────────┬───────────┘
                      ↓
               Vectorization
                      ↓
             ML From Scratch
                      ↓
             Scikit-learn
                      ↓
              Deep Learning
                      ↓
             PyTorch / TensorFlow
```

### Recommended next NumPy topics

After these 9 files, learn:

1. `dtype`
2. `axis`
3. `sum`, `mean`, `std`, `var`
4. Boolean indexing
5. Broadcasting
6. `np.random`
7. `np.concatenate`
8. `np.stack`
9. `np.vstack` / `np.hstack`
10. `np.unique`
11. `np.argsort`
12. `np.clip`
13. `np.isnan`
14. `np.isinf`
15. `np.linalg`
16. Matrix multiplication
17. Vectorization
18. Views vs copies
19. `einsum`
20. Numerical stability

---

# 🎯 NumPy → Advanced ML Checklist

Use this as your progress tracker.

## Fundamentals

- [ ] What is NumPy?
- [ ] `ndarray`
- [ ] `np.array()`
- [ ] `np.arange()`
- [ ] `np.zeros()`
- [ ] `np.ones()`
- [ ] `np.full()`
- [ ] `shape`
- [ ] `ndim`
- [ ] `size`
- [ ] `dtype`

## Indexing

- [ ] Basic indexing
- [ ] Slicing
- [ ] Negative indexing
- [ ] Step slicing
- [ ] 2D indexing
- [ ] Boolean indexing
- [ ] `np.where()`

## Array Manipulation

- [ ] `reshape()`
- [ ] `flatten()`
- [ ] `ravel()`
- [ ] transpose
- [ ] `concatenate()`
- [ ] `stack()`
- [ ] `vstack()`
- [ ] `hstack()`

## Numerical Computing

- [ ] ufuncs
- [ ] vectorization
- [ ] broadcasting
- [ ] aggregation
- [ ] random numbers
- [ ] statistics
- [ ] NaN handling
- [ ] infinity handling

## Advanced

- [ ] copy vs view
- [ ] memory sharing
- [ ] strides
- [ ] `np.linalg`
- [ ] matrix multiplication
- [ ] eigenvalues/eigenvectors
- [ ] SVD
- [ ] `einsum`
- [ ] numerical stability
- [ ] floating-point precision

## ML Application

- [ ] Standardization
- [ ] Min-Max scaling
- [ ] Linear Regression from scratch
- [ ] Gradient Descent from scratch
- [ ] Logistic Regression from scratch
- [ ] KNN from scratch
- [ ] K-Means from scratch
- [ ] PCA from scratch

---

# 🧠 Final Goal

Do not try to memorize every NumPy function.

The real goal is to become comfortable with:

```text
ARRAY
  ↓
SHAPE
  ↓
INDEXING
  ↓
RESHAPING
  ↓
BROADCASTING
  ↓
VECTORIZATION
  ↓
MATRIX OPERATIONS
  ↓
LINEAR ALGEBRA
  ↓
MACHINE LEARNING
```

If you can look at an ML equation and translate it into efficient NumPy code, you have reached the level of NumPy that actually matters for Machine Learning.

---

## 📂 Files in This Folder

| File | Main Topic |
|---|---|
| `01.intro.py` | NumPy introduction and array creation |
| `02.slice.py` | Indexing and slicing |
| `03.universal.py` | Universal functions and numerical operations |
| `04.copyview.py` | Copy vs View |
| `05.shape.py` | Shape and reshaping |
| `06.iterating.py` | Array iteration |
| `07.sorting.py` | Sorting |
| `08.searching.py` | Searching with `np.where()` |
| `09.filter.py` | Boolean filtering |

---

**Author:** Taqi Tahmid  
**Focus:** Python → NumPy → Machine Learning → Advanced ML
