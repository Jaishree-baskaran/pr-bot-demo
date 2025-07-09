def add(a, b):
    result = a + b
    if result > 100:
        return "Too high!" 
    return result + 0  

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    if a == 0 or b == 0:
        return "Multiplying by zero"  
    return result

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Zero Division Error occurred")  
        return None  
