# 07. File Handling in Python

## 📌 Overview

File handling allows Python programs to store, retrieve, modify, and manage data outside the program's memory. It is useful for working with text files, CSV datasets, JSON data, directories, and binary files.

### Learning Objectives

By completing this section, you will learn how to:

- Read and write text files.
- Understand file modes such as `r`, `w`, `a`, and `x`.
- Use the `with` statement to manage files safely.
- Read and write CSV and JSON files.
- Work with paths, directories, and file metadata.
- Read and write binary data.
- Understand `struct` and `pickle`.
- Handle files efficiently and avoid common file-handling mistakes.

---

## 📂 Project Structure

```text
07_File_Handling/
├── practice_files/
├── 01_read_write_text.py
├── 02_file_modes.py
├── 03_with_statement.py
├── 04_csv_files.py
├── 05_json_files.py
├── 06_paths_and_directories.py
└── 07_binary_files.py
```

| File | Description |
|---|---|
| `01_read_write_text.py` | Reading, writing, appending, and iterating over text files |
| `02_file_modes.py` | Understanding file-opening modes |
| `03_with_statement.py` | Automatic resource management and context managers |
| `04_csv_files.py` | Working with CSV files using the `csv` module |
| `05_json_files.py` | Reading and writing JSON data |
| `06_paths_and_directories.py` | Managing paths, directories, and file information |
| `07_binary_files.py` | Binary I/O, `struct`, and `pickle` |

---

## 1. Reading and Writing Text Files

**File:** `01_read_write_text.py`

Python provides the built-in `open()` function to access files.

### 1.1 Writing to a File

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file!\n")
    file.write("Second line.\n")
```

- `open()` opens the file.
- `"w"` means write mode.
- `write()` writes a string to the file.
- `\n` represents a newline.
- `encoding="utf-8"` makes the intended text encoding explicit.

**Important:** Write mode creates the file if it does not exist, but truncates an existing file. Its previous contents are lost.

### 1.2 Reading an Entire File

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

`read()` reads the remaining contents of a file and returns them as a string.

To inspect whitespace and newline characters, use:

```python
print(repr(content))
```

### 1.3 Reading All Lines

```python
with open("sample.txt", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

`readlines()` returns a list of strings, usually retaining the newline character at the end of each line.

### 1.4 Reading Line by Line

```python
with open("sample.txt", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line.rstrip())
```

Iterating directly over the file is generally more memory-efficient than reading the entire file into memory.

- `enumerate()` provides line numbers.
- `rstrip()` removes trailing whitespace, including newline characters.
- Avoid removing whitespace indiscriminately if it is meaningful to your data.

### 1.5 Appending to a File

```python
with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Another line.\n")
```

Append mode adds new data at the end of the file without deleting its existing contents.

### 1.6 `write()` vs. `writelines()`

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First\n")
    file.writelines(["Second\n", "Third\n"])
```

- `write()` writes one string.
- `writelines()` writes an iterable of strings.
- Neither method automatically inserts newline characters.

---

## 2. File Modes

**File:** `02_file_modes.py`

A file mode specifies how Python should open a file.

| Mode | Meaning |
|---|---|
| `"r"` | Read; file must already exist |
| `"w"` | Write; creates or truncates the file |
| `"a"` | Append; creates the file if missing |
| `"x"` | Exclusive creation; fails if the file exists |
| `"b"` | Binary mode modifier |
| `"t"` | Text mode modifier; the default |
| `"+"` | Enables both reading and writing |

### Common Mode Combinations

| Mode | Behavior |
|---|---|
| `"rb"` | Read binary data |
| `"wb"` | Write binary data; truncates existing file |
| `"ab"` | Append binary data |
| `"r+"` | Read and write without initially truncating |
| `"w+"` | Read and write; truncates existing file |
| `"a+"` | Read and append |
| `"x"` | Create a new file only if it does not exist |

### Example: Read and Write

```python
with open("modes.txt", "w", encoding="utf-8") as file:
    file.write("First line\nSecond line\n")

with open("modes.txt", "r+", encoding="utf-8") as file:
    contents = file.read()
    file.seek(0)
    file.write("NEW\n")

print(open("modes.txt", encoding="utf-8").read())
```

In `"r+"` mode, `seek(0)` moves the file position to the beginning. Writing does not automatically insert characters or shift existing content; it overwrites bytes or characters at the current position according to the text stream's behavior.

For clean, safe examples, use a context manager for every file, including the final read:

```python
with open("modes.txt", encoding="utf-8") as file:
    print(file.read())
```

### Exclusive Creation

```python
try:
    with open("new_file.txt", "x", encoding="utf-8") as file:
        file.write("Created successfully")
except FileExistsError:
    print("File already exists.")
```

Use `"x"` when overwriting an existing file would be undesirable.

---

## 3. The `with` Statement

**File:** `03_with_statement.py`

The `with` statement manages resources and ensures that they are properly released when the block exits, including when an exception occurs.

### 3.1 Opening a File Without `with`

```python
file = open("data.txt", "w", encoding="utf-8")

try:
    file.write("Hello")
finally:
    file.close()
```

The `finally` block ensures that the file is closed even if an error occurs.

### 3.2 Opening a File With `with`

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

This is the preferred approach because Python automatically closes the file when the block ends.

### 3.3 Working With Multiple Files

```python
with (
    open("input.txt", encoding="utf-8") as source,
    open("output.txt", "w", encoding="utf-8") as destination
):
    for line in source:
        destination.write(line.upper())
```

This reads one line at a time, converts it to uppercase, and writes the result to another file.

The parenthesized multiple-context-manager syntax requires Python 3.10 or later. On older Python versions, use a single `with` statement on one line with a backslash or nest the statements.

### 3.4 Custom Context Managers

A context manager implements `__enter__()` and `__exit__()` to manage setup and cleanup.

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f} seconds")
        return False

with Timer():
    sum(range(1_000_000))
```

- `__enter__()` runs when entering the block.
- `__exit__()` runs when leaving the block.
- Returning `False` means exceptions are not suppressed.
- `time.perf_counter()` is suitable for measuring elapsed time.

---

## 4. Working With CSV Files

**File:** `04_csv_files.py`

CSV stands for **Comma-Separated Values**. It is commonly used for spreadsheets, tabular data, and datasets.

Python provides the built-in `csv` module for reading and writing CSV files.

### 4.1 Writing CSV Data

```python
import csv

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 30, "NYC"])
    writer.writerow(["Bob", 25, "LA"])
```

- `csv.writer()` creates a writer object.
- `writerow()` writes one row.
- `newline=""` is recommended when opening CSV files to prevent unwanted extra blank lines on some platforms.

### 4.2 Reading CSV Data

```python
import csv

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Each row is returned as a list of strings. Convert values to `int`, `float`, or other types when needed.

### 4.3 Using `DictReader`

`DictReader` maps each row to a dictionary using the column headers as keys.

```python
import csv

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["age"])
```

This is often more readable than accessing columns by numeric index.

### 4.4 Using `DictWriter`

```python
import csv

