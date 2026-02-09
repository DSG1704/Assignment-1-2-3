#Question 2

def PrintFactors(no):
    for i in range(1 , ( no+2)//2):
        if(no % i == 0):
            print(i)
            
def main():
    no = int(input("Enter a number : "))
    PrintFactors(no)

if __name__ == "__main__":
    main()
