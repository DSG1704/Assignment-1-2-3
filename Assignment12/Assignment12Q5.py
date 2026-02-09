# Question 5
def PrintNumber(no):
    for i in range(no, 0, -1):
        print(i)

def main():
    value = int(input("Enter a number:"))
    PrintNumber(value)

if __name__ == "__main__":
    main()
