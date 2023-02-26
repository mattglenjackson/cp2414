import random
import string


def generate_password():
    # define possible characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # generate random password length between 8 and 20 characters
    password_length = random.randint(8, 20)

    # generate password using random characters
    password = ''.join(random.choice(chars) for _ in range(password_length))

    return password


password = generate_password()
print(password)
