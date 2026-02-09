def AreaOfrectangle(length, breadth):
    return length * breadth


def main():

    Value1 = int(input("Enter length:"))
    Value2 = int(input("Enter width:"))

    iret = AreaOfrectangle(Value1,Value2)
    print("Area of rectangle is:",iret)


if __name__ == "__main__":
    main()