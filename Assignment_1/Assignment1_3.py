def Add(num1,num2):
    Addition = num1 + num2
    print("Addition of numbers is: ",Addition)

def main():
    print("Enter the first number: ")
    m = int(input())

    print("Enter the second number: ")
    n = int(input())

    result = Add(m,n)

if __name__ == "__main__":
    main()