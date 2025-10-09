acc = ["@wiggins","@paul","@basmaci"]
balance = [10000,70,5000]

check = False
while check == False:
    for i in range (len(acc)):
         print (f"Banking information for. {acc[i]}. Balance: {balance[i]}")
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Add Account")
    print("4. Delete Accout")
    print("5. Transfer")

option = input("What would you like to do today! Press quit to exit: ")

if option == "1":
        name = input("Which account is depositing? ")
        index = acc.index(name)
        deposit = input("State the amount being deposited: ")
        deposit = int(deposit)
        balance[index] = balance[index] + deposit

"""elif option == "2":
        name = input("Remove account: ")
        index = bank1.append(name)
        acc.pop(index)
        acc.pop(index)

    elif option == "3":
        name = input("Which account is depositing? ")
        index = bank1.index(name)
        money = input("State the amount being deposited: ")
        money = int(money)
        bank2[index] = bank2[index] + money

    elif option == "4":
        name = input("Which account is withdrawing? ")
        index = bank1.index(name)
        money = input("State the amount being withdrawn: ")
        money = int(money)
        bank2[index] = bank2[index] - money

    elif option == "5":
        name = input("Which account is making the transfer?: ")
        index = bank1.index(name)
        name2 = input("To which account?: ")
        index2 = bank1.index(name2)
        transfer = input("State the amount being transferred: ")
        transfer = int(transfer)
        bank2[index] = bank2[index] - transfer
        bank2[index2] = bank2[index2] + transfer

    if option == "quit":
        check = True











name = input("Welcome to the Bank! Enter your account name: ")
if name == "@wiggins":
    password = input("What is you password?: ") 
    if password == "maddox!":
        print ("You have signed in!")
    check = False

while check == False:
    print("1. deposit")
    print("2. withdraw")
    print("3. log in ")
    print("4. sign in ")
    print("5. transfer")
    oper = input(" What would you like to do?: ")
    if oper == "deposit":
        num = input("What amount?: ")
        num = int(num)
    
        print (f"You have deposited ${num} into your account: ")

    elif oper == "withdraw":
        num7 = input("What is number 7:")
        num8 = input("What is number 8:")
        num7 = int(num7)
        num8 = int(num8)
        diff = num7 - num8
        print (f"The difference of {num7} and {num8} is {diff}")

    elif oper == "sign in":
        num5 = input("What is number 5:")
        num6 = input("What is number 6:")
        num5 = int(num5)
        num6 = int(num6)
        multi = num5 * num6
        print (f"The product of {num5} and {num6} is {multi}")
    
    elif oper == ("log in"):
        num3 = input("What is number 3:")
        num4 = input("What is number 4:")
        num3 = int(num3)
        num4 = int(num4)
        div = num3 / num4
        print (f"The divident of {num3} and {num4} is {div}")
        
    elif oper == "transfer":
        num5 = input("What is number 5:")
        num6 = input("What is number 6:")
        num5 = int(num5)
        num6 = int(num6)
        multi = num5 * num6
        print (f"The product of {num5} and {num6} is {multi}")
    elif oper == "quit":
        check = True"""
        
     