"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

"""
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# The values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# Print the data type of a dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))

# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
