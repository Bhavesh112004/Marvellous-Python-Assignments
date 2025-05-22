def main():
    
    num = int(input("Enter the Number : "))

    count = 1
    result = 1
    while (count <= 10):
        result = count * num
        print(num," x ",count," = ",result)
        count = count + 1
        
if __name__ == "__main__":
    main()