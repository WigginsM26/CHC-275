"""
Name: Maddox Wiggins
Section: 1
Description: Lab 4
"""

import math

"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied
"""
def getList():

    userList = []

    print("Enter -1 to stop entering numbers")

    while True:

        num = int(input("Enter a number: "))

        if num == -1:
            break

        userList.append(num)

    return userList


"""
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():

    print("Choose your function:")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Standard Deviation")
    print("6. Clear List")
    print("0. Exit")


"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value
"""
def getMean(userList):

    total = 0

    for num in userList:
        total = total + num

    mean = total / len(userList)

    return mean


"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value
"""
def getMedian(userList):
    length = len(userList)
    mid = length // 2

    if length % 2 == 1:
        return userList[mid]
    else:
        return (userList[mid - 1] + userList[mid]) / 2


"""
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):

    minimum = userList[0]

    for num in userList:

        if num < minimum:
            minimum = num

    return minimum


"""
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):

    maximum = userList[0]

    for num in userList:

        if num > maximum:
            maximum = num

    return maximum


"""
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):

    mean = getMean(userList)

    SSE = 0

    for current in userList:

        SSE = SSE + (current - mean) ** 2

    n = len(userList)

    SSE = SSE / n

    stdDev = math.sqrt(SSE)

    return stdDev


def main():

    userList = getList()

    while True:

        printMenu()

        function = int(input("Please enter your choice, or 0 to exit: "))

        if function == 1:

            print("The minimum value is:", getMin(userList))

        elif function == 2:
            print("The maximum value is:", getMax(userList))

        elif function == 3:

            print("The mean value is:", getMean(userList))

        elif function == 4:
            print("The median value is:", getMedian(userList))

        elif function == 5:

            print("The standard deviation is:", getStdDev(userList))

        elif function == 6:
            userList = getList()

        elif function == 0:

            print("Exiting program")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()