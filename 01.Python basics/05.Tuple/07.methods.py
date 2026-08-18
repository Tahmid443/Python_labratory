"""
COMPREHENSIVE PYTHON TUPLE METHODS DEMONSTRATION
All 2 tuple methods with examples and explanations
"""

print("=" * 80)
print("PYTHON TUPLE METHODS - COMPLETE REFERENCE")
print("=" * 80)

# Create sample tuples for demonstration
fruits = ("apple", "banana", "cherry", "date", "apple", "elderberry")
numbers = (10, 20, 30, 40, 50, 20, 30, 20)
mixed_tuple = (1, "hello", 3.14, True, "hello", 42)
nested_tuple = (1, 2, (3, 4), 5, (3, 4))

print("\n📋 SAMPLE TUPLES CREATED:")
print(f"Fruits tuple: {fruits}")
print(f"Numbers tuple: {numbers}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Nested tuple: {nested_tuple}")
print("\n" + "=" * 80)

# 1. count() - Returns the number of times a specified value occurs in a tuple
print("\n1. count()")
print("-" * 50)

# Basic usage with fruits tuple
print(f"Tuple: {fruits}")
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Count of 'banana': {fruits.count('banana')}")
print(f"Count of 'grape': {fruits.count('grape')}")  # Returns 0 if not found

# With numbers tuple
print(f"\nNumbers tuple: {numbers}")
print(f"Count of 20: {numbers.count(20)}")
print(f"Count of 30: {numbers.count(30)}")
print(f"Count of 99: {numbers.count(99)}")

# With mixed data types
print(f"\nMixed tuple: {mixed_tuple}")
print(f"Count of 'hello': {mixed_tuple.count('hello')}")
print(f"Count of 1: {mixed_tuple.count(1)}")
print(f"Count of True: {mixed_tuple.count(True)}")  # True equals 1 in Python

# With nested tuples
print(f"\nNested tuple: {nested_tuple}")
print(f"Count of (3, 4): {nested_tuple.count((3, 4))}")
print(f"Count of 2: {nested_tuple.count(2)}")

# Practical example - Counting votes
print("\n📊 Practical Example - Vote Counting:")
votes = ("A", "B", "A", "C", "A", "B", "A", "D", "C", "A")
print(f"Votes: {votes}")
print(f"Votes for A: {votes.count('A')}")
print(f"Votes for B: {votes.count('B')}")
print(f"Votes for C: {votes.count('C')}")
print(f"Votes for D: {votes.count('D')}")
total_votes = len(votes)
print(f"Total votes: {total_votes}")

print("\n→ Returns the number of occurrences of a value in tuple")
print("→ Returns 0 if value is not found")
print("→ Works with any data type (strings, numbers, tuples, etc.)")
print("→ Case-sensitive: 'apple' and 'Apple' are different")

# Important note about count with True/False
print("\n⚠️ Important: True counts as 1, False counts as 0")
bool_tuple = (True, 1, False, 0, True, 1)
print(f"Tuple: {bool_tuple}")
print(f"Count of True: {bool_tuple.count(True)}")  # Counts True and 1
print(f"Count of 1: {bool_tuple.count(1)}")  # Counts 1 and True
print(f"Count of False: {bool_tuple.count(False)}")  # Counts False and 0
print(f"Count of 0: {bool_tuple.count(0)}")  # Counts 0 and False

# 2. index() - Searches the tuple for a specified value and returns the position
print("\n2. index()")
print("-" * 50)

# Basic usage with fruits tuple
print(f"Tuple: {fruits}")
print(f"Index of 'cherry': {fruits.index('cherry')}")
print(f"Index of 'date': {fruits.index('date')}")
print(f"Index of 'apple' (first occurrence): {fruits.index('apple')}")

# With numbers tuple and start/end parameters
print(f"\nNumbers tuple: {numbers}")
print(f"Index of 20 (first occurrence): {numbers.index(20)}")
print(f"Index of 20 from position 3: {numbers.index(20, 3)}")
print(f"Index of 20 between positions 3-6: {numbers.index(20, 3, 6)}")
print(f"Index of 50: {numbers.index(50)}")

