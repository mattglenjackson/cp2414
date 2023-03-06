import random
import string
import hashlib
import re


def main():
    choice = menu()
    while choice != "Q":
        # if choice == 1:
        #     password = generate_password()
        #     print(password)

        if choice == 1:
            password = str(input("Enter password: "))
            while not is_valid_password(password):
                password = str(input("Enter password: "))
            menu()

        elif choice == 2:
            password = str(input("Enter the password to verify"))
            verify_password(password)
            menu()

        else:
            print("Invalid input")
            menu()

    hash_value = hash_value_generator(password)
    with open('hashed_password.txt', 'w') as f:
        f.write(hash_value)


def menu():
    print("To type a password press 1 \nTo verify password press 2")
    choice = int(input('>>> '))
    return choice


def generate_password():
    # Define the length of the password
    min_length = 8
    max_length = 20

    # Define the types of characters to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits

    # Generate a list of characters to use in the password
    all_characters = (
            list(uppercase_letters) +
            list(lowercase_letters) +
            list(symbols) +
            list(numbers)
    )

    # Make sure there is at least one character from each category in the password
    password = (
            random.choice(uppercase_letters) +
            random.choice(lowercase_letters) +
            random.choice(symbols) +
            random.choice(numbers)
    )

    # Add additional random characters to the password
    password += ''.join(random.choice(all_characters) for _ in range(random.randint(min_length - 4, max_length - 4)))

    # Shuffle the characters in the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password


def is_valid_password(password):
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


def hash_value_generator(password):
    # number = random.randint(1, 100000000000000)

    salt = "123"
    with open('salt.txt', 'w') as f:
        f.write(salt)
    hash_password = password + salt
    # password = "James12matt@"

    hash_value = hashlib.md5(hash_password.encode()).hexdigest()

    print("Hash value:", hash_value)
    return hash_value


def verify_password(password):
    with open('salt.txt', 'r') as f:
        salt = f.read()
    password = password + salt
    hash_value = hashlib.md5(password.encode()).hexdigest()
    with open('hashed_password.txt', 'r') as f:
        hash_password = f.read()
    if hash_password == hash_value:
        print("Congrats, correct password")
    else:
        print("Incorrect password")


main()
