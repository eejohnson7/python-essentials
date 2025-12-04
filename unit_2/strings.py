'''
Your final challenge in this lesson, Space Explorer, is to manipulate a string - the essential skill of any Galactic Pioneer. 
You're given a mission name (a string), and your task is to change its first and last characters. Show the original first and 
last characters, make the changes, and then display the updated string. Remember, strings are immutable, so you'll need to 
find a creative way to achieve your goal!
'''

# Given mission name
mission_name = "Sort"

# TODO: Print the first and the last character of the mission name
print(mission_name[0])
print(mission_name[-1])

# TODO: The mission needs a minor update. We aim to change its first letter to 'P' and the last letter to `k`, obtaining the word "Pork".
# Remember, strings in Python are immutable, so you cannot alter them directly.
mission_name = "P" + mission_name[1:3] + "k"

# TODO: Print the updated mission name
print(mission_name)