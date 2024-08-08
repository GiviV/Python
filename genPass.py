import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include an uppercase letter, a lowercase letter, a digit, and a symbol.")
    
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one of each required character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password with random characters
    password += random.choices(uppercase + lowercase + digits + symbols, k=length-4)
    
    # Shuffle the list to prevent predictable patterns
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Example usage
password_length = 12
password = generate_password(password_length)
print("Generated Password:", password)
