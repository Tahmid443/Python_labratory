# ============================================================
#                  PYTHON EXCEPTIONS
# ============================================================


# 1. ArithmeticError
try:
    result = 10 / 0
except ArithmeticError:
    print("1. ArithmeticError")


# 2. AssertionError
try:
    age = 15
    assert age >= 18
except AssertionError:
    print("2. AssertionError")


# 3. AttributeError
try:
    text = "Hello"
    text.append(" World")
except AttributeError:
    print("3. AttributeError")


# 4. Exception
try:
    x = 10 / 0
except Exception:
    print("4. Exception")


# 5. EOFError
try:
    name = input("Enter your name: ")
except EOFError:
    print("5. EOFError")


# 6. FloatingPointError
try:
    raise FloatingPointError("Floating point error")
except FloatingPointError:
    print("6. FloatingPointError")


# 7. GeneratorExit
def my_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("7. GeneratorExit")


g = my_generator()
next(g)
g.close()


# 8. ImportError
try:
    from math import something_that_does_not_exist
except ImportError:
    print("8. ImportError")


# 9. IndentationError
# IndentationError is a SyntaxError subclass and is difficult
# to demonstrate inside a running try/except block.
#
# Example:
#
# if True:
# print("Hello")


# 10. IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("10. IndexError")


# 11. KeyError
student = {"name": "Tahmid", "age": 20}

try:
    print(student["address"])
except KeyError:
    print("11. KeyError")


# 12. KeyboardInterrupt
# Press Ctrl+C to trigger this exception.
#
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("12. KeyboardInterrupt")


# 13. LookupError
try:
    numbers = [10, 20, 30]
    print(numbers[10])
except LookupError:
    print("13. LookupError")


# 14. MemoryError
try:
    raise MemoryError("Not enough memory")
except MemoryError:
    print("14. MemoryError")


# 15. NameError
try:
    print(username)
except NameError:
    print("15. NameError")


# 16. NotImplementedError
class Animal:
    def sound(self):
        raise NotImplementedError("sound() must be implemented")


try:
    animal = Animal()
    animal.sound()
except NotImplementedError:
    print("16. NotImplementedError")


# 17. OSError
try:
    with open("unknown_file.txt", "r") as f:
        print(f.read())
except OSError:
    print("17. OSError")


# 18. OverflowError
import math

try:
    math.exp(1000)
except OverflowError:
    print("18. OverflowError")


# 19. ReferenceError
# ReferenceError normally occurs when using weak references.
#
# Example:
#
# import weakref
#
# class Student:
#     pass
#
# student = Student()
# reference = weakref.ref(student)
#
# del student
#
# if reference() is None:
#     print("19. ReferenceError - object no longer exists")


# 20. RuntimeError
try:
    raise RuntimeError("Something went wrong")
except RuntimeError:
    print("20. RuntimeError")


# 21. StopIteration
numbers = iter([10, 20])

try:
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
except StopIteration:
    print("21. StopIteration")


# 22. SyntaxError
# SyntaxError happens before the program starts running.
#
# Example:
#
# if True
#     print("Hello")


# 23. TabError
# TabError occurs when tabs and spaces are mixed incorrectly.
#
# Example:
#
# if True:
#     print("Hello")
#       print("World")


# 24. SystemError
try:
    raise SystemError("Internal system error")
except SystemError:
    print("24. SystemError")


# 25. SystemExit
import sys

try:
    sys.exit()
except SystemExit:
    print("25. SystemExit")


# 26. TypeError
try:
    result = "10" + 5
except TypeError:
    print("26. TypeError")


# 27. UnboundLocalError
x = 10


def test():
    try:
        print(x)
        x = 20
    except UnboundLocalError:
        print("27. UnboundLocalError")


test()


# 28. UnicodeError
try:
    raise UnicodeError("Unicode problem")
except UnicodeError:
    print("28. UnicodeError")


# 29. UnicodeEncodeError
try:
    text = "বাংলা"
    text.encode("ascii")
except UnicodeEncodeError:
    print("29. UnicodeEncodeError")


# 30. UnicodeDecodeError
try:
    data = b"\xff"
    data.decode("utf-8")
except UnicodeDecodeError:
    print("30. UnicodeDecodeError")


# 31. UnicodeTranslateError
try:
    raise UnicodeTranslateError("translation", "text", 0, 1, "translation failed")
except UnicodeTranslateError:
    print("31. UnicodeTranslateError")


# 32. ValueError
try:
    number = int("hello")
except ValueError:
    print("32. ValueError")


# 33. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("33. ZeroDivisionError")
