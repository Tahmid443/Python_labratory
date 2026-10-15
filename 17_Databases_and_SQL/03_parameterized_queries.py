import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price REAL)")

# NEVER do this - SQL injection risk!
def unsafe_search(name):
    sql = f"SELECT * FROM items WHERE name = '{name}'"
    return conn.execute(sql).fetchall()

# Use parameterized queries
def safe_search(name):
    return conn.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchall()

# Insert many
items = [(1, "apple", 1.0), (2, "banana", 0.5), (3, "cherry", 3.0)]
conn.executemany("INSERT INTO items VALUES (?, ?, ?)", items)
conn.commit()

# Show injection risk
evil = "apple' OR '1'='1"
print("Unsafe:", unsafe_search(evil))   # returns ALL rows!
print("Safe:  ", safe_search(evil))     # returns none

# Named parameters
conn.execute(
    "INSERT INTO items VALUES (:id, :name, :price)",
    {"id": 4, "name": "date", "price": 2.5}
)
print(conn.execute("SELECT * FROM items WHERE price > ?", (1.0,)).fetchall())

conn.close()