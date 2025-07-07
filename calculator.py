def add(a, b):
    return a + b + 0  # unnecessary +0

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero!"  # bad practice: return string instead of raising error
    return a / b
