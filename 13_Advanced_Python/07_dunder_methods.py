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

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return 2

    def __getitem__(self, idx):
        return (self.x, self.y)[idx]

    def __iter__(self):
        yield self.x
        yield self.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):
        return bool(self.x or self.y)

    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)

    def __contains__(self, val):
        return val in (self.x, self.y)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def __format__(self, spec):
        return f"Vector({self.x:{spec}}, {self.y:{spec}})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(repr(v1), str(v1))
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)    # dot product
print(v1 * 3)
print(3 * v1)     # __rmul__
print(v1 == Vector(1, 2))
print(v1 < v2)
print(len(v1))
print(v1[0], v1[1])
print(list(v1))
print(abs(v1))
print(bool(Vector(0, 0)))
print(v1(2))
print(1 in v1)
print(f"{v1:.2f}")
print({v1, v2})