def power(n,p):
    assert p>=0 and int(p) == p,"The power must be positive number!!!"
    if p == 0:
        return 1
    if p == 1:
        return n
    return n * power(n, p-1)


num = float(input("Enter your base number: "))
p = float(input("Enter your power: "))
print(round(power(num,p),3))