
def encrypt(cleartext, offset):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if cleartext == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    encrypted = ""
    cleartext = cleartext.upper()
    for char in cleartext:
        if char == " ":
            encrypted += char
        elif (alphabet.index(char) + offset) > 25:
            encrypted += alphabet[(alphabet.index(char) + offset - 26)]
        elif (alphabet.index(char) + offset) < 0:
            encrypted += alphabet[(alphabet.index(char) + offset + 26)]
        else:
            encrypted += alphabet[(alphabet.index(char) + offset)]
    return encrypted


def decrypt(encrypt, offset):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if encrypt == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    decrypted = ""
    encrypt = encrypt.upper()
    for char in encrypt:
        if char == " ":
            decrypted += char
        elif (alphabet.index(char) - offset) > 25:
            decrypted += alphabet[(alphabet.index(char) - offset - 26)]
        elif (alphabet.index(char) - offset) < 0:
            decrypted += alphabet[(alphabet.index(char) - offset + 26)]
        else:
            decrypted += alphabet[(alphabet.index(char) - offset)]
    return decrypted.lower()