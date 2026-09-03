import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def choose_character_types():
    while True:
        print("\nChoose what your password should contain:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Numbers")
        print("4. Special characters")

        choice = input("Enter your choices (e.g. 1234): ")

        if choice and all(char in "1234" for char in choice):
            return choice

        print("Invalid choice. Please choose from 1, 2, 3, 4.")


def build_character_pool(choice):
    characters = ""

    if "1" in choice:
        characters += string.ascii_lowercase

    if "2" in choice:
        characters += string.ascii_uppercase

    if "3" in choice:
        characters += string.digits

    if "4" in choice:
        characters += string.punctuation

    return characters


def generate_password(length, characters):
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 35)
    print("      PASSWORD GENERATOR")
    print("=" * 35)

    length = get_password_length()
    choice = choose_character_types()

    characters = build_character_pool(choice)

    password = generate_password(length, characters)

    print("\nYour generated password:")
    print(password)


if __name__ == "__main__":
    main()
