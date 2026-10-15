class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return 2

    def __getitem__(self, idx):
        return (self.x, self.y)[idx]

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 == Vector(1, 2))
print(len(v1))
print(v1[0], v1[1])
print(abs(v1))
print(bool(Vector(0, 0)))
print(v1(2))
print({v1, v2})   # hashable