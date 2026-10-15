from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    def execute(self, sql):
        self.connect()
        return self.query(sql)

class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"
    def query(self, sql):
        return f"MySQL result: {sql}"

class Postgres(Database):
    def connect(self):
        return "Connected to Postgres"
    def query(self, sql):
        return f"Postgres result: {sql}"

# db = Database()  # TypeError: abstract

for db in [MySQL(), Postgres()]:
    print(db.execute("SELECT * FROM users"))

# Abstract properties
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    @property
    def area(self):
        return self.side ** 2

print(Square(5).area)