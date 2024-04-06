# We can use list with tuples

my_list = []

for x in range(10+1):
    my_list.append((x, x * 2))
    
print(my_list)

"""
    output
    
    [(0, 0), (1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18)]
"""