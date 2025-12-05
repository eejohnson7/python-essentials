'''
Great progress! Now it's your turn to craft the code. We want to build a string of fruit names separated by spaces, 
but we aim to avoid a trailing space at the end. Add the missing code to achieve this.
'''

# This code will create a simplified fruit salad with the provided fruits
fruits = ['apple', 'banana', 'cherry', 'date']
fruits_in_salad = ""

index = 0
# TODO: Create a while loop that assembles a string of fruit names separated by spaces, without adding a space after the last fruit
# Hint: Consider using a conditional to determine when to add a space
while index < len(fruits):
    fruits_in_salad += fruits[index] + " " if index != len(fruits) - 1 else fruits[index] 
    index += 1

print(fruits_in_salad)  # Output the fruits in the salad