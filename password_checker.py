import re


def password_checker(password):
    # Check length
    if len(password) < 8 and len(password) <= 20:
        print("password length must be between 8 and 20 characters long")
        return False
    # Check uppercase
    if not re.search(r'[A-Z]', password):
        print("password must contain uppercase characters")
        return False
    # Check lowercase
    if not re.search(r'[a-z]', password):
        print("password must contain lowercase characters")
        return False
    # Check digit
    if not re.search(r'\d', password):
        print("password must contain at least one digit")
        return False
    # Check symbol
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("password must contain at least one symbol '!@#$%^&*(),.?' etc")
        return False
    return True


def main():
    password = input("Password: ")
    password_checker(password)


main()
