def CheckPrime(no):

    if no <= 1:
        return False

    elif (no == 2):
            return True

    for i in range(3,int(no**0.5)+1,2):

        if (no % i == 0):
            return False

        else :
            return True

def main():
    
    print("Enter the Number : ")
    num = int(input())

    ret = CheckPrime(num)

    if (ret == True):
        print("The number is prime")
    else :
        print("The number is not prime")

if __name__ == "__main__":
    main()