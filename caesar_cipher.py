# Caesar Cipher implementation

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice! Please select 'e' or 'd'.")

if __name__ == "__main__":
    main()
