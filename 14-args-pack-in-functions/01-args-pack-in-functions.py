

#We use *args when our function receive unknow size values

def sum_a_lot_of_numbers(*args) -> int:
    # (1,2,3,4,5,6,7,8) <-- tuple
    return sum(args)         
    
    
result_sum = sum_a_lot_of_numbers(1,2,3,4,5,6,7,8)
print(result_sum) # 36