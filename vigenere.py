from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.1234567890'

myKey = "FACEBOOKPASSWORD"

myText = "Yhwvtroi, 28 Yuqa 2016"

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result

def show_result(plaintext, key):

    print 'Decrytped: %s' % decrypted


decrypted = decrypt(myKey, myText)

show_result(decrypted, myKey)
