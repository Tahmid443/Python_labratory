"""
COMPREHENSIVE PYTHON STRING METHODS DEMONSTRATION
All 47 string methods with examples and explanations
"""

# Sample string for demonstration
text = "  hello world!  "
sample = "Python Programming 2024"
mixed_case = "Hello World"
number_str = "12345"
alnum_str = "Python3"
alpha_str = "HelloWorld"
whitespace_str = "   \t\n  "
title_str = "The Quick Brown Fox"
comma_str = "apple,banana,cherry,date"

print("=" * 80)
print("PYTHON STRING METHODS - COMPLETE REFERENCE")
print("=" * 80)

# 1. capitalize() - Converts first character to uppercase and rest to lowercase
print("\n1. capitalize()")
print("-" * 50)
print(f"Original: '{text}'")
print(f"Result: '{text.capitalize()}'")
print("→ Capitalizes only first letter, converts all other letters to lowercase")
print("→ Useful for normalizing sentence case")

# 2. casefold() - Aggressive lowercase conversion for case-insensitive matching
print("\n2. casefold()")
print("-" * 50)
german_text = "Straße"
print(f"Original: '{german_text}'")
print(f"Result: '{german_text.casefold()}'")
print("→ More aggressive than lower(), handles special characters like ß → ss")
print("→ Best for case-insensitive string comparisons")

# 3. center() - Centers string within given width with padding character
print("\n3. center()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Result: '{sample.center(40, '*')}'")
print("→ Centers text in a field of specified width")
print("→ Optional fill character (default is space)")

# 4. count() - Counts occurrences of substring in string
print("\n4. count()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Count of 'o': {sample.count('o')}")
print("→ Returns number of non-overlapping occurrences")
print("→ Can specify start and end indices")

# 5. encode() - Returns encoded version of string (bytes)
print("\n5. encode()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Result: {sample.encode('utf-8')}")
print("→ Converts string to bytes using specified encoding")
print("→ Default encoding is UTF-8")

# 6. endswith() - Checks if string ends with specified suffix
print("\n6. endswith()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Ends with '2024': {sample.endswith('2024')}")
print("→ Returns True if string ends with the given suffix")
print("→ Can check multiple suffixes using tuple")

# 7. expandtabs() - Replaces tabs with spaces
print("\n7. expandtabs()")
print("-" * 50)
tab_text = "Hello\tWorld\tPython"
print(f"Original: '{tab_text}'")
print(f"Result: '{tab_text.expandtabs(10)}'")
print("→ Replaces tab characters with spaces")
print("→ Tab size can be specified (default is 8)")

# 8. find() - Finds first occurrence of substring
print("\n8. find()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Find 'gram': {sample.find('gram')}")
print("→ Returns index of first occurrence or -1 if not found")
print("→ Safer than index() as it doesn't raise exception")

# 9. format() - Formats string using placeholders
print("\n9. format()")
print("-" * 50)
formatted_string = "Hello {}, you are {} years old".format("John", 25)
print(f"Result: '{formatted_string}'")
print("→ Powerful string formatting with positional/named placeholders")
print("→ Supports alignment, padding, number formatting")

# 10. format_map() - Formats using dictionary mapping
print("\n10. format_map()")
print("-" * 50)
data = {"name": "Alice", "age": 30}
formatted_map = "My name is {name} and I am {age} years old".format_map(data)
print(f"Result: '{formatted_map}'")
print("→ Similar to format() but uses dictionary for values")
print("→ Useful when values are in a dictionary")

# 11. index() - Finds first occurrence like find() but raises ValueError
print("\n11. index()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Index of 'gram': {sample.index('gram')}")
print("→ Returns index of first occurrence")
print("→ Raises ValueError if substring not found")

# 12. isalnum() - Checks if all characters are alphanumeric
print("\n12. isalnum()")
print("-" * 50)
print(f"'{alnum_str}' is alphanumeric: {alnum_str.isalnum()}")
print(f"'{alpha_str}' is alphanumeric: {alpha_str.isalnum()}")
print("→ Returns True if all chars are letters or digits")
print("→ Empty string returns False")

# 13. isalpha() - Checks if all characters are alphabetic
print("\n13. isalpha()")
print("-" * 50)
print(f"'{alpha_str}' is alphabetic: {alpha_str.isalpha()}")
print(f"'{alnum_str}' is alphabetic: {alnum_str.isalpha()}")
print("→ Returns True if all chars are letters only")
print("→ No digits or special characters allowed")

# 14. isascii() - Checks if all characters are ASCII
print("\n14. isascii()")
print("-" * 50)
ascii_text = "Hello123"
non_ascii = "Hellö"
print(f"'{ascii_text}' is ASCII: {ascii_text.isascii()}")
print(f"'{non_ascii}' is ASCII: {non_ascii.isascii()}")
print("→ Returns True if all characters are in ASCII range (0-127)")
print("→ Useful for validating ASCII-only input")

