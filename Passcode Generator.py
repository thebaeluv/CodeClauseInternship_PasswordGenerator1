import random
import string


def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    """
    Generates a secure password based on user-specified requirements.

    Args:
        length (int): The desired length of the password (default: 12).
        include_uppercase (bool): Whether to include uppercase letters (default: True).
        include_lowercase (bool): Whether to include lowercase letters (default: True).
        include_digits (bool): Whether to include digits (default: True).
        include_symbols (bool): Whether to include symbols (default: True).

    Returns:
        str: The generated secure password.
    """
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter the desired password length (default: 12): ") or 12)
    include_uppercase = input("Include uppercase letters? (y/n, default: y): ").lower() != 'n'
    include_lowercase = input("Include lowercase letters? (y/n, default: y): ").lower() != 'n'
    include_digits = input("Include digits? (y/n, default: y): ").lower() != 'n'
    include_symbols = input("Include symbols? (y/n, default: y): ").lower() != 'n'

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
    if password:
        print(f"Your secure password is: {password}")
