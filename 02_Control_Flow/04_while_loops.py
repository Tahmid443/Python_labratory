# Basic while
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# While with break
n = 1
while True:
    if n > 5:
        break
    print(n, end=" ")
    n += 1
print()

# Factorial
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Fibonacci
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

# Collatz
def collatz(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

if __name__ == "__main__":
    print(factorial(5))
    print(fib(10))
    print(collatz(27))