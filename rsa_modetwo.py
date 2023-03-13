import rsa


def main():
    print("(C)reate new account\n(L)og-in account\n(Q)uit")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            valid_username = get_valid_username()
            valid_password = get_valid_password()
            (public_key, private_key) = generate_rsa_keys()
            encrypted_pass = encrypt_pass(valid_password, public_key)
            save_to_file(valid_username, encrypted_pass, private_key, public_key)
        elif choice == "L":
            verify_account()

        else:
            print("Incorrect choice!")

        print("(C)reate new account\n(L)og-in account\n(Q)uit")
        choice = input(">>>").upper()
    print("Thank you for using encryption mode! Have a good encrypted day!")


def generate_rsa_keys():
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key


def encrypt_pass(valid_password, public_key):
    encrypted_pass = rsa.encrypt(valid_password.encode(), public_key)
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
        if not any(c.isupper() for c in password):
            print("password must contain uppercase characters")
            password = str(input("Password: "))
        # Check lowercase
        if not any(c.islower() for c in password):
            print("password must contain lowercase characters")
            password = str(input("Password: "))
        # Check digit
        if not any(c.isdigit() for c in password):
            print("password must contain at least one digit")
            password = str(input("Password: "))
        # Check symbol
        if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
            print("password must contain at least one symbol '!@#$%^&*(),.?' etc")
            password = str(input("Password: "))
        else:
            is_valid = True
    return password


def save_to_file(valid_username, encrypted_password, private_key, public_key):
    with open(f'{valid_username}_private_key.txt', 'w') as f:
        f.write(private_key.save_pkcs1().decode())
    with open(f'{valid_username}_public_key.txt', 'w') as f:
        f.write(public_key.save_pkcs1().decode())
    with open(f'{valid_username}_encrypted_password.txt', 'w') as f:
        f.write(str(encrypted_password))
    print("Account Created!")
    return valid_username, encrypted_password


def verify_account():
    username = input("Username: ")
    private_key = rsa.PrivateKey.load_pkcs1(open(f'{username}_private_key.txt', 'rb').read())
    encrypted_password = open(f'{username}_encrypted_password.txt', 'r').read()
    is_valid = False
    while not is_valid:
        login_password = input("Password: ")
        decrypted_password = rsa.decrypt(encrypted_password, private_key).decode()
        if login_password != decrypted_password:
            print("Invalid password!")
        else:
            is_valid = True
    print("Account verified!")


main()
