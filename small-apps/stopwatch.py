import time

def stopwatch(seconds):
    for i in range(seconds):
        minute, second = divmod(seconds - i, 60)
        text = f"{minute:02d}:{second:02d}"
        print(text, end="\r")
        time.sleep(1)
        
limit_time = None

while limit_time is None:    
    value_inputed = input("The timer stops at: ")
    if (value_inputed.isnumeric()):
        limit_time = value_inputed
    
stopwatch(int(limit_time))