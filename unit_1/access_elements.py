'''
Welcome to your first hands-on exercise! Let's ensure that you are comfortable working with basic syntax of lists. 
Complete the following code to correctly access and print the specified elements from the list.
'''

def access_elements(my_list):
    # Access and print the first element
    print(my_list[0])
    
    # Access and print the last element
    print(my_list[len(my_list) - 1])

# Example list
example_list = [10, 20, 30, 40, 50]
access_elements(example_list)

# Expected Output:
# 10
# 50