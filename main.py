import random
import string
import hashlib
import re


def main():
    output = int(input("To generate a password press 1, or to type a password press 2: "))
    if output == 1:
        password = generate_password()
        print(password)
    elif output == 2:
        password = str(input("Enter password: "))
        length, has_uppercase, has_lowercase, has_number, has_symbol = check_string(password)
        if 8 <= length <= 20:
            print("Length is fine")
        else:
            password = str(input("Enter password with 8-20 characters: "))
        if (has_uppercase, has_lowercase, has_number, has_symbol) == True:
            print(f"String length: {length}")
            print(f"Contains uppercase: {has_uppercase}")
            print(f"Contains lowercase: {has_lowercase}")
            print(f"Contains number: {has_number}")
            print(f"Contains symbol: {has_symbol}")
        else:
            # while (has_uppercase, has_lowercase, has_number, has_symbol) == False:
            password = str(input("Enter password uppercase, lowercase number and symbols: "))

    else:
        print("Invalid input")

    length, has_uppercase, has_lowercase, has_number, has_symbol = check_string(password)
    print(f"String length: {length}")
    print(f"Contains uppercase: {has_uppercase}")
    print(f"Contains lowercase: {has_lowercase}")
    print(f"Contains number: {has_number}")
    print(f"Contains symbol: {has_symbol}")

    hash_value = hash_value_generator(password)
    print("Hash value:", hash_value)


def generate_password():
    # define possible characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # generate random password length between 8 and 20 characters
    password_length = random.randint(8, 20)

    # generate password using random characters
    password = ''.join(random.choice(chars) for _ in range(password_length))

    return password


def check_string(password):
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    return length, has_uppercase, has_lowercase, has_number, has_symbol


def hash_value_generator(password):
    # number = random.randint(1, 100000000000000)

    salt = "123"
    hash_password = password + salt
    # password = "James12matt@"

    hash_value = hashlib.md5(password.encode()).hexdigest()

    final_hash = hash_value
    return final_hash


main()
