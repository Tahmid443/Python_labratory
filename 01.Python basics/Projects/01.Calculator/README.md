# 🧮 Python Calculator

A simple and interactive **command-line calculator built with Python**.  
This project was created to practice and demonstrate core Python programming concepts such as functions, conditional logic, loops, pattern matching with `match-case`, exception handling, lists, user input, and file handling.

The calculator supports basic arithmetic operations and can **save calculation history to a text file**, allowing previous calculations to remain available even after the program is closed.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- `%` Modulo
- `^` Power
- 🔢 Supports decimal numbers using `float`
- 🛡️ Handles division by zero
- 🛡️ Handles modulo by zero
- 🛡️ Handles invalid numeric input
- ⚠️ Handles invalid operators
- 📜 Displays calculation history
- 💾 Saves calculation history permanently to `history.txt`
- 🔄 Runs continuously until the user chooses to exit
- 🖥️ Fully command-line based

---

## 🛠️ Technologies Used

- **Python 3**
- Python built-in file handling
- `match-case`
- Exception handling with `try-except`
- No external libraries required

---

## 📂 Project Structure

```text
python-calculator/
│
├── calc.py          # Main calculator program
├── history.txt      # Generated automatically to store calculations
├── README.md        # Project documentation
└── .gitignore       # Git ignore rules
```

> `history.txt` is created automatically when the calculator saves its first calculation.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Enter the project directory

```bash
cd python-calculator
```

### 3. Run the calculator

```bash
python calc.py
```

Depending on your system, you may need:

```bash
python3 calc.py
```

---

## 🎮 How to Use

When the program starts, it asks whether you want to use the calculator.

```text
Do you want to use this calculator?
1.Yes
2.No
```

### Choose `1`

The calculator starts and asks for an operator:

```text
Enter operator(+, -, /, *, ^, %)
[Enter H to show history]
[Enter 1 to exit]:
```

### Choose an operator

For example:

```text
Enter operator: +
Enter your first number: 10
Enter your second number: 20
```

Output:

```text
Sum of 10.0 and 20.0 is : 30.0
```

---

## ➗ Supported Operations

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2` |
| `%` | Modulo | `10 % 3 = 1` |
| `^` | Power | `2 ^ 3 = 8` |

---

## 📜 Calculation History

The calculator includes persistent history.

Press:

```text
H
```

to display saved calculations.

Example:

```text
===== CALCULATION HISTORY =====
Sum of 10.0 and 20.0 is : 30.0
Multiplication of 5.0 and 6.0 is: 30.0
Division of 20.0 and 4.0 is: 5.0
2.0 to the power 5.0 is: 32.0
```

### How it works

The project uses Python's file handling:

```python
with open("history.txt", "a") as file:
    file.write(result)
```

The `"a"` mode means **append**, so new calculations are added without deleting previous calculations.

When history is requested, the program reads the file:

```python
with open("history.txt", "r") as file:
    history = file.read()
```

This means calculation history can persist even after the calculator is closed.

---

## 🛡️ Error Handling

The calculator handles several common errors.

### Division by zero

```text
Cannot divide by zero (Undefined)
```

### Modulo by zero

```text
Cannot perform modulo by zero (Undefined)
```

### Invalid number input

If the user enters something that cannot be converted to a number:

```text
Invalid operand!
```

### Invalid operator

If an unsupported operator is entered:

```text
Invalid operator!
```

### Missing history file

If `history.txt` does not exist yet, the program safely reports:

```text
No calculation history yet.
```

---

## 🧠 Python Concepts Practiced

This project helped practice several important Python concepts:

### 1. Functions

Each arithmetic operation is implemented as a separate function.

```python
def add(a, b):
    return f"Sum of {a} and {b} is : {a+b}"
```

This makes the operations easier to understand and maintain.

### 2. Loops

A `while True` loop keeps the calculator running until the user chooses to exit.

### 3. Conditional Statements

The program uses `if`, `elif`, and `else` to control the application flow.

### 4. `match-case`

Python's `match-case` is used to select the appropriate calculation based on the operator.

```python
match operator:
    case "+":
        ...
    case "-":
        ...
```

### 5. Exception Handling

`try-except` is used to prevent the program from crashing when invalid input or mathematical errors occur.

### 6. Lists

A `history` list is used to keep calculation results during the current program session.

### 7. File Handling

The project uses `open()` with read and append modes to store calculation history permanently.

### 8. Main Guard

The program uses:

```python
if __name__ == "__main__":
    main()
```

This is a standard Python pattern for controlling program execution.

---

## 💡 Example Session

```text
============== Welcome to python calculator ===============

Do you want to use this calculator?
1.Yes
2.No

1

Enter operator(+, -, /, *, ^, %)
[Enter H to show history]
[Enter 1 to exit]: *

Enter your first number: 12
Enter your second number: 5

Multiplication of 12.0 and 5.0 is: 60.0

Enter operator: ^

Enter your first number: 2
Enter your second number: 4

2.0 to the power 4.0 is: 16.0

Enter operator: H

===== CALCULATION HISTORY =====
Multiplication of 12.0 and 5.0 is: 60.0
2.0 to the power 4.0 is: 16.0

Enter operator: 1
```

---

## 🔮 Future Improvements

Possible improvements for future versions include:

- [ ] Add a **clear history** option
- [ ] Add a **GUI version** using Tkinter
- [ ] Improve the formatting of calculation history
- [ ] Add more mathematical operations
- [ ] Add square root and other scientific functions
- [ ] Add calculation timestamps
- [ ] Separate calculator logic into multiple modules
- [ ] Improve the user interface
- [ ] Add automated tests
- [ ] Store history in a more structured format such as JSON

---

## 📌 Learning Goal

The main goal of this project was not simply to create a calculator, but to practice building a complete small Python application from scratch.

The project demonstrates the progression from basic Python syntax to combining multiple concepts into a working program:

```text
Input
  ↓
Validation
  ↓
Operator Selection
  ↓
Calculation
  ↓
Error Handling
  ↓
Display Result
  ↓
Save History
```

---

## 👨‍💻 Author

**Taqi Tahmid**

This project is part of my Python learning journey and is focused on strengthening programming fundamentals through hands-on projects.

---

## 📄 License

This project is open for learning and educational purposes.
