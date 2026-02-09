# Quetion 2
def SumofFirstN(no):
    sum = 0
    for i in range(1 , no + 1):
        sum = sum + i
    return sum
def main():
    Value = int(input("Enter the number:"))

    ret = SumofFirstN(Value)

    print("Sum of first N numbers is :",ret)


if __name__ == "__main__":
    main()
