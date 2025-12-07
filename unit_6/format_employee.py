'''
You have a list of employees, each with their name, job title, and years since last training, all in a single string.

Your task is to:

Split and process each employee's information
Check if they have gone more than 2 years without training
If so, append a note indicating they need a training refresh
Display the result in a clear and readable format
'''

# A tiny piece of code that represents an HR Employee Training Management system.
# This code will manage a simple string that contains employee data.

employee_data = "Alice,Developer,3|Bob,Manager,1|Charlie,Designer,4"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and training status
for employee in employee_list:
    # TODO: Parse the employee data and add training refresh note if applicable
    employee_info = employee.split(',')
    name = employee_info[0]
    role = employee_info[1]
    years_since_training = employee_info[2]
    training_status = " - Needs training refresh" if int(years_since_training) > 2 else ""

    print(f"Name: {name} - Role: {role} - Years since training: {years_since_training}{training_status}")
    # Example: Name: Alice - Role: Developer - Years since training: 3 - Needs training refresh