# Notes

    In Python, we can access the ID that the language uses to identify our variables in memory.


Using method `id(our var)`

~~~python
    var1 = "Hello"

    print(id(var1))

    """
        output

        139985339388464
    """
~~~

    With the goal of being faster, the language uses the same memory address to occupy less space if our variables have the same value (depending on the operating system).

~~~python
    var1 = "Hello"
    var2 = "Hello"

    print(id(var1))
    print(id(var2))

    """
        output

        139995625099760
        139995625099760
    """
~~~