"""
Practice Exercises
"""

# 1. Circle area
def circle_area(radius):
    import math
    return math.pi * radius ** 2

# 2. Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# 3. Swap without temp
def swap(a, b):
    return b, a

# 4. Sum of digits
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 5. Reverse a number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

# 6. Check even/odd
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 7. Find max of 3
def max_of_three(a, b, c):
    return max(a, b, c)

# 8. BMI calculator
def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    print(f"Circle area (r=5): {circle_area(5):.2f}")
    print(f"25°C = {c_to_f(25)}°F")
    print(f"Swap 1,2: {swap(1, 2)}")
    print(f"Sum digits 12345: {sum_digits(12345)}")
    print(f"Reverse 12345: {reverse_number(12345)}")
    print(f"7 is {even_or_odd(7)}")
    print(f"Max of 1,5,3: {max_of_three(1, 5, 3)}")
    print(f"BMI (70kg, 1.75m): {bmi(70, 1.75):.2f}")