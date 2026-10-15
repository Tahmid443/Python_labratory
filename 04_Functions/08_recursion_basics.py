# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])

# Sum of list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))

# Reverse string
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello"))

# Binary search
def bsearch(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return bsearch(arr, target, mid + 1, hi)
    return bsearch(arr, target, lo, mid - 1)

print(bsearch([1, 3, 5, 7, 9], 7))

# Tower of Hanoi
def hanoi(n, src, dst, aux):
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    hanoi(n - 1, src, aux, dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n - 1, aux, dst, src)

hanoi(3, "A", "C", "B")