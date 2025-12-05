'''
Great progress, Space Voyager! It seems that one of our fruit counters is malfunctioning and not producing the correct total. 
Could you identify the glitch in the program and fix it so that we can know exactly how many fruits we have for the salad?
'''

# List of fruits for the fruit salad
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Count the number of fruits in the salad
fruit_count = 0
# Loop over each fruit in the fruits list
for fruit in fruits:
    # The wrong operator is used here, it should increase the count
    fruit_count += 1  
print(fruit_count)  # This should print the total number of fruits in the salad