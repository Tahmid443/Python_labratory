# 17. Databases and SQL with Python

A database is an organized collection of data. SQL (Structured Query Language) is used to create, retrieve, update, and delete data stored in relational databases.

Python provides the built-in `sqlite3` module for working with SQLite databases. SQLite is lightweight, stores data in a file or in memory, and does not require a separate database server.

## 📁 Project Structure

```text
17_Databases_and_SQL/
├── 01_sqlite_basics.py
├── 02_crud_operations.py
├── 03_parameterized_queries.py
└── 04_transactions.py
```

## 🎯 Learning Objectives

By completing this module, you should understand how to:

- Connect Python to a SQLite database.
- Create tables and define columns.
- Insert, retrieve, update, and delete records.
- Use cursors and execute SQL statements.
- Write parameterized queries to prevent SQL injection.
- Insert multiple records efficiently.
- Use transactions and roll back failed operations.
- Organize database operations inside a Python class.
- Handle database connections and errors responsibly.

---

## 1. SQLite Basics — `01_sqlite_basics.py`

### 1.1 Importing SQLite

Python includes the `sqlite3` module, so no additional package is required.

```python
import sqlite3
```

### 1.2 Connecting to a database

There are two common ways to create a SQLite connection.

**In-memory database:**

```python
conn = sqlite3.connect(":memory:")
```

This database exists only while the connection remains open. It is useful for examples and tests.

**File-based database:**

```python
conn = sqlite3.connect("app.db")
```

This creates or opens a database file named `app.db` in the current working directory.

The file-based database persists after the program exits, whereas an in-memory database does not.

### 1.3 Creating a cursor

A cursor executes SQL statements and can retrieve query results.

```python
cursor = conn.cursor()
```

You can also execute statements directly through the connection:

```python
conn.execute("SELECT 1")
```

Both approaches are useful; direct connection methods are convenient for simple queries.

### 1.4 Creating a table

```python
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")
```

Column definitions:

| Definition | Meaning |
|---|---|
| `id INTEGER PRIMARY KEY` | Defines the table's primary key |
| `AUTOINCREMENT` | Prevents reuse of previously assigned row IDs under SQLite's AUTOINCREMENT rules |
| `name TEXT NOT NULL` | Name must not be `NULL` |
| `age INTEGER` | Stores an integer value when supplied |
| `email TEXT UNIQUE` | Prevents duplicate non-`NULL` email values |

`AUTOINCREMENT` is not necessary for most tables. An `INTEGER PRIMARY KEY` already automatically assigns a row ID when one is omitted.

### 1.5 Inserting records

```python
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("Alice", 30, "alice@example.com")
)

cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("Bob", 25, "bob@example.com")
)

conn.commit()
```

The `?` characters are parameter placeholders. The values are passed separately from the SQL statement.

`commit()` saves the changes to the database transaction.

### 1.6 Retrieving records

```python
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)
```

`fetchall()` returns all remaining query results as a list of rows.

You can retrieve only selected columns:

```python
cursor.execute("SELECT name, age FROM users")

for row in cursor.fetchall():
    print(row)
```

Useful retrieval methods:

| Method | Purpose |
|---|---|
| `fetchone()` | Returns the next row, or `None` if there are no more rows |
| `fetchmany(n)` | Retrieves up to `n` rows |
| `fetchall()` | Retrieves all remaining rows |

For large result sets, iterate over the cursor instead of loading every row into memory at once.

### 1.7 Getting column names

```python
cursor.execute("SELECT name, age FROM users")

column_names = [description[0] for description in cursor.description]
print(column_names)
```

Output:

```text
['name', 'age']
```

`cursor.description` contains metadata about the query's result columns.

### 1.8 Returning dictionary-like rows

The default row representation is a tuple. SQLite also provides `sqlite3.Row`, which supports access by column name.

```python
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor:
    print(row["name"], row["age"])
```

Set `row_factory` before creating cursors whose results should use this row representation.

### 1.9 Closing the connection

```python
conn.close()
```

Closing the connection releases database resources.

**When should you use this file's concepts?**

- When learning basic SQL.
- When creating small local applications.
- When prototyping data storage.
- When writing tests that need an isolated database.
- When learning how Python communicates with relational databases.

---

## 2. CRUD Operations — `02_crud_operations.py`

CRUD stands for:

- **C** — Create
- **R** — Read
- **U** — Update
- **D** — Delete

These four operations form the foundation of many database applications.

### 2.1 Creating a database class

Your `UserDB` class groups database operations into a single reusable object.

```python
import sqlite3


class UserDB:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._create()
```

