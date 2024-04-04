"""
    List comprehension is a concise and efficient way to create lists in Python. 
It allows you to generate a new list by applying an expression to each element of 
an existing list, optionally filtering the elements based on a specified condition.


    The basic syntax of list comprehension in Python is as follows:

    new_list = [expression for element in original_list if condition]

    Where:

    expression is the expression to apply to each element of the original list.
    element is a variable representing each item in the original list.
    original_list is the existing list from which elements are extracted.
    condition is an optional condition that filters the elements of the original list before applying the expression.
"""

squares = [x ** 2 for x in range(1, 6)]
# Output: [1, 4, 9, 16, 25]