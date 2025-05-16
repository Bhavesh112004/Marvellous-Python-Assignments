def main():

    print("Enter the count of elements in the list")
    size = int(input())

    lst = []

    for i in range(size):
        ele = int(input())
        lst.append(ele)
    
    max = lst[0]
    for i in lst:
        if (i > max):
            max = i
    print("The maximum number from the list is : ",max)


if __name__ == "__main__":
    main()
