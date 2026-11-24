# calculator.py - a simple calculator

def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    else:
        return "Error: unknown operator"

print("Simple Calculator (type 'q' to quit)")

while True:
    first = input("Enter first number: ")
    if first == "q":
        break
    op = input("Enter operator (+, -, *, /): ")
    second = input("Enter second number: ")

    try:
        result = calculate(float(first), op, float(second))
        print("Result:", result)
    except ValueError:
        print("Error: please enter valid numbers")