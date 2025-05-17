Mult = lambda X,Y : X * Y

def main():
    
    
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))

    ret = Mult(num1, num2)
    print("The product of two numbers is: ",ret)

if __name__ == "__main__":
    main()