Power = lambda X : X ** 2

def main():
    
    print("Enter the number : ")
    num  = int(input())

    print("The power of number is : ")
    ret = Power(num)
    print(ret)


if __name__ == "__main__":
    main()