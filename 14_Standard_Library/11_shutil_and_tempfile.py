import shutil
import tempfile
import os
from pathlib import Path

# Copy
with tempfile.TemporaryDirectory() as tmp:
    src = Path(tmp) / "a.txt"
    src.write_text("hello")

    dst = Path(tmp) / "b.txt"
    shutil.copy(src, dst)
    print(dst.read_text())

    # copy2 (preserves metadata)
    shutil.copy2(src, Path(tmp) / "c.txt")

    # Directory copy
    dir1 = Path(tmp) / "dir1"
    dir1.mkdir()
    (dir1 / "f.txt").write_text("x")
    shutil.copytree(dir1, Path(tmp) / "dir2")

    # Move
    shutil.move(str(dst), str(Path(tmp) / "moved.txt"))

# Disk usage
print(shutil.disk_usage("."))

# Which (find executable)
print(shutil.which("python"))

# rmtree
with tempfile.TemporaryDirectory() as tmp:
    (Path(tmp) / "a").mkdir()
    (Path(tmp) / "a" / "b").mkdir()
    shutil.rmtree(Path(tmp) / "a")

# Temp files
with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt", delete=True) as f:
    f.write("hello")
    f.seek(0)
    print(f.read())

# Temp dir
with tempfile.TemporaryDirectory() as d:
    print(f"Temp: {d}")

# mkstemp
fd, path = tempfile.mkstemp()
try:
    os.write(fd, b"data")
finally:
    os.close(fd)
    os.unlink(path)

# mkdtemp
d = tempfile.mkdtemp()
print(d)
shutil.rmtree(d)