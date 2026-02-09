#Question 3
def performMath(no1, no2, operation):
    if operation == 'add':
        return no1 + no2
    elif operation == 'subtract':
        return no1 - no2
    elif operation == 'multiply':
        return no1 * no2
    elif operation == 'divide':
        if no2 != 0:
            return no1 / no2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def main():
    try:
        Value1 = int(input("Enter first number:"))
        Value2 = int(input("Enter second number:"))
    except ValueError as obj:
        print("Error:", obj)
        print("Enter a positive integer")
        return

    print("Operations to perform")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            Operation = int(input("Enter your Number: "))

            if Operation == 1:
                print("Result:", performMath(Value1, Value2, "add"))
            elif Operation == 2:
                print("Result:", performMath(Value1, Value2, "subtract"))
            elif Operation == 3:
                print("Result:", performMath(Value1, Value2, "multiply"))
            elif Operation == 4:
                print("Result:", performMath(Value1, Value2, "divide"))
            else:
                print("Invalid operation")

            break

        except ValueError as obj:
            print("Error:", obj)
            print("Enter a positive integer")

if __name__ == "__main__":
    main()
