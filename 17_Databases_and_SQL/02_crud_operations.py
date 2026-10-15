import sqlite3

class UserDB:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._create()

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

    def create(self, name, email, age=None):
        cur = self.conn.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        self.conn.commit()
        return cur.lastrowid

    def read(self, user_id=None):
        if user_id:
            cur = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cur.fetchone()
        return self.conn.execute("SELECT * FROM users").fetchall()

    def update(self, user_id, **fields):
        if not fields:
            return
        sets = ", ".join(f"{k} = ?" for k in fields)
        values = list(fields.values()) + [user_id]
        self.conn.execute(f"UPDATE users SET {sets} WHERE id = ?", values)
        self.conn.commit()

    def delete(self, user_id):
        self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = UserDB()
    uid1 = db.create("Alice", "a@x.com", 30)
    uid2 = db.create("Bob", "b@x.com", 25)

    print(db.read(uid1)["name"])
    print(len(db.read()))

    db.update(uid1, age=31, name="Alicia")
    print(db.read(uid1)["age"])

    db.delete(uid2)
    print(len(db.read()))

    db.close()