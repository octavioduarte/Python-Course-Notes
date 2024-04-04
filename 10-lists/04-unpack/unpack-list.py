bands = [
    {"name": "Sepultura", "country": "Brazil"},
    {"name": 'Metallica', "country": 'Eua'}
]

band1, band2 = *bands,

print(band1, band2, sep='\n')

"""
    output:
    
    {'name': 'Sepultura', 'country': 'Brazil'}
    {'name': 'Metallica', 'country': 'Eua'}
"""