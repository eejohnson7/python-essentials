'''
Excellent progress! In this challenge, you are tasked with implementing the encryption logic for the Caesar Cipher from 
scratch. Your task is to update the placeholders to provide the correct ASCII values required to shift the characters within 
a string.

About the Caesar Cipher:
The Caesar Cipher is a classic encryption technique that dates back to ancient Rome. It works by shifting each letter in the 
plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, a becomes d, b becomes e, and so 
on. When the end of the alphabet is reached, the cipher "wraps around" so that x becomes a, y becomes b, and z becomes c. 
Only alphabetic characters are shifted; all other characters (such as punctuation and spaces) remain unchanged.
'''

# A simple text encryption exercise using the Caesar Cipher technique.
# The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
# a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

# Implement the encryption logic by shifting each alphabet character

def encrypt_text(text):
    encrypted = ""
    for char in text:
        if char.isalpha():  # check if the character is an alphabet
            shift = 3
            # TODO: Use the correct ASCII values to shift the character and add it to 'encrypted'
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            # Hint: You can use the modulo operator (%) to make the alphabet "wrap around" when shifting past 'z' or 'Z'.
            # Hint: Each letter has a unique ASCII value. For example, ord('A') = 65 and ord('a') = 97.
            # Hint: To shift a letter within the alphabet, first convert the character to its ASCII value.
            # Remember to handle both uppercase and lowercase letters.
        else:
            encrypted += char  # keep non-alphabet characters unchanged
    return encrypted

# Example text to encrypt
original_text = "Hello, Python!"
# The encrypted_text function call and print statement should be the same as in the solution
encrypted_text = encrypt_text(original_text)
print(encrypted_text)  # The correct output after implementing the TODO should be 'Khoor, Sbwkrq!'