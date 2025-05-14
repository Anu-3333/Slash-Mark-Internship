import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password should be at least 6 characters long.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator!")
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is:\n{password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
