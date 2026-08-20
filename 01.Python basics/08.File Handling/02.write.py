"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
# Open the file "demofile.txt" and append content to the file:

with open(
    "d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt", "a"
) as f:
    f.write("Now the file has more content!")

# open and read the file after the appending:
with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.read())

# Open the file "demofile.txt" and overwrite the content:

with open(
    "d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt", "w"
) as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting:
with open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt") as f:
    print(f.read())

"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists
"""
# Create a new file called "myfile.txt":

f = open("d:/Python_labratory/01.Python basics/08.File Handling/myfile.txt", "x")
