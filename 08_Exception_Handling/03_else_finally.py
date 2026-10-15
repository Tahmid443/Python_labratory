def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        # Runs only if no exception
        print("Division successful")
        return result
    finally:
        # Always runs
        print("Cleanup complete")

print(divide(10, 2))
print("---")
print(divide(10, 0))

# Resource cleanup
def read_file(path):
    f = None
    try:
        f = open(path)
        return f.read()
    except FileNotFoundError:
        return ""
    finally:
        if f:
            f.close()

# finally with return (tricky!)
def tricky():
    try:
        return 1
    finally:
        print("finally runs before return")
        # return 2  # this would override!

print(tricky())