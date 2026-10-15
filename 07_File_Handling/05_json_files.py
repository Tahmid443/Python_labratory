import json
import os

FILENAME = "data.json"

# Python -> JSON
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"],
    "address": {"city": "NYC", "zip": "10001"},
}

with open(FILENAME, "w") as f:
    json.dump(data, f, indent=2)

# JSON -> Python
with open(FILENAME) as f:
    loaded = json.load(f)
print(loaded["name"])
print(loaded["hobbies"])

# String conversions
json_str = json.dumps(data)
print(json_str)

parsed = json.loads(json_str)
print(parsed["address"]["city"])

# Pretty print
print(json.dumps(data, indent=2, sort_keys=True))

# Handle non-serializable
from datetime import datetime
try:
    json.dumps({"now": datetime.now()})
except TypeError as e:
    print(f"Error: {e}")

def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError

print(json.dumps({"now": datetime.now()}, default=default_handler))

os.remove(FILENAME)