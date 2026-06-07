from argon2 import PasswordHasher
import secrets
import string

class password_builder:
    def generate_passphrase(word_count=4):
        words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "house", "ice", "jungle"]
        selected_words = [secrets.choice(words) for _ in range(word_count)]
        return "-".join(selected_words)
    def generate_random_password(length=16):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    htb_1 = "1) the passphase way"
    htb_2 = "2) the safest way for password"

    print(f"{htb_1}\n {htb_2}")
    while True:
        how_to_build = input("how to generate your password (1 or 2): ")
        if how_to_build == "1":
            get = generate_passphrase()
            break
        elif how_to_build == "2":
            get = generate_random_password()
            break
        else:
            print("ERROR: you have to choose one of them")

    ph = PasswordHasher()
    a = ph.hash(get)
    print(f"hashed is: {a}")
    print(f"real password is: {get}")

if __name__ == "__main__":
    password_builder