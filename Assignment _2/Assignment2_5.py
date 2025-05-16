def CheckPrimeNo(No):

    '''if (No % 2 != 0 and  No % 3 != 0):
        print("It is Prime Number")

    else: 
        print("It is not Prime Number")'''

    if (No <= 1):
        print("Not Possible")
 

    for i in range(2,No):
        if (No % i != 0):
            print("It is prime number")
            return

        else :
            print("It is not prime")
            return
             
        
            


def main():

    print("Enter the number")
    Num = int(input())

    Result = CheckPrimeNo(Num)


if __name__ == "__main__":
    main()