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

elif option == "2":
    name = input("Which account is withdrawing? ")
    index = acc.index(name)
    deposit = input("State the amount being withdrawn: ")
    deposit = int(deposit)
    balance[index] = balance[index] - deposit

elif option == "3":
    name = input("Add account: ")
    acc.append(name)
    num = input("How much is on your account? ")
    num = int(num)
    balance.append(num)

elif option == "4":
    name = input("Remove account: ")
    index = acc.append(name)
    acc.pop(index)
    balance.pop(index)

elif option == "5":
    name = input("Which account is making the transfer?: ")
    index = acc.index(name)
    name2 = input("To which account?: ")
    index2 = acc.index(name2)
    deposit = input("State the amount being transferred: ")
    deposit = int(deposit)
    balance[index] = balance[index] - deposit
    balance[index2] = balance[index2] + deposit

if option == "quit":
        check = True