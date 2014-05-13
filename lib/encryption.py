
def encrypt(cleartext, offset):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if cleartext == '':
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    for i in cleartext:
       cleartext[i] = alphabet.index(cleartext[i])

    return ''