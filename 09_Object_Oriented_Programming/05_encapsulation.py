class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance       # protected (convention)
        self.__pin = "0000"           # private (name-mangled)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Invalid PIN")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def set_pin(self, old, new):
        if old != self.__pin:
            raise ValueError("Wrong PIN")
        self.__pin = new

acc = BankAccount("Alice", 100)
acc.deposit(50)
print(acc.balance)

acc.withdraw(30, "0000")
print(acc.balance)

# Name mangling
print(acc._BankAccount__pin)   # still accessible!

# Property demo
acc._balance = 10000   # still possible (Python trusts developers)

# Validation property
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

p = Person(30)
print(p.age)
p.age = 35
print(p.age)
# p.age = -1  # ValueError