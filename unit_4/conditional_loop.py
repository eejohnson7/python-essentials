'''
You're almost there, Space Voyager! Now it's time to combine everything you've learned about conditional loops, as well as 
the 'break' and 'continue' statements, in a single challenge. We're working with a list of temperatures again. Write the 
entire loop from scratch following the guidelines.
'''

# TODO: Define a list of temperatures
temps = [20, 33, 18, 15]

# TODO: Write a loop to go through each temperature in the list
for temp in temps:
    # TODO: Add an 'if' statement to check if the temperature is over a really hot threshold
    if temp > 30:
        # TODO: Print a message for being really hot and then exit the loop
        print("It is really hot.")
        break
    # TODO: Add an 'elif' condition before the general temperature message to check if it's too cold
    elif temp < 20:
        # TODO: For temperatures that are too cold, print a specific message and skip to the next one
        print("It is really cold")
        continue
    # TODO: Print a message saying the temperature is nice for all other cases
    print("The weather is nice.")