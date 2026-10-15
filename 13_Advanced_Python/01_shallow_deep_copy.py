import copy

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0].append(99)
print("Original:", original)   # inner list shared!
print("Shallow: ", shallow)

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(99)
print("Original:", original)
print("Deep:    ", deep)

# Assignment vs copy
a = [1, 2, 3]
b = a             # same object
c = a.copy()      # shallow
d = list(a)       # shallow
e = a[:]          # shallow
f = copy.deepcopy(a)

# Compare
b.append(4)
print(a, b, c)

# For immutable elements, shallow == deep
nums = [1, 2, 3]
shallow = copy.copy(nums)
deep = copy.deepcopy(nums)
shallow[0] = 99
print(nums, shallow, deep)

# Custom __copy__ / __deepcopy__
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []
    def __repr__(self):
        return f"Node({self.val}, {self.children})"

n = Node(1, [Node(2), Node(3)])
n_copy = copy.deepcopy(n)
n.children[0].val = 99
print(n)
print(n_copy)