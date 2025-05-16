from  Arithmetic import Add,Sub,Mult,Div 

def main():
    print("Enter the first number")
    num1 = int(input())

    print("Enter the second number")
    num2 = int(input())

    Result1 = Add(num1,num2)
    Result1 = Sub(num1,num2)
    Result1 = Mult(num1,num2)
    Result1 = Div(num1,num2)

if __name__ == "__main__":
    main()