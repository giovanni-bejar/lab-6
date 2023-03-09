def main():
    while True:
        print("\nChoose an option:")
        print("1. Encoder")
        print("2. Decoder")
        print("3. Exit\n")

        choice = input("Enter choice: ")

        if choice == "1":
            password = input("Enter an 8-digit password to encode: ")
            encoded_password = encode(password)
            print(f"Encoded password: {encoded_password}")
        elif choice == "2":
            encoded_password = input("Enter an encoded password to decode: ")
            password = decode(encoded_password)
            print(f"Decoded password: {password}")
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def encode(password): #Giovanni Bejar
    encoded_password = ""
    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)
    return encoded_password

def decode(encoded_password):


if __name__ == "__main__":
    main()
