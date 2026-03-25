import re

# standalone functions for input validation using regex

def check_username(username):
    # username must be 3 to 20 characters, only letters numbers and underscore
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Username must be 3-20 chars. Only letters, numbers, underscore allowed.")

def check_email(email):
    # basic email format check
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,6}$', email):
        raise ValueError("Enter a valid email like abc@gmail.com")

def check_password(password):
    # password must be atleast 6 chars and have one number
    if len(password) < 6:
        raise ValueError("Password must be atleast 6 characters.")
    if not re.search(r'[0-9]', password):
        raise ValueError("Password must have atleast one number.")

def check_answer(answer):
    # answer must be A B C or D only
    if not re.match(r'^[AaBbCcDd]$', answer):
        raise ValueError("Please enter only A, B, C or D.")
