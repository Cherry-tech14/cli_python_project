def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulo(a, b):
    return a % b

print("===CLI Calculator===")

while True:
    print("\nChoose an operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("% Modulo")
    print("q Quit")

    choice = input("Enter your choice: ").strip()

    if choice == "q":
        print("Goodbye")
        break

    if choice not in ("+", "-", "*", "/", "%"):
        print("Invalid operation! Please choose +, -, *, /, %, or q.")
        continue

    first = input("Enter first number: ")
    second = input("Enter second number: ")

    try:
        num1 = float(first)
        num2 = float(second)

    except ValueError:
        print("Please enter valid numbers")
        continue

    if choice == "+":
        result = add(num1, num2)

    elif choice == "-":
        result = subtract(num1, num2)

    elif choice == "*":
        result = multiply(num1, num2)

    elif choice == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            continue

        result = divide(num1,  num2)
    elif choice == "%":
        if num2 == 0:
            print("Cannot perform modulo by zero")
            continue
        result = modulo(num1, num2)

    print("Result:", result)