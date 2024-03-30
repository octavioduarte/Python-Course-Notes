# https://github.com/luizomf/cursopython2023/blob/6004f564d66693090a1e55c7f2e3568d4c1fc5de/aula80.py

list_numbers = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 3, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

first_occurrence_list = [[] for _ in range(len(list_numbers))] 
second_ocurrence_list = []


def load_repeated_values_by_row(index_row):
    repeated_items = []
    for item_internal_list in item:
        if (item_internal_list not in first_occurrence_list[index_row]): 
            first_occurrence_list[index_row].append(item_internal_list)
        else:
            repeated_items.append(item_internal_list)
            break;
    second_ocurrence_list.append(repeated_items)    
    
    
def logs():
    print(f"{index + 1}º list: {item}")
    if (len(second_ocurrence_list[index]) > 0):
        print("First repeated value", second_ocurrence_list[index][0])
    else: 
        print("Without repeated values")
    print()
    
            

for index, item in enumerate(list_numbers):
    load_repeated_values_by_row(index)
    logs()
 




            