# 15. isdecimal() - Checks if all characters are decimals
print("\n15. isdecimal()")
print("-" * 50)
decimal_str = "12345"
print(f"'{decimal_str}' is decimal: {decimal_str.isdecimal()}")
print(f"'{number_str}' is decimal: {number_str.isdecimal()}")
print("→ Returns True if all chars are decimal numbers (0-9)")
print("→ Superscripts and fractions are not decimals")

# 16. isdigit() - Checks if all characters are digits
print("\n16. isdigit()")
print("-" * 50)
digit_str = "123"
sup_str = "²"
print(f"'{digit_str}' is digit: {digit_str.isdigit()}")
print(f"'{sup_str}' is digit: {sup_str.isdigit()}")
print("→ Broader than isdecimal() (accepts superscripts, etc.)")
print("→ Returns True for Unicode digit characters")

# 17. isidentifier() - Checks if string is valid Python identifier
print("\n17. isidentifier()")
print("-" * 50)
print(f"'variable_name' is identifier: {'variable_name'.isidentifier()}")
print(f"'123abc' is identifier: {'123abc'.isidentifier()}")
print("→ Returns True if string is valid Python variable name")
print("→ Must start with letter or underscore")

# 18. islower() - Checks if all characters are lowercase
print("\n18. islower()")
print("-" * 50)
print(f"'{mixed_case}' is lowercase: {mixed_case.islower()}")
print(f"'hello' is lowercase: {'hello'.islower()}")
print("→ Returns True if at least one cased char and all are lowercase")
print("→ Ignores non-alphabetic characters")

# 19. isnumeric() - Checks if all characters are numeric
print("\n19. isnumeric()")
print("-" * 50)
num_str = "123"
frac_str = "½"
print(f"'{num_str}' is numeric: {num_str.isnumeric()}")
print(f"'{frac_str}' is numeric: {frac_str.isnumeric()}")
print("→ Most comprehensive: accepts fractions, superscripts, etc.")
print("→ Includes all numeric Unicode characters")

# 20. isprintable() - Checks if all characters are printable
print("\n20. isprintable()")
print("-" * 50)
printable = "Hello World!"
non_printable = "Hello\nWorld"
print(f"'{printable}' is printable: {printable.isprintable()}")
print(f"'{non_printable}' is printable: {non_printable.isprintable()}")
print("→ Returns True if all characters are printable")
print("→ Control characters like \\n, \\t are not printable")

# 21. isspace() - Checks if all characters are whitespace
print("\n21. isspace()")
print("-" * 50)
print(f"'{whitespace_str}' is whitespace: {whitespace_str.isspace()}")
print(f"'Hello' is whitespace: {'Hello'.isspace()}")
print("→ Returns True if all chars are whitespace (space, tab, newline)")
print("→ Empty string returns False")

# 22. istitle() - Checks if string is in title case
print("\n22. istitle()")
print("-" * 50)
print(f"'{title_str}' is title: {title_str.istitle()}")
print(f"'The quick brown fox' is title: {'The quick brown fox'.istitle()}")
print("→ Checks if first letter of each word is uppercase")
print("→ All other letters must be lowercase")

# 23. isupper() - Checks if all characters are uppercase
print("\n23. isupper()")
print("-" * 50)
print(f"'{mixed_case}' is uppercase: {mixed_case.isupper()}")
print(f"'HELLO' is uppercase: {'HELLO'.isupper()}")
print("→ Returns True if at least one cased char and all are uppercase")
print("→ Ignores non-alphabetic characters")

# 24. join() - Joins elements with string as separator
print("\n24. join()")
print("-" * 50)
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"Joined: '{', '.join(fruits)}'")
print("→ Joins iterable elements with the string as separator")
print("→ The string calls join() on the iterable")

# 25. ljust() - Left justifies string within width
print("\n25. ljust()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Result: '{sample.ljust(30, '.')}'")
print("→ Left-justifies text in field of specified width")
print("→ Fills remaining space with fill character")

# 26. lower() - Converts entire string to lowercase
print("\n26. lower()")
print("-" * 50)
print(f"Original: '{mixed_case}'")
print(f"Result: '{mixed_case.lower()}'")
print("→ Converts all uppercase letters to lowercase")
print("→ Simple case conversion for general use")

# 27. lstrip() - Removes leading characters
print("\n27. lstrip()")
print("-" * 50)
print(f"Original: '{text}'")
print(f"Result: '{text.lstrip()}'")
print("→ Removes leading whitespace by default")
print("→ Can specify characters to remove")

# 28. maketrans() - Creates translation table for translate()
print("\n28. maketrans()")
print("-" * 50)
trans = str.maketrans("aeiou", "12345")
translated = "hello world".translate(trans)
print(f"Original: 'hello world'")
print(f"Translated: '{translated}'")
print("→ Creates mapping for character translation")
print("→ Must have same length for source and destination")

