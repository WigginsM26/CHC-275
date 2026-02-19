def getMin(userList):
    candidate = userList[0]
    for value in userList:
        if value < candidate:
            candidate = value
    return candidate

first = [1, 2, 3, 4]
print (first)
print(f"minimum of first list: {getMin(first)}")
second = [4, 1, 3, 2,]
print(second)
print(f"minimum of second list: {getMin(second)}")