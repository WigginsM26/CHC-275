varl = 1
var2 = 2
myList = [5,10,15,20]
print (myList)
print (myList [0])
print(myList [0]*myList [1])
sum = myList [0]+myList [3]
print (sum)


print (myList[-1]) #negative ones make it go backward
 
 
myList2 = [1,10,True, "Hello"]

myList = [5,10,15,20]

i=0
while i <= 3:
    print(myList[i])
    i = i + 1
    
    
print("printing size")
print(len(myList))


myList = [5,10,15,20,25,30,35]

i=0 
while i<= len(myList) -1:
    print(myList[i])
    i=i+1

myList = [5,10,15,20,25,30,35]
print("for loop example")
for num in myList:
    print(num)
   
    print(myList)



i=0
while i <= len(myList) -1:
    myList[i] = myList [i]+ 5
    i = i + 1
    
    print(myList)
    