# 29. partition() - Splits string at first occurrence
print("\n29. partition()")
print("-" * 50)
print(f"Original: '{comma_str}'")
print(f"Partition: {comma_str.partition(',')}")
print("→ Returns tuple (before, separator, after)")
print("→ Splits only at first occurrence")

# 30. replace() - Replaces all occurrences of substring
print("\n30. replace()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Result: '{sample.replace('Python', 'Java')}'")
print("→ Replaces all occurrences by default")
print("→ Can limit number of replacements with count parameter")

# 31. rfind() - Finds last occurrence of substring
print("\n31. rfind()")
print("-" * 50)
text_with_o = "hello world wow"
print(f"Original: '{text_with_o}'")
print(f"Last 'o' at: {text_with_o.rfind('o')}")
print("→ Finds last occurrence, returns -1 if not found")
print("→ Searches from right to left")

# 32. rindex() - Like rfind() but raises ValueError
print("\n32. rindex()")
print("-" * 50)
print(f"Original: '{text_with_o}'")
print(f"Last 'o' at: {text_with_o.rindex('o')}")
print("→ Same as rfind() but raises ValueError if not found")
print("→ Searches from right to left")

# 33. rjust() - Right justifies string within width
print("\n33. rjust()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Result: '{sample.rjust(30, '.')}'")
print("→ Right-justifies text in field of specified width")
print("→ Fills remaining space with fill character")

# 34. rpartition() - Splits at last occurrence
print("\n34. rpartition()")
print("-" * 50)
print(f"Original: '{comma_str}'")
print(f"Rpartition: {comma_str.rpartition(',')}")
print("→ Returns tuple (before, separator, after)")
print("→ Splits at last occurrence")

# 35. rsplit() - Splits from right with max splits
print("\n35. rsplit()")
print("-" * 50)
print(f"Original: '{comma_str}'")
print(f"rsplit: {comma_str.rsplit(',', 2)}")
print("→ Splits from right, returns list")
print("→ Can limit number of splits with maxsplit")

# 36. rstrip() - Removes trailing characters
print("\n36. rstrip()")
print("-" * 50)
print(f"Original: '{text}'")
print(f"Result: '{text.rstrip()}'")
print("→ Removes trailing whitespace by default")
print("→ Can specify characters to remove")

# 37. split() - Splits string into list
print("\n37. split()")
print("-" * 50)
print(f"Original: '{comma_str}'")
print(f"Split: {comma_str.split(',')}")
print("→ Splits at every separator by default")
print("→ Returns list of strings")

# 38. splitlines() - Splits at line breaks
print("\n38. splitlines()")
print("-" * 50)
multiline = "Line1\nLine2\nLine3"
print(f"Original: '{multiline}'")
print(f"Splitlines: {multiline.splitlines()}")
print("→ Splits at line breaks (\\n, \\r\\n, etc.)")
print("→ Keeps or removes line breaks with parameter")

# 39. startswith() - Checks if string starts with prefix
print("\n39. startswith()")
print("-" * 50)
print(f"Original: '{sample}'")
print(f"Starts with 'Python': {sample.startswith('Python')}")
print("→ Returns True if string starts with prefix")
print("→ Can check multiple prefixes using tuple")

# 40. strip() - Removes leading and trailing characters
print("\n40. strip()")
print("-" * 50)
print(f"Original: '{text}'")
print(f"Result: '{text.strip()}'")
print("→ Removes both leading and trailing whitespace")
print("→ Can specify characters to remove")

# 41. swapcase() - Swaps case of letters
print("\n41. swapcase()")
print("-" * 50)
print(f"Original: '{mixed_case}'")
print(f"Result: '{mixed_case.swapcase()}'")
print("→ Converts uppercase to lowercase and vice versa")
print("→ Useful for toggling case")

# 42. title() - Converts to title case
print("\n42. title()")
print("-" * 50)
print(f"Original: '{mixed_case}'")
print(f"Result: '{mixed_case.title()}'")
print("→ Capitalizes first letter of each word")
print("→ All other letters become lowercase")

# 43. translate() - Translates using translation table
print("\n43. translate()")
print("-" * 50)
print(f"Original: 'hello world'")
print(f"Translated: '{'hello world'.translate(trans)}'")
print("→ Uses translation table from maketrans()")
print("→ More efficient than replace() for multiple replacements")

# 44. upper() - Converts entire string to uppercase
print("\n44. upper()")
print("-" * 50)
print(f"Original: '{mixed_case}'")
print(f"Result: '{mixed_case.upper()}'")
print("→ Converts all lowercase letters to uppercase")
print("→ Simple case conversion for general use")

# 45. zfill() - Pads string with zeros on left
print("\n45. zfill()")
print("-" * 50)
num = "42"
print(f"Original: '{num}'")
print(f"Result: '{num.zfill(5)}'")
print("→ Pads with zeros on the left to specified width")
print("→ Useful for formatting numbers with leading zeros")

print("\n" + "=" * 80)
print("END OF STRING METHODS DEMONSTRATION")
print("=" * 80)