rows = [
    {"name": "Charlie", "age": 35},
    {"name": "Dana", "age": 28},
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(rows)
```

- `fieldnames` defines the column names and their order.
- `writeheader()` writes the header row.
- `writerows()` writes multiple dictionaries.

**Key point:** Use the `csv` module instead of manually splitting lines on commas. CSV fields may contain commas, quotes, and newlines that require proper parsing.

---

## 5. Working With JSON Files

**File:** `05_json_files.py`

JSON stands for **JavaScript Object Notation**. It is a text format commonly used for APIs, configuration files, and data exchange.

### 5.1 Python Objects and JSON

Common mappings include:

| Python | JSON |
|---|---|
| `dict` | Object |
| `list`, `tuple` | Array |
| `str` | String |
| `int`, finite `float` | Number |
| `True`, `False` | `true`, `false` |
| `None` | `null` |

Not every Python object can be represented directly in JSON.

### 5.2 Writing JSON to a File

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"],
    "address": {"city": "NYC", "zip": "10001"},
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
```

`json.dump()` serializes a Python object and writes it directly to a file. `indent=2` makes the JSON easier to read.

### 5.3 Reading JSON From a File

```python
import json

with open("data.json", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["name"])
print(loaded["hobbies"])
print(loaded["address"]["city"])
```

`json.load()` parses JSON content from a file and returns the corresponding Python object.

### 5.4 JSON Strings

Use `dumps()` and `loads()` when working with JSON strings rather than files.

```python
import json

data = {"name": "Alice", "score": 95}

json_string = json.dumps(data)
print(json_string)

parsed = json.loads(json_string)
print(parsed["score"])
```

Remember:

- `dump()` writes to a file-like object.
- `dumps()` returns a JSON string.
- `load()` reads JSON from a file-like object.
- `loads()` parses a JSON string.

### 5.5 Pretty Printing

```python
print(json.dumps(data, indent=2, sort_keys=True))
```

- `indent=2` adds indentation.
- `sort_keys=True` sorts object keys in the output.

### 5.6 Handling Unsupported Objects

Objects such as `datetime` instances are not serializable by the default JSON encoder.

```python
import json
from datetime import datetime

def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

    raise TypeError(f"Unsupported type: {type(obj).__name__}")

data = {"now": datetime.now()}

print(json.dumps(data, default=default_handler))
```

The `isoformat()` method converts a datetime into an ISO-style string. The JSON decoder will not automatically convert that string back into a `datetime`; you must parse it separately if required.

**Security note:** When reading JSON from untrusted sources, validate the structure and values before using them.

---

## 6. Paths and Directories

**File:** `06_paths_and_directories.py`

Python provides both `os.path` and `pathlib` for working with paths. `pathlib` is often the more convenient modern interface.

### 6.1 Useful `os.path` Functions

```python
import os

print(os.getcwd())
print(os.path.join("folder", "file.txt"))
print(os.path.exists("."))
print(os.path.isfile("file.txt"))
print(os.path.isdir("."))
print(os.path.basename("/a/b/c.txt"))
print(os.path.dirname("/a/b/c.txt"))
print(os.path.splitext("file.txt"))
```

| Function | Purpose |
|---|---|
| `os.getcwd()` | Gets the current working directory |
| `os.path.join()` | Joins path components |
| `os.path.exists()` | Checks whether a path exists |
| `os.path.isfile()` | Checks whether a path is a file |
| `os.path.isdir()` | Checks whether a path is a directory |
| `os.path.basename()` | Gets the final path component |
| `os.path.dirname()` | Gets the directory portion |
| `os.path.splitext()` | Separates the final extension |

### 6.2 Using `pathlib.Path`

```python
from pathlib import Path

path = Path("folder") / "file.txt"
print(path)
print(path.exists())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
```

Useful attributes and methods:

- `name`: final path component.
- `stem`: filename without its final suffix.
- `suffix`: final extension, such as `.txt`.
- `parent`: parent directory.
- `exists()`: checks whether the path exists.
- `stat()`: obtains file metadata, including size.

The `/` operator joins path components in a platform-aware way.

### 6.3 Creating Directories

```python
from pathlib import Path

Path("testdir").mkdir(exist_ok=True)
Path("testdir/nested").mkdir(parents=True, exist_ok=True)
```

- `exist_ok=True` avoids an error if the target directory already exists.
- `parents=True` creates missing parent directories as needed.

### 6.4 Listing Files

```python
from pathlib import Path

path = Path(".")

print(list(path.iterdir()))
print(list(path.glob("*.py")))
print(list(path.rglob("*.py")))
```

- `iterdir()` lists immediate directory contents.
- `glob()` finds matching entries in the current directory.
- `rglob()` searches recursively through subdirectories.

For large directories, iterate over the results instead of converting them all to a list.

### 6.5 Reading and Writing With `pathlib`

```python
from pathlib import Path

file_path = Path("sample.txt")

file_path.write_text("Hello", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))

file_path.write_text("Line 1\nLine 2\n", encoding="utf-8")
print(file_path.read_text(encoding="utf-8").splitlines())
```

`write_text()` overwrites an existing file. Use ordinary `open()` in append mode when you need to add data without replacing the existing contents.

### 6.6 Removing Files and Directories

```python
from pathlib import Path
import shutil

Path("sample.txt").unlink(missing_ok=True)
shutil.rmtree("testdir", ignore_errors=True)
```

`unlink()` removes a file or symbolic link. `shutil.rmtree()` recursively removes a directory tree.

**Warning:** Recursive deletion can permanently remove many files. Verify the target path before running cleanup code, and avoid suppressing errors unless that behavior is intentional.

---

## 7. Binary Files

**File:** `07_binary_files.py`

Text files store human-readable characters using an encoding. Binary files store bytes and are commonly used for images, audio, compressed data, and structured data.

### 7.1 Writing and Reading Bytes

```python
data = bytes([0, 1, 2, 3, 255])

with open("data.bin", "wb") as file:
    file.write(data)

with open("data.bin", "rb") as file:
    raw = file.read()

print(raw)
print(list(raw))
```

- `"wb"` opens a file for binary writing.
- `"rb"` opens a file for binary reading.
- `bytes` represents an immutable sequence of byte values from `0` to `255`.

Unlike text mode, binary mode does not decode bytes into strings.

### 7.2 The `struct` Module

The `struct` module packs Python values into a byte sequence and unpacks bytes into Python values according to a specified binary layout.

```python
import struct

packed = struct.pack("<iif", 42, -7, 3.14)
print(packed)

a, b, c = struct.unpack("<iif", packed)
print(a, b, c)
```

The format string `"<iif"` means:

- `<`: little-endian byte order, with standard sizes.
- `i`: signed integer.
- `i`: another signed integer.
- `f`: 32-bit floating-point number.

Using an explicit byte order is often preferable when defining a file format or communicating between different systems.

### 7.3 The `pickle` Module

`pickle` serializes many Python objects into a binary representation.

```python
import pickle

data = {"name": "Alice", "scores": [1, 2, 3]}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

with open("data.pkl", "rb") as file:
    loaded = pickle.load(file)

print(loaded)
```

- `pickle.dump()` serializes an object into a file.
- `pickle.load()` reconstructs the object from a file.

**Critical security warning:** Never unpickle data from an untrusted source. Malicious pickle data can execute arbitrary code during deserialization.

Pickle is also Python-specific and is not intended as a universal data-exchange format. Use JSON when you need a broadly supported, text-based format for compatible data.

---

## 8. Important Concepts to Remember

### File Handling Summary

| Task | Recommended Approach |
|---|---|
| Read a small text file | `Path.read_text()` or `open()` |
| Process a large text file | Iterate line by line |
| Replace file contents | `"w"` mode |
| Add to the end of a file | `"a"` mode |
| Prevent accidental overwrite | `"x"` mode |
| Read or write tabular data | `csv` module |
| Store structured compatible data | `json` module |
| Work with filesystem paths | `pathlib` |
| Read or write raw bytes | `"rb"` and `"wb"` |
| Pack fixed binary structures | `struct` |
| Serialize trusted Python objects | `pickle` |

### Common Mistakes

1. **Forgetting to close files:** Prefer `with open(...)` for automatic cleanup.
2. **Overwriting files unintentionally:** `"w"` truncates an existing file.
3. **Ignoring encodings:** Specify `encoding="utf-8"` when working with text unless another encoding is required.
4. **Using `read()` on huge files:** Process large files incrementally.
5. **Manually parsing CSV:** Use `csv.reader()` or `csv.DictReader()`.
6. **Confusing JSON functions:** Remember `dump`/`load` for file-like objects and `dumps`/`loads` for strings.
7. **Confusing relative paths with script locations:** Relative paths are usually resolved from the current working directory, not necessarily the directory containing the Python file.
8. **Unpickling untrusted data:** Never do this.
9. **Deleting directories carelessly:** Verify paths before recursive deletion.

---

## 9. Practice Checklist

- [ ] Create a text file and write multiple lines.
- [ ] Read a file using `read()`, `readlines()`, and line-by-line iteration.
- [ ] Append new content without overwriting the file.
- [ ] Experiment with `r`, `w`, `a`, `x`, and `r+`.
- [ ] Use `with` to open multiple files safely.
- [ ] Convert a CSV file into a list of dictionaries.
- [ ] Save a Python dictionary to JSON and load it again.
- [ ] Create nested directories with `pathlib`.
- [ ] Find all `.py` files in a directory tree.
- [ ] Write bytes to a binary file and read them back.
- [ ] Pack and unpack values using `struct`.
- [ ] Explain why untrusted pickle files are dangerous.
- [ ] Build a small program that saves and loads a list of records.

---

## 10. Mini Project: Student Record Manager

Create a small application that stores student records in a JSON file.

**Requirements:**

1. Add a student's name, ID, and marks.
2. Save records in `students.json`.
3. Load saved records when the program starts.
4. Display all stored students.
5. Search for a student by ID.
6. Handle the case where the JSON file does not exist.
7. Use `with` and UTF-8 encoding for file operations.

Example data structure:

```python
students = [
    {"id": 101, "name": "Alice", "marks": 90},
    {"id": 102, "name": "Bob", "marks": 85},
]
```

This project combines dictionaries, lists, functions, JSON serialization, and safe file handling.

---

## ▶️ Running the Examples

Run each script from the `07_File_Handling` directory:

```bash
python 01_read_write_text.py
python 02_file_modes.py
python 03_with_statement.py
python 04_csv_files.py
python 05_json_files.py
python 06_paths_and_directories.py
python 07_binary_files.py
```

The examples create and delete temporary files and directories. Run them in a practice directory, and make sure important files are not overwritten or removed.

**Recommended learning order:** Text Files → File Modes → `with` Statement → CSV → JSON → Paths and Directories → Binary Files.