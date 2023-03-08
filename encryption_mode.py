import re


def main():
    print("(C)reate new account\n(L)og-in account\n(Q)uit")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            valid_username = get_valid_username()
            valid_password = get_valid_password()
            caesar_cipher = encrypt_pass(valid_password)
            save_to_file(valid_username, caesar_cipher)
        elif choice == "L":
            verify_account()

        else:
            print("Incorrect choice!")

        print("(C)reate new account\n(L)og-in account\n(Q)uit")
        choice = input(">>>").upper()
    print("Thank you for using encryption mode! Have a good encrypted day!")


def encrypt_pass(valid_password):
    encryption = []
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>?,./"
    char_parts = [char for char in characters]
    for char in valid_password:
        char_index = int(char_parts.index(char.upper()))
        if char_index > 52:
            encryption.append(char_parts[char_parts.index(char.upper()) + 3])
        else:
            encryption.append(char_parts[(char_parts.index(char.upper()) + 3) - 52])
    encrypted_pass = "".join(encryption)
    return encrypted_pass


def get_valid_username():
    username = input("Username: ")
    print(username)
    return username


def get_valid_password():
    # Check length
    password = str(input("Password: "))
    is_valid = False
    while not is_valid:
        if len(password) < 8 and len(password) <= 20:
            print("password length must be between 8 and 20 characters long")
            password = str(input("Password: "))
        # Check uppercase
        if not re.search(r'[A-Z]', password):
            print("password must contain uppercase characters")
            password = str(input("Password: "))
        # Check lowercase
        if not re.search(r'[a-z]', password):
            print("password must contain lowercase characters")
            password = str(input("Password: "))
        # Check digit
        if not re.search(r'\d', password):
            print("password must contain at least one digit")
            password = str(input("Password: "))
        # Check symbol
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("password must contain at least one symbol '!@#$%^&*(),.?' etc")
            password = str(input("Password: "))
        else:
            is_valid = True
    return password


def save_to_file(valid_username, encrypted_password):
    with open('username_file.txt', 'w') as f:
        f.write(valid_username)
    with open('encrypted_password.txt', 'w') as f:
        f.write(encrypted_password)
    print("Account Created!")
    return valid_username, encrypted_password


def verify_account():
    with open('username_file.txt', 'r') as f:
        saved_username = f.read()
    with open('encrypted_password.txt', 'r') as f:
        saved_password = f.read()
    is_valid = False
    while not is_valid:
        login_username = input("Username: ")
        login_password = input("Password: ")
        verified_encryption = encrypt_pass(login_password)
        if login_username != saved_username:
            print("Invalid username!")
        elif saved_password != verified_encryption:
            print("Invalid password!")
        else:
            is_valid = True
    print("Account verified!")


main()
