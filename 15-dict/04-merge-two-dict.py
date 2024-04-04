

data = {
    'name': 'Corinthians',
    'year': 1910
}

titles = {
    'brasileiro': [1990, 1998, 1999, 2005, 2011, 2015, 2017],
    'mundial': [2000, 2012]
}


sccp = {**data, **titles, "supporters_amount": 3700000}

print(sccp)

"""
{
    'name': 'Corinthians',
    'year': 1910,
    'brasileiro': [1990, 1998, 1999, 2005, 2011, 2015, 2017],
    'mundial': [2000, 2012],
    'supporters_amount': 3700000
}
"""