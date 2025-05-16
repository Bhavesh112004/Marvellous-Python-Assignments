def main():
    
    
    print("Enter the count of elements in the list : ")
    size = int(input())

    lst = []
    for i in range(size):
        ele = int(input())
        lst.append(ele)

    num  = int(input("Enter the number to check frequency: "))

    if num in lst:
        cnt = 0
        for i in (lst):
            if (i == num):
                cnt = cnt + 1
        print("The number of times the number occured in list is :  ",cnt)

    else :
        print("The Number not in list")


            


if __name__ == "__main__":
    main()