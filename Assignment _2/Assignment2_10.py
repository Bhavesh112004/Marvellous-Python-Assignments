
def DigitNo(n):
    n = str(n)
    
    digits = (map(int, n))
    lst = (list(digits)) 
    sum = 0
    for i in lst:
        sum = sum + i

    print(sum)
        

def main():
   
    print("Enter the number")
    num = int(input())

    result = DigitNo(num)

if __name__ == "__main__":
    main()