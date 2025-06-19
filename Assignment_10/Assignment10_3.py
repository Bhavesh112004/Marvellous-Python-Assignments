from functools import reduce

def GreaterEqual(no):
    if (no >= 70 and no <= 90):
        return no

def Increase(no):
    no  = no + 1
    return no

def Product(no1,no2):
    return no1 * no2



def main():
    
    print("Enter the number of elements to insert: ")
    size = int(input())

    lst = []
    for i in range(size):
        ele = int(input())
        lst.append(ele)
    

    Fdata = list(filter(GreaterEqual,lst))
    print("List after filter: ",Fdata)

    Mdata = list(map(Increase,Fdata))
    print("List after map: ",Mdata)

    Rdata = reduce(Product,Mdata)
    print("Output of reduce: ",Rdata)


if __name__ == "__main__":
    main()