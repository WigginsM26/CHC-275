smallmush = []
medmush = []
largemush = []

while True:
    mushroom = input("Enter the size of the mushroom(or type 'stop' to finish): "). strip()
    size = int(mushroom)
    if  mushroom.lower() == 'stop':
        print ("small mushroom:", smallmush)
        print ("medium mushroom:", medmush)
        print ("large mushroom:", largemush)
        
        
        if size < 100:
            smallmush.append(size)
        elif size < 200:
            medmush.append(size)
        else:
            largemush.append(size)