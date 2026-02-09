# Quetion 5
def chechkPalindrome(no):
    iDigit = 0
    Check = list()
    val = no
    i = 0

    if(no<= 0):
        print("Enter a valid number")
        return
    
    while(val !=0):
        iDigit = val % 10
        Check.append(iDigit)
        val = val // 10

    val = no
    for iCnt in range(len(Check)):

        if( val % 10 == Check[iCnt]):
            val = val // 10
            if (val == 0):
                print("Number is Palindrome")

        else:
            print("Number is not Palindrome")
            break
def main():

    value = int(input("Enter the number:"))

    chechkPalindrome(value)

if __name__ == "__main__":
    main()    