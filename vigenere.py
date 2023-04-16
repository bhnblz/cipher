# Use vigenere cipher to encrypt plaintext
def encrypt_plaintext(message, keyword):
    ciphertext = ""
    index = 0

    for i in message:
        if i.isalpha():
        # Convert into numerical value
            message_val = ord(A) - 65
            key_val = ord(keyword[index]) - 65
            index = (index + 1) % len(keyword)