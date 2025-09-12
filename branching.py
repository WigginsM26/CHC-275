x = 10
if x % 2 == 1:
    print(f"{x} is divisble by 2")
    print ("Test")

    print(" This is not part of the if statement")    

x = 10
if 10 % 2 == 1:
    print(f"{x} is divisble by 2")
    print ("Test")
else:
    print(" This is not part of the if statement")    


x = 3
if x % 5 == 0:
    print(f"{x} is divisble by 5")
elif x % 2 == 0:
    print(f"{x} is divisible by 2")
else:
    print (f"{x} is not divisible by 5 or 2")


x = 10
if x > 5 and x > 15:
    print (f"{x} is greater then 5 and 15")
if x > 5 and x > 15:
    print (f"{x} is greater then 5 or 15")