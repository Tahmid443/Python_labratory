# import sys
# sys.setrecursionlimit(10000)


def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter your number: "))
try:
    print(f"factorial of {n} is ",factorial(n))
except RecursionError:
    print("Please try positive integer!!!")



"""
def factorial(n):
    #check if n is greater or equal than zero and n is a positive number
    assert n>=0 and int(n) == n, "The number must be positive integer only"
    
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter your number: "))
print(f"factorial of {n} is ", factorial(n))
"""

