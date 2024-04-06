clubs = [
    {"name": "SCCP", "year": 1910, "state": "SP", "word_cup_champion": "?"},
    {"name": "SPFC", "year": 1930, "state": "SP", "word_cup_champion": "?"},
    {"name": "SFC", "year": 1912, "state": "SP",  "word_cup_champion": "?"},
    {"name": "SEP", "year": 1914, "state": "SP",  "word_cup_champion": "?"},
]


world_cup_champions_fifa = ["SCCP", "SPFC", "SFC"]

clubs_with_world_cup_champions_data = [
    {**club, "word_cup_champion": True}
    if club["name"] in world_cup_champions_fifa else {**club, "word_cup_champion": False}
    for club in clubs
]

print(*clubs_with_world_cup_champions_data, sep='\n')

"""
    output
    
    {'name': 'SCCP', 'year': 1910, 'word_cup_champion': True}
    {'name': 'SPFC', 'year': 1930, 'word_cup_champion': True}
    {'name': 'SFC', 'year': 1912, 'word_cup_champion':  True}
    {'name': 'SEP', 'year': 1914, 'word_cup_champion':  False}
"""



# Filter and Map using list comprehension:

# Add a new club in our lists
clubs.append(
        {"name": "SCI", "year": 1909, "state": "RS", "word_cup_champion": "?"},
)

world_cup_champions_fifa.append("SCI")


    
clubs_sp_with_world_cup_champions_data = [
    
    #This code, before the for loop, will map all items of the list and include 
    #them in our new list.
    
    {**club, "word_cup_champion": True}
    if club["name"] in world_cup_champions_fifa else {**club, "word_cup_champion": False}
    
    for club in clubs
    
    
    #After the for loop, this code will apply a conditional statement to filter data, which
    #will then be included in our array.
    #We don't use else in this case.
    
    if club["state"] == "SP" # This block remove our new club added  on line 33.
]

print()
print(*clubs_sp_with_world_cup_champions_data, sep='\n')
