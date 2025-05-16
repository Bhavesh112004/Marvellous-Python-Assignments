def factorial(No):
    if No < 0:
        print("Give positive no")

    elif No == 0:
        print("Factorial of zero is 0")
    
    else:
        cnt = 1
        fact =1
        while (cnt <= No):
            fact= cnt * fact
            
            cnt = cnt + 1
        return fact


def main():
    print("Enter the number: ")
    num = int(input())

    ret = print("The factorial of the no is :",factorial(num))

if __name__ == "__main__":
    main()