# Quetion 4
def printEven(no):

    for i in range(1, no + 1):
        if (i % 2 == 0):
            print(i)
def main():
    Value = int(input("Enter the number:"))
    printEven(Value)

if __name__ == "__main__":
    main()    
    