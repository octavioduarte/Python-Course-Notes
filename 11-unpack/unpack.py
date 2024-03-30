# In Python, we can unpack values without referring to indices using unpacking.


c1, c2, c3 = ["Brazil", "Argentina", "Russian"]
print(c1, c2, c3) # Brazil Argentina Russian


#If we need to unpack more or fewer values than the size of our list, we can use this strategy:


b1, *_ = ["Black Sabbath", "Sepultura", "Led Zeppelin"]
print(b1) # Black Sabbath