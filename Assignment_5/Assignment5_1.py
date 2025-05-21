def Addition(no1, no2):
    result = no1 + no2
    return result

def Substraction(no1, no2):
    result = no1 - no2
    return result

def Multiplication(no1, no2):
    result = no1 * no2
    return result

def Division(no1, no2):
    result = no1 / no2
    return result


def main():

    print("Enter the first number: ")
    num1  = int(input())

    print("Enter the second number: ")
    num2  = int(input())

    ret1 = Addition(num1 , num2)
    print("The addition of two numbers is       :  ",ret1)

    ret2 = Substraction(num1 , num2)
    print("The Substraction of two numbers is   : ",ret2)

    ret3 = Multiplication(num1 , num2)
    print("The multiplication of two numbers is : ",ret3)

    ret4 = Division(num1 , num2)
    print("The Division of two numbers is       : ",ret4)

if __name__ == "__main__":
    main()