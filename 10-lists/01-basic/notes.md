# Notes

Different from primitive types, lists are mutable in Python. The code below works:

~~~python
    club = ["Janis Joplin", "Jimi Hendrix", "Kurt Cobain", "Keith Richards"]
    #or 
    #club = list(["Janis Joplin", "Jimi Hendrix", "Kurt Cobain", "Keith Richards"])
    
    club[3] = "Brian Jones"
    
    print(club)

    """
        output

        ["Janis Joplin", "Jimi Hendrix", "Kurt Cobain", "Brian Jones"]
    """
~~~