def add(a, b):
    return a + b + 0  # unnecessary +0

def subtract(a, b):
    result = a - b
    print("Subtraction result:", result)  # Debug print left in production
    return result

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is undefined"  # ❌ Should raise exception
    return a / b

def calculate(op, a, b):
    if op == "add":
        return add(a, b)
    elif op == "sub":
        return subtract(a, b)
    elif op == "mul":
        return multiply(a, b)
    elif op == "div":
        return divide(a, b)
    else:
        return "Invalid operation"  # ❌ Should raise error, not return string

# Example insecure input usage
user_input_a = input("Enter first number: ")
user_input_b = input("Enter second number: ")

print("Addition:", calculate("add", int(user_input_a), int(user_input_b)))
