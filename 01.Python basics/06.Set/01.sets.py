"""
************Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate member************
"""
thisset = {"apple", "banana", "cherry"}  # can have duplicates but other will ignored
print(thisset)
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#it will ignore 1

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Get the number of items in a set:
thisset = {"apple", "banana", "cherry", "apple"}
print(len(thisset))#number of unique items in the set

# set constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
