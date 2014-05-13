
def encrypt(cleartext, offset):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if cleartext == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    encrypted = ""
    for char in cleartext:
        if char == " ":
            encrypted += char
        elif (alphabet.index(char) + offset) > 25:
            encrypted += alphabet[(alphabet.index(char) + offset - 26)]
        elif (alphabet.index(char) + offset) < 0:
            encrypted += alphabet[(alphabet.index(char) + offset + 24)]
        else:
            encrypted += alphabet[(alphabet.index(char) + offset)]
    return encrypted





    # for index, char in enumerate(cleartext):
    #     if cleartext[index] == " ":
    #         pass
    #     else:
    #         cleartext[index] += offset
    # for index, char in enumerate(cleartext):
    #     if cleartext[index] == " ":
    #         pass
    #     else:
    #         cleartext[index] = alphabet[char]
    # return ' '

#char = cleartext[index]