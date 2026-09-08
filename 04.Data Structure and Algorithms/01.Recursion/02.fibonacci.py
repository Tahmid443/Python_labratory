def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
num = int(input("Enter the numbers: "))
for i in range(num):
    print(fibo(i), end=" ")
