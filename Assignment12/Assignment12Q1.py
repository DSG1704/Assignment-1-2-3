#Question 1
def CheckCharacter(ch):
    if ch in ('a','e','i','o','u','A','E','I','O','U'):
        return True
    else:
        return False

def main():
    iret = False
    ch = input("Enter a character : ")

    iret = CheckCharacter(ch)

    if iret:
        print(ch, "is Vowel")
    else:
        print(ch, "is not Vowel")

if __name__ == "__main__":
    main()