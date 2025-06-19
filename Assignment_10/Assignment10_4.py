from functools import reduce

def Even(no):
    if (no % 2 == 0):
        return no

def Square (no):
    return no * no

def Addition (no1,no2):
    return no1 + no2



def main():
    
    print("Enter the number of elements to insert: ")
    size = int(input())

    lst = []
    for i in range(size):
        ele = int(input())
        lst.append(ele)
    

    Fdata = list(filter(Even,lst))
    print("List after filter: ",Fdata)

    Mdata = list(map(Square,Fdata))
    print("List after map: ",Mdata)

    Rdata = reduce(Addition,Mdata)
    print("Output of reduce: ",Rdata)


if __name__ == "__main__":
    main()