a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def add(x, y): 
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y    
print("Addition: ", add(a, b))
print("Subtraction: ", subtract(a, b))
print("Multiplication: ", multiply(a, b))
print("Division: ", divide(a, b))