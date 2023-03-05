import hashlib
import os

def generate_salt_and_hash(password):
    """Generate a random salt and hash the given password using the salt."""
    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password using SHA256 algorithm and the salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()

    # Return the salt and hashed password as a tuple
    return (salt, hashed_password)

def verify_password(password, salt, hashed_password):
    """Verify the given password using the given salt and hashed password."""
    # Hash the entered password using the same salt and algorithm
    hashed_password_to_check = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()

    # Compare the hashes and return the result
    return hashed_password == hashed_password_to_check

# Get password from user
password = input("Enter your password: ")

# Generate a random salt and hash the password
salt, hashed_password = generate_salt_and_hash(password)

# Save the salt and hashed password to files
with open('salt.txt', 'wb') as f:
    f.write(salt)

with open('hashed_password.txt', 'w') as f:
    f.write(hashed_password)

# Print a message to confirm that the salt and hashed password have been saved
print("Salt and hashed password saved to files.")

# Verify the password
password_to_check = input("Enter the password again to verify: ")

# Load the salt and hashed password from files
with open('salt.txt', 'rb') as f:
    salt = f.read()

with open('hashed_password.txt', 'r') as f:
    hashed_password = f.read()

# Verify the entered password using the loaded salt and hashed password
if verify_password(password_to_check, salt, hashed_password):
    print("Password verified!")
else:
    print("Password verification failed.")
