def AgeChk(no):
    if (no >= 18):
        print("Eligible to vote")

    else:
        print("Not eligible to vote")

def main():

    print("Enter the age :")
    age = int(input())

    ret = AgeChk(age)
    print(ret)


if __name__ == "__main__":
    main()