The constructor:

1. Opens the database connection.
2. Configures row results.
3. Creates the table if it does not already exist.

The `path` argument lets you choose between an in-memory database and a persistent database file.

### 2.2 Creating a table

```python
def _create(self):
    self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """)
    self.conn.commit()
```

`CREATE TABLE IF NOT EXISTS` avoids an error if the table already exists.

The underscore in `_create()` is a Python naming convention indicating that the method is intended for internal use.

### 2.3 Create — Insert a record

```python
def create(self, name, email, age=None):
    cur = self.conn.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (name, email, age)
    )
    self.conn.commit()
    return cur.lastrowid
```

Example:

```python
db = UserDB()

uid = db.create("Alice", "alice@example.com", 30)
print(uid)
```

`lastrowid` provides the row ID associated with the most recent successful insert performed by that cursor.

### 2.4 Read — Retrieve records

```python
def read(self, user_id=None):
    if user_id is not None:
        cur = self.conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        )
        return cur.fetchone()

    return self.conn.execute(
        "SELECT * FROM users"
    ).fetchall()
```

Usage:

```python
print(db.read(uid)["name"])
print(db.read())
```

When an ID is supplied, the method returns one row or `None`. Without an ID, it returns a list of rows.

Using `user_id is not None` is more precise than `if user_id`, because it checks explicitly whether the argument was omitted.

### 2.5 Update — Modify a record

```python
def update(self, user_id, **fields):
    if not fields:
        return

    allowed_fields = {"name", "email", "age"}

    if not fields.keys() <= allowed_fields:
        raise ValueError("Unsupported field")

    sets = ", ".join(f"{key} = ?" for key in fields)
    values = list(fields.values()) + [user_id]

    self.conn.execute(
        f"UPDATE users SET {sets} WHERE id = ?",
        values
    )
    self.conn.commit()
```

Example:

```python
db.update(uid, name="Alicia", age=31)
```

Here, `**fields` collects keyword arguments into a dictionary.

The query might become:

```sql
UPDATE users SET name = ?, age = ? WHERE id = ?
```

**Important security distinction:** SQL parameter placeholders protect values, but they cannot represent table or column identifiers. Because the column names are inserted into the SQL string, validate them against an explicit allowlist, as shown above.

### 2.6 Delete — Remove a record

```python
def delete(self, user_id):
    self.conn.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    self.conn.commit()
```

Example:

```python
db.delete(uid)
```

The record with the matching ID is deleted.

A delete operation should use an appropriate `WHERE` condition. Omitting it from a `DELETE` statement can remove every row in the table.

### 2.7 Closing the database

```python
def close(self):
    self.conn.close()
```

Always close database connections when they are no longer needed.

For more complex applications, you can also implement `__enter__()` and `__exit__()` to manage the connection through a context manager.

### 2.8 CRUD summary

| Operation | SQL command | Example purpose |
|---|---|---|
| Create | `INSERT` | Add a user |
| Read | `SELECT` | Find a user |
| Update | `UPDATE` | Change a user's age |
| Delete | `DELETE` | Remove a user |

### Mini exercise

Extend `UserDB` with:

1. `count()` — return the number of users.
2. `find_by_email(email)` — find a user by email.
3. `list_by_age(min_age)` — retrieve users whose age meets a minimum.
4. `clear()` — delete all records from the table.

Use parameterized queries for every supplied value.

---

## 3. Parameterized Queries — `03_parameterized_queries.py`

Parameterized queries are one of the most important database security practices.

They separate SQL instructions from user-supplied data, helping prevent SQL injection.

### 3.1 The unsafe approach

```python
def unsafe_search(name):
    sql = f"SELECT * FROM items WHERE name = '{name}'"
    return conn.execute(sql).fetchall()
```

This uses an f-string to place the supplied value directly into the SQL statement.

An attacker could supply a value that changes the meaning of the query.

For example:

```python
evil = "apple' OR '1'='1"
```

Depending on the constructed SQL, this can make the condition true for every row.

### 3.2 The safe approach

```python
def safe_search(name):
    return conn.execute(
        "SELECT * FROM items WHERE name = ?",
        (name,)
    ).fetchall()
```

The SQL structure and the supplied value are passed separately.

```python
safe_search("apple")
safe_search("apple' OR '1'='1")
```

The second value is treated as ordinary data, not executable SQL.

**Rule:** Never build SQL value conditions by concatenating or interpolating untrusted input. Use placeholders and parameter binding.

### 3.3 Inserting multiple records

