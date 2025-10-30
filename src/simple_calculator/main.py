# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("🧮 Simple Calculator 🧮")
print("Operations: +, -, *, /")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", add(num1, num2))
    elif operator == '-':
        print("Result:", subtract(num1, num2))
    elif operator == '*':
        print("Result:", multiply(num1, num2))
    elif operator == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator. Please use +, -, * or /.")

except ValueError:
    print("Invalid input! Please enter numbers only.")
