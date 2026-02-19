def getMedian(userList):
    length = len(userList)
    mid = length // 2

    if length % 2 == 1:
        return userList[mid]
    else:
        return (userList[mid - 1] + userList[mid]) / 2

print(getMedian([1, 2, 3, 4]))