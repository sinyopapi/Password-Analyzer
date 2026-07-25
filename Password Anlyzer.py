import string
MIN_LENGTH = 8

def check_char(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbols = False

    for letters in password:
        if letters.islower():
            has_lower = True
        if letters.isupper():
            has_upper = True
        if letters.isdigit():
            has_digit = True
        if letters in string.punctuation:
            has_symbols = True

    return has_upper, has_lower, has_digit, has_symbols

def check_password(password):
    score = 0
    length = len(password)
    strength = ""

    has_upper, has_lower, has_digit, has_symbols = check_char(password)

    checks = [
        length >= MIN_LENGTH,
        has_upper,
        has_lower,
        has_digit,
        has_symbols
    ]

    for check in checks:
        if check:
            score += 20

    if score <= 20:
        strength = "Weak"
    elif score <= 60:
        strength = "Fairly Weak"
    elif score <= 80:
        strength = "Good"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "length": length,
        "uppercase": has_upper,
        "lowercase": has_lower,
        "digit": has_digit,
        "symbol": has_symbols
    }

def show_report(result):

    score = result["score"]
    strength = result["strength"]
    length = result["length"]
    has_upper = result["uppercase"]
    has_lower = result["lowercase"]
    has_digit = result["digit"]
    has_symbols = result["symbol"]

    print("=" * 20)
    print("PASSWORD ANALYZER")
    print("=" * 20)

    checks = [
        ("Length (>= 8)", length >= MIN_LENGTH),
        ("Uppercase", has_upper),
        ("Lowercase", has_lower),
        ("Digit", has_digit),
        ("Symbols", has_symbols)
    ]

    for name, passed in checks:
        if passed:
            print(f"✅ {name}")
        else:
            print(f"❌ {name}")

    print(f"Password length: {length}")
    print(f"Score: {score}/100")
    print(f"Strength: {strength}")

while True:
    password = input("Enter password: ")

    result = check_password(password)

    show_report(result)