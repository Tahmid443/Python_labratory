"""
Control Flow Practice
"""

def fizzbuzz(n):
    """Classic FizzBuzz"""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:4}", end="")
        print()

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    print("FizzBuzz 1-15:")
    fizzbuzz(15)
    print(f"\nPrimes under 30: {print_primes(30)}")
    print("\nMultiplication table 5x5:")
    multiplication_table(5)
    print("\nPyramid:")
    pyramid(5)