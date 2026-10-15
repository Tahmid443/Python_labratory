class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(25)
print(t.celsius, t.fahrenheit)

t.fahrenheit = 100
print(t.celsius)

t.celsius = -300  # ValueError

# Computed property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        import math
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.area, c.circumference)

# Cached property
from functools import cached_property

class Data:
    def __init__(self, nums):
        self.nums = nums

    @cached_property
    def total(self):
        print("Computing...")
        return sum(self.nums)

d = Data([1, 2, 3])
print(d.total)   # computes
print(d.total)   # cached