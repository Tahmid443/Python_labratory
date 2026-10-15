import subprocess

# Run command
result = subprocess.run(
    ["python", "-c", "print('hello')"],
    capture_output=True,
    text=True,
    check=False,
)
print(result.stdout)
print(result.returncode)

# With shell
r = subprocess.run("echo hello", shell=True, capture_output=True, text=True)
print(r.stdout)

# Environment
env = {"MY_VAR": "1", **__import__("os").environ}
subprocess.run(["env"], env=env)

# Check errors
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error code: {e.returncode}")

# Popen (streaming)
proc = subprocess.Popen(
    ["python", "-c", "print('a'); print('b')"],
    stdout=subprocess.PIPE,
    text=True,
)
out, _ = proc.communicate()
print(out)

# Pipe commands
p1 = subprocess.Popen(["echo", "hello"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["wc", "-c"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()
out, _ = p2.communicate()
print(f"bytes: {out.strip()}")

# Timeout
try:
    subprocess.run(["sleep", "5"], timeout=1)
except subprocess.TimeoutExpired:
    print("Timed out")