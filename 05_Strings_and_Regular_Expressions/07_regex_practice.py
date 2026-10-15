import re

# Email validation
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Phone (US)
def is_valid_phone(phone):
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone))

# URL
def is_valid_url(url):
    pattern = r"^https?://[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#\[\]@!$&'()*+,;=]*$"
    return bool(re.match(pattern, url))

# Password strength
def password_strength(pw):
    checks = {
        "length": len(pw) >= 8,
        "upper":  bool(re.search(r"[A-Z]", pw)),
        "lower":  bool(re.search(r"[a-z]", pw)),
        "digit":  bool(re.search(r"\d", pw)),
        "special": bool(re.search(r"[!@#$%^&*]", pw)),
    }
    return checks

# Extract data
def extract_dates(text):
    return re.findall(r"\d{4}-\d{2}-\d{2}", text)

def extract_hashtags(text):
    return re.findall(r"#(\w+)", text)

def extract_urls(text):
    return re.findall(r"https?://\S+", text)

# Clean whitespace
def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()

if __name__ == "__main__":
    print(is_valid_email("alice@example.com"))
    print(is_valid_email("bad-email"))
    print(is_valid_phone("(123) 456-7890"))
    print(is_valid_phone("1234567890"))
    print(is_valid_url("https://example.com/path"))
    print(password_strength("Abc123!@#"))
    print(extract_dates("2024-01-01 and 2025-12-31"))
    print(extract_hashtags("#python #dsa"))
    print(extract_urls("Visit https://a.com and http://b.org"))
    print(normalize_whitespace("  too   much   space  "))