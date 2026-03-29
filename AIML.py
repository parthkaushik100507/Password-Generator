import string
import random

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    required = include_uppercase + include_numbers + include_special
    if length < required:
        raise ValueError("Length is too short for the selected criteria.")

    password = ""

    # Guarantee at least one of each selected type
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    # Build character pool
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Fill remaining length
    for _ in range(length - len(password)):
        password += random.choice(characters)

    # Shuffle to avoid predictable pattern
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def check_strength(length, include_uppercase, include_numbers, include_special):
    score = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if include_uppercase: score += 1
    if include_numbers:   score += 1
    if include_special:   score += 1

    if score <= 2:   return "Weak 🔴"
    elif score <= 4: return "Medium 🟡"
    else:            return "Strong 🟢"


def save_password(label, password):
    with open("saved_passwords.txt", "a") as f:
        f.write(f"Label: {label} | Password: {password}\n")
    print("✅ Password saved to saved_passwords.txt")


def main():
    while True:
        print("\n🔐 Password Generator")
        print("-" * 30)

        # --- Get user inputs ---
        while True:
            try:
                length = int(input("Enter the length of the password: "))
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers   = input("Include numbers? (y/n): ").lower() == 'y'
        include_special   = input("Include special characters? (y/n): ").lower() == 'y'

        if not (include_uppercase or include_numbers or include_special):
            print("⚠️  Note: Generating with lowercase letters only.")

        # --- Generate password ---
        try:
            password = generate_password(length, include_uppercase, include_numbers, include_special)
            strength = check_strength(length, include_uppercase, include_numbers, include_special)

            print(f"\n✅ Generated Password : {password}")
            print(f"💪 Password Strength  : {strength}")

        except ValueError as e:
            print(f"❌ Error: {e}")
            continue

        # --- Save option ---
        save = input("\nDo you want to save this password? (y/n): ").lower()
        if save == 'y':
            label = input("Enter a label for this password (e.g. Gmail): ")
            save_password(label, password)

        # --- Repeat option ---
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Goodbye! Stay secure.")
            break


if __name__ == "__main__":
    main()