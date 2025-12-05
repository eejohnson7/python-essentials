'''
Change the current code so that the loop stops when it encounters a temperature below 20 degrees Celsius rather than 
stopping at the current temperature threshold. Additionally, update the printed statement to reflect the new condition. 
Observe how the break statement alters the control flow.
'''

# We'll check a series of temperatures and print a message accordingly
temperatures = [18, 22, 30, 35]

for temp in temperatures:
    if temp > 32:
        print('It is very hot.')
        break
    elif temp > 25:
        print('It is warm outside.')
        continue
    elif temp < 20:
        print('Might be chilly, dress appropriately.')
        break