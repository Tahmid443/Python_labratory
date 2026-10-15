# 00. Setup and Environment — Python Notes

## 1. Python Installation and Environment

### 1.1 What is Python?

Python is a high-level, general-purpose programming language known for its readable syntax. It is widely used in web development, automation, data science, artificial intelligence, and competitive programming.

### 1.2 Installing Python

Download Python from the official website:

https://www.python.org/downloads/

After installation, open a terminal or command prompt and execute:

```bash
python --version
```

Alternatively, use:

```bash
python3 --version
```

If Python is installed correctly, the command displays the installed version.

**Important for Windows users:** Enable **Add Python to PATH** during installation when that option is available.

### 1.3 Understanding the Installation Check Script

File: `01_install_python.py`

This script uses Python's built-in `sys` and `platform` modules to display information about the Python installation and the operating system.

#### Important concepts

**1. `import sys`**

The `sys` module provides access to interpreter-related information and functionality.

**2. `import platform`**

The `platform` module provides information about the operating system and hardware environment.

**3. `sys.version`**

Returns a string describing the Python interpreter version and build information.

```python
import sys

print(sys.version)
```

**4. `sys.version_info`**

Returns structured version information, including the major, minor, and micro version numbers.

```python
import sys

print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)
```

For example, a version such as Python 3.12.4 has:

- Major version: `3`
- Minor version: `12`
- Micro version: `4`

**5. `sys.executable`**

Returns the path to the Python interpreter executable running the current program.

```python
import sys

print(sys.executable)
```

This is useful when multiple Python installations exist on the same computer.

**6. `platform.platform()`**

Returns a string describing the operating system and platform.

```python
import platform

print(platform.platform())
```

**7. `platform.architecture()`**

Returns information about the interpreter's architecture, commonly including `32bit` or `64bit`.

```python
import platform

print(platform.architecture())
```

**8. `platform.machine()`**

Returns the machine hardware identifier, such as `x86_64` or `AMD64`, depending on the system.

```python
import platform

print(platform.machine())
```

### 1.4 Checking the Python Version

The script uses a conditional statement to determine whether the installed version meets its minimum requirement.

```python
import sys

major, minor = sys.version_info[:2]

if (major, minor) >= (3, 8):
    print("Python version is acceptable.")
else:
    print("Please upgrade Python.")
```

Here:

- `sys.version_info[:2]` extracts the major and minor version numbers.
- Tuple comparison compares the version numbers in order.
- `if` executes a block when the condition is true.
- `else` executes when the condition is false.

For example, `(3, 12) >= (3, 8)` evaluates to `True`.

**Note:** Python 3.8 is no longer supported. For a new project, use a currently supported Python release.

### 1.5 The `__name__ == "__main__"` Convention

You will frequently see this pattern in Python programs:

```python
def main():
    print("Program started.")

if __name__ == "__main__":
    main()
```

The special variable `__name__` tells you how a Python module is being used.

- When a file runs directly, `__name__` is set to `"__main__"`.
- When the file is imported as a module, `__name__` is normally set to the module's name.

This convention lets you write reusable code that only runs its main program when executed directly.

---

## 2. Understanding the Python Interpreter

File: `02_python_interpreter.py`

### 2.1 What is a Python Interpreter?

A Python interpreter is the software that executes Python programs.

In a typical CPython implementation, source code is compiled into bytecode, which is then executed by the Python virtual machine.

Python code can be executed in several ways.

### 2.2 Interactive Mode (REPL)

REPL stands for **Read–Eval–Print Loop**.

In this mode, you enter Python statements and see their results immediately.

Start the interactive interpreter by running:

```bash
python
```

Example:

```python
>>> 10 + 20
30

>>> print("Hello, Python!")
Hello, Python!
```

**Advantages:**

- Quickly test small pieces of code.
- Experiment with expressions and functions.
- Learn Python syntax interactively.

Exit the interpreter using `exit()` or the appropriate keyboard shortcut for your operating system.

### 2.3 Script Mode

In script mode, Python executes code saved in a `.py` file.

For example, create a file named `hello.py`:

```python
print("Hello, World!")
```

Run it with:

```bash
python hello.py
```

**Advantages:**

- Suitable for larger programs.
- Makes code easy to save and reuse.
- Useful for projects, DSA implementations, and competitive programming.

