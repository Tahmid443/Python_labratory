"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

# To open a file for reading it is enough to specify the name of the file:
f = open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt")
# The code above is the same as:
f = open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

"""
Note: Make sure the file exists, or else you will get an error.
"""
# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt")
print(f.read())

# You can also use the with statement when opening a file:
with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.read())

# It is a good practice to always close the file when you are done with it.
# If you are not using the with statement, you must write a close statement in order to close the file:
# Close the file when you are finished with it:

f = open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt")
print(f.readline())
f.close()

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:

with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.read(5))

# You can return one line by using the readline() method:
# Read one line of the file:

with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.readline())
# By calling readline() two times, you can read the two first lines:
# Read two lines of the file:

with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.readline())
    print(f.readline())

# Loop through the file line by line:

with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    for x in f:
        print(x)
