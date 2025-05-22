def main():
    
    print("Enter the Number : ")
    num = int(input())

    fact = 1
    for i in range(num,0,-1):
        fact = fact * i
    
    print("The factorial of ",num,"is ",fact)
        

if __name__ == "__main__":
    main()