### 2.4 Module Mode

The `-m` option runs a module as a script.

General syntax:

```bash
python -m module_name
```

Example:

```bash
python -m http.server
```

This starts Python's simple HTTP server using the `http.server` module.

Another example:

```bash
python -m pip --version
```

This displays information about the `pip` installation associated with the selected Python interpreter.

**Why use `-m`?**

It can help ensure that a module or tool runs through the Python interpreter selected by the `python` command.

### 2.5 Command Execution Mode

The `-c` option executes Python code supplied directly on the command line.

Example:

```bash
python -c "print(1 + 1)"
```

Output:

```text
2
```

Another example:

```bash
python -c "print('Hello from Python')"
```

This is useful for quick calculations and simple tests without creating a file.

### 2.6 Understanding `sys.argv`

`sys.argv` is a list containing the command-line arguments passed to a Python script.

Example script:

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

Run the script:

```bash
python 02_python_interpreter.py hello python 123
```

The arguments after the script name are accessible through `sys.argv[1:]`.

For example:

```python
sys.argv[1:]
```

returns:

```python
["hello", "python", "123"]
```

**Important points:**

- `sys.argv[0]` usually contains the script name or path.
- `sys.argv[1:]` contains the additional arguments.
- Command-line arguments are strings by default.
- Convert arguments when numeric values are needed.

Example:

```python
import sys

number = int(sys.argv[1])
print(number * 2)
```

Run:

```bash
python example.py 25
```

Output:

```text
50
```

### 2.7 Understanding `sys.path`

`sys.path` is a list of locations Python searches when importing modules.

Example:

```python
import sys

print(sys.path)
```

It may contain:

- The script's directory or another initial import location.
- Directories specified by environment configuration.
- Standard library locations.
- Installed package directories.

Python uses this search path to locate modules during import operations.

**Example:**

```python
import math

print(math.sqrt(25))
```

Python locates the built-in `math` module and makes its functionality available to the program.

The exact contents and order of `sys.path` depend on how Python was launched and how the environment is configured.

---

## 3. Important Differences

| Feature | Purpose | Example |
|---|---|---|
| `sys.version` | Displays version details | `print(sys.version)` |
| `sys.version_info` | Provides structured version numbers | `sys.version_info.major` |
| `sys.executable` | Shows the active interpreter path | `print(sys.executable)` |
| `sys.argv` | Accesses command-line arguments | `print(sys.argv)` |
| `sys.path` | Shows module search locations | `print(sys.path)` |
| `platform.platform()` | Describes the operating system | `print(platform.platform())` |
| REPL | Executes code interactively | `python` |
| Script mode | Executes a Python file | `python main.py` |
| Module mode | Executes a module | `python -m pip` |
| Command mode | Executes inline code | `python -c "print(2)"` |

---

## 4. Practice Questions

Try answering these questions without looking at the explanations above.

1. What is the difference between `sys.version` and `sys.version_info`?
2. Why might `sys.executable` be useful when multiple Python versions are installed?
3. What does REPL stand for?
4. How do you execute a Python file from the terminal?
5. What is the purpose of the `-m` flag?
6. How can you execute a Python expression without creating a `.py` file?
7. What information does `sys.argv` contain?
8. Why are command-line arguments usually converted using `int()` or `float()`?
9. What is the purpose of `sys.path`?
10. Why do Python programs use `if __name__ == "__main__":`?

### Practical Tasks

- [ ] Run the installation-check script.
- [ ] Print the Python major, minor, and micro version numbers.
- [ ] Print the interpreter executable path.
- [ ] Run a Python script with three command-line arguments.
- [ ] Execute `print(100 * 100)` using command mode.
- [ ] Run `python -m pip --version`.
- [ ] Write a script that accepts two numbers from command-line arguments and prints their sum.

---

## 5. Key Takeaways

- Python must be installed before you can run Python programs locally.
- The `sys` module provides information about the interpreter and program execution.
- The `platform` module helps identify the operating system and hardware environment.
- Python supports interactive, script, module, and inline command execution.
- `sys.argv` provides access to command-line arguments.
- `sys.path` helps Python locate importable modules.
- The `__name__ == "__main__"` convention separates direct execution from importing a module.

**Study principle:** Understand each concept, run the examples yourself, and complete the practice tasks before moving to the next topic.
