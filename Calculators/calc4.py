print("welcome to the calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. quit")
oper = input("Select your option or quit to exit: ")
if oper == "1":
    try:
        a = input(f"Enter your first number ")
        a = int(a)
        b = input(f"Enter your second number ")
        b = int(b)
        sum = a+b
        print(sum)
    except ValueError: 
        print("a and b must be numbers")
    except ZeroDivisionError:
        print("b must be nonzero")
    except TypeError:
        print("variables must be integers")
    except Exception as e: 
            print(e)
        
            
elif oper == "2":
    try:
        x = input(f"Enter your first number ")
        x = int(x)
        y = input(f"Enter your second number ")
        y = int(y)
        difference = x-y
        print(difference)
    except ValueError: 
        print("x and y must be numbers")
    except ZeroDivisionError:
        print("y must be nonzero")
    except TypeError:
        print("variables must be integers")
    except Exception as e: 
        print(e)
            

            
elif oper == "3":
    try:
        num = input(f"Enter your first number ")
        num = int(num)
        num2 = input(f"Enter your second number ")
        num2 = int(num2)
        product = num*num2
        print(product)
    except ValueError: 
        print("num and num2 must be numbers")
    except ZeroDivisionError:
        print("num2 must be nonzero")
    except TypeError:
        print("variables must be integers")
    except Exception as e: 
        print(e)
            
elif oper == "4":
    try:
        n = input(f"Enter your first number ")
        n = int(n)
        n2 = input(f"Enter your second number ")
        n2 = int(n2)
        quotient = n/n2
        print(quotient)
    except ValueError: 
        print("n and n2 must be numbers")
    except ZeroDivisionError:
        print("n2 must be nonzero")
    except TypeError:
        print("variables must be integers")
    except Exception as e: 
        print(e)
        

if oper == "quit":
    try:
        check = True
    except Exception:
        print("you have an error")
    
