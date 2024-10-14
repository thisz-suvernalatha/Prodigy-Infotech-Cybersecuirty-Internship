lowerCase_alphabet = "abcdefghijklmnopqrstuvwxyz"
upperCase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\n")
print("Welcome to the Caesar Cipher Tool")

while True:
    print("\n")
    print("Enter '1' to encrypt or '2' to decrypt")
    
    while True:
        choice = input("Enter your choice: ")
        if choice in ['1', '2']:
            break
        else:
            print("Invalid input. Please enter '1' or '2'.")

    text = input("Enter your text here: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == '1':
        encryptedText = ""
        for char in text:
            if char in lowerCase_alphabet:
                index = lowerCase_alphabet.index(char)
                shifted_char = (index + shift) % 26
                encryptedChar = lowerCase_alphabet[shifted_char]
                encryptedText += encryptedChar
            elif char in upperCase_alphabet:
                index = upperCase_alphabet.index(char)
                shifted_char = (index + shift) % 26
                encryptedChar = upperCase_alphabet[shifted_char]
                encryptedText += encryptedChar
            else:
                encryptedText += char

        print("-" * 40)
        print("Encrypted Text: ", encryptedText)
        print("-" * 40)

    elif choice == '2':
        decryptedText = ""
        for char in text:
            if char in lowerCase_alphabet:
                index = lowerCase_alphabet.index(char)
                shifted_char = (index - shift) % 26
                decryptedChar = lowerCase_alphabet[shifted_char]
                decryptedText += decryptedChar
            elif char in upperCase_alphabet:
                index = upperCase_alphabet.index(char)
                shifted_char = (index - shift) % 26
                decryptedChar = upperCase_alphabet[shifted_char]
                decryptedText += decryptedChar
            else:
                decryptedText += char

        print("-" * 40)
        print("Decrypted Text: ", decryptedText)
        print("-" * 40)
