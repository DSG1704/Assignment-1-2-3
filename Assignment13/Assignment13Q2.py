from math import pi
def AreOfcircle(radius):
    return pi*radius**2


def main():

    Value = int(input("Enter radius:"))
    iret = AreOfcircle(Value)
    print("Area of circle is:",iret)


if __name__ == "__main__":
    main()