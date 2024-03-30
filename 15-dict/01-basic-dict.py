"""

    In Python, a dict (short for dictionary) is a built-in data type that stores a collection of key-value 
pairs. It is mutable, unordered, and iterable. Dictionaries are often referred to as "associative arrays"
or "hash maps" in other programming languages.
"""

sccp = {
    'team': "Corinthians",
    'year': 1910 ,
    'last_south_american_club_championship_world_cup': True,
    'titles': [
        {'name': 'Brasileirão Série A', 'years':[1990, 1998, 1999, 2005, 2011, 2015, 2017]},
        {'name': 'Libertadores', 'years':[2012]},
        {'name': 'Mundial de Clubes', 'years':[2000, 2012]},
        {'name': 'Copa do Brasil', 'years':[1995, 2002, 2009]},
    ]
}


print(sccp)


print("-" * 10)
# Also works

sccp1910 = dict(team="Corinthians", year=1910)

print(sccp1910)

print("-" * 10)

#Dictionaries aren't iterable in Python. If we use a 'for' loop, we will 
# iterate over the keys of our dictionary

for key_of_sccp in sccp:
    print(key_of_sccp)
    
    """
        output
        
        team
        year
        last_south_american_club_championship_world_cup
        titles
    """