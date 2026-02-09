# Quetion 3
def SumDigits(no):
    sum = 0
    iDigit = 0

    if(no < 0):
        print("Enter aa valid Number")
        return
    while(no !=0):
        iDigit = no % 10
        no = no // 10
        return sum
def main():
    Value = int(input("Enter the number:"))

    ret = SumDigits(Value)

    print("Sum of given numbers are :", ret)
    

if __name__ == "__main__":
    main()    
