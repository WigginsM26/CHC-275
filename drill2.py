"""
Programming drill 2:
    - call the file drill2.py
    - write a function called makeList() that
        - takes in numbers via input() and typecasts them to integers, then appends them to a list called
        "nums" UNTIL the user types in "stop"
        - returns that list
        
    - try making two lists using makeList() and print those lists out
"""


def makeList():
    nums = []
    numbering = True
    while numbering == True:
        numinput = input("list numbers:" )
        if numinput =="stop":
            numbering = False
        else:
            nums.append(int(numinput))
    
    return nums


