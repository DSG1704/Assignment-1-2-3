# Quetion 3
def Factorial(no):
    Fact = 1

    for i in range(1,no + 1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("Enter the number:"))

    ret = Factorial(Value)

    print("Factorial of a number is :",ret)

if __name__ == "__main__":
    main()    