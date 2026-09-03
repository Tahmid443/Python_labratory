# 🔐 Password Generator

A simple and customizable **Password Generator built with Python**.

This project generates random passwords based on the user's preferred password length and character types. It was created as a Python practice project to work with functions, loops, conditional statements, user input, and Python's built-in modules.

---

## ✨ Features

* 🔢 Choose your desired password length
* 🔤 Include lowercase letters
* 🔠 Include uppercase letters
* 🔢 Include numbers
* 🔣 Include special characters
* ⚠️ Validates password length
* ⚠️ Handles invalid user input
* 🎲 Generates a random password automatically
* 📋 Optional copy-to-clipboard feature with `pyperclip`

---

## 🛠️ Technologies Used

* **Python 3**
* `random`
* `string`
* `pyperclip`

---

## 📂 Project Structure

```text
Password-Generator/
│
├── pass.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-generator.git
```

### 2. Navigate to the project directory

```bash
cd password-generator
```

### 3. Install the required package

If you are using the clipboard feature:

```bash
python -m pip install pyperclip
```

### 4. Run the program

```bash
python pass.py
```

---

## 🎮 How It Works

When you run the program, you first choose the password length.

```text
Enter password length: 12
```

Then select the character types you want:

```text
Choose what your password should contain:
1. Lowercase letters
2. Uppercase letters
3. Numbers
4. Special characters

Enter your choices (e.g. 1234): 1234
```

The program then generates a random password:

```text
Your generated password:
aG7@kP2!xQ9#
```

You can also choose whether to copy the password to your clipboard:

```text
Copy password to clipboard? (y/n): y

Password copied to clipboard! ✅
```

---

## 🧠 Project Structure

The program is divided into several functions:

```text
main()
 ├── get_password_length()
 ├── choose_character_types()
 ├── build_character_pool()
 ├── generate_password()
 └── copy password to clipboard
```

### `get_password_length()`

Takes the desired password length from the user and validates the input.

### `choose_character_types()`

Allows the user to choose which types of characters should be included.

### `build_character_pool()`

Creates the collection of characters that can be used for generating the password.

### `generate_password()`

Randomly selects characters from the character pool to create the final password.

---

## 📚 Python Concepts Practiced

This project helped practice:

* Functions
* Function arguments and return values
* `while` loops
* `for` loops
* `if / elif / else`
* User input
* Exception handling
* `try / except`
* String manipulation
* Python modules
* `random`
* `string`
* External packages
* Clipboard operations

---

## 🔮 Future Improvements

Some features I plan to add:

* [ ] Password strength checker
* [ ] Generate multiple passwords at once
* [ ] Regenerate password option
* [ ] Exclude ambiguous characters such as `0`, `O`, `l`, and `1`
* [ ] GUI version using Tkinter
* [ ] Use Python's `secrets` module for stronger password generation
* [ ] Add password history
* [ ] Add customizable minimum requirements for each character type

---

## ⚠️ Disclaimer

This project is mainly created for **learning and practicing Python**.

For passwords used in real-world security-sensitive situations, use a trusted password manager or a cryptographically secure password-generation method.

---

## 👨‍💻 Author

**Taqi Tahmid**

If you found this project useful, feel free to ⭐ the repository!

---

## 📄 License

This project is open-source and available under the **MIT License**.
