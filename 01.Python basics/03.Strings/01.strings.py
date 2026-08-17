print("Taqi Tahmid")
print('Taqi Tahmid')

countryName = "Bangladesh"
print(countryName)

multiLineString = """
Hello this is a multiline
string. It help to store multiple
line in a variable
"""
print(multiLineString)

#string concatenation
a = "apple"
b = "is a fruit"
c = a + " " + b
print(c)

#we can get char position(index) wise. String = Char array
fruit = "Apple"
print(fruit[2])

#we can loop through a string
for x in "Tahmid":
    print(x)
    
#to get the length of a string we can use len()
name = "Taqi Tahmid Dhrubo"
print(len(name))

#we can check string inside a string if it is present
txt = "My college name is Sylhet Engineering College"
print("college" in txt) #True
#or we can use conditional statement as well
if "Sylhet" in txt:
    print("Yes, it is present")
    
#we can also check if not present
print("Dhaka" not in txt)#True
#or we can use conditional statement as well
if "Dhaka" not in txt:
    print("Dhaka is absent in txt")