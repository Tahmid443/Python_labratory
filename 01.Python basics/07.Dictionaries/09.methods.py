# ============================================================
#                 PYTHON DICTIONARY METHODS
# ============================================================

# A dictionary stores data in KEY : VALUE pairs.

student = {"name": "Tahmid", "age": 21, "department": "CSE", "cgpa": 3.75}


# ------------------------------------------------------------
# 1. clear()
# ------------------------------------------------------------
# Removes all elements from the dictionary.

data = {"name": "Tahmid", "age": 21}
data.clear()

print(data)
# Output: {}


# ------------------------------------------------------------
# 2. copy()
# ------------------------------------------------------------
# Returns a copy of the dictionary.

student = {"name": "Tahmid", "age": 21}

new_student = student.copy()

print(new_student)
# Output: {'name': 'Tahmid', 'age': 21}


# ------------------------------------------------------------
# 3. fromkeys()
# ------------------------------------------------------------
# Creates a new dictionary using specified keys
# and a common value.

keys = ("name", "age", "department")

student = dict.fromkeys(keys, "Unknown")

print(student)
# Output:
# {'name': 'Unknown', 'age': 'Unknown', 'department': 'Unknown'}

# Without specifying a value:
data = dict.fromkeys(["a", "b", "c"])

print(data)
# Output: {'a': None, 'b': None, 'c': None}


# ------------------------------------------------------------
# 4. get()
# ------------------------------------------------------------
# Returns the value associated with a specified key.

student = {"name": "Tahmid", "age": 21}

print(student.get("name"))
# Output: Tahmid

print(student.get("age"))
# Output: 21

# If the key does not exist, get() returns None.
print(student.get("email"))
# Output: None

# We can also provide a default value.
print(student.get("email", "Not Found"))
# Output: Not Found


# ------------------------------------------------------------
# 5. items()
# ------------------------------------------------------------
# Returns all key-value pairs as dictionary view objects.
# Each pair behaves like a tuple.

student = {"name": "Tahmid", "age": 21}

print(student.items())
# Output:
# dict_items([('name', 'Tahmid'), ('age', 21)])

# Using a loop:
for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Tahmid
# age : 21


# ------------------------------------------------------------
# 6. keys()
# ------------------------------------------------------------
# Returns all keys of the dictionary.

student = {"name": "Tahmid", "age": 21, "department": "CSE"}

print(student.keys())
# Output:
# dict_keys(['name', 'age', 'department'])

# Using a loop:
for key in student.keys():
    print(key)


# ------------------------------------------------------------
# 7. pop()
# ------------------------------------------------------------
# Removes the element with the specified key
# and returns its value.

student = {"name": "Tahmid", "age": 21, "department": "CSE"}

removed_value = student.pop("age")

print(removed_value)
# Output: 21

print(student)
# Output:
# {'name': 'Tahmid', 'department': 'CSE'}

# If the key does not exist, it causes a KeyError.
# student.pop("email")

# We can provide a default value:
print(student.pop("email", "Not Found"))
# Output: Not Found


# ------------------------------------------------------------
# 8. popitem()
# ------------------------------------------------------------
# Removes and returns the LAST inserted key-value pair.

student = {"name": "Tahmid", "age": 21, "department": "CSE"}

removed_item = student.popitem()

print(removed_item)
# Output: ('department', 'CSE')

print(student)
# Output:
# {'name': 'Tahmid', 'age': 21}


# ------------------------------------------------------------
# 9. setdefault()
# ------------------------------------------------------------
# Returns the value of the specified key.
#
# If the key does not exist, it inserts the key
# with the specified default value.

student = {"name": "Tahmid", "age": 21}

print(student.setdefault("name", "Unknown"))
# Output: Tahmid

print(student)
# No change because "name" already exists.


# Key does not exist:
print(student.setdefault("department", "CSE"))
# Output: CSE

print(student)
# Output:
# {'name': 'Tahmid', 'age': 21, 'department': 'CSE'}


# ------------------------------------------------------------
# 10. update()
# ------------------------------------------------------------
# Updates the dictionary with new key-value pairs.

student = {"name": "Tahmid", "age": 21}

student.update({"department": "CSE", "cgpa": 3.75})

print(student)
# Output:
# {
#   'name': 'Tahmid',
#   'age': 21,
#   'department': 'CSE',
#   'cgpa': 3.75
# }

# update() can also modify an existing key:
student.update({"age": 22})

print(student["age"])
# Output: 22


# ------------------------------------------------------------
# 11. values()
# ------------------------------------------------------------
# Returns all values of the dictionary.

student = {"name": "Tahmid", "age": 21, "department": "CSE"}

print(student.values())
# Output:
# dict_values(['Tahmid', 21, 'CSE'])

# Using a loop:
for value in student.values():
    print(value)


# ============================================================
#                   QUICK REVISION
# ============================================================

"""
clear()       -> Removes all elements
copy()        -> Returns a copy of the dictionary
fromkeys()    -> Creates dictionary from specified keys
get()         -> Returns value of a specified key
items()       -> Returns key-value pairs
keys()        -> Returns all keys
pop()         -> Removes specified key
popitem()     -> Removes last inserted key-value pair
setdefault()  -> Returns value; inserts key if it doesn't exist
update()      -> Updates/adds key-value pairs
values()      -> Returns all values
"""


# ============================================================
#              MOST IMPORTANT DIFFERENCES
# ============================================================

"""
get() vs []

student["age"]
    -> Raises KeyError if key doesn't exist.

student.get("age")
    -> Returns None if key doesn't exist.


pop() vs popitem()

student.pop("age")
    -> Removes a specific key.

student.popitem()
    -> Removes the last inserted key-value pair.


copy() vs assignment

a = student.copy()
    -> Creates a separate dictionary.

a = student
    -> Both variables refer to the same dictionary.


items() vs keys() vs values()

items() -> key + value
keys()  -> only keys
values()-> only values
"""
