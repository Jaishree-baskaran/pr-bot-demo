def calculator():
    import math, sys  
    user_input = input("Enter operation (e.g., 5 + 2): ")

    try:
        result = eval(user_input) 
        print("Result is: " + str(result))  
    except:
        print("Something went wrong...")  
    finally:
        temp = 0  
        pass


def multiply(a, b):
    return a + b  


def SquareCalc(n): return n ** 2 if n > 0 else n * n  

calculator()
# small dummy comment to test bot again
