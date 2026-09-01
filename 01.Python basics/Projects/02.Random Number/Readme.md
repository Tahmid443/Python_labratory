# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game built with Python**.  
The player chooses a difficulty level, tries to guess a randomly generated number, receives hints after each guess, and earns a score based on how quickly they find the number.

This project was created as a Python practice project to improve my understanding of **functions, loops, conditional statements, dictionaries, exception handling, random numbers, and modular programming**.

---

## 🎮 Features

- 🎯 Three difficulty levels
  - 🟢 Easy — Number between **1–10**
  - 🟡 Medium — Number between **1–20**
  - 🔴 Hard — Number between **1–30**
- 🔢 Random number generation
- ❤️ Maximum **7 attempts** per game
- 📈 Higher/Lower hints
- 🏆 Difficulty-based scoring system
- 📜 Guess history
- 🔢 Total guess counter
- 🔄 Play again option
- 🛡️ Input validation
- ❌ Handles invalid user input without crashing
- 🧩 Modular function-based structure

---

## 🕹️ How the Game Works

### 1. Start the Game

The program asks:

```text
Do you want to play?
1. Yes
2. No
```

If you choose `2`, the game exits.

### 2. Choose Difficulty

You can choose one of three difficulty levels:

```text
1. Easy   (1 - 10)
2. Medium (1 - 20)
3. Hard   (1 - 30)
```

The difficulty determines the range of the randomly generated number.

### 3. Guess the Number

You have a maximum of **7 attempts**.

After every incorrect guess, the game gives you a hint:

```text
📉 Try lower!
```

or

```text
📈 Try higher!
```

### 4. Score

Your score depends on the difficulty and the number of attempts used.

| Difficulty | Base Score |
|---|---:|
| Easy | 100 |
| Medium | 150 |
| Hard | 200 |

The score decreases by **10 points for each unsuccessful attempt**.

---

## 📜 Guess History

The game keeps track of all guesses made during the round.

Example:

```text
📜 Guess History:
5 → 8 → 7 → 6
```

It also displays the total number of guesses made.

---

## 🧩 Project Structure

The program is divided into several functions:

```text
main()
│
├── get_player_choice()
├── choose_difficulty()
├── generate_number()
├── calculate_score()
├── play_game()
├── show_result()
└── play_again()
```

### Functions

#### `get_valid_integer()`

Handles user input and validates whether the entered value is a valid integer within the required range.

#### `get_player_choice()`

Asks the player whether they want to start the game.

#### `choose_difficulty()`

Allows the player to select Easy, Medium, or Hard difficulty.

#### `generate_number()`

Generates the random number using Python's `random` module.

#### `calculate_score()`

Calculates the player's score based on difficulty and attempts.

#### `play_game()`

Contains the main guessing-game logic and tracks the player's guesses.

#### `show_result()`

Displays the final result, score, lucky number, and guess history.

#### `play_again()`

Allows the player to start another round.

#### `main()`

Controls the overall flow of the program.

---

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- Functions
- Loops
- Conditional statements
- Dictionaries
- Exception handling
- Lists
- F-strings

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd YOUR-REPOSITORY
```

### 3. Run the program

```bash
python rand.py
```

If your system uses `python3`:

```bash
python3 rand.py
```

---

## 💻 Example Gameplay

```text
=============================================
        NUMBER GUESSING GAME
=============================================

Do you want to play?
1. Yes
2. No

Enter your choice (1 or 2): 1

==============================
       DIFFICULTY
==============================

1. Easy   (1 - 10)
2. Medium (1 - 20)
3. Hard   (1 - 30)

Choose difficulty (1, 2 or 3): 1

---------------------------------------------
Guess the number between 1 and 10.
You have 7 attempts.
---------------------------------------------

Attempt 1/7 - Enter your guess: 5
📈 Try higher!

Attempts remaining: 6

Attempt 2/7 - Enter your guess: 8
📉 Try lower!

Attempts remaining: 5

Attempt 3/7 - Enter your guess: 7

🎉 CONGRATULATIONS!
You guessed the number in 3 attempt(s).
🏆 Your score: 80

📜 Guess History:
5 → 8 → 7

Total guesses: 3
```

---

## 📚 What I Learned

Through this project, I practiced:

- How to create and call functions
- Passing arguments to functions
- Returning multiple values
- Using `while` and `for` loops
- Using dictionaries to organize data
- Handling invalid input with `try/except`
- Using the `random` module
- Working with lists
- Building reusable functions
- Separating a program into smaller components
- Designing a program using a `main()` function

---

## 🔮 Future Improvements

Possible features I may add later:

- 💾 Save high scores to a file
- 🏆 Leaderboard system
- 👤 Player names
- 📊 Statistics across multiple games
- 🎨 Improved terminal UI
- ⏱️ Time-based scoring
- 🔊 Sound effects
- 💾 Save game history
- 🧱 Object-Oriented Programming version
- 🌐 GUI version

---

## 👨‍💻 Author

**Taqi Tahmid**

Computer Science Engineering Student | Python Learner | Programmer

---

## ⭐ If You Like This Project

If you found this project useful or interesting, consider giving the repository a ⭐!

---

> **This project is part of my journey to master Python through hands-on projects. 🐍🚀**