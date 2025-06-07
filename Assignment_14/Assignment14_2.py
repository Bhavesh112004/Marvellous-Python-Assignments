class Rectangle:

    def __init__(self,length,breadth):
        self.Length = length
        self.Breadth = breadth

    def Area(self):
        result = self.Length * self.Breadth
        print("The area of rectangle is : ",result)

    def Perimeter(self):
        result = 2 * (self.Length + self.Breadth)
        print("The perimeter of rectangle is : ",result)

def main():

    rect_len = int(input("Enter the length of rectangle  : "))
    rect_bre = int(input("Enter the breadth of rectangle : "))

    Obj = Rectangle(rect_len,rect_bre)
    Obj.Area()
    Obj.Perimeter()

if __name__ == "__main__":
    main()

