# Numeric
integer = 42
floating = 3.14
complex_num = 2 + 3j

# Text
text = "Hello"

# Boolean
flag = True

# None
nothing = None

# Collections
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

# Check types
print(type(integer))       # <class 'int'>
print(type(floating))      # <class 'float'>
print(type(text))          # <class 'str'>
print(type(flag))          # <class 'bool'>
print(type(my_list))       # <class 'list'>
print(type(my_dict))       # <class 'dict'>

# isinstance check
print(isinstance(integer, int))     # True
print(isinstance(floating, int))    # False

# Integer precision (unlimited in Python)
big = 10 ** 100
print(f"Big number: {big}")