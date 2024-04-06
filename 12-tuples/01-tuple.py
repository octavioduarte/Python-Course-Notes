"""
    In Python, a tuple is an immutable sequence of elements. It is similar to
a list, but unlike lists, tuples cannot be modified once they are created.

    Tuples are defined by enclosing elements in parentheses ( ), and the elements within 
a tuple are separated by commas.
"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple, type(my_tuple)) # (1, 2, 3, 4, 5) <class 'tuple'>


"""
# I can't do:
my_tuple[0] = 3

#Because: 
#TypeError: 'tuple' object does not support item assignment
"""
