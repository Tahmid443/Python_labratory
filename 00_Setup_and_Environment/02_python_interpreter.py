"""
Understanding the Python Interpreter
"""
import sys

def main():
    print("Python Interpreter Modes:")
    print("1. Interactive (REPL):  $ python")
    print("2. Script mode:         $ python script.py")
    print("3. Module mode:         $ python -m module_name")
    print("4. Command execution:   $ python -c 'print(1+1)'")
    print()

    # sys.argv holds command-line arguments
    print(f"Script name: {sys.argv[0]}")
    print(f"Arguments:   {sys.argv[1:]}")

    # Environment variables
    print(f"\nPython path: {sys.path[:3]}...")

if __name__ == "__main__":
    main()