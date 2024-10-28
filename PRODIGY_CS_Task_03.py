def lengthChecker(password):
    if len(password) >= 8:
        return True
    print("\nA strong password requires at least 8 characters.")
    return False

def upperCase_Checker(password):
    if any(char.isupper() for char in password):
        return True
    print("\nConsider adding uppercase letters for a stronger password.")
    return False

def lowerCase_Checker(password):
    if any(char.islower() for char in password):
        return True
    print("\nConsider adding lowercase letters for a stronger password.")
    return False

def specialChar_Checker(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        return True
    print("\nConsider adding special characters for a stronger password.")
    return False

def number_Checker(password):
    if any(char.isdigit() for char in password):
        return True
    print("\nConsider adding numbers for a stronger password.")
    return False

def passwordStrength(password):
    length = lengthChecker(password)
    upperCase = upperCase_Checker(password)
    lowerCase = lowerCase_Checker(password)
    specialChar = specialChar_Checker(password)
    number = number_Checker(password)

    if all([length, upperCase, lowerCase, specialChar, number]):
        print("\nYour password is STRONG!")
    elif length and (upperCase or lowerCase) and (specialChar or number):
        print("\nYour password is moderate. Consider adding more variety for extra strength.")
    else:
        print("\nYour password is weak. Try adding more characters, including uppercase letters, lowercase letters, numbers, and special characters.")

while True:
    password = input("Enter your password: ")
    passwordStrength(password)
    print("\n")
