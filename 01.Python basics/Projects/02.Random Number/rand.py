import random


MAX_ATTEMPTS = 7


def get_valid_integer(prompt, min_value=None, max_value=None):
    """Get a valid integer from the user within an optional range."""

    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a number <= {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_player_choice():
    """Ask the player whether they want to play."""

    print("\n" + "=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)

    print("\nDo you want to play?")
    print("1. Yes")
    print("2. No")

    return get_valid_integer(
        "\nEnter your choice (1 or 2): ",
        1,
        2
    )


def choose_difficulty():
    """Let the player choose a difficulty level."""

    print("\n" + "=" * 30)
    print("       DIFFICULTY")
    print("=" * 30)

    print("1. Easy   (1 - 10)")
    print("2. Medium (1 - 20)")
    print("3. Hard   (1 - 30)")

    choice = get_valid_integer(
        "\nChoose difficulty (1, 2 or 3): ",
        1,
        3
    )

    difficulty = {
        1: ("Easy", 10),
        2: ("Medium", 20),
        3: ("Hard", 30)
    }

    return difficulty[choice]


def generate_number(limit):
    """Generate a random number within the selected range."""

    return random.randint(1, limit)


def calculate_score(attempt, difficulty):
    """Calculate score based on attempts and difficulty."""

    base_scores = {
        "Easy": 100,
        "Medium": 150,
        "Hard": 200
    }

    base_score = base_scores[difficulty]

    # Lose 10 points for every unsuccessful attempt.
    score = base_score - ((attempt - 1) * 10)

    return max(score, 10)


def play_game(number, limit, difficulty):
    """Run the guessing game and return the result."""

    guesses = []

    print("\n" + "-" * 45)
    print(f"Guess the number between 1 and {limit}.")
    print(f"You have {MAX_ATTEMPTS} attempts.")
    print("-" * 45)

    for attempt in range(1, MAX_ATTEMPTS + 1):

        guess = get_valid_integer(
            f"\nAttempt {attempt}/{MAX_ATTEMPTS} - "
            f"Enter your guess: ",
            1,
            limit
        )

        guesses.append(guess)

        if guess == number:
            score = calculate_score(attempt, difficulty)
            return attempt, True, score, guesses

        if guess > number:
            print("📉 Try lower!")

        else:
            print("📈 Try higher!")

        remaining = MAX_ATTEMPTS - attempt

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    return MAX_ATTEMPTS, False, 0, guesses


def show_result(attempt, won, number, score, guesses):
    """Display the final result and game statistics."""

    print("\n" + "=" * 45)

    if won:
        print("🎉 CONGRATULATIONS!")
        print(f"You guessed the number in {attempt} attempt(s).")
        print(f"🏆 Your score: {score}")
    else:
        print("😔 GAME OVER!")
        print(f"The lucky number was: {number}")

    print("\n📜 Guess History:")
    print(" → ".join(map(str, guesses)))

    print(f"\nTotal guesses: {len(guesses)}")

    print("=" * 45)


def play_again():
    """Ask the player whether they want another round."""

    print("\nDo you want to play again?")
    print("1. Yes")
    print("2. No")

    choice = get_valid_integer(
        "\nEnter your choice (1 or 2): ",
        1,
        2
    )

    return choice == 1


def main():
    """Main program."""

    while True:

        choice = get_player_choice()

        if choice == 2:
            print("\nOkay, goodbye! 👋")
            break

        difficulty, limit = choose_difficulty()

        number = generate_number(limit)

        attempt, won, score, guesses = play_game(
            number,
            limit,
            difficulty
        )

        show_result(
            attempt,
            won,
            number,
            score,
            guesses
        )

        if not play_again():
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()

