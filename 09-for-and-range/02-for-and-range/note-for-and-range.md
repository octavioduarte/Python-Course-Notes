# Notes

With 'for', we can access each value of our range created... The 'for' loop will receive the next value of each iteration according to the rules that we defined in our 'range'.

~~~python
    for value in range(10):
        print(value) 

    """
        output

        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
    """
~~~

~~~python
    for value in range(0, 100, 2):
        print(value)

    """
        output  
        0
        2
        4
        6
        8
        10
        ...until 100
    """
~~~