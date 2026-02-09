# Quetion 4
def Printreverse(no):
    iDigit = 0
    if( no <0):
        print("Enter a valid number")
        return
    while(no !=0):
        iDigit = no % 10
        print(iDigit)
        no = no // 10
def main():
    Value = int(input("Enter the number:"))

    Printreverse(Value)

if __name__ == "__main__":
    main()    
