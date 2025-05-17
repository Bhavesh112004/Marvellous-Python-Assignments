from functools import reduce

def FilterCon(A):
    if (A % 2 == 0):
        return A

def MapCon(A):
    A = A * A
    return A

def RedCon(A,B):
    Add = A + B
    return Add


def main():

    print("Enter the count of list elements")
    size = int(input())

    lst =[]

    for i in range(size):
        ele = int(input())
        lst.append(ele)
        
    
    Fdata = list(filter(FilterCon,lst))
    print("List after filter: ",Fdata)

    Mdata = list(map(MapCon,Fdata))
    print("List after map: ",Mdata)

    Rdata = reduce(RedCon,Mdata)
    print("Output of reduce: ",Rdata)

if __name__ == "__main__":
    main()