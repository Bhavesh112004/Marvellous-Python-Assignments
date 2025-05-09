def CheckNumber(no):
    if no > 0:
        print("Positive Number")
    
    elif no < 0:
        print("Negative Number")

    else:
        print("Zero")

def main():
    print("Enter the number: ")
    num = int(input())
    result = CheckNumber(num)

if __name__ == "__main__":
    main()