# Basic custom exception
class AppError(Exception):
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    pass

# Usage
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("age", "must be an integer")
    if age < 0:
        raise ValidationError("age", "must be non-negative")
    if age > 150:
        raise ValidationError("age", "seems unrealistic")
    return age

def find_user(users, uid):
    if uid not in users:
        raise NotFoundError(f"User {uid} not found")
    return users[uid]

# Testing
for age in [25, -1, "abc", 200]:
    try:
        validate_age(age)
        print(f"Valid: {age}")
    except ValidationError as e:
        print(f"Invalid: {e.field} -> {e.message}")

try:
    find_user({1: "Alice"}, 2)
except NotFoundError as e:
    print(e)