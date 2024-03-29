# Notes

First of all, 'for' and 'range' aren't bound. While 'for' is a traditional method in programming languages to execute the same code a finite number of times, 'range' is used to generate numbers.


# Range

The syntax:

~~~python
    range(start, stop, step)

    #"start" is the starting number of the sequence (optional, default is 0).
    #"stop" is the ending number of the sequence (exclusive).
    #"step" is the increment between numbers in the sequence (optional, default is 1).


    """
     In Python 3, the range() function doesn't directly generate a list. Instead, it produces a range object that represents a sequence of numbers. This object behaves like a list in many contexts but doesn't actually store all the numbers in memory at once. It generates the numbers dynamically as they are needed, which is memory-efficient, particularly for large ranges.
    """
~~~

~~~python
    range_with_numbers_between_0_and_10 = range(10)
    range_with_even_numbers_between_0_and_100 = range(0, 100, 2)


    print(range_with_numbers_between_0_and_10)
    print(range_with_even_numbers_between_0_and_100)

    """
        output

        range(0, 10)
        range(0, 100, 2)
    """
~~~