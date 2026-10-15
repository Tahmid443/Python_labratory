"""
Python Installation Guide (run this to check your version)
"""
import sys
import platform

def check_python():
    print("=" * 50)
    print("PYTHON INSTALLATION CHECK")
    print("=" * 50)
    print(f"Python Version: {sys.version}")
    print(f"Version Info:   {sys.version_info}")
    print(f"Executable:     {sys.executable}")
    print(f"Platform:       {platform.platform()}")
    print(f"Architecture:   {platform.architecture()[0]}")
    print(f"Machine:        {platform.machine()}")
    print("=" * 50)

    major, minor = sys.version_info[:2]
    if (major, minor) >= (3, 8):
        print("✅ Your Python version is modern. You're good to go!")
    else:
        print("⚠️  Please upgrade to Python 3.8 or newer.")

if __name__ == "__main__":
    check_python()

# Installation instructions:
# Windows: https://www.python.org/downloads/  (check "Add to PATH")
# macOS:   brew install python@3.12
# Linux:   sudo apt install python3 python3-pip