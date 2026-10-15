import csv
import os

FILENAME = "data.csv"

# Write
with open(FILENAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 30, "NYC"])
    writer.writerow(["Bob", 25, "LA"])

# Read
with open(FILENAME) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader
with open(FILENAME) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# DictWriter
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows([
        {"name": "Charlie", "age": 35},
        {"name": "Dana", "age": 28},
    ])

with open("out.csv") as f:
    print(f.read())

os.remove(FILENAME)
os.remove("out.csv")