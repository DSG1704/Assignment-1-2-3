# Quetion 5
def printOdd(no):
    for i in range(1, no + 1):
        if (i % 2 != 0):
            print(i)
def main():
    Value = int(input("Enter the number:"))
    printOdd(Value)

if __name__ == "__main__":
    main()    