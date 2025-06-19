from functools import reduce

def PrimeNo(number):
    if number <= 1:
            return False  
    for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False  
    return True 


def Multiply(num):
    num= num * 2
    return num

def MaxNo(Max,num):
    Max  = 0
    for i in range(num):
        if i > Max:
            Max = num
    return Max


def main():

    print("Enter the count of list elements")
    size = int(input())

    lst =[]

    for i in range(size):
        ele = int(input())
        lst.append(ele)
        
    
    Fdata = list(filter(PrimeNo,lst))
    print("List after filter: ",Fdata)

    Mdata = list(map(Multiply,Fdata))
    print("List after map: ",Mdata)

    Rdata = reduce(MaxNo,Mdata)
    print("Output of reduce: ",Rdata)

if __name__ == "__main__":
    main()