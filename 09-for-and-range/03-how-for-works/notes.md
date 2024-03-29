# Notes

In Python, everything is an object. One method that we can use is 'iter'. This method returns an iterator object, which can be called until our iterable object ends. After the last call, an error 'StopIteration' is triggered. 

~~~python
    team = "Corinthians"

    print(iter(team)) 
    # or 
    print(team.__iter__())

    """
        output:

        <str_iterator object at 0x7fb625cdfd00>

        This is an iterator object. It provides us with the memory address of our current iterator.
    """    
~~~

So with current address memory we can access the next iterator with next():

~~~python
    team = "Corinthians"

    currentInteratorObject = iter(team)
    print(next(currentInteratorObject)) # or currentInteratorObject.__next__()
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    print(next(currentInteratorObject))
    # After last loop of interation, the next method returns a error "StopInterator"
    print(next(currentInteratorObject))



    """
        output

        C
        o
        r
        i
        n
        t
        h
        i
        a
        n
        s
        StopIteration <--- error
    """
~~~ 

So for handle this error when it identify that your interator throws.