def AreaRect(length,breadth):
    Area = length * breadth
    return Area

def PerimeterRect(length, breadth):
    Perimeter = 2 * (length + breadth)
    return Perimeter

def main():

    print("Enter the length of rectangle : ")
    len = int(input())
    
    print("Enter the breadth of rectangle: ")
    bre = int(input())

    ret1 = AreaRect(len, bre)
    print("The area of rectangle is : ",ret1)

    ret2 = PerimeterRect(len, bre)
    print("The perimeter of rectangle is : ",ret2)


if __name__ == "__main__":
    main()