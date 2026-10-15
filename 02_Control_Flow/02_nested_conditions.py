def classify_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    return "Not a triangle"

def login(username, password, is_admin=False):
    if username and password:
        if len(password) >= 8:
            if is_admin:
                return "Admin access granted"
            return "User access granted"
        return "Password too short"
    return "Missing credentials"

if __name__ == "__main__":
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(3, 3, 4))
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(1, 1, 3))
    print(login("alice", "secure123"))
    print(login("admin", "secure123", is_admin=True))