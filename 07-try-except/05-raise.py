clubs_sp = ['SCCP', 'SPFC', 'SFC', 'SEP']
club_inputed = input('Input a club from big four of SP: ')
MY_CUSTOM_MESSAGE_ERROR='Invalid club'


try:
    if (club_inputed not in clubs_sp):
        raise ValueError(MY_CUSTOM_MESSAGE_ERROR) 
    
    print(f"You inputed: {club_inputed}")
    
except ValueError as error:
    print(error.args[0])
    
    
#About errors in Python: https://docs.python.org/3/library/exceptions.html