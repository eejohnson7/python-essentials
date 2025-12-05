'''
Well done on your progress so far! Here's a new challenge for you. The code below is supposed to iterate through a list of 
temperatures, printing out a message based on the value of each temperature. However, it seems not to behave as expected. 
Can you spot the issue and fix it to ensure it runs correctly? Good luck, Explorer!
'''

temperatures = [18, 22, 30, 35]
i = 0
while i < len(temperatures):
    if temperatures[i] > 20:
        print("Temperature", temperatures[i], "is greater than 20.")
        i += 1
        continue
    print("Temperature", temperatures[i], "might require a jacket.")
    i += 1