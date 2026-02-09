def CheckPerfect(no):

    sum = 0
    for i in range(1 ,(no+2)//2):
        if(no % i == 0):
            sum = sum + i

    if(sum == no):
        return True

def main():
    ret = False
    Value = int(input("Enter a number:"))
    ret = CheckPerfect(Value)
    if(ret == True):
        print("Number is perfect")
    else:
        print("Number is not perfect")

if __name__ == "__main__":
    main()