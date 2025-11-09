#Andres Antelis
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

a = float(input("First number: "))
op = input("+, -, *, /: ")
b = float(input("Second number: "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
else:
    print("Invalid operator!")

