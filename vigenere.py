# Use vigenere cipher to encrypt plaintext
def encrypt_plaintext(message, keyword):
    ciphertext = ""
    index = 0

    for i in message:
        if i.isalpha():