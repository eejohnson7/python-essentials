'''
Time to exercise your coding muscles! In this practice task, I want you to refine your packing list. Instead of adding 
'sunglasses' at the end of the list, please place them precisely at index 2. Remember how the insert function works from the 
lesson? Go ahead and apply that knowledge.
'''

# A packing list for a journey using Python collections (Lists and Strings)
travel_items = ['passport', 'camera', 'sunscreen', 'hat']
travel_message = "Ready for the adventure!"

# Currently, sunglasses are being appended to the list.
# Your task is to add them at index 2 instead.
travel_items.insert(2, 'sunglasses')
print("Updated travel items: " + str(travel_items))

# Accessing the first and the last item packed
first_item = travel_items[0]
last_item = travel_items[-1]

print(f"First packed item: {first_item}, last packed item: {last_item}")
print("Travel message in lowercase:", travel_message.lower())