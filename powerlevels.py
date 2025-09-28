n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    print("number 1 wins")
elif n1 < n2:
    print("number 2 wins")
else:
    print("It's a tie")