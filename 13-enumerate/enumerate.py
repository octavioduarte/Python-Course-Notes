"""
    enumerate is a built-in function in Python that adds a counter to an iterable and returns it as 
an enumerate object. This enumerate object can then be used in a loop to iterate over the original 
iterable while also keeping track of the index of each item.
"""

my_list = ["João", "Ana", "Maria"]

for index, value in enumerate(my_list):
    print(index, value)
    
    """
        output
        
        0 João
        1 Ana
        2 Maria
    """

for item in enumerate(my_list):
    print(type(item))
    
"""
    output
    
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    
    enumarate convert each item of our list in tuples
"""