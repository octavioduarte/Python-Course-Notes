try:
    a = 10
    b = "?"
    c = a / b
    print(c)    
except (ZeroDivisionError, TypeError) as error: # variable error receive error instance exception
    print(error.__class__.__name__) #TypeError