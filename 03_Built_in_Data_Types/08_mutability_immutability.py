# Immutable: int, float, str, tuple, frozenset, bool, None
# Mutable: list, dict, set, bytearray

# Immutable example
s = "hello"
s2 = s
s += " world"
print(s, s2)   # s2 unchanged

# Mutable example
lst = [1, 2, 3]
lst2 = lst       # same object!
lst.append(4)
print(lst, lst2)  # both changed

# Proper copy
lst3 = lst.copy()
lst.append(5)
print(lst, lst3)

# Nested mutable issue (shallow copy)
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)
original[0].append(99)
print("Original:", original)
print("Shallow: ", shallow)   # inner list shared!
print("Deep:    ", deep)

# Identity vs equality
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (value)
print(a is b)   # False (different objects)

# Tuples containing mutable
t = ([1, 2], [3, 4])
t[0].append(99)     # allowed (inner list mutable)
print(t)
# t[0] = [9, 9]     # TypeError