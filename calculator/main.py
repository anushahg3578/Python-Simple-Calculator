try:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    print("Choose an operation:")
    print("Press + : Addition")
    print("Press - : Subtraction")
    print("Press * : Multiplication")
    print("Press / : Division")

    operation = input("Enter the operation: ")

    match operation:
        case "+":
            print(f"The result is: {a + b}")

        case "-":
            print(f"The result is: {a - b}")

        case "*":
            print(f"The result is: {a * b}")

        case "/":
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")

        case _:
            print("Invalid operation.")

except ValueError:
    print("Please enter valid numeric values.")