clubs = [
    {"name": "SCCP", "year": 1910, "word_cup_champion": "?"},
    {"name": "SPFC", "year": 1930, "word_cup_champion": "?"},
    {"name": "SFC", "year": 1912, "word_cup_champion": "?"},
    {"name": "SEP", "year": 1914, "word_cup_champion": "?"},
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