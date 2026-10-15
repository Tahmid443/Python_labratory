import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL)")
conn.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 1000), (2, 500)])
conn.commit()

def transfer(from_id, to_id, amount):
    try:
        conn.execute("BEGIN")
        # Withdraw
        conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?",
                     (amount, from_id))
        # Check balance
        row = conn.execute("SELECT balance FROM accounts WHERE id = ?",
                           (from_id,)).fetchone()
        if row[0] < 0:
            raise ValueError("Insufficient funds")
        # Deposit
        conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?",
                     (amount, to_id))
        conn.commit()
        print("Transfer successful")
    except Exception as e:
        conn.rollback()
        print(f"Rolled back: {e}")

def show():
    for row in conn.execute("SELECT * FROM accounts"):
        print(row)

show()
transfer(1, 2, 300)
show()
transfer(1, 2, 1000)   # should fail
show()

# Using connection as context manager
with conn:
    conn.execute("UPDATE accounts SET balance = 0 WHERE id = 1")

show()
conn.close()