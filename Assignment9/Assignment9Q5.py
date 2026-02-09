#question 5
def checkDivisible(no):

    if( no % 3 == 0):
        if(no % 5 == 0):
            return True


    return False    


def main():

    value = int(input("enter the number :"))
    ret = checkDivisible(value)

    if (ret == True ):
        print(value,"is Divisble by 3 & 5,")
    else:
        print(value,"is not divisble by 3 & 5, ")
    
if __name__ == "__main__":
    main()
