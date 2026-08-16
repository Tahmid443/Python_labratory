# -----------------------if else elif-------------------------#
a = 33
b = 21
if a>b:
    print(f"'{a} is greater")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater")

# another way
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)


# default
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.
age = 20

if age < 18:
    pass  
else:
    print("Access granted")


# -----------------------match-------------------------#
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
