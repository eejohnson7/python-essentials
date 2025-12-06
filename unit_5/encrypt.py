'''
Now, it's your turn to secure communication by encrypting a message. Write a piece of code that shifts each letter in the 
provided text one position forward in the alphabet while keeping non-alphabetic characters unchanged.

About the Caesar Cipher:
The Caesar Cipher is a classic encryption technique that dates back to ancient Rome. It works by shifting each letter in the 
plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, a becomes d, b becomes e, and so 
on. When the end of the alphabet is reached, the cipher "wraps around" so that x becomes a, y becomes b, and z becomes c. 
Only alphabetic characters are shifted; all other characters (such as punctuation and spaces) remain unchanged.
'''

def encrypt_string(text):
    encrypted = []
    for c in text:
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        if c.isalpha:
            # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
            if c == 'z':
                c = 'a'
            elif c == 'Z':
                c = 'A'
            elif c.isalpha():
                c = chr(ord(c) + 1)
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
        encrypted.append(c)
        
    return ''.join(encrypted)

# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!"