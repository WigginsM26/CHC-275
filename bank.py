acc = ["@wiggins","@paul","@basmaci"]
balance = [10000,70,5000]

check = False
while check == False:
    for i in range (len(acc)):
         print (f"Banking information for. {acc[i]}. Balance: {balance[i]}")
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Add Account")
    print("4. Remove Accout")
    print("5. Transfer")

    option = input("What would you like to do today! Press quit to exit: ")

    if option == "deposit":    # Finds the account by name and adds the inputted deposit amount.
        name = input("Which account is depositing? ")
        index = acc.index(name)
        deposit = input("State the amount being deposited: ")
        deposit = int(deposit)
        balance[index] = balance[index] + deposit

    elif option == "withdrawl":   # After account is listed this allows user to enter the amount they want to take from the acoount.
        index = acc.index(name)
        deposit = input("State the amount being withdrawn: ")
        deposit = int(deposit)
        balance[index] = balance[index] - deposit

    elif option == "add":   #Allows user to add an account that wasn't listed in the beginning. They can also list their account balance. 
        name = input("Add account: ")
        acc.append(name)
        num = input("How much is on your account? ")
        num = int(num)
        balance.append(num)

    elif option == "remove":   #Allows any account previously listed or recently added to be removed. 
        name = input("Remove account: ")
        index = acc.index(name)
        acc.pop(index)
        balance.pop(index)

    elif option == "transfer":  #Allows user to choose an account to tranfer money to
        name = input("What is the transfer account?: ")
        index = acc.index(name)
        name2 = input("To which account?: ")
        index2 = acc.index(name2)
        deposit = input("Amount being transferred: ")
        deposit = int(deposit)
        balance[index] = balance[index] - deposit
        balance[index2] = balance[index2] + deposit

    if option == "quit":
            check = True