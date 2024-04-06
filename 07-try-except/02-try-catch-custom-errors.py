# Bad code, we don't what's the error 

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except:
    print("Ocurred a error, but I don't know what??? 🤷‍♂️")
    
    
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError: # Exceptions in Pyhon are class
    print("Ocurred a error, you can't divide by 0.")
    
    
try:
    a = 10
    b = "?"
    c = a / b
    print(c)
except (ZeroDivisionError, TypeError): # We can use tuples to apply same code to diff errors class
    print("Invalid arguments to make calc.")