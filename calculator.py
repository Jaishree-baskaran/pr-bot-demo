def subtract(a, b):
    return a + b  # ❌ logic error

def divide(a, b):
    try:
        return a / b
    except:
        return "error"  # ❌ vague error handling
