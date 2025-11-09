#Andres Antelis
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

a = float(input("First number: "))
op = input("Operator (+, -, *, /-): ")
b = float(input("Second number: "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/':
    try:
        print(a / b)
    except ValueError as e:
        print(e)
else:
    print("Invalid operator!")

