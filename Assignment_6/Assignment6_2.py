def main():

    count = 1
    sum = 0
    while (count <= 100):
        if (count %2 == 0):
            sum = sum + count
        count = count + 1
    print("The sum of even numbers between 1 to 100 is : ",sum)

if __name__ == "__main__":
    main()