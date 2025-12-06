'''
Your current task is to tweak the given string manipulation code. Modify the loop so that, instead of altering the letter 
cases, it counts the number of lowercase characters in the text. Use the final print statement to display the count.
'''

text = "Python is fun!"
cleaned_text = ""
count = 0

for char in text:
    if char.islower():
        # cleaned_text += char.upper()
        count += 1
    elif char.isupper():
        # cleaned_text += char.lower()
        continue
    else:  # Keep non-alphabetical characters unchanged
        # cleaned_text += char
        continue

# print(cleaned_text)  # Initially outputs: "pYTHON IS FUN!"
print(count)