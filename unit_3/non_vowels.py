'''
Wrap up our journey with fruit salads by writing a script to count non-vowel characters in a given string. Remember, 
vowels are 'a', 'e', 'i', 'o', 'u', and all other letters are non-vowels. Use your knowledge of loops to complete this 
final mission!
'''

# Define a string named 'word' to represent the phrase we'll work with
word = 'FRUIT Salad'

# TODO: Initialize a counter to hold the number of non-vowel characters
count = 0

# TODO: Use a 'for' loop to iterate over each character in the string
for letter in word:
    count += 0 if letter.lower() in ['a', 'e', 'i', 'o', 'u', ' '] else 1

# TODO: Inside the loop, write a condition to check if it's not a vowel or a space
# Don't forget that letters can be lowercase and uppercase


# TODO: If the condition is true, increase the counter for non-vowel characters

# TODO: Finally, print out the count of non-vowel characters
print(count)