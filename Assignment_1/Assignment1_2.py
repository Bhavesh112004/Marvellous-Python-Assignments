def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")   


def main():
    num = int(input("Enter The Number: "))
    result = ChkNum(num)

if __name__ == "__main__":
    main()
