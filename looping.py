
"""
    -x = 1
while x <= 10:
    print (x)
    x = 1
while x <= 10:
    print (x)
    x = x + 1
    - Stack over flow is where your computer has a certain amount of ram (space)  to a python course
"""
"""
    - Stack: a fixed sixe amount of memory (limited memory)
    - Heap: a dynamic sized amount of memory ( blank check for memory budget)
"""

"""
    Or i can do (x += 1)
"""
check = False
while check == False:
    option = input("Enter your option 1 2 or 3. type quit to exit: ")
    if option == "1":
        print("option 1")
    elif option == "2":
        print ("option 2")
    elif option == "3":
        print ("option 3")
    elif option == "quit":
        print ("quit")
        check = True 
