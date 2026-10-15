import sqlite3

# In-memory
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")

# Insert
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
               ("Alice", 30, "alice@example.com"))
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
               ("Bob", 25, "bob@example.com"))
conn.commit()

# Select
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Column names
cursor.execute("SELECT name, age FROM users")
print([d[0] for d in cursor.description])

# Row factory (dict-like)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor:
    print(row["name"], row["age"])

conn.close()