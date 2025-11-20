print("welcome to the calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

oper = input(" Enter the operaation you want to use: ")
if oper == "addition":
    num1 = input("What is number 1:")
    num2 = input("What is number 2:")
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    print (f"The sum of {num1} and {num2} is {sum}")

elif oper == "subtraction":
    num7 = input("What is number 7:")
    num8 = input("What is number 8:")
    num7 = int(num7)
    num8 = int(num8)
    diff = num7 - num8
    print (f"The difference of {num7} and {num8} is {diff}")

elif oper == "multiplicaton":
    num5 = input("What is number 5:")
    num6 = input("What is number 6:")
    num5 = int(num5)
    num6 = int(num6)
    multi = num5 * num6
    print (f"The product of {num5} and {num6} is {multi}")
  
elif oper == ("division"):
    num3 = input("What is number 3:")
    num4 = input("What is number 4:")
    num3 = int(num3)
    num4 = int(num4)
    div = num3 / num4
    print (f"The divident of {num3} and {num4} is {div}")