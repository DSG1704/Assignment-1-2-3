#question 4
def cubenumber(no):
    return no * no * no


def main():
    Value = int(input("enter number:"))

    ret = cubenumber(Value)

    print("Cube of given number is :",ret)
    
if __name__ == "__main__":
    main()