```python
items = [
    (1, "apple", 1.0),
    (2, "banana", 0.5),
    (3, "cherry", 3.0),
]

conn.executemany(
    "INSERT INTO items VALUES (?, ?, ?)",
    items
)

conn.commit()
```

`executemany()` executes a statement repeatedly for a sequence of parameter sets. It is often convenient and efficient for batch inserts.

### 3.4 Named parameters

Instead of positional `?` placeholders, you can use named placeholders.

```python
conn.execute(
    "INSERT INTO items VALUES (:id, :name, :price)",
    {"id": 4, "name": "date", "price": 2.5}
)
```

Named parameters can improve readability when a query contains several values.

### 3.5 Querying with conditions

```python
rows = conn.execute(
    "SELECT * FROM items WHERE price > ?",
    (1.0,)
).fetchall()
```

This retrieves records with prices greater than `1.0`.

Remember that a one-element tuple requires a trailing comma:

```python
(1.0,)
```

Without the comma, `(1.0)` is simply a number enclosed in parentheses.

### 3.6 What if the query needs a dynamic column?

Placeholders are for values, not SQL identifiers.

This does not work as a way to choose a column:

```python
# Incorrect approach for selecting a column dynamically:
# conn.execute("SELECT ? FROM items", ("name",))
```

Instead, choose identifiers from an allowlist:

```python
allowed_columns = {"id", "name", "price"}

def get_sorted_items(column):
    if column not in allowed_columns:
        raise ValueError("Invalid column")

    sql = f"SELECT * FROM items ORDER BY {column}"
    return conn.execute(sql).fetchall()
```

The interpolated identifier is safe here because it must match one of the predefined column names. Any actual data values should still be parameterized.

### Common SQL injection mistakes

- Using f-strings to insert user values into SQL.
- Concatenating strings to build conditions.
- Assuming placeholders can replace table names or column names.
- Treating escaping alone as a substitute for parameterized queries.

---

## 4. Transactions — `04_transactions.py`

A transaction is a group of database operations that should succeed or fail together.

For example, transferring money between accounts involves two operations:

1. Subtract money from the sender.
2. Add money to the recipient.

If only one operation succeeds, the balances become inconsistent.

Transactions help prevent this.

### 4.1 Creating account records

```python
import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute("""
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        balance REAL
    )
""")

conn.executemany(
    "INSERT INTO accounts VALUES (?, ?)",
    [(1, 1000), (2, 500)]
)

conn.commit()
```

### 4.2 Starting a transaction

Your original function begins explicitly:

```python
conn.execute("BEGIN")
```

Operations performed within the transaction can be committed together or rolled back.

### 4.3 Committing changes

```python
conn.commit()
```

`commit()` makes the transaction's changes permanent.

### 4.4 Rolling back changes

```python
conn.rollback()
```

`rollback()` cancels uncommitted changes in the current transaction.

### 4.5 Implementing a safer transfer

The following version validates the amount and checks that both accounts exist before completing the transfer.

```python
def transfer(conn, from_id, to_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if from_id == to_id:
        raise ValueError("Accounts must be different")

    try:
        conn.execute("BEGIN")

        sender = conn.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (from_id,)
        ).fetchone()

        recipient = conn.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (to_id,)
        ).fetchone()

        if sender is None or recipient is None:
            raise ValueError("Account not found")

        if sender[0] < amount:
            raise ValueError("Insufficient funds")

        conn.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )

        conn.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise
```

The exception is re-raised after rollback so that the caller can decide how to report or handle the failure.

This is usually better than printing an error inside the database function and silently returning.

**Production note:** Real financial systems need stronger design considerations, including appropriate constraints, concurrency handling, audit records, and integer-based monetary units or a suitable decimal representation. The example illustrates transaction basics, not a complete banking implementation.

### 4.6 Using a connection as a context manager

SQLite connections support the `with` statement:

```python
with conn:
    conn.execute(
        "UPDATE accounts SET balance = 0 WHERE id = ?",
        (1,)
    )
```

The context manager commits an open transaction on successful exit or rolls it back if an exception occurs.

However, `with conn:` does **not** close the connection. Close it separately when finished:

```python
conn.close()
```

### 4.7 Transaction workflow

<escape>1.</escape> Begin a transaction when needed.

<escape>2.</escape> Execute related database operations.

<escape>3.</escape> Validate the result.

<escape>4.</escape> Commit if everything succeeds.

<escape>5.</escape> Roll back if an operation fails.

This workflow protects consistency by preventing partial changes from being committed.

---

## 5. Common Mistakes and Best Practices

### Mistake 1: Forgetting to commit

Inserting or updating data without committing may leave the changes uncommitted.

