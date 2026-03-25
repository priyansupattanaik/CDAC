import re


def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    if not re.match(pattern, username):
        raise ValueError("Username must be 3-20 characters. Only letters, numbers and underscore allowed.")
    return True


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,6}$'
    if not re.match(pattern, email):
        raise ValueError("Please enter a valid email address (example: abc@gmail.com)")
    return True


def validate_password(password):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    if not re.search(r'[0-9]', password):
        raise ValueError("Password must have at least one number in it.")
    return True


def validate_answer(answer):
    pattern = r'^[AaBbCcDd]$'
    if not re.match(pattern, answer):
        raise ValueError("Please enter only A, B, C or D.")
    return True