# With mixed data types
print(f"\nMixed tuple: {mixed_tuple}")
print(f"Index of 'hello': {mixed_tuple.index('hello')}")
print(f"Index of 3.14: {mixed_tuple.index(3.14)}")
print(f"Index of True: {mixed_tuple.index(True)}")

# With nested tuple
print(f"\nNested tuple: {nested_tuple}")
print(f"Index of (3, 4): {nested_tuple.index((3, 4))}")

# Error handling - value not found
print("\n⚠️ Error Handling - Value Not Found:")
try:
    print(fruits.index("mango"))
except ValueError as e:
    print(f"❌ Error: {e}")
    print("→ index() raises ValueError when value not found")

# Practical examples
print("\n📊 Practical Examples:")

# Example 1: Finding position in a list of students
students = ("Alice", "Bob", "Charlie", "David", "Emma")
print(f"Students: {students}")
student_name = "Charlie"
position = students.index(student_name)
print(f"'{student_name}' is at position {position}")

# Example 2: Using start parameter to find second occurrence
colors = ("red", "blue", "green", "red", "yellow", "red")
print(f"\nColors: {colors}")
first_red = colors.index("red")
second_red = colors.index("red", first_red + 1)
third_red = colors.index("red", second_red + 1)
print(f"First 'red' at: {first_red}")
print(f"Second 'red' at: {second_red}")
print(f"Third 'red' at: {third_red}")

# Example 3: Finding position of maximum value
print(f"\nNumbers: {numbers}")
max_value = max(numbers)
max_index = numbers.index(max_value)
print(f"Maximum value {max_value} found at index {max_index}")

# Example 4: Finding all positions of a value
print(f"\n🔍 Finding all positions of a value:")


def find_all_positions(tuple_data, value):
    positions = []
    start = 0
    while True:
        try:
            pos = tuple_data.index(value, start)
            positions.append(pos)
            start = pos + 1
        except ValueError:
            break
    return positions


test_tuple = (5, 2, 8, 2, 9, 2, 1, 2)
print(f"Tuple: {test_tuple}")
print(f"All positions of 2: {find_all_positions(test_tuple, 2)}")
print(f"All positions of 5: {find_all_positions(test_tuple, 5)}")
print(f"All positions of 10: {find_all_positions(test_tuple, 10)}")

print("\n→ Returns the index of the first occurrence of a value")
print("→ Raises ValueError if value is not found")
print("→ Can specify start and end search range with parameters")
print("→ Syntax: tuple.index(value, start, end)")
print("→ Works with any data type (strings, numbers, tuples, etc.)")

# Comparison between count() and index()
print("\n" + "=" * 80)
print("📝 COMPARISON: count() vs index()")
print("-" * 50)
sample = (1, 2, 3, 2, 4, 2, 5)
print(f"Sample tuple: {sample}")
print(f"count(2): {sample.count(2)} - Tells HOW MANY times 2 appears")
print(f"index(2): {sample.index(2)} - Tells WHERE the first 2 is located")
print("→ count() for quantity, index() for position")
print("→ Both work on tuples (immutable)")

print("\n" + "=" * 80)
print("📚 QUICK REFERENCE SUMMARY")
print("-" * 50)
print("count(value) → Returns number of occurrences of value")
print("index(value) → Returns position of first occurrence of value")
print("=" * 80)

# Bonus: Tuple vs List methods comparison
print("\n💡 IMPORTANT: Tuple vs List")
print("-" * 50)
print("✅ Tuple has only 2 methods: count() and index()")
print(
    "✅ List has 11 methods (append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort)"
)
print("✅ Tuples are IMMUTABLE - cannot be modified after creation")
print("✅ Lists are MUTABLE - can be modified after creation")
print("✅ Use tuples for data that shouldn't change (coordinates, database records)")
print("✅ Use lists for data that will change (dynamic collections)")

# Convert tuple to list for modification
print("\n🔄 Converting tuple to list if you need more methods:")
tuple_data = (1, 2, 3, 4, 5)
list_data = list(tuple_data)
list_data.append(6)
list_data.remove(3)
tuple_data = tuple(list_data)
print(f"Original tuple converted to list, modified, and back to tuple: {tuple_data}")
print("=" * 80)
