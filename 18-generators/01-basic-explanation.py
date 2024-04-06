import sys

my_list =      [n for n in range(10000)]
my_generator = (n for n in range(10000))

print(sys.getsizeof(my_list)) # 87616 kb
print(sys.getsizeof(my_generator)) # 112 kb


"""
    One of the main advantages of generators in Python is that they allow values to be generated
on demand, meaning only the next value is calculated and held in memory during the algorithm's execution.
This contrasts with the approach of creating a complete list of 10000 indices (or any list size) all at once,
which would require memory space to store all those values simultaneously.

    By using generators, you can iterate over the values as they are generated, thus avoiding the need
to allocate a large amount of memory to store all values at once. This makes generators memory-efficient, especially
when dealing with large volumes of data or when values are generated iteratively during the processing of an algorithm.
"""
