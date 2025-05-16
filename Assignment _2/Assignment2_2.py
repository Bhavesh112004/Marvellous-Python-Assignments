def StarPrint(no):
    for i in range(1,no+1):
        for j in range(1,no):
            print("*" ,end = "")
        print("*")
        
def main():
    print("Enter the number")

    num = int(input())

    result = StarPrint(num)

if __name__ == "__main__":
    main()