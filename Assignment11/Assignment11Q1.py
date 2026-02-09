# Quetion 1
def Checkprime(no):
    
    for i in range (2 , no):
        if( no % i == 0):
            return False
        
    return True    
def main():
    Value = int(input("Enter the Number:"))

    ret = Checkprime(Value)

    if(ret == True):
        print(Value, "is a prime number")
    else:
        print(Value,"is not a prime number")



if __name__ == "__main__":
    main()   