**Solution:** Use `commit()` at the appropriate transaction boundary or use a connection context manager.

### Mistake 2: Using unsafe SQL interpolation

```python
# Unsafe:
sql = f"SELECT * FROM users WHERE name = '{name}'"
```

**Solution:** Bind values using `?` or named placeholders.

### Mistake 3: Forgetting the tuple comma

```python
# Wrong: not a one-element tuple
("Alice")

# Correct:
("Alice",)
```

### Mistake 4: Forgetting to close the connection

An unclosed connection can keep resources occupied longer than necessary.

**Solution:** Close connections reliably, including when exceptions occur.

### Mistake 5: Building unrestricted dynamic SQL

Parameter binding cannot protect interpolated table or column identifiers.

**Solution:** Use allowlists for any dynamic SQL identifiers.

### Mistake 6: Updating without validating fields

Allowing arbitrary keyword names into an `UPDATE` statement can produce invalid SQL or introduce injection vulnerabilities.

**Solution:** Restrict field names to a predefined set and bind the values.

### Mistake 7: Assuming a context manager closes SQLite

`with conn:` handles transaction completion, not connection closure.

**Solution:** Close the connection separately or use a carefully designed connection-management wrapper.

### Mistake 8: Catching every exception and hiding it

Silently swallowing exceptions makes database failures difficult to diagnose.

**Solution:** Roll back when necessary, then propagate or appropriately handle the error.

---

## 6. Practice Checklist

### SQLite basics

- [ ] Connect to an in-memory database.
- [ ] Create a table with a primary key.
- [ ] Insert and retrieve records.
- [ ] Read rows by column name using `sqlite3.Row`.
- [ ] Close the database connection.

### CRUD operations

- [ ] Implement `create()`.
- [ ] Implement `read()` for one record and all records.
- [ ] Implement `update()` with a field allowlist.
- [ ] Implement `delete()`.
- [ ] Handle missing IDs and duplicate emails.

### Query safety

- [ ] Use positional parameters.
- [ ] Use named parameters.
- [ ] Insert multiple records with `executemany()`.
- [ ] Explain why SQL f-strings are dangerous for untrusted values.
- [ ] Safely handle dynamic column selection.

### Transactions

- [ ] Commit successful changes.
- [ ] Roll back failed operations.
- [ ] Transfer funds between two accounts.
- [ ] Reject invalid transfer amounts.
- [ ] Check that balances remain unchanged after a failed transfer.

---

## 7. Mini Project — Student Management System

Build a small student database with SQLite.

### Requirements

Create a `students` table with:

- `id` — primary key.
- `name` — required text.
- `age` — integer.
- `grade` — numeric value.

Implement the following operations:

1. Add a student.
2. Display all students.
3. Find a student by ID.
4. Update a student's grade.
5. Delete a student.
6. Find students whose grades exceed a given value.
7. Insert several students with `executemany()`.
8. Use parameterized queries for every supplied value.
9. Handle duplicate or missing records appropriately.
10. Close the connection after use.

### Starter code

```python
import sqlite3


class StudentDB:
    def __init__(self, path="students.db"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade REAL
            )
        """)

        self.conn.commit()

    def add_student(self, name, age, grade):
        cur = self.conn.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade)
        )
        self.conn.commit()
        return cur.lastrowid

    def get_students(self):
        return self.conn.execute(
            "SELECT * FROM students ORDER BY id"
        ).fetchall()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = StudentDB()

    db.add_student("Alice", 20, 90.5)
    db.add_student("Bob", 21, 85.0)

    for student in db.get_students():
        print(dict(student))

    db.close()
```

### Extra challenges

- Add validation for student age and grade.
- Add a search function by student name.
- Sort students by grade in descending order.
- Add a transaction for updating multiple students.
- Write automated tests using `pytest` and an in-memory database.

---

## 8. Suggested Learning Order

1. Learn SQL basics: `CREATE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.
2. Understand connections, cursors, and row results.
3. Practice CRUD operations through a Python class.
4. Master parameterized queries and SQL injection prevention.
5. Learn transactions, commits, and rollbacks.
6. Build the student management project.
7. Add automated tests and handle database errors.

## Final Takeaway

SQLite is a practical starting point for learning relational databases in Python.

The most important habits are:

- Use parameterized queries for supplied values.
- Validate dynamic SQL identifiers.
- Commit related operations at appropriate transaction boundaries.
- Roll back failed transactions.
- Close connections when they are no longer needed.
- Test both successful operations and failure cases.

These fundamentals provide a strong foundation for larger database-backed applications and for learning other SQL databases later.