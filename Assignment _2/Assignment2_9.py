def DigitNo(n):
    n = str(n)
    print("The no of digits in the number is : ",len(n))

def main():
   
    print("Enter the number")
    num = int(input())

    result = DigitNo(num)

if __name__ == "__main__":
    main()