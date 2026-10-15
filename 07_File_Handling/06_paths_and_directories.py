import os
from pathlib import Path

# os.path
print(os.getcwd())
print(os.path.join("dir", "file.txt"))
print(os.path.exists("."))
print(os.path.isfile("file.txt"))
print(os.path.isdir("."))
print(os.path.basename("/a/b/c.txt"))
print(os.path.dirname("/a/b/c.txt"))
print(os.path.splitext("file.txt"))

# pathlib (modern, recommended)
p = Path(".")
print(p.cwd())
print(p / "subdir" / "file.txt")

# Create directory
Path("testdir").mkdir(exist_ok=True)
Path("testdir/nested").mkdir(parents=True, exist_ok=True)

# List files
print(list(Path(".").iterdir()))
print(list(Path(".").glob("*.py")))
print(list(Path(".").rglob("*.py")))  # recursive

# File info
f = Path(__file__)
print(f.name)
print(f.stem)
print(f.suffix)
print(f.parent)
print(f.exists())
print(f.stat().st_size)

# Read/write with pathlib
tmp = Path("testdir/sample.txt")
tmp.write_text("Hello")
print(tmp.read_text())
tmp.write_text("Line1\nLine2\n")
print(tmp.read_text().splitlines())

# Cleanup
import shutil
shutil.rmtree("testdir")