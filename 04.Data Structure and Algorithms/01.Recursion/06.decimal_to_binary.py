def dec_to_binary(n):
    if n==0:
        return 0
    else:
        return n % 2 + 10 * dec_to_binary(int(n / 2))
try:
    num = int(input("Enter the decimal number: "))
    print("Binary =",dec_to_binary(num))
except ValueError:
    print("Integer number only!!!")
