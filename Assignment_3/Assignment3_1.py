def main():
     
    print("Enter the count of elements")
    size = int(input())

    data = list()
    for i in range(size):
        no = int(input())
        data.append(no)
    # print(data)

    sum = 0
    for i in data:
        sum = sum + i

    print("The sum of elements in the list is : ",sum)

if __name__ == "__main__":
    main()