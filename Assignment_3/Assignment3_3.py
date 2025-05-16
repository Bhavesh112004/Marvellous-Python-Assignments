def main():
    
    
    print("Enter the count of elements in the list : ")
    size = int(input())

    lst = []
    for i in range(size):
        ele = int(input())
        lst.append(ele)

    min = lst[0]
    for i in lst:
        if (i < min):
            min = i

    print("The minimum number from the list is : ",min)



if __name__ == "__main__":
    main()