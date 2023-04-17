# Import pyfiglet module to change the font
import pyfiglet

# Import colorama module to change color of the font
import colorama
from colorama import Fore

# Apply pyfiglet and colorama module
title = "The Vigenere Cipher"
print(pyfiglet.figlet_format(title, font = "digital") + Fore.LIGHTCYAN_EX)

# Use vigenere cipher to encrypt plaintext
def encrypt_plaintext(message, keyword):
    ciphertext = ""
    index = 0

    for i in message:
        if i.isalpha():
        # Convert into numerical value
            message_val = ord(i) - 65
            key_val = ord(keyword[index]) - 65
            index = (index + 1) % len(keyword)
        
        # Encrypt the plaintext
            ciphertext_val = (message_val + key_val) % 26

        # Convert ciphertext back to letter value
            ciphertext_char = chr(ciphertext_val + 65)
            ciphertext += ciphertext_char
        else:
            ciphertext += i
    return ciphertext

# Ask for the input
message = input("What is the message? ")
keyword = input("What is the keyword? ")

ciphertext = encrypt_plaintext(message, keyword)

# Print the output
print("=" * 45)
print("*" * 45)
print(Fore.LIGHTMAGENTA_EX + ("\033[7mThe ciphertext is: " + ciphertext))