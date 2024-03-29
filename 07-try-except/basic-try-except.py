try:
    inputValue = input("Input a invalid number: ")
    print(f"Your value is a valid number {int(inputValue)}.")    
except:
    print("This code is being executed because ocurred an error while converting your invalid number.")