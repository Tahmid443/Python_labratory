def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return int(n%10) + int(sum_of_digits(int(n/10)))

try:
    n = int(input("Enter yout number: "))    
    if n>=0:
        print("Sum of the digits are:", sum_of_digits(n))
    else:
        print("please input a positive integer!!!")
except ValueError:
    print("Please input a positive integer!!!")
