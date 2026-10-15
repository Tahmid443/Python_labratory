def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Ternary
def is_adult(age):
    return "Adult" if age >= 18 else "Minor"

if __name__ == "__main__":
    for s in [95, 85, 75, 65, 55]:
        print(f"Score {s}: {grade(s)}")
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))
    print(is_adult(20))