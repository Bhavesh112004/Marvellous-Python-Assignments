def EvenOddChk(no):
    if (no %2 == 0):
        print("Even number")

    else :
        print("Odd number")

def main():

    print("Enter the number : ")
    num1 = int(input())

    ret = EvenOddChk(num1)
    print(ret)

if __name__ == "__main__":
    main()