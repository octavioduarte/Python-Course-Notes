import copy

dic1 = {'c1': 1, 'c2': 2}

# now dic2 see the same address memory that dic1.
dic2 = dic1

dic2['c1'] = 0
# So this line update the address memory, so it affect also dic1.


print(dic1) #{'c1': 0, 'c2': 2}
print(dic2) #{'c1': 0, 'c2': 2}



print("-" * 15)

"""
    in Python, the deepcopy() function from the copy module is used to create a deep copy of an object. A
deep copy creates a new object and then, recursively, inserts copies into it of the objects found in 
the original. This means that changes made to the original object won't affect the deep copy, and vice 
versa.
"""

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

# Modify the original list
original_list[0][0] = 100

# Printing both lists
print("Original list:", original_list)
print("Deep copied list:", deep_copied_list)