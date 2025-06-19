Power = lambda X, Y: X * Y

def main():
    
    print("Enter the number1 : ")
    num1  = int(input())

    print("Enter the number2 : ")
    num2 = int(input())

    print("The power of number is : ")
    ret = Power(num1, num2)
    print(ret)


if __name__ == "__main__":
    main()