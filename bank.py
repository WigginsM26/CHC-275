name = ["Maddox", "Paul", "Mr. Basmaci", ]
accname = ["@wiggins" ,"@paul", "@basmaci"]
balance = [10,000, 70 ,5000]
print (f"Banking information for {name[0]}). {accname[0]}. {balance[0]}")
for i in range (len(name)):
    print (f"Banking information for {name[i]}. {accname[i]}. {balance[i]}")






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
        check = True
        
     