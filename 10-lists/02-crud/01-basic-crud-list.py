club = ["Janis Joplin", "Jimi Hendrix", "Kurt Cobain", "Brian Jones"]


#CREATE
club.append("Robert Johnson")
#["Janis Joplin", "Jimi Hendrix", "Jim Morrison", "Brian Jones", "Robert Johnson"]


#READ
print(club[3])
# Brian Jones


#UPDATE
club[2] = "Jim Morrison"
#["Janis Joplin", "Jimi Hendrix", "Jim Morrison", "Brian Jones"]


#DELETE
club.pop() # <-- Return element deleted
# ["Janis Joplin", "Jimi Hendrix", "Jim Morrison", "Brian Jones"]