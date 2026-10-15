# Return single value
def square(x):
    return x * x

# Return None implicitly
def log(msg):
    print(f"[LOG] {msg}")

result = log("test")
print(result)  # None

# Return multiple (tuple)
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([1, 2, 3, 4, 5])
print(lo, hi, avg)

# Early return
def is_even(n):
    if n % 2 != 0:
        return False
    return True

# Return vs print
def add_print(a, b):
    print(a + b)     # prints, returns None

def add_return(a, b):
    return a + b     # returns value

x = add_print(1, 2)  # prints 3, x = None
y = add_return(1, 2)  # y = 3
print(x, y)

# Return None explicitly
def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None