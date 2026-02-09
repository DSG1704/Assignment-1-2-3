def DisplayGarde(no):
    if(no>=75):
        print("Distinction")
    elif(no>=60 and no<75):
        print("First Class")
    elif(no>=50 and no<60):
        print("Second Class")
    else:
        print("Fail")


def main():
    value = int(input("Enter a number:"))
    DisplayGarde(value)
if __name__ == "__main__":
    main()