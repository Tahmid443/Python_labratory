class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        """Instance method - needs self"""
        return self.celsius * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, f):
        """Class method - needs cls, alternative constructor"""
        return cls((f - 32) * 5/9)

    @staticmethod
    def is_freezing(celsius):
        """Static method - no self, no cls"""
        return celsius <= 0

t = Temperature(25)
print(t.to_fahrenheit())

t2 = Temperature.from_fahrenheit(77)
print(t2.celsius)

print(Temperature.is_freezing(0))
print(Temperature.is_freezing(10))

# Summary
class Demo:
    class_var = "class"

    def __init__(self):
        self.instance_var = "instance"

    def instance_method(self):
        return f"instance: {self.instance_var}, class: {Demo.class_var}"

    @classmethod
    def class_method(cls):
        return f"class: {cls.class_var}"

    @staticmethod
    def static_method():
        return "static: no access to self/cls"

d = Demo()
print(d.instance_method())
print(Demo.class_method())
print(Demo.static_method())