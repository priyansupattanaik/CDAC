import re

def validate_username(username):
    # Username must be 3-20 characters, letters and numbers only
    pattern = r"^[a-zA-Z0-9]{3,20}$"
    try:
        if re.match(pattern, username):
            return True
        return False
    except Exception as e:
        print(f"Regex validation error: {e}")
        return False

def validate_email(email):
    # Standard email validation regex
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    try:
        if re.match(pattern, email):
            return True
        return False
    except Exception as e:
        print(f"Regex validation error: {e}")
        return False

def validate_password(password):
    if len(password) > 0:
        return True
    return False

def validate_answer(answer_str):
    # Answer must be exactly one digit from 1 to 4
    pattern = r"^[1-4]$"
    try:
        if re.match(pattern, answer_str.strip()):
            return True
        return False
    except Exception as e:
        print(f"Regex validation error: {e}")
        return False
