'''
Great job! Now, we need more control over our messages. Add temperature-based control to the weather app. Your task is to:

Complete the for-loop header to iterate over the temperatures list.
If a temperature is below 15, print "Wear warm clothes." and stop checking further temperatures.
If a temperature is 20 or above, print "You can wear light clothes." and skip the fallback message for that iteration.
Otherwise, print "Consider a light jacket."
Fill in the missing code to manage the output based on the temperature.
'''

# Sequence of temperatures throughout the day
temperatures = [16, 14, 20, 22, 19, 13]

# TODO: Loop through temperatures to suggest clothing
for temp in temperatures:
    if temp < 15:
        print("Wear warm clothes.")
        # TODO: If it's cold outside, we stop checking the temperatures. Add the needed line to interrupt the loop.
        break
    elif temp >= 20:
        print("You can wear light clothes.")
        # TODO: Add a line here that will skip the final print statement when it's warm enough for light clothes.
        continue
    print("Consider a light jacket.")  # Suggestion for in-between temperatures