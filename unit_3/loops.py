'''
Change the for loop in the starter code to a while loop to iterate over the fruit list for our fruit salad. Make sure to 
add all the fruits!
'''

# List of fruits to include in a fruit salad
fruits = ['apple', 'banana', 'orange', 'kiwi', 'melon']

# Using a for loop to iterate over the list of fruits
'''
for fruit in fruits:
    print(f"Adding {fruit} to the salad.")
'''

i = 0
while i < len(fruits):
    print(f"Adding {fruits[i]} to the salad.")
    i += 1