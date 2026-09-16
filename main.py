import random
import string

def generate_password():
    print("=== PyPassword Generator ===")
    
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Generate random selections using Python standard library strings
    password_chars = (
        [random.choice(string.ascii_letters) for _ in range(nr_letters)] +
        [random.choice(string.punctuation) for _ in range(nr_symbols)] +
        [random.choice(string.digits) for _ in range(nr_numbers)]
    )

    # Shuffle characters and join into a single string
    random.shuffle(password_chars)
    password = "".join(password_chars)

    print(f"\nYour generated password is: {password}\n")

if __name__ == "__main__":
    generate_password()