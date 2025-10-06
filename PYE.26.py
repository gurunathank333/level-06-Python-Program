def add(a, b):
    c = a + b
    print("Addition:", c)

def sub(a, b):
    c = a - b
    print("Subtraction:", c)

def mul(a, b):
    c = a * b
    print("Multiplication:", c)

def div(a, b):
    c = a / b
    print("Division:", c)

def mod(a, b):
    c = a % b
    print("Modulus:", c)


print("Arithmetic Operations Using Functions")
print("-------------------------------------")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

add(x, y)
sub(x, y)
mul(x, y)
div(x, y)   
mod(x, y)   
