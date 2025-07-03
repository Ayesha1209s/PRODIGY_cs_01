
#Q1
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption Tool !")
    while True:
        choice = input("\nDo you want to E = Encrypt, D = Decrypt or Q = Quit? (Use capital letter to enter your choice) ").upper()

        if choice == 'Q':
            print("Exiting...")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                if not (0 <= shift <= 25):
                    print("Shift must be between 0 and 25.")
                    continue
            except ValueError:
                print("Invalid shift. Please enter a number.")
                continue

            if choice == 'E':
                encrypted = encrypt(message, shift)
                print("Encrypted message:", encrypted)
            else:
                decrypted = decrypt(message, shift)
                print("Decrypted message:", decrypted)
        else:
            print("Invalid choice. Please select E, D, or Q.")

if __name__ == "__main__":
    main()
