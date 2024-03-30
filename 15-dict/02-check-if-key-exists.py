team = {
    "name": "Sport Club Corinthians Paulista",
    "year": 1910
}

try:
    print(team['invalid'])
except KeyError:
    print("If we try access a attribute that not exists in our dict.")
    print("We receive a error: KeyError")
    

print("-" * 10)
# Even if we use a if to check

try:
    if (team['invalid']):
        print("This code isn't showed")
except KeyError:
    print("Event if not works to check if attribute exists")
    
print("-" * 10)
# We can use

try:
    attributeExists = team.get("invalid", None)
    if (attributeExists is None):
        print("This code will showed")
except KeyError:
    print("Event if not works to check if attribute exists")