# any - True if any element is truthy
print(any([False, True, False]))
print(any([0, 0, 1]))
print(any([]))   # False

# all - True if all elements are truthy
print(all([True, True, True]))
print(all([1, 2, 3]))
print(all([]))   # True (vacuous)

# Common usage
nums = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in nums))   # all even?
print(any(x > 10 for x in nums))       # any > 10?

# Validation
def is_valid_user(user):
    return all([
        user.get("name"),
        user.get("age", 0) >= 18,
        user.get("email", "").count("@") == 1,
    ])

u = {"name": "Alice", "age": 30, "email": "a@b.com"}
print(is_valid_user(u))

# Find first match
def first_even(nums):
    return next((x for x in nums if x % 2 == 0), None)

print(first_even([1, 3, 5, 4, 7]))
print(first_even([1, 3, 5]))

# Short-circuit
def check(n):
    print(f"Checking {n}")
    return n > 0

any(check(x) for x in [0, 1, 2])   # stops at 1
all(check(x) for x in [1, 2, 0])   # stops at 0