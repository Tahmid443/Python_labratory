# ============================================================
#              PYTHON ESCAPE SEQUENCES
# ============================================================
#
# Escape sequences are special character combinations that
# begin with a backslash (\) and are used inside strings.
#
# Common Python Escape Sequences:
#
#   \'    -> Single Quote
#   \\    -> Backslash
#   \n    -> New Line
#   \r    -> Carriage Return
#   \t    -> Tab
#   \b    -> Backspace
#   \f    -> Form Feed
#   \ooo  -> Octal Value
#   \xhh  -> Hexadecimal Value
#
# ============================================================


# ------------------------------------------------------------
# 1. Single Quote (\')
# ------------------------------------------------------------
# Used to insert a single quote inside a string that is
# surrounded by single quotes.

print("I don't like Python.")

# Output:
# I don't like Python.


# ------------------------------------------------------------
# 2. Backslash (\\)
# ------------------------------------------------------------
# A single backslash has a special meaning in Python.
# To print an actual backslash, use two backslashes.

print("This is a backslash: \\")

# Output:
# This is a backslash: \


# ------------------------------------------------------------
# 3. New Line (\n)
# ------------------------------------------------------------
# Moves the cursor to the next line.

print("Hello\nWorld")

# Output:
# Hello
# World


# ------------------------------------------------------------
# 4. Carriage Return (\r)
# ------------------------------------------------------------
# Moves the cursor back to the beginning of the current line.
# Text written after \r can overwrite the previous text
# depending on the output environment.

print("Hello\rWorld")

# Possible output:
# World
#
# Explanation:
# "World" starts writing from the beginning of the line.


# ------------------------------------------------------------
# 5. Tab (\t)
# ------------------------------------------------------------
# Inserts a horizontal tab space.

print("Name:\tTahmid")
print("Age:\t20")
print("Language:\tPython")

# Output:
# Name:   Tahmid
# Age:    20
# Language:       Python


# ------------------------------------------------------------
# 6. Backspace (\b)
# ------------------------------------------------------------
# Moves the cursor one position backward.
# It can remove/overwrite the previous character depending
# on the terminal.

print("Helloo\b")

# The final appearance may look like:
# Hello


# ------------------------------------------------------------
# 7. Form Feed (\f)
# ------------------------------------------------------------
# Form feed was traditionally used to advance to the next
# page in printers.
#
# In modern terminals, its visual effect may vary.

print("Hello\fWorld")

# The exact appearance depends on the terminal.


# ------------------------------------------------------------
# 8. Octal Value (\ooo)
# ------------------------------------------------------------
# Represents a character using an octal (base-8) value.
#
# Syntax:
#       \ooo
#
# Example:
#       \101
#
# 101 in octal represents the ASCII character 'A'.

print("\101")

# Output:
# A


# Another example:
print("\110\145\154\154\157")

# Output:
# Hello


# ------------------------------------------------------------
# 9. Hexadecimal Value (\xhh)
# ------------------------------------------------------------
# Represents a character using a hexadecimal (base-16) value.
#
# Syntax:
#       \xhh
#
# Example:
#       \x41
#
# 41 in hexadecimal represents the ASCII character 'A'.

print("\x41")

# Output:
# A


# Another example:
print("\x48\x65\x6c\x6c\x6f")

# Output:
# Hello


# ============================================================
#                  PRACTICE EXAMPLE
# ============================================================

# Here we combine multiple escape sequences together.

print("================================")
print("\tMY PROFILE")
print("================================")
print("Name:\tTahmid")
print("Language:\tPython")
print("Goal:\tMaster Python")
print('Quote:\t"Never stop learning!"')
print("Path:\tC:\\Users\\Tahmid\\Python")
print("Message:\nKeep Learning!\nKeep Coding!")
print("================================")


# ============================================================
# IMPORTANT NOTE
# ============================================================
#
# Escape sequences are interpreted inside normal strings:
#
#     print("Hello\nWorld")
#
# But raw strings (r"...") treat backslashes mostly literally:
#
#     print(r"Hello\nWorld")
#
# Output:
#     Hello\nWorld
#
# Raw strings are especially useful for Windows file paths
# and regular expressions.
#
# Example:
#
#     path = r"C:\Users\Tahmid\Documents"
#
# ============================================================
