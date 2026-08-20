# 🗂️ Python File Handling --- Complete Revision Notes

This README is a **revision-friendly guide to Python File Handling**,
based on the practice programs in this folder.

It covers opening, reading, writing, creating, updating, closing, and
deleting files, along with file modes, text/binary modes, `with`,
`read()`, `readline()`, iteration, and the `os` module.

------------------------------------------------------------------------

## 📚 Table of Contents

1.  [What is File Handling?](#1-what-is-file-handling)
2.  [The `open()` Function](#2-the-open-function)
3.  [File Opening Modes](#3-file-opening-modes)
4.  [Text Mode and Binary Mode](#4-text-mode-and-binary-mode)
5.  [Opening a File for Reading](#5-opening-a-file-for-reading)
6.  [Reading File Content with
    `read()`](#6-reading-file-content-with-read)
7.  [Reading a Limited Number of
    Characters](#7-reading-a-limited-number-of-characters)
8.  [Reading Lines with `readline()`](#8-reading-lines-with-readline)
9.  [Looping Through a File](#9-looping-through-a-file)
10. [Closing a File](#10-closing-a-file)
11. [The `with` Statement](#11-the-with-statement)
12. [Writing to a File](#12-writing-to-a-file)
13. [Append Mode --- `a`](#13-append-mode---a)
14. [Write Mode --- `w`](#14-write-mode---w)
15. [Create Mode --- `x`](#15-create-mode---x)
16. [Creating a New File](#16-creating-a-new-file)
17. [Deleting Files with
    `os.remove()`](#17-deleting-files-with-osremove)
18. [Checking Whether a File Exists](#18-checking-whether-a-file-exists)
19. [Deleting Folders with
    `os.rmdir()`](#19-deleting-folders-with-osrmdir)
20. [File Paths](#20-file-paths)
21. [Common Errors](#21-common-errors)
22. [Important Differences](#22-important-differences)
23. [Quick Revision Sheet](#23-quick-revision-sheet)
24. [Practice Files](#24-practice-files)
25. [Final Checklist](#25-final-checklist)

------------------------------------------------------------------------

# 1. What is File Handling?

**File handling** means working with files stored on a computer.

A Python program can:

-   create files
-   open files
-   read files
-   write to files
-   append data
-   overwrite data
-   update files
-   delete files
-   check whether files exist

File handling is useful when data needs to remain available after a
Python program finishes.

For example, instead of storing information only in variables:

``` python
name = "Tahmid"
```

we can save information in a file:

``` text
student.txt
```

and read it later.

------------------------------------------------------------------------

# 2. The `open()` Function

The main function used for file handling in Python is:

``` python
open()
```

Basic syntax:

``` python
open(filename, mode)
```

Example:

``` python
f = open("demofile.txt", "r")
```

Here:

``` text
demofile.txt → file name
r             → opening mode
f             → file object
```

The returned file object can then be used to read or write data.

------------------------------------------------------------------------

## 2.1 Basic example

``` python
f = open("demofile.txt", "r")

print(f.read())

f.close()
```

The process is:

``` text
open file
   ↓
get file object
   ↓
read/write
   ↓
close file
```

------------------------------------------------------------------------

# 3. File Opening Modes

Python provides several important modes.

  Mode   Name     Purpose
  ------ -------- -------------------------
  `r`    Read     Read an existing file
  `a`    Append   Add data to the end
  `w`    Write    Write/overwrite content
  `x`    Create   Create a new file
  `t`    Text     Text mode
  `b`    Binary   Binary mode

------------------------------------------------------------------------

## `r` --- Read

``` python
open("demofile.txt", "r")
```

Opens a file for reading.

If the file does not exist, Python raises:

``` text
FileNotFoundError
```

`r` is the default mode.

Therefore:

``` python
open("demofile.txt")
```

is equivalent to:

``` python
open("demofile.txt", "rt")
```

------------------------------------------------------------------------

## `a` --- Append

``` python
open("demofile.txt", "a")
```

Opens the file for appending.

New content is added to the **end of the existing file**.

If the file does not exist, Python creates it.

------------------------------------------------------------------------

## `w` --- Write

``` python
open("demofile.txt", "w")
```

Opens the file for writing.

Important:

> If the file already contains data, `w` replaces the existing content.

If the file does not exist, Python creates it.

------------------------------------------------------------------------

## `x` --- Create

``` python
open("myfile.txt", "x")
```

Creates a new file.

If the file already exists, Python raises:

``` text
FileExistsError
```

------------------------------------------------------------------------

# 4. Text Mode and Binary Mode

Python can work with files in **text** or **binary** mode.

## `t` --- Text mode

``` python
open("demofile.txt", "rt")
```

Text mode is used for text data.

`"t"` is the default.

Therefore:

``` python
open("demofile.txt", "r")
```

and:

``` python
open("demofile.txt", "rt")
```

are equivalent for normal text reading.

------------------------------------------------------------------------

## `b` --- Binary mode

Binary mode is used for data such as:

-   images
-   audio
-   video
-   PDFs
-   other binary files

Example:

``` python
open("image.jpg", "rb")
```

Common binary combinations include:

``` python
"rb"   # read binary
"wb"   # write binary
"ab"   # append binary
```

------------------------------------------------------------------------

# 5. Opening a File for Reading

The simplest example:

``` python
f = open("demofile.txt")
```

Because `r` and `t` are defaults, this means:

``` python
f = open("demofile.txt", "rt")
```

Then:

``` python
print(f.read())
```

reads the file.

------------------------------------------------------------------------

## Important

The file must exist when using read mode.

If it does not exist:

``` python
open("missing.txt", "r")
```

causes:

``` text
FileNotFoundError
```

------------------------------------------------------------------------

# 6. Reading File Content with `read()`

The `read()` method reads content from a file.

Example:

``` python
with open("demofile.txt") as f:
    print(f.read())
```

If the file contains:

``` text
Hello Python
Welcome to file handling
```

the output is:

``` text
Hello Python
Welcome to file handling
```

------------------------------------------------------------------------

## 6.1 `read()` reads the entire file

``` python
f.read()
```

By default, it reads all remaining content from the current file
position.

------------------------------------------------------------------------

## 6.2 File position matters

After:

``` python
f.read()
```

the file cursor is normally at the end of the content.

Calling:

``` python
f.read()
```

again will usually return an empty string because there is nothing left
to read from the current position.

------------------------------------------------------------------------

# 7. Reading a Limited Number of Characters

`read()` can accept a number.

``` python
f.read(5)
```

This reads up to the next **5 characters** from the current file
position.

Example:

``` python
with open("demofile.txt") as f:
    print(f.read(5))
```

If the file begins with:

``` text
Hello Python
```

the result is:

``` text
Hello
```

------------------------------------------------------------------------

## Syntax

``` python
file.read(number)
```

Examples:

``` python
f.read(10)
f.read(50)
f.read(100)
```

This is useful when you don't want to load all available content at
once.

------------------------------------------------------------------------

# 8. Reading Lines with `readline()`

The `readline()` method reads one line at a time.

Example:

``` python
with open("demofile.txt") as f:
    print(f.readline())
```

This reads the first line.

------------------------------------------------------------------------

## 8.1 Reading two lines

Calling `readline()` repeatedly advances the file position.

``` python
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
```

The first call reads line 1.

The second call reads line 2.

------------------------------------------------------------------------

## `read()` vs `readline()`

  Method         Reads
  -------------- -----------------------
  `read()`       All remaining content
  `read(n)`      Up to `n` characters
  `readline()`   One line

------------------------------------------------------------------------

# 9. Looping Through a File

A file object can be iterated line by line.

Example:

``` python
with open("demofile.txt") as f:
    for x in f:
        print(x)
```

This processes the file one line at a time.

Conceptually:

``` text
File
 ↓
Line 1 → process
Line 2 → process
Line 3 → process
...
```

This is often convenient for text files and avoids manually calling
`readline()` repeatedly.

------------------------------------------------------------------------

# 10. Closing a File

When you manually open a file:

``` python
f = open("demofile.txt", "r")
```

you should close it when finished:

``` python
f.close()
```

Example:

``` python
f = open("demofile.txt", "r")

print(f.read())

f.close()
```

Closing a file releases the resources associated with the open file.

------------------------------------------------------------------------

## Why close files?

Good file-handling practice helps:

-   release system resources
-   ensure data is properly flushed when writing
-   avoid keeping unnecessary file handles open
-   prevent problems when other code needs access to the file

------------------------------------------------------------------------

# 11. The `with` Statement

The recommended approach for most normal file operations is:

``` python
with open("demofile.txt", "r") as f:
    print(f.read())
```

The `with` statement manages the file resource automatically.

After leaving the block, the file is closed.

------------------------------------------------------------------------

## 11.1 Why `with` is better

Compare:

``` python
f = open("demofile.txt", "r")

print(f.read())

f.close()
```

with:

``` python
with open("demofile.txt", "r") as f:
    print(f.read())
```

The second version is cleaner and safer because Python handles closing
the file when the block exits, including when an exception occurs during
the block.

### Recommended pattern

``` python
with open("filename.txt", "r") as f:
    data = f.read()
```

Use this pattern whenever possible.

------------------------------------------------------------------------

# 12. Writing to a File

The `write()` method is used to write text to a file.

Example:

``` python
with open("demofile.txt", "w") as f:
    f.write("Hello Python")
```

The mode determines what happens to existing content.

------------------------------------------------------------------------

# 13. Append Mode --- `a`

Append mode adds new content to the end of a file.

Example from the practice code:

``` python
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")
```

If the file already contains:

``` text
Hello
```

after appending it may contain:

``` text
Hello
Now the file has more content!
```

depending on whether your string includes a newline.

------------------------------------------------------------------------

## Important: `write()` does not automatically add a newline

This:

``` python
f.write("Hello")
f.write("World")
```

can produce:

``` text
HelloWorld
```

If you want separate lines:

``` python
f.write("Hello\n")
f.write("World\n")
```

Result:

``` text
Hello
World
```

------------------------------------------------------------------------

# 14. Write Mode --- `w`

Write mode can overwrite an existing file.

Example:

``` python
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")
```

If the file already contained data, the previous content is replaced.

### ⚠️ Important

`w` is destructive when used on an existing file.

Think:

``` text
w → replace existing content
```

Use it carefully.

------------------------------------------------------------------------

# 15. Create Mode --- `x`

The `x` mode is specifically for creating a new file.

Example:

``` python
f = open("myfile.txt", "x")
```

If `myfile.txt` does not exist:

``` text
File created
```

If it already exists:

``` text
FileExistsError
```

------------------------------------------------------------------------

## `x` vs `w`

  Mode   File doesn't exist   File already exists
  ------ -------------------- ---------------------
  `x`    Creates it           Error
  `w`    Creates it           Overwrites it

This difference is very important.

------------------------------------------------------------------------

# 16. Creating a New File

There are several ways to create a file depending on your goal.

### Using `x`

``` python
open("myfile.txt", "x")
```

Creates a new file and fails if it already exists.

### Using `w`

``` python
open("myfile.txt", "w")
```

Creates it if necessary, but overwrites an existing file.

### Using `a`

``` python
open("myfile.txt", "a")
```

Creates it if necessary and appends when it already exists.

------------------------------------------------------------------------

# 17. Deleting Files with `os.remove()`

Python's `os` module provides functions for interacting with the
operating system.

Import it:

``` python
import os
```

To delete a file:

``` python
os.remove("demofile.txt")
```

This permanently removes the file from its filesystem location.

------------------------------------------------------------------------

## ⚠️ Be careful

This is a destructive operation:

``` python
os.remove("demofile.txt")
```

Always make sure the path points to the intended file.

------------------------------------------------------------------------

# 18. Checking Whether a File Exists

Before deleting a file, it is often useful to check whether it exists.

Use:

``` python
os.path.exists()
```

Example:

``` python
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
```

The logic is:

``` text
Does file exist?
       ↓
     Yes ──→ Delete
       ↓
      No ──→ Print message
```

------------------------------------------------------------------------

## Why use `os.path.exists()`?

It prevents your program from blindly attempting to remove a path that
may not exist.

It can also be used before other file operations where existence
matters.

------------------------------------------------------------------------

# 19. Deleting Folders with `os.rmdir()`

To remove a directory:

``` python
import os

os.rmdir("myfolder")
```

Important:

> `os.rmdir()` is for removing an empty directory.

If the directory contains files or subdirectories, `os.rmdir()` normally
fails.

------------------------------------------------------------------------

## File vs folder deletion

### File

``` python
os.remove("file.txt")
```

### Empty folder

``` python
os.rmdir("myfolder")
```

Remember:

``` text
remove() → file
rmdir()  → directory
```

------------------------------------------------------------------------

# 20. File Paths

A file path tells Python where a file is located.

Example from the practice code:

``` python
open("d:/Python_labratory/01.Python basics/08.File Handling/demofile.txt")
```

This is an **absolute path** because it specifies the full location
starting from the drive.

------------------------------------------------------------------------

## 20.1 Relative path

A simpler path is:

``` python
open("demofile.txt")
```

Python interprets this relative to the program's **current working
directory**.

This is important.

If you have:

``` text
project/
├── main.py
└── demofile.txt
```

and Python's current working directory is `project`, then:

``` python
open("demofile.txt")
```

can find the file.

But if the current working directory is different, Python may raise:

``` text
FileNotFoundError
```

------------------------------------------------------------------------

## 20.2 Common path problem

You may see:

``` text
FileNotFoundError:
[Errno 2] No such file or directory
```

even though the file exists somewhere on your computer.

Usually this means Python is looking in a different directory than you
expected.

Useful debugging:

``` python
import os

print(os.getcwd())
```

This shows Python's current working directory.

------------------------------------------------------------------------

## 20.3 Windows path example

A Windows path may look like:

``` text
D:\Python_labratory\file.txt
```

In Python, backslashes can introduce escape sequences.

Safer alternatives include:

### Raw string

``` python
path = r"D:\Python_labratory\file.txt"
```

### Forward slashes

``` python
path = "D:/Python_labratory/file.txt"
```

### `pathlib`

Modern Python code often uses:

``` python
from pathlib import Path

path = Path("D:/Python_labratory/file.txt")
```

------------------------------------------------------------------------

# 21. Common Errors

## 21.1 `FileNotFoundError`

Example:

``` python
open("demofile.txt", "r")
```

If Python cannot find the file in the location it is checking:

``` text
FileNotFoundError
```

### Check:

-   Is the filename correct?
-   Is the extension correct?
-   Is the path correct?
-   Is Python using the expected working directory?
-   Does the file actually exist?

------------------------------------------------------------------------

## 21.2 `FileExistsError`

Using:

``` python
open("myfile.txt", "x")
```

when the file already exists causes:

``` text
FileExistsError
```

Remember:

``` text
x → create only
```

------------------------------------------------------------------------

## 21.3 Accidentally deleting data with `w`

This:

``` python
open("demofile.txt", "w")
```

can erase existing content when you write to the file.

If you want to add data instead, use:

``` python
open("demofile.txt", "a")
```

------------------------------------------------------------------------

## 21.4 Forgetting to close manually opened files

If you use:

``` python
f = open("file.txt")
```

remember:

``` python
f.close()
```

Better:

``` python
with open("file.txt") as f:
    ...
```

------------------------------------------------------------------------

## 21.5 Wrong file path

A path such as:

``` python
"D:\new\test.txt"
```

can be problematic because sequences such as `\n` may be interpreted as
escapes.

Prefer:

``` python
r"D:\new\test.txt"
```

or:

``` python
"D:/new/test.txt"
```

------------------------------------------------------------------------

# 22. Important Differences

## `r` vs `a` vs `w` vs `x`

  Mode   Main purpose   Existing file
  ------ -------------- -------------------------------
  `r`    Read           Reads content
  `a`    Append         Keeps content and adds to end
  `w`    Write          Replaces content
  `x`    Create         Raises error

### Easy memory trick

``` text
r → Read
a → Add
w → Write/replace
x → eXclusive creation
```

------------------------------------------------------------------------

## `read()` vs `readline()`

  Method         Purpose
  -------------- -----------------------------
  `read()`       Reads all remaining content
  `read(n)`      Reads up to `n` characters
  `readline()`   Reads one line

------------------------------------------------------------------------

## `remove()` vs `rmdir()`

``` python
os.remove("file.txt")
```

→ removes a file.

``` python
os.rmdir("folder")
```

→ removes an empty directory.

------------------------------------------------------------------------

## `close()` vs `with`

Manual:

``` python
f = open("file.txt")
data = f.read()
f.close()
```

Recommended:

``` python
with open("file.txt") as f:
    data = f.read()
```

------------------------------------------------------------------------

# 23. Quick Revision Sheet

## Open a file

``` python
f = open("file.txt", "r")
```

------------------------------------------------------------------------

## Read entire file

``` python
print(f.read())
```

------------------------------------------------------------------------

## Read first `n` characters

``` python
print(f.read(n))
```

------------------------------------------------------------------------

## Read one line

``` python
print(f.readline())
```

------------------------------------------------------------------------

## Read line by line

``` python
for line in f:
    print(line)
```

------------------------------------------------------------------------

## Close manually

``` python
f.close()
```

------------------------------------------------------------------------

## Recommended pattern

``` python
with open("file.txt", "r") as f:
    data = f.read()
```

------------------------------------------------------------------------

## Append

``` python
with open("file.txt", "a") as f:
    f.write("New content")
```

------------------------------------------------------------------------

## Overwrite

``` python
with open("file.txt", "w") as f:
    f.write("New content")
```

------------------------------------------------------------------------

## Create only if it doesn't exist

``` python
f = open("file.txt", "x")
```

------------------------------------------------------------------------

## Delete a file

``` python
import os

os.remove("file.txt")
```

------------------------------------------------------------------------

## Check existence

``` python
import os

if os.path.exists("file.txt"):
    print("File exists")
```

------------------------------------------------------------------------

## Delete an empty folder

``` python
import os

os.rmdir("myfolder")
```

------------------------------------------------------------------------

## Find current working directory

``` python
import os

print(os.getcwd())
```

------------------------------------------------------------------------

# 24. Practice Files

  -----------------------------------------------------------------------
  File                                Main Topics
  ----------------------------------- -----------------------------------
  `01.intro_and_open.py`              File handling introduction,
                                      `open()`, modes, reading, `read()`,
                                      `readline()`, iteration, `close()`,
                                      `with`

  `02.write.py`                       Append, overwrite, `write()`,
                                      creating files with `x`, `a`, and
                                      `w`

  `03.delete.py`                      `os.remove()`, `os.path.exists()`,
                                      `os.rmdir()`

  `demofile.txt`                      Practice text file used by the
                                      examples
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 25. Final Checklist

Before moving to the next Python topic, make sure you can:

-   [ ] Explain what file handling is
-   [ ] Use `open()`
-   [ ] Explain `r`, `a`, `w`, and `x`
-   [ ] Explain text mode `t`
-   [ ] Explain binary mode `b`
-   [ ] Read an entire file using `read()`
-   [ ] Read a limited number of characters
-   [ ] Read individual lines using `readline()`
-   [ ] Loop through a file line by line
-   [ ] Close a manually opened file
-   [ ] Use the `with` statement
-   [ ] Write content using `write()`
-   [ ] Append content using `a`
-   [ ] Understand why `w` can erase existing content
-   [ ] Create a file using `x`
-   [ ] Explain the difference between `x` and `w`
-   [ ] Delete a file using `os.remove()`
-   [ ] Check whether a path exists using `os.path.exists()`
-   [ ] Delete an empty directory using `os.rmdir()`
-   [ ] Understand absolute and relative paths
-   [ ] Diagnose `FileNotFoundError`
-   [ ] Understand the current working directory
-   [ ] Handle Windows file paths safely

------------------------------------------------------------------------

# 🧠 Final Mental Model

Think of file handling as a simple lifecycle:

``` text
             FILE HANDLING
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
      OPEN                CREATE
        │
   ┌────┼────┬────┐
   ↓    ↓    ↓    ↓
 READ WRITE APPEND ...
   │    │    │
   └────┴────┴────┐
                  ↓
                CLOSE
                  │
                  ↓
               DELETE
```

The most important patterns to remember are:

``` python
# Read
with open("file.txt", "r") as f:
    data = f.read()
```

``` python
# Append
with open("file.txt", "a") as f:
    f.write("New content")
```

``` python
# Overwrite
with open("file.txt", "w") as f:
    f.write("New content")
```

``` python
# Create
with open("file.txt", "x") as f:
    pass
```

``` python
# Delete
import os
os.remove("file.txt")
```

------------------------------------------------------------------------

## 🎯 The Most Important Things to Memorize

``` text
open()       → open a file
read()       → read content
readline()   → read one line
write()      → write content
close()      → close manually opened file
with         → automatically manage file closing

r → read
a → append
w → overwrite/write
x → create

os.remove()  → delete file
os.rmdir()   → delete empty folder
os.path.exists() → check existence
```

> **Revision tip:** Always practice file handling with a small test file
> before working with important data. Be especially careful with `w` and
> `os.remove()` because both can destroy existing data.
