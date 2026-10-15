import re

text = "John: 30, Jane: 25, Bob: 45"

# Capturing groups
pattern = r"(\w+): (\d+)"
for m in re.finditer(pattern, text):
    print(f"Name: {m.group(1)}, Age: {m.group(2)}")
    print(f"  All groups: {m.groups()}")

# Named groups
pattern = r"(?P<name>\w+): (?P<age>\d+)"
for m in re.finditer(pattern, text):
    print(m.group("name"), m.group("age"))
    print(m.groupdict())

# Non-capturing group
pattern = r"(?:Mr|Ms|Dr)\. (\w+)"
print(re.findall(pattern, "Mr. Smith and Ms. Jones"))

# Backreference
pattern = r"\b(\w+)\s+\1\b"
print(re.findall(pattern, "hello hello world"))

# Alternation
print(re.findall(r"cat|dog", "cat dog bird"))

# Lookahead / lookbehind
# Positive lookahead: (?=...)
print(re.findall(r"\d+(?= dollars)", "100 dollars, 200 euros"))
# Negative lookahead: (?!...)
print(re.findall(r"\d+(?! dollars)", "100 dollars, 200 euros"))
# Positive lookbehind: (?<=...)
print(re.findall(r"(?<=\$)\d+", "$100 $200"))
# Negative lookbehind: (?<!...)
print(re.findall(r"(?<!\$)\b\d+", "$100 200"))

# Greedy vs non-greedy
html = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.+>", html))     # greedy
print(re.findall(r"<.+?>", html))    # non-greedy