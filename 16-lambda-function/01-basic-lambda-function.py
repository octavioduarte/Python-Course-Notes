"""
    In Python, a lambda function is a small, anonymous function defined using the lambda keyword. 
Lambda functions can take any number of arguments but can only have one expression. They are typically
used for short, simple operations where defining a full function using the def keyword would be overkill.

The syntax for a lambda function is:

lambda arguments: expression
"""

users_to_use_with_defined_function = [
    {'name': "Janis", 'lastname': "Joplin"},
    {'name': "Ronnie", 'lastname': "Dio"},    
    {'name': "Ian", 'lastname': "Gillan"},    
]

def sort_list_with_normal_function(item):
    return item['name']

users_to_use_with_defined_function.sort(key=sort_list_with_normal_function)
print(users_to_use_with_defined_function)


users_to_use_with_lambda_function = [
    {'name': "Janis", 'lastname': "Joplin"},
    {'name': "Ronnie", 'lastname': "Dio"},    
    {'name': "Ian", 'lastname': "Gillan"},    
]

users_to_use_with_lambda_function.sort(key=lambda x: x["name"])

print(users_to_use_with_lambda_function)