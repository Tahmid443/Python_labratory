# Creating
nums = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4]]
empty = []
from_range = list(range(5))

# Access
print(nums[0], nums[-1])
print(nums[1:3])

# Modify
nums[0] = 100
print(nums)

# Add
nums.append(6)
nums.insert(0, 0)
nums.extend([7, 8])
print(nums)

# Remove
nums.remove(100)
popped = nums.pop()
del nums[0]
nums.clear()

# Operations
a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 2)
print(len(a))
print(3 in a)
print(max(a), min(a), sum(a))

# Sort
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print(sorted([3, 1, 4]))

# Reverse
nums.reverse()
print(nums)

# Copy
original = [1, 2, 3]
shallow = original.copy()