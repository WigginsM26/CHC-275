myList = [5,10,15,20,25,30,35]
print("for loop example")
for num in myList:
    print(num)
   
print(myList)

i=0
while i <= len (myList) -1:
    myList[i] = myList [i]+ 5
    i = i + 1
    
print(myList)
    