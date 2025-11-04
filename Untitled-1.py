try: 
    x = input("Enter num 1: ")
    y = input("enter num 2: ")
    x = int(x) #value error if not a number
    y = int(y)
    quotient = x/y 
    print(quotient)
    #Dividing by zero is no good. 
except ValueError: 
    print("x and y must be numbers")
except ZeroDivisionError:
    #you can catch multiple exceptions 
    print("y must be nonzero")
except TypeError:
    print("variables must be integers")
except Exception as e: 
    #capture exceptions that i'm not expecting and print that exception out
    print(e)
finally: 
    #executes codeblock no matter what
    print("Thanks for using the calculator ")