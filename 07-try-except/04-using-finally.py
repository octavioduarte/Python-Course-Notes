try:
    print("Hello")
    print(1910 / 0)
except ZeroDivisionError:
    print("Error zero division") 
finally: # Finally, always executes
    print("World")