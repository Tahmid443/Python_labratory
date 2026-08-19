x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# ============================================================
# PYTHON FROZENSET METHODS
# ============================================================
# A frozenset is an immutable version of a set.
# Once created, its elements cannot be changed.
#
# Example:
# fs = frozenset([1, 2, 3])
# ============================================================


# ------------------------------------------------------------
# 1. copy()
# ------------------------------------------------------------
# Returns a shallow copy of the frozenset.

A = frozenset([1, 2, 3])

B = A.copy()

print(B)
# Output: frozenset({1, 2, 3})


# ------------------------------------------------------------
# 2. difference()  /  -
# ------------------------------------------------------------
# Returns a new frozenset containing elements that are
# present in the first frozenset but not in the second.

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.difference(B))
# Output: frozenset({1, 2})

print(A - B)
# Output: frozenset({1, 2})


# ------------------------------------------------------------
# 3. intersection()  /  &
# ------------------------------------------------------------
# Returns a new frozenset containing elements common
# to both frozensets.

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.intersection(B))
# Output: frozenset({3, 4})

print(A & B)
# Output: frozenset({3, 4})


# ------------------------------------------------------------
# 4. isdisjoint()
# ------------------------------------------------------------
# Returns True if two frozensets have NO elements in common.
# Returns False if they have at least one common element.

A = frozenset([1, 2, 3])
B = frozenset([4, 5, 6])

print(A.isdisjoint(B))
# Output: True

C = frozenset([3, 4, 5])

print(A.isdisjoint(C))
# Output: False


# ------------------------------------------------------------
# 5. issubset()  /  <=  /  <
# ------------------------------------------------------------
# Checks whether all elements of one frozenset are
# contained in another frozenset.
#
# <=  means subset (can be equal)
# <   means proper subset (must be smaller)

A = frozenset([1, 2])
B = frozenset([1, 2, 3])

print(A.issubset(B))
# Output: True

print(A <= B)
# Output: True

print(A < B)
# Output: True


# ------------------------------------------------------------
# 6. issuperset()  /  >=  /  >
# ------------------------------------------------------------
# Checks whether a frozenset contains all elements
# of another frozenset.
#
# >=  means superset (can be equal)
# >   means proper superset (must be larger)

A = frozenset([1, 2, 3])
B = frozenset([1, 2])

print(A.issuperset(B))
# Output: True

print(A >= B)
# Output: True

print(A > B)
# Output: True


# ------------------------------------------------------------
# 7. symmetric_difference()  /  ^
# ------------------------------------------------------------
# Returns elements that are present in either frozenset,
# but NOT present in both.
#
# In other words:
# A ^ B = (A - B) UNION (B - A)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.symmetric_difference(B))
# Output: frozenset({1, 2, 5, 6})

print(A ^ B)
# Output: frozenset({1, 2, 5, 6})


# ------------------------------------------------------------
# 8. union()  /  |
# ------------------------------------------------------------
# Returns a new frozenset containing all unique elements
# from both frozensets.

A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A.union(B))
# Output: frozenset({1, 2, 3, 4, 5})

print(A | B)
# Output: frozenset({1, 2, 3, 4, 5})


# ============================================================
# QUICK SUMMARY
# ============================================================
#
# Method                    Operator       Purpose
#
# copy()                    —              Shallow copy
# difference()              -              Elements only in first set
# intersection()            &              Common elements
# isdisjoint()              —              No common elements
# issubset()                <= / <         Check subset
# issuperset()              >= / >         Check superset
# symmetric_difference()    ^              Elements in either, not both
# union()                   |              All unique elements
#
# ============================================================
