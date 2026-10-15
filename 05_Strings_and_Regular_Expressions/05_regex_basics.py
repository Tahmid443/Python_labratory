import re

text = "The year is 2024 and the month is 10."

# search - first match
m = re.search(r"\d+", text)
print(m.group(), m.start(), m.end())

# findall - all matches
print(re.findall(r"\d+", text))

# finditer - iterator of match objects
for m in re.finditer(r"\d+", text):
    print(m.group(), m.span())

# match - only from start
print(re.match(r"The", text))
print(re.match(r"year", text))   # None

# fullmatch
print(re.fullmatch(r"\d+", "12345"))
print(re.fullmatch(r"\d+", "12a45"))

# sub - replace
print(re.sub(r"\d+", "X", text))

# split
print(re.split(r"\s+", "a  b   c"))

# Compiled pattern (efficient for reuse)
pattern = re.compile(r"\d+")
print(pattern.findall(text))

# Character classes
print(re.findall(r"[aeiou]", "hello world"))
print(re.findall(r"[^aeiou]", "hello"))
print(re.findall(r"\w+", "hi there_42!"))
print(re.findall(r"\s", "a b\tc"))

# Anchors
print(re.findall(r"^\w+", "hello world"))
print(re.findall(r"\w+$", "hello world"))

# Quantifiers
print(re.findall(r"a+", "aaa b aa c a"))
print(re.findall(r"a*", "aaa"))
print(re.findall(r"a?", "aaa"))
print(re.findall(r"a{2,3}", "a aa aaa aaaa"))

# Flags
print(re.findall(r"hello", "Hello World", re.I))
print(re.findall(r"^world", "hello\nworld", re.M))