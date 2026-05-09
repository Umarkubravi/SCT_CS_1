def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose option: ")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == "2":
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice")