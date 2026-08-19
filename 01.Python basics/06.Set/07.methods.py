# ============================================================
# PYTHON SET METHODS
# ============================================================
# A set is an unordered, mutable collection of unique elements.
#
# Example:
# my_set = {1, 2, 3}
#
# Sets:
# - Do not allow duplicate elements
# - Are mutable
# - Do not support indexing
# ============================================================


# ------------------------------------------------------------
# 1. add()
# ------------------------------------------------------------
# Adds an element to the set.

A = {1, 2, 3}

A.add(4)

print(A)
# Output: {1, 2, 3, 4}


# ------------------------------------------------------------
# 2. clear()
# ------------------------------------------------------------
# Removes all elements from the set.

A = {1, 2, 3}

A.clear()

print(A)
# Output: set()


# ------------------------------------------------------------
# 3. copy()
# ------------------------------------------------------------
# Returns a shallow copy of the set.

A = {1, 2, 3}

B = A.copy()

print(B)
# Output: {1, 2, 3}


# ------------------------------------------------------------
# 4. difference()  /  -
# ------------------------------------------------------------
# Returns elements that are present in the first set
# but not in the second set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))
# Output: {1, 2}

print(A - B)
# Output: {1, 2}


# ------------------------------------------------------------
# 5. difference_update()  /  -=
# ------------------------------------------------------------
# Removes elements from the original set that are also
# present in another set.
#
# IMPORTANT:
# This method modifies the original set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)

print(A)
# Output: {1, 2}


# Operator version

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A -= B

print(A)
# Output: {1, 2}


# ------------------------------------------------------------
# 6. discard()
# ------------------------------------------------------------
# Removes a specified element from the set.
#
# If the element does not exist, discard() does NOT
# raise an error.

A = {1, 2, 3}

A.discard(2)

print(A)
# Output: {1, 3}

A.discard(10)  # No error


# ------------------------------------------------------------
# 7. intersection()  /  &
# ------------------------------------------------------------
# Returns elements that are common to both sets.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))
# Output: {3, 4}

print(A & B)
# Output: {3, 4}


# ------------------------------------------------------------
# 8. intersection_update()  /  &=
# ------------------------------------------------------------
# Keeps only the elements that are common to the sets.
#
# IMPORTANT:
# This modifies the original set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)
# Output: {3, 4}


# Operator version

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A &= B

print(A)
# Output: {3, 4}


# ------------------------------------------------------------
# 9. isdisjoint()
# ------------------------------------------------------------
# Returns True if two sets have NO elements in common.
# Otherwise, returns False.

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
# Output: True

C = {3, 4, 5}

print(A.isdisjoint(C))
# Output: False


# ------------------------------------------------------------
# 10. issubset()  /  <=  /  <
# ------------------------------------------------------------
# Checks whether all elements of one set are contained
# in another set.
#
# <=  : subset, equality is allowed
# <   : proper subset, must be smaller

A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
# Output: True

print(A <= B)
# Output: True

print(A < B)
# Output: True


# Equal sets

A = {1, 2}
B = {1, 2}

print(A <= B)
# Output: True

print(A < B)
# Output: False


# ------------------------------------------------------------
# 11. issuperset()  /  >=  /  >
# ------------------------------------------------------------
# Checks whether a set contains all elements of another set.
#
# >=  : superset, equality is allowed
# >   : proper superset, must be larger

A = {1, 2, 3}
B = {1, 2}

print(A.issuperset(B))
# Output: True

print(A >= B)
# Output: True

print(A > B)
# Output: True


# ------------------------------------------------------------
# 12. pop()
# ------------------------------------------------------------
# Removes and returns an arbitrary element from the set.
#
# IMPORTANT:
# Sets are unordered, so you cannot predict which element
# will be removed.

A = {10, 20, 30, 40}

x = A.pop()

print(x)
print(A)

# The removed element can be different depending on
# the set's internal arrangement.


# ------------------------------------------------------------
# 13. remove()
# ------------------------------------------------------------
# Removes a specified element from the set.
#
# IMPORTANT:
# If the element does not exist, remove() raises KeyError.

A = {1, 2, 3}

A.remove(2)

print(A)
# Output: {1, 3}

# A.remove(10)
# KeyError: 10


# ------------------------------------------------------------
# 14. symmetric_difference()  /  ^
# ------------------------------------------------------------
# Returns elements that are present in either set,
# but NOT in both sets.
#
# Example:
#
# A = {1, 2, 3}
# B = {3, 4, 5}
#
# Result = {1, 2, 4, 5}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))
# Output: {1, 2, 5, 6}

print(A ^ B)
# Output: {1, 2, 5, 6}


# ------------------------------------------------------------
# 15. symmetric_difference_update()  /  ^=
# ------------------------------------------------------------
# Updates the original set with the symmetric difference.
#
# IMPORTANT:
# This modifies the original set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.symmetric_difference_update(B)

print(A)
# Output: {1, 2, 5, 6}


# Operator version

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ^= B

print(A)
# Output: {1, 2, 5, 6}


# ------------------------------------------------------------
# 16. union()  /  |
# ------------------------------------------------------------
# Returns a new set containing all unique elements
# from both sets.

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
# Output: {1, 2, 3, 4, 5}

print(A | B)
# Output: {1, 2, 3, 4, 5}


# ------------------------------------------------------------
# 17. update()  /  |=
# ------------------------------------------------------------
# Adds all elements from another set (or other iterables)
# to the original set.
#
# IMPORTANT:
# This modifies the original set.

A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
# Output: {1, 2, 3, 4, 5}


# Operator version

A = {1, 2, 3}
B = {3, 4, 5}

A |= B

print(A)
# Output: {1, 2, 3, 4, 5}


# ============================================================
# QUICK SUMMARY
# ============================================================
#
# Method                         Operator       Purpose
#
# add()                          —              Add an element
# clear()                        —              Remove all elements
# copy()                         —              Create a copy
# difference()                   -              Elements only in first set
# difference_update()            -=             Remove common elements
# discard()                      —              Remove element safely
# intersection()                &              Common elements
# intersection_update()         &=             Keep only common elements
# isdisjoint()                  —              Check for NO common elements
# issubset()                    <= / <         Check subset
# issuperset()                  >= / >         Check superset
# pop()                          —              Remove arbitrary element
# remove()                      —              Remove specified element
# symmetric_difference()        ^              Elements in either, not both
# symmetric_difference_update() ^=             Update with symmetric difference
# union()                       |              Combine unique elements
# update()                      |=             Add elements to original set
#
# ============================================================


# ============================================================
# IMPORTANT DIFFERENCE: remove() vs discard()
# ============================================================

A = {1, 2, 3}

A.remove(2)  # Removes 2
# A.remove(10)    # Raises KeyError

A.discard(10)  # No error even though 10 doesn't exist


# ============================================================
# IMPORTANT DIFFERENCE: NORMAL vs UPDATE METHODS
# ============================================================
#
# Normal methods:
# difference()
# intersection()
# symmetric_difference()
# union()
#
# These return a NEW set and don't modify the original set.
#
#
# Update methods:
# difference_update()
# intersection_update()
# symmetric_difference_update()
# update()
#
# These MODIFY the original set.
#
# ============================================================
