name = "Tahmid"
age = 22

print(type(name.upper()))#str objects, upper() is the method of this object
print(type(age))#int objects

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #method
    def bark(self):
        print("whoof whoof")

dog1 = Dog("Tommy","Scottish terrier") #creating a Dog object and assigning it in a variable called dog1
dog1.bark() #accessing method from the object
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Bruce","Greyhound")
dog2.bark()
print(dog2.name)
print(dog2.breed)
