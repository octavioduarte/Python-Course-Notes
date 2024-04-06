def generator():
    n = 1
    print("This is a generator funcion")
    yield n

    n += 1
    yield n

    n += 1
    yield n
    

my_gen_function = generator()

print(my_gen_function) # <generator object generator at 0x7fc963d42970>  - Address memory, we need use next() to access the value
print(next(my_gen_function)) # 1
print(next(my_gen_function)) # 2
print(next(my_gen_function)) # 3
print(next(my_gen_function)) # StopIteration Error



"""
    One important thing that we need to remember to understand how generator functions work is about the 'for' loop.
'For' loops are structures of repetition; the Python interpreter checks if there exists a next item and calls it with 
'next()'. If it's the last loop (looking for the exception 'StopIteration'), the interpreter stops the process.
    With iterators, we are responsible for handling this process. The generator returns a value from the list with
'yield'. If we need the next value from our generator function, we must use 'next()'.
"""

        