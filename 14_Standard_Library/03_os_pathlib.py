import os
from pathlib import Path

# Environment
print(os.getcwd())
print(os.name)
print(os.environ.get("HOME"))

# Paths
print(os.path.join("a", "b", "c.txt"))
print(os.path.basename("/a/b/c.txt"))
print(os.path.dirname("/a/b/c.txt"))
print(os.path.splitext("f.txt"))
print(os.path.abspath("."))

# Files
print(os.path.exists("."))
print(os.path.isfile(__file__))
print(os.path.isdir("."))
print(os.path.getsize(__file__))

# pathlib (recommended)
p = Path(__file__)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
print(p.absolute())

# Join
print(Path("a") / "b" / "c.txt")

# Create dirs
tmp = Path("test_dirs/a/b")
tmp.mkdir(parents=True, exist_ok=True)

# Write/read
f = tmp / "data.txt"
f.write_text("hello")
print(f.read_text())

# Iterate
print(list(Path(".").iterdir())[:3])
print(list(Path(".").glob("*.py"))[:3])

# Cleanup
import shutil
shutil.rmtree("test_dirs")