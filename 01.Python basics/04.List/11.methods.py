"""
COMPREHENSIVE PYTHON LIST METHODS DEMONSTRATION
All 11 list methods with examples and explanations
"""

print("=" * 80)
print("PYTHON LIST METHODS - COMPLETE REFERENCE")
print("=" * 80)

# Create a sample list for demonstration
fruits = ["apple", "banana", "cherry", "date"]
numbers = [5, 2, 8, 1, 9, 3]
mixed_list = [1, "hello", 3.14, True]

print("\n📋 SAMPLE LISTS CREATED:")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed_list}")
print("\n" + "=" * 80)

# 1. append() - Adds an element at the end of the list
print("\n1. append()")
print("-" * 50)
print(f"Original list: {fruits}")
fruits.append("elderberry")
print(f"After append('elderberry'): {fruits}")
print("→ Adds a single element to the end of the list")
print("→ Modifies the original list in place")
print("→ Can append any data type (string, number, list, etc.)")

# Reset fruits for next examples
fruits = ["apple", "banana", "cherry", "date"]

# 2. clear() - Removes all the elements from the list
print("\n2. clear()")
print("-" * 50)
temp_list = ["a", "b", "c", "d"]
print(f"Original list: {temp_list}")
temp_list.clear()
print(f"After clear(): {temp_list}")
print("→ Removes all elements from the list")
print("→ List becomes empty but still exists")
print("→ Useful for resetting a list")

# 3. copy() - Returns a copy of the list
print("\n3. copy()")
print("-" * 50)
print(f"Original list: {fruits}")
fruits_copy = fruits.copy()
print(f"Copy of list: {fruits_copy}")
print(f"Are they the same object? {fruits is fruits_copy}")
print("→ Creates a shallow copy of the list")
print("→ New list has same elements but different memory location")
print("→ Use when you need to modify a list without changing original")

# 4. count() - Returns the number of elements with the specified value
print("\n4. count()")
print("-" * 50)
fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "date"]
print(f"List: {fruits_with_duplicates}")
apple_count = fruits_with_duplicates.count("apple")
print(f"Count of 'apple': {apple_count}")
print(f"Count of 'banana': {fruits_with_duplicates.count('banana')}")
print("→ Returns the number of occurrences of a value")
print("→ Returns 0 if value not found")
print("→ Works with any data type")

# 5. extend() - Add elements of an iterable to the end of current list
print("\n5. extend()")
print("-" * 50)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
list1.extend(list2)
print(f"After extend(list2): {list1}")
print("→ Adds multiple elements from an iterable")
print("→ Modifies original list (doesn't create new one)")
print("→ Can extend with any iterable (list, tuple, string, etc.)")

# Example with string
letters = ["a", "b"]
letters.extend("cd")
print(f"Extending with string 'cd': {letters}")
print("→ String 'cd' is treated as iterable, adding 'c' and 'd'")

# 6. index() - Returns the index of the first element with the specified value
print("\n6. index()")
print("-" * 50)
print(f"List: {fruits}")
print(f"Index of 'cherry': {fruits.index('cherry')}")
print(f"Index of 'banana': {fruits.index('banana')}")
print("→ Returns the first occurrence index of a value")
print("→ Raises ValueError if value not found")
print("→ Can specify start and end search range")

# With start/end parameters
numbers = [10, 20, 30, 20, 40, 20, 50]
print(f"\nNumbers: {numbers}")
print(f"Index of 20 (from position 3): {numbers.index(20, 3)}")
print(f"Index of 20 (between 2-5): {numbers.index(20, 2, 5)}")

# 7. insert() - Adds an element at the specified position
print("\n7. insert()")
print("-" * 50)
colors = ["red", "green", "blue"]
print(f"Original list: {colors}")
colors.insert(1, "yellow")
print(f"After insert(1, 'yellow'): {colors}")
colors.insert(0, "purple")
print(f"After insert(0, 'purple'): {colors}")
colors.insert(len(colors), "orange")
print(f"After insert(len, 'orange'): {colors}")
print("→ Inserts element at specific index")
print("→ Elements after index shift right")
print("→ Index can be negative (counts from end)")

# 8. pop() - Removes the element at the specified position
print("\n8. pop()")
print("-" * 50)
animals = ["cat", "dog", "bird", "fish", "hamster"]
print(f"Original list: {animals}")
removed = animals.pop(2)
print(f"After pop(2): {animals}")
print(f"Removed element: '{removed}'")
removed_last = animals.pop()
print(f"After pop() (last element): {animals}")
print(f"Removed last element: '{removed_last}'")
print("→ Removes and returns element at specified index")
print("→ If no index, removes and returns last element")
print("→ Raises IndexError if list is empty")

# 9. remove() - Removes the item with the specified value
print("\n9. remove()")
print("-" * 50)
vegetables = ["carrot", "broccoli", "spinach", "carrot", "peas"]
print(f"Original list: {vegetables}")
vegetables.remove("carrot")
print(f"After remove('carrot'): {vegetables}")
print("→ Removes the first occurrence of the specified value")
print("→ Raises ValueError if value not found")
print("→ Only removes first occurrence, not all")

# Trying to remove non-existent value
try:
    vegetables.remove("mushroom")
except ValueError as e:
    print(f"❌ Error: {e}")
    print("→ Always check if value exists before removing")

# 10. reverse() - Reverses the order of the list
print("\n10. reverse()")
print("-" * 50)
letters = ["a", "b", "c", "d", "e"]
print(f"Original list: {letters}")
letters.reverse()
print(f"After reverse(): {letters}")
print("→ Reverses the list in place (modifies original)")
print("→ Does not create a new list")
print("→ Use reversed() if you need a new reversed copy")

# Demonstration of reversed() vs reverse()
original = [1, 2, 3, 4]
reversed_copy = list(reversed(original))
print(f"\nOriginal: {original}")
print(f"reversed(original): {reversed_copy}")
print(f"Original unchanged: {original}")

# 11. sort() - Sorts the list
print("\n11. sort()")
print("-" * 50)
numbers = [5, 2, 8, 1, 9, 3]
print(f"Original list: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

# Sorting descending
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sorting strings
words = ["banana", "apple", "date", "cherry"]
print(f"\nWords: {words}")
words.sort()
print(f"After sort(): {words}")
words.sort(key=len)
print(f"After sort(key=len): {words}")
print("→ Sorts list in ascending order by default")
print("→ Modifies original list (in-place sort)")
print("→ Parameters: reverse=True for descending, key for custom sorting")

# Sorting with key parameter
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20), ("David", 35)]
print(f"\nPeople list: {people}")
people.sort(key=lambda x: x[1])  # Sort by age
print(f"Sorted by age: {people}")
people.sort(key=lambda x: x[0])  # Sort by name
print(f"Sorted by name: {people}")

print("\n" + "=" * 80)
print("END OF LIST METHODS DEMONSTRATION")
print("=" * 80)

# BONUS: Quick Reference Summary
print("\n📚 QUICK REFERENCE SUMMARY")
print("-" * 50)
print("append()  → Add element at end")
print("clear()   → Remove all elements")
print("copy()    → Create a copy")
print("count()   → Count occurrences")
print("extend()  → Add multiple elements")
print("index()   → Find position of element")
print("insert()  → Insert at specific position")
print("pop()     → Remove and return element")
print("remove()  → Remove first occurrence")
print("reverse() → Reverse order")
print("sort()    → Sort elements")
print("=" * 80)
