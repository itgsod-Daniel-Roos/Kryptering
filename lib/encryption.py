
def encrypt(cleartext, offset):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if cleartext == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    for index, char in enumerate(cleartext):
        if cleartext[index] == " ":
            pass
        else:
            cleartext[index] = alphabet.index(char)
    for index, char in enumerate(cleartext):
        if cleartext[index] == " ":
            pass
        else:
            cleartext[index] += offset
    for index, char in enumerate(cleartext):
        if cleartext[index] == " ":
            pass
        else:
            cleartext[index] = alphabet[char]

    return cleartext

#char = cleartext[index]