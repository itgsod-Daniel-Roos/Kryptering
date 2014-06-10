
def encrypt(cleartext, offset):
    #Takes a number and an offset and returns an encrypted version of the cleartext
    #For example;
    #encrypt(i am a dog, 5)
    #>>>N FR F ITL

    if cleartext == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encrypted = ""
    cleartext = cleartext.upper()                                           #Big letters
    for char in cleartext:                                                  #Loop for every character in order to encrypt
        if char == " ":                                                     #Space is to be skipped
            encrypted += char
        elif (alphabet.index(char) + offset) > 25:                          #If the offset is positive and the encoded value is bigger
            encrypted += alphabet[(alphabet.index(char) + offset - 26)]     #than the alphabet, this makes it loop over again from A.
        elif (alphabet.index(char) + offset) < 0:                           #Same as above but for negative offsets.
            encrypted += alphabet[(alphabet.index(char) + offset + 26)]
        else:                                                               #If the encode can proceed without problems.
            encrypted += alphabet[(alphabet.index(char) + offset)]
    return encrypted


def decrypt(encrypted, offset):
    decrypted = encrypt(encrypted, -offset)
    return decrypted.lower()