'''
Great job, Space Voyager! I have a new mission for you. Below is a piece of code meant to process a string into uppercase 
(the code should process only the alphanumeric characters into an output string), but it has a small bug. Your task is to 
identify and fix the issue. Remember, characters must be letters before they are converted to uppercase.

Note: the output of the code should not include characters that aren't letters.
'''

def process_text(text):
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char.upper()            
    print(f"Processed Text: {new_text}")

process_text("Happy Coding, Friends!")