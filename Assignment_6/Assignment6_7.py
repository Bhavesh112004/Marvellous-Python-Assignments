def main():

    print("Enter the 5 numbers ")
    size = 5
    lst = []
    for i in range(size):
        num = int(input("Enter the number : "))
        if num not in lst:

            lst.append(num)
            
    max = 0
    for i in lst:
        if (i > max):
            max = i
    print("The largest number is : ",max)
    
        
if __name__ == "__main__":
    main()