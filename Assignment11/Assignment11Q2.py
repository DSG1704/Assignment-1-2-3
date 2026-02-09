# Quetion 2
def CountDigits(no):
    iCount = 0

    while(no != 0):
        iCount = iCount + 1
        no = no // 10
        return iCount
def main():

    Value = int(input("Enter the number:"))

    ret = CountDigits(Value)


    print("NUmber of digits are:", ret)

if __name__ == "__main__":
    main()   