def LargestNo(no1, no2, no3):
    if (no1 > no2 and no1>no3):
        print(no1," is the largest")

    elif (no2> no1 and no2>no3):
        print(no2," is the largest")

    else:
        print(no3," is the largest")

    
def main():


    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number : "))

    ret = LargestNo(num1, num2, num3)
    print(ret)



if __name__ == "__main__":
    main()