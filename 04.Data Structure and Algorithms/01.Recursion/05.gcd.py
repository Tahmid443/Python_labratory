"""
Euclidean Algorithm

gcd(48,18)
step 1: 48/18 = 2 remainder 12
step 2: 18/12 = 1 remainder 6
step 1: 12/6 = 2 remainder 0

the remainder is 0 that means gcd is 6

gcd(a,0) = a
gcd(a,b) = gcd(b, a mod b)
"""
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD =",gcd(abs(a),abs(b)))
except ValueError:
    print("Please input number only